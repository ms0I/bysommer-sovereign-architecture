#!/usr/bin/env python3
"""Generate the TONE Patent Portfolio Transmittal Letter as a styled PDF."""

import os
from weasyprint import HTML

# Create output directories if needed
os.makedirs("patent/out", exist_ok=True)
os.makedirs("docs/out", exist_ok=True)

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  @page {
    size: A4;
    margin: 20mm 15mm 20mm 15mm;
    background-color: #fcfcfd;
    @bottom-right {
      content: "Page " counter(page) " of " counter(pages);
      font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
      font-size: 8pt;
      color: #718096;
    }
    @bottom-left {
      content: "CONFIDENTIAL // ATTORNEY-CLIENT PRIVILEGED COMMUNICATION";
      font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
      font-size: 8pt;
      color: #e53e3e;
      font-weight: bold;
    }
  }

  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 10pt;
    line-height: 1.5;
    color: #1a202c;
    margin: 0;
    padding: 0;
  }

  .header-table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 25px;
    border-bottom: 2px solid #2b6cb0;
    padding-bottom: 15px;
  }

  .header-table td {
    vertical-align: top;
  }

  .brand-title {
    font-size: 18pt;
    font-weight: 800;
    color: #1a365d;
    letter-spacing: -0.5px;
    text-transform: uppercase;
  }

  .brand-sub {
    font-size: 9pt;
    color: #4a5568;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 2px;
  }

  .meta-box {
    background-color: #ebf8ff;
    border-left: 4px solid #3182ce;
    padding: 12px 15px;
    margin-bottom: 20px;
    border-radius: 0 4px 4px 0;
  }

  .meta-grid {
    width: 100%;
    border-collapse: collapse;
    font-size: 9.5pt;
  }

  .meta-grid td {
    padding: 3px 0;
  }

  .meta-label {
    font-weight: 700;
    color: #2c5282;
    width: 22%;
  }

  .meta-val {
    color: #1a202c;
  }

  h2 {
    font-size: 12pt;
    color: #2b6cb0;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 5px;
    margin-top: 20px;
    margin-bottom: 10px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  p {
    margin-top: 0;
    margin-bottom: 12px;
    text-align: justify;
  }

  ul, ol {
    margin-top: 0;
    margin-bottom: 12px;
    padding-left: 20px;
  }

  li {
    margin-bottom: 6px;
  }

  table.data-table {
    width: 100%;
    border-collapse: collapse;
    margin: 15px 0;
    font-size: 9pt;
  }

  table.data-table th {
    background-color: #2b6cb0;
    color: white;
    text-align: left;
    padding: 8px 10px;
    font-weight: 600;
  }

  table.data-table td {
    padding: 7px 10px;
    border-bottom: 1px solid #e2e8f0;
  }

  table.data-table tr:nth-child(even) td {
    background-color: #f7fafc;
  }

  .privilege-notice {
    background-color: #fff5f5;
    border: 1px solid #feb2b2;
    color: #9b2c2c;
    padding: 10px 12px;
    font-size: 8.5pt;
    border-radius: 4px;
    margin-bottom: 20px;
  }

  .signature-block {
    margin-top: 30px;
    page-break-inside: avoid;
  }

  .signature-line {
    border-top: 1px solid #a0aec0;
    width: 220px;
    margin-top: 40px;
    margin-bottom: 5px;
  }

  .checklist {
    background-color: #f0fff4;
    border: 1px solid #9ae6b4;
    border-radius: 4px;
    padding: 12px 15px;
    margin: 15px 0;
  }

  .checklist h3 {
    font-size: 10pt;
    color: #276749;
    margin: 0 0 8px 0;
  }

  .checklist ul {
    margin-bottom: 0;
  }

  .checklist li {
    margin-bottom: 4px;
    font-size: 9pt;
  }

  .footer-note {
    margin-top: 25px;
    padding-top: 12px;
    border-top: 1px solid #e2e8f0;
    font-size: 8pt;
    color: #718096;
    text-align: center;
  }
</style>
</head>
<body>

<table class="header-table">
  <tr>
    <td>
      <div class="brand-title">BY SOMMER</div>
      <div class="brand-sub">Sovereign Architecture &amp; Intellectual Property Governance</div>
    </td>
    <td style="text-align: right; font-size: 9pt; color: #4a5568;">
      <strong>Date:</strong> August 6, 2026<br>
      <strong>Location:</strong> Hellerup, Denmark<br>
      <strong>Ref:</strong> TRANSMITTAL-TONE-2026-01
    </td>
  </tr>
</table>

<div class="privilege-notice">
  <strong>CONFIDENTIAL &amp; ATTORNEY-CLIENT PRIVILEGED COMMUNICATION</strong><br>
  The information contained in this transmission and attached documents is intended solely for the use of the designated patent attorney/counsel. It contains legal strategy, proprietary trade secrets, and non-public patent disclosures.
</div>

<div class="meta-box">
  <table class="meta-grid">
    <tr>
      <td class="meta-label">TO:</td>
      <td class="meta-val">Patent Prosecution Practice Group (Plougmann Vingtoft / Zacco / Patrade)</td>
    </tr>
    <tr>
      <td class="meta-label">FROM:</td>
      <td class="meta-val">Michael Sommer | BY SOMMER Sovereign Architecture</td>
    </tr>
    <tr>
      <td class="meta-label">SUBJECT:</td>
      <td class="meta-val">Formal Intake &amp; Priority Filing Instruction: TONE Sovereign Architecture Portfolio (Docket: TONE-2026-PCT-01)</td>
    </tr>
    <tr>
      <td class="meta-label">PRIORITY TARGET:</td>
      <td class="meta-val">Danish Patent &amp; Trademark Office (DKPTO) National Priority Filing (~DKK 3,000&ndash;5,000)</td>
    </tr>
  </table>
</div>

<p>Dear Patent Prosecution Team,</p>

<p>We are formally submitting the complete, publication-ready patent application package for the <strong>TONE Architecture</strong> (<em>System and Method for Telemetry-Driven Active Inference, Zero-Knowledge Jurisdictional Compliance, and Autonomous Dividend Accrual</em>). We request your formal intake review, prior art search validation, and preparation of the national priority filing before the Danish Patent and Trademark Office (DKPTO).</p>

<h2>1. Portfolio Scope &amp; Claim Architecture Summary</h2>

<p>The TONE invention spans physiological telemetry processing, zero-knowledge cryptographic compliance, and autonomous non-profit ledger mechanics. The application comprises <strong>15 formal claims</strong> (3 independent, 12 dependent) structured as follows:</p>

<table class="data-table">
  <thead>
    <tr>
      <th>Claim</th>
      <th>Type</th>
      <th>Technical Perimeter &amp; Focus</th>
      <th>Key Statutory / Technical Anchor</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Claim 1</strong></td>
      <td>Independent</td>
      <td>Biosecurity &amp; Active Inference Circuit Breaker</td>
      <td>Variational Free Energy divergence threshold (&#119871;&#916; &ge; 3.0) &rarr; automated financial lock.</td>
    </tr>
    <tr>
      <td><strong>Claim 2</strong></td>
      <td>Independent</td>
      <td>Location-Aware Zero-Knowledge Jurisdictional Matcher</td>
      <td>Multi-tiered rule engine (EU IOSS &lt; &euro;150, Danish VAT 25%, Municipal ULEZ) with <code>cpr_zk_hash</code>.</td>
    </tr>
    <tr>
      <td><strong>Claim 3</strong></td>
      <td>Independent</td>
      <td>Autonomous Non-Profit Surplus Ledger Engine</td>
      <td>Daily increment calculation (&Delta;surplus = 2.30 DKK/day) with atomic Dec 10th payout epoch.</td>
    </tr>
    <tr>
      <td><strong>Claim 8</strong></td>
      <td>Dependent (1)</td>
      <td>NemRefusion ZK Biosecurity Bridge</td>
      <td>Danish Sickness Benefits Act (<em>Sygedagpengeloven</em> &mdash; LBK nr 1293); GDPR Art. 9 insulated.</td>
    </tr>
    <tr>
      <td><strong>Claim 12</strong></td>
      <td>Dependent (2)</td>
      <td>GDPR Recital 26 Identity Hashing</td>
      <td>Explicit classification of <code>cpr_zk_hash</code> as <em>pseudonymous</em> under EU law.</td>
    </tr>
    <tr>
      <td><strong>Claim 15</strong></td>
      <td>Dependent (1)</td>
      <td>Planetary Shield Interoperability</td>
      <td>Pathogen transmission coefficient (R&#8320; &gt; 1.0) cross-correlation with diagnostic production.</td>
    </tr>
  </tbody>
</table>

<h2>2. International Priority &amp; Prosecution Roadmap</h2>

<p>We request execution according to the following strict statutory timeline:</p>
<ul>
  <li><strong>Milestone 1 (August 2026):</strong> DKPTO National Priority Application filing (establishing Priority Date).</li>
  <li><strong>Milestone 2 (August 2027):</strong> PCT International Application filing (via RO/DK, designating ISA/EPO) within the 12-month Paris Convention window.</li>
  <li><strong>Milestone 3 (February&ndash;March 2029):</strong> Regional/National Phase Entries at EPO (31 months) and USPTO (30 months).</li>
</ul>

<h2>3. Key Legal &amp; Doctrine Defense Points for Counsel Review</h2>

<p>During your intake review, we request particular focus on the following two prosecution strategies already embedded in the specification:</p>
<ol>
  <li><strong>EPO Art. 52(2)(c) Technical Character Defense:</strong> The specification grounds all software logic in physical hardware sensors (HRV, core temperature, SpO&#8322;) and tangible control outcomes (circuit breaker transaction locking). Please verify alignment with landmark decisions <em>T 154/04</em>, <em>G 1/19</em>, <em>T 625/11</em>, and <em>T 1227/05</em>.</li>
  <li><strong>GDPR Article 9 &amp; Health Information Act Compliance:</strong> Claim 8 transmits strictly a binary incapacitation indicator (<code>IS_INCAPACITATED: true</code>) via ZK-proofs. Diagnostic string transmission (e.g., <code>SICKNESS_FEBRILE</code>) has been completely scrubbed to prevent regulatory liability under Danish <em>Helbredsoplysningsloven</em>.</li>
</ol>

<h2>4. Transmitted Enclosures &amp; Repository Index</h2>

<p>The following complete files are attached and accessible in the repository under <code>/patent/</code>:</p>
<ul>
  <li><code>PATENT_PORTFOLIO_HANDOFF.md</code> &mdash; Attorney Executive Summary &amp; Intake Briefing</li>
  <li><code>TONE_PATENT_EFILING_PACKAGE.md</code> &mdash; Complete USPTO/EPO E-Filing Ready Application</li>
  <li><code>TONE_PATENT_SPECIFICATION.md</code> &mdash; Detailed Specification &amp; Enablement</li>
  <li><code>CLAIMS_DRAFT.md</code> &mdash; 15 Formal Claims Standalone Text</li>
  <li><code>DIAGRAMS_DESCRIPTION.md</code> &mdash; Drawing Reference Manual</li>
  <li><code>diagrams/FIG_1_System_Architecture.svg</code> through <code>FIG_9_HITL_Level_2_Override_Workflow.svg</code> &mdash; 9 High-Contrast SVG Vector Drawings with USPTO Badges</li>
</ul>

<p>The full repository is available at: <strong>github.com/MSDK0I/bysommer-sovereign-architecture</strong> (private &mdash; access credentials provided separately).</p>

<h2>5. Counsel Action Checklist</h2>

<div class="checklist">
  <h3>Requested Actions for Patent Counsel</h3>
  <ul>
    <li>&#9744; Confirm receipt of this transmittal and all enclosed documents</li>
    <li>&#9744; Conduct formal patentability search against CPC classes: G06F 21/62, G16H 40/67, G06Q 20/40, G06N 3/00</li>
    <li>&#9744; Validate Claim 1 and Claim 8 novelty against identified prior art</li>
    <li>&#9744; Review EPO Art. 52(2)(c) technical character defense and confirm landmark case applicability</li>
    <li>&#9744; Verify GDPR Recital 26 classification of <code>cpr_zk_hash</code> as pseudonymous data</li>
    <li>&#9744; Prepare DKPTO national priority application filing package</li>
    <li>&#9744; Confirm filing fee schedule and estimated timeline for DKPTO priority application</li>
    <li>&#9744; Advise on PCT international filing strategy (RO/DK, ISA/EPO designation)</li>
  </ul>
</div>

<p>Please confirm receipt of this transmittal and advise on your availability for a 30-minute intake alignment call next week.</p>

<div class="signature-block">
  <p>Respectfully submitted,</p>
  <div class="signature-line"></div>
  <p style="margin-top: 5px;">
    <strong>Michael Sommer</strong><br>
    Founder, BY SOMMER Sovereign Architecture<br>
    Hellerup, Denmark<br>
    <em>Attorney Docket: TONE-2026-PCT-01</em>
  </p>
</div>

<div class="footer-note">
  This document is confidential and subject to attorney-client privilege. Unauthorized distribution is prohibited.<br>
  BY SOMMER Sovereign Architecture &mdash; github.com/MSDK0I/bysommer-sovereign-architecture &mdash; August 2026
</div>

</body>
</html>"""

# Generate the PDF
output_path = "patent/out/TONE_PATENT_TRANSMITTAL.pdf"
HTML(string=html_content).write_pdf(output_path)
print(f"Transmittal letter generated: {output_path}")
print(f"File size: {os.path.getsize(output_path)} bytes")

# Also save the HTML version for email embedding
html_path = "patent/out/TONE_PATENT_TRANSMITTAL.html"
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"HTML version saved: {html_path}")
