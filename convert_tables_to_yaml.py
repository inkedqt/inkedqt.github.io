#!/usr/bin/env python3
import sys, re, pathlib, yaml
from bs4 import BeautifulSoup

def td_text(td):
    return re.sub(r'\s+', ' ', td.get_text(separator=' ', strip=True))

def extract_links(td):
    anchors = td.find_all("a")
    if not anchors:
        return None, None
    if len(anchors) == 1:
        return anchors[0].get("href", "").strip(), None
    links = [{"title": a.get_text(strip=True), "url": a.get("href","").strip()} for a in anchors]
    return None, links

def extract_img_src(td):
    img = td.find("img")
    return (img.get("src","").strip() if img else "") or None

def parse_retired_table(soup):
    # first <table> in the file is the Retired HTB Machines table
    table = soup.find("table")
    if not table: return []
    tbody = table.find("tbody") or table
    out = []
    for tr in tbody.find_all("tr", recursive=False):
        tds = tr.find_all("td", recursive=False)
        if len(tds) < 6:  # name..summary (tags optional)
            continue
        name        = td_text(tds[0])
        difficulty  = td_text(tds[1])
        status      = td_text(tds[2])
        proof_img   = extract_img_src(tds[3])
        link, links = extract_links(tds[4])
        summary     = td_text(tds[5]) if len(tds) > 5 else ""
        tags_raw    = td_text(tds[6]) if len(tds) > 6 else ""
        tags        = [t for t in tags_raw.split() if t] or None

        rec = {
            "name": name,
            "difficulty": difficulty,
            "status": status,
            "proof_img": proof_img,
            "summary": summary or None,
        }
        if links: rec["links"] = links
        elif link: rec["link"] = link
        if tags: rec["tags"] = tags
        out.append({k:v for k,v in rec.items() if v is not None})
    return out

def find_table_after_h2(soup, needle):
    h2 = None
    for tag in soup.find_all(["h2","h3","h1"]):
        if needle.lower() in tag.get_text(" ", strip=True).lower():
            h2 = tag
            break
    return h2.find_next("table") if h2 else None

def parse_simple_table(table):  # for PG / THM: Box, Difficulty, Status, Proof, Writeup, Notes
    if not table: return []
    tbody = table.find("tbody") or table
    out = []
    for tr in tbody.find_all("tr", recursive=False):
        tds = tr.find_all("td", recursive=False)
        if len(tds) < 6:
            continue
        name       = td_text(tds[0])
        difficulty = td_text(tds[1])
        status     = td_text(tds[2])
        proof_img  = extract_img_src(tds[3])
        link, links= extract_links(tds[4])
        notes      = td_text(tds[5])
        rec = {
            "name": name,
            "difficulty": difficulty,
            "status": status,
            "proof_img": proof_img,
            "notes": notes or None
        }
        if links: rec["links"] = links
        elif link: rec["link"] = link
        out.append({k:v for k,v in rec.items() if v is not None})
    return out

def main():
    if len(sys.argv) != 2:
        print("Usage: python convert_tables_to_yaml.py _includes/retired-table.html")
        sys.exit(1)

    src = pathlib.Path(sys.argv[1])
    html = src.read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(html, "html.parser")

    retired = parse_retired_table(soup)
    pg_tbl  = find_table_after_h2(soup, "Proving Grounds (PG) Boxes")
    thm_tbl = find_table_after_h2(soup, "Try Hack Me (THM) Boxes")
    pg  = parse_simple_table(pg_tbl)
    thm = parse_simple_table(thm_tbl)

    data_dir = pathlib.Path("_data")
    data_dir.mkdir(parents=True, exist_ok=True)

    def dump(path, obj):
        with path.open("w", encoding="utf-8") as f:
            yaml.safe_dump(obj, f, sort_keys=False, allow_unicode=True, width=120)

    dump(data_dir / "retired.yml", retired)
    dump(data_dir / "pg.yml", pg)
    dump(data_dir / "thm.yml", thm)

    print(f"Wrote: {_len(retired)} -> _data/retired.yml")
    print(f"Wrote: {_len(pg)} -> _data/pg.yml")
    print(f"Wrote: {_len(thm)} -> _data/thm.yml")

def _len(x): return len(x) if x is not None else 0

if __name__ == "__main__":
    main()
