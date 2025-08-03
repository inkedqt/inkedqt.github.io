---
layout: default
title: Inksec.io – CTF Writeups, Cybersecurity Portfolio, and Certifications
description: Explore detailed Hack The Box writeups, cyber certs like CPTS & eJPT, and real-world experience in ethical hacking and penetration testing.
keywords: CTF, Hack The Box, CPTS, Cybersecurity, Penetration Testing, OSCP, CBBH, writeups, inksec, eJPT, infosec portfolio
author: Tate Pannam
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
  <!-- CPTS Card -->
  <div class="cert-card">
    <img src="https://raw.githubusercontent.com/inkedqt/ctf-writeups/main/assets/certs/cpts.png" alt="Hack The Box CPTS Certificate – Tate Pannam" class="cert-img" />
    <h3>CPTS – Certified Penetration Testing Specialist</h3>
    <p>
      Credential ID: <span style="background: #1a1a1a; padding: 2px 6px; border-radius: 4px;">HTBCERT-3C9B65A17A</span>
    </p>
    <p>
      <a href="https://www.credly.com/badges/3dff4822-f70f-40c8-a4b4-ee19a43b1d26/public_url" target="_blank">
        View Verified Badge on Credly
      </a>
    </p>
    <p>
      <a href="https://www.hackthebox.com/certificates" target="_blank">
        Verify on Hack The Box
      </a>
    </p>
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
    <!-- Cert IV in Info Tech (2003) -->
    <div class="cert-card">
      <img src="https://raw.githubusercontent.com/inkedqt/ctf-writeups/main/assets/certs/certiv-it.png" alt="Cert IV Info Tech Badge" class="cert-img" />
      <h3>Certificate IV in Information Technology</h3>
      by <em>Computer Power Training Institute</em><br />
      <em>Completed at a now-defunct training Institute – old school creds!</em></p>
    </div>
    <div class="cert-card">
      <img src="https://raw.githubusercontent.com/inkedqt/ctf-writeups/main/assets/certs/iprimus.png" alt="iPrimus Logo" class="cert-img" />
      <h3>IT Helpdesk Support</h3>
      <p><strong>iPrimus Telecom, Melbourne</strong><br />
      2002 – 2010<br />
      Provided technical support, diagnostics, and customer assistance across residential and business internet services. Gained strong foundations in networking, troubleshooting, and client communication.</p>
    </div>
  </div>
  </div>
<p style="text-align: center; font-size: 0.9em; margin-top: 20px; margin-bottom: 0;">
  📋 
  <a href="/prep.html" style="text-decoration: none; color: #ff99ff;">
    Current Cert Prep List
  </a> | 
  <a href="/oscp.html" style="text-decoration: none; color: #ff99ff;">
    OSCP Bonus Boxes
  </a>
</p>
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
