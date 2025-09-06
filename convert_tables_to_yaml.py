#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import sys, re, yaml
from bs4 import BeautifulSoup

# ---------- utilities ----------
def t(x):
    if x is None: return ""
    s = " ".join(x.stripped_strings) if hasattr(x, "stripped_strings") else str(x)
    s = re.sub(r"\s+", " ", s).strip()
    return s

def first_img_src(td):
    img = td.find("img")
    return img["src"].strip() if img and img.has_attr("src") else ""

def first_link(td):
    a = td.find("a")
    return a["href"].strip() if a and a.has_attr("href") else ""

def normalise_row(cells):
    out = {}
    # try to map the usual columns by position; tolerate missing columns
    if len(cells) >= 1: out["name"] = t(cells[0])
    if len(cells) >= 2: out["difficulty"] = t(cells[1])
    if len(cells) >= 3: out["status"] = t(cells[2])
    if len(cells) >= 4:
        out["proof_img"] = first_img_src(cells[3]) or t(cells[3])
    if len(cells) >= 5:
        out["writeup_url"] = first_link(cells[4])  # may be ""
    if len(cells) >= 6: out["summary"] = t(cells[5])
    if len(cells) >= 7: out["tags"] = t(cells[6])
    return out

def guess_kind_from_path(p: Path):
    n = p.name.lower()
    if "retired"   in n: return "retired"
    if "active"    in n: return "active"
    if "seasonal"  in n: return "seasonal"
    return "retired"   # safe default before we had kinds

# ---------- main ----------
def main():
    if len(sys.argv) < 2:
        print("Usage: python convert_tables_to_yaml.py <path-to-include.html> [retired|active|seasonal]")
        sys.exit(1)

    src = Path(sys.argv[1])
    if not src.exists():
        print(f"File not found: {src}")
        sys.exit(1)

    kind = sys.argv[2].lower() if len(sys.argv) >= 3 else guess_kind_from_path(src)
    out_path = Path("_data") / f"{kind}.yml"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    html = src.read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(html, "html.parser")

    # take ALL tables in the include; for each table, parse rows (<tbody> > <tr>)
    items = []
    for table in soup.find_all("table"):
        tbody = table.find("tbody") or table
        for tr in tbody.find_all("tr"):
            tds = tr.find_all("td")
            if not tds: 
                continue
            row = normalise_row(tds)
            # require at least a name
            if row.get("name"):
                items.append(row)

    # write yaml (list of maps)
    with out_path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(items, f, sort_keys=False, allow_unicode=True)

    print(f"Wrote: {len(items)} -> {out_path}")

if __name__ == "__main__":
    main()
