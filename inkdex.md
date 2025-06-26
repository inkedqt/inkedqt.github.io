---
layout: default
title: "🛡️ Tate Pannam – Cyber Security Portfolio"
description: "A showcase of Hack The Box writeups and offensive security journey."
---

<link rel="stylesheet" href="/assets/css/style.css">

<div class="portfolio">
  <h1 class="highlight">🛡️ Cyber Security Portfolio</h1>
  <p>Hi, I'm <strong>Tate Pannam</strong>, a cyber security student at Victoria University in Melbourne, Australia. This site showcases my HTB journey through <em>retired</em>, <em>active</em>, and <em>seasonal</em> CTFs.</p>

  <h2 class="section-title">✅ Retired HTB Machines</h2>
  {% include retired-table.html %}

  <h2 class="section-title">🔒 Active HTB Machines</h2>
  <p class="private-note">(Writeups private until box retirement)</p>
  {% include active-table.html %}

  <h2 class="section-title">🗓️ Seasonal HTB Boxes</h2>
  <p class="private-note">(Writeups private until box retirement)</p>
  {% include seasonal-table.html %}

  <footer>
    <p>Proofs stored in <code>/HTB/proofs/</code> | Maintained by <a href="https://github.com/inkedqt">inksec</a></p>
  </footer>
</div>