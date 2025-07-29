---
layout: default
title: "🛡️ Tate Pannam – Cyber Security Portfolio"
description: "A showcase of Hack The Box writeups and offensive security journey."
---

<link rel="stylesheet" href="/assets/css/style.css">
<div class="container">
 <div class="portfolio">
  <h1 class="highlight">🛡️ Cyber Security Portfolio</h1>
  <p>Hi, I'm <strong>Tate Pannam</strong>, a cyber security student at Victoria University in Melbourne, Australia. This site showcases my HTB journey through hands-on exploration of <em>retired</em>, <em>active</em>, and <em>seasonal</em> CTFs.</p>
  <p>Many of the retired boxes were completed by referencing community writeups to reinforce concepts by doing — I believe the best way to learn is to <strong>break things and solve them</strong>.</p>

<!-- Hero Banner -->
<div class="hero">
  <img src="https://raw.githubusercontent.com/inkedqt/ctf-writeups/main/assets/tate-banner.png" alt="Tate hacking banner" class="hero-banner" />
  <div class="hero-text">
    <h1>Hi, I'm <span class="highlighted">Tate Pannam</span> 👋</h1>
    <p>💻 Cyber security student | CTF enthusiast | Hands-on Learner<br />
    🧠 Retired/Active/Seasonal HTB boxes | 🛠️ Exploits | 🚩 Root flags | 🔐 PrivEsc</p>
  </div>
 <!-- Certifications -->
  <h2 class="section-title">📜 Certifications</h2>
  <div class="cert-grid">
    <!-- eJPT Card -->
    <div class="cert-card">
      <img src="https://raw.githubusercontent.com/inkedqt/ctf-writeups/main/assets/certs/ejpt.png" alt="INE eJPT Certification Badge" class="cert-img" />
      <h3>eJPT – Junior Penetration Tester</h3>
      <p><a href="https://certs.ine.com/418db589-3ab5-4b4e-9a3c-236681afa28a#acc.9iOk41zd" target="_blank">Issued by INE | Verified Credential</a></p>
    </div>
    <!-- ICCA Card -->
    <div class="cert-card">
      <img src="https://raw.githubusercontent.com/inkedqt/ctf-writeups/main/assets/certs/icca.png" alt="INE ICCA Certification Badge" class="cert-img" />
      <h3>ICCA – INE Certified Cloud Associate</h3>
      <p><a href="https://certs.ine.com/7e00ab5d-87c4-426d-b3f0-2f97dcdd19b7#acc.thj68QBy" target="_blank">Issued by INE | Verified Credential</a></p>
    </div>
    <!-- CPTS Card (Placeholder) -->
    <div class="cert-card">
      <img src="https://raw.githubusercontent.com/inkedqt/ctf-writeups/main/assets/certs/cpts.png" alt="Hack The Box CPTS Badge" class="cert-img" />
      <h3>CPTS – Certified Penetration Testing Specialist</h3>
      <p><em>Pending verification…</em></p>
    </div>
    <!-- CBBH Card -->
    <div class="cert-card">
      <img src="https://raw.githubusercontent.com/inkedqt/ctf-writeups/main/assets/certs/cbbh2.png" alt="Hack The Box CBBH Badge" class="cert-img" />
      <h3>CBBH – Certified Bug Bounty Hunter</h3>
      <p><em>Training path completed</em></p>
    </div>
    <!-- Cert IV Cyber Security -->
    <div class="cert-card">
      <img src="https://raw.githubusercontent.com/inkedqt/ctf-writeups/main/assets/certs/vu-cyber.png" alt="Victoria University Cyber Security" class="cert-img" />
      <h3>Cert IV – Cyber Security</h3>
      <p>Victoria University, Australia<br /><em>TAFE Accredited</em></p>
      <p><em>Currently completing</em></p>
    </div>
  </div>
  </div>

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
</div>
