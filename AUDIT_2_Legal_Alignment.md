# Audit Report: Legal & Regulatory Alignment (By Sommer TONE Architecture)

**Document ID:** AUDIT-2026-LEG-02  
**Date:** 06 August 2026  
**Auditor:** Legal & Regulatory Audit Specialist  
**Repository Scope:** `/app/conversations/6a7429ca11d24606474d4e85/bysommer_archive/`  
**Target Documents Audited:**
1. `bysommer_archive/03_Compliance_Legal/By_Sommer_Compliance_Book_Consolidated.md`
2. `bysommer_archive/03_Compliance_Legal/L-LEG_Living_Legal_Operating_System.md`
3. `bysommer_archive/03_Compliance_Legal/IP_Anti_Counterfeiting_Protocol.md`
4. `bysommer_archive/01_Core_Architecture_Protocols/Symmetrical_Governmental_Support_Protocol.md`
5. `bysommer_archive/patent/TONE_PATENT_SPECIFICATION.md`
6. `bysommer_archive/patent/CLAIMS_DRAFT.md` (and `DIAGRAMS_DESCRIPTION.md`)

---

## Executive Summary

This audit evaluated the By Sommer TONE Architecture repository for **Legal & Regulatory Alignment** across current Danish national law and European Union statutory frameworks. 

Overall, the repository demonstrates a sophisticated "compliance-by-design" architectural vision. The core zero-knowledge (ZK) boundary concept, sovereign layer isolation, and ethical veto mechanisms align remarkably well with high-level regulatory objectives. However, detailed examination revealed several **critical legal inaccuracies, conflated regulatory timelines, missing statutory references, and one potential statutory violation in the patent specification payload design**.

### Key Findings Summary:
- **Critical Violation (Action Required):** The NemRefusion biosecurity bridge payload specification in `TONE_PATENT_SPECIFICATION.md` (Section 2.5) and `DIAGRAMS_DESCRIPTION.md` (FIG. 4) includes diagnostic codes (`SICKNESS_FEBRILE`). Transmitting clinical diagnosis indicators to employer-facing channels violates the Danish Health Information Act (*Helbredsoplysningsloven* § 1 / § 2) and GDPR Article 9.
- **Inaccurate Timelines / Conflation:** NIS2 incident reporting timelines (24h / 72h / 1 month) are conflated with EU AI Act serious incident reporting timelines (15 days) across multiple documents. Additionally, IOSS filing frequency (monthly) is incorrectly described as quarterly in sections of the Symmetrical Protocol.
- **Missing Regulatory Citations:** The statutory framework for sickness benefits (*Sygedagpengeloven* and its 30-day employer period / Day 31+ municipal transition), the EU-wide €10,000 threshold for OSS B2C cross-border VAT, and the General Product Safety Regulation (GPSR Regulation (EU) 2023/988) are missing.
- **EU AI Act Article Mapping Error:** Article 16 is cited as "Obligations of deployers", whereas under EU AI Act Regulation (EU) 2024/1689, Article 16 governs **providers**, and Article 26 governs **deployers**.
- **GDPR Terminology Precision:** `cpr_zk_hash` is described as "anonymous" / "non-reversible", whereas under GDPR Recital 26 and CJEU case law, un-salted hashes of static national IDs are **pseudonymous personal data**.

---

## Regulatory Framework Verification Table

| Framework / Regulation | Citation in Docs | Status | Notes & Findings |
| :--- | :--- | :--- | :--- |
| **EU IOSS (< €150 Threshold)** | Symmetrical Protocol (L131, L148, L232, L285); CLS Spec (L219) | **PASS** | Correctly identifies the < €150 intrinsic value threshold for third-country import VAT via IOSS. |
| **EU OSS (€10,000 Threshold)** | Symmetrical Protocol (L68, L127, L284) | **INCOMPLETE** | Cites OSS and Danish DKK 50,000 threshold, but **omits** the EU-wide **€10,000 cross-border B2C threshold**. |
| **IOSS / OSS Filing Frequency** | Symmetrical Protocol (L148, L245 vs L285) | **INCORRECT** | L148 & L245 state IOSS has "quarterly settlement". **IOSS is monthly**; **OSS is quarterly**. L285 correctly lists IOSS as monthly, creating internal inconsistency. |
| **National VAT Rates** | TONE Patent Spec (L63); Symmetrical Protocol (L70, L148) | **PASS** | Danish 25%, German 19%, French 20% VAT rates are accurately stated. |
| **Danish Sickness Benefits Act (*Sygedagpengeloven*)** | TONE Patent Spec (Section 2.5); Claim 8 | **MISSING / INCOMPLETE** | Mentions NemRefusion, but **fails to cite *Sygedagpengeloven*** and **omits the 30-day employer period** vs. Day 31+ municipal takeover. |
| **Danish Health Info Act (*Helbredsoplysningsloven*)** | TONE Patent Spec (L154); FIG. 4 (L137) | **INCORRECT / VIOLATION** | Payload includes `SICKNESS_FEBRILE`. Disclosing diagnostic/clinical codes violates *Helbredsoplysningsloven* and GDPR Art. 9. Must be binary (`IS_INCAPACITATED`). |
| **GDPR Article 9 (Special Category Data)** | Compliance Book (L307); L-LEG (L243); Patent Spec (L193) | **PASS / CONDITIONAL** | Correctly identifies biometric/health data restrictions. ZK trust boundary keeps raw telemetry in PDT. Requires payload fix for `SICKNESS_FEBRILE`. |
| **GDPR Anonymization vs. Pseudonymization** | Patent Spec (L188-193); Claims (Claim 2) | **OUTDATED TERMINOLOGY** | Refers to `cpr_zk_hash` as "anonymous" or "non-reversible". Under GDPR Recital 26, static ID hashes are **pseudonymous personal data**. |
| **EU AI Act High-Risk Classification** | Compliance Book (Section 7.1) | **PASS** | Sound rationale under Annex III Point 5(a) (essential public services / benefits eligibility) and Point 1 (biometrics). |
| **EU AI Act Article Mapping** | Compliance Book (Section 7.2) | **INCORRECT** | Maps Art. 16 as "Obligations of deployers". Under Regulation (EU) 2024/1689, **Art. 16 = Providers**, **Art. 26 = Deployers**. |
| **NIS2 Incident Reporting Timelines** | Compliance Book (L116, L358, L464); L-LEG (L291) | **INCORRECT / CONFLATED** | Conflates NIS2 (24h / 72h / 1 month) with AI Act Art. 73 (15 days). Multiple sections list "NIS2 (24h/72h/15-day)". |
| **eIDAS 2 (EUDI Wallet)** | Compliance Book (Section 2.4); L-LEG (L290) | **PASS** | Correctly aligns with EUDI Wallet / eIDAS 2. Should add official citation: **Regulation (EU) 2024/1183**. |
| **Danish Bookkeeping Act (*Bogføringsloven*)** | Compliance Book (Section 2.5); L-LEG (L253) | **PASS** | Correctly cites 5-year financial record retention under *Bogføringsloven* (LBK nr 700/2022 § 12), overriding 30-day default deletion. |
| **CE Marking & Product Safety** | Symmetrical Protocol (L133, L384); Compliance Book (Section 7.4) | **INCOMPLETE** | Cites CE Marking in general terms and AI Act Art. 48, but **omits General Product Safety Regulation (EU) 2023/988 (GPSR)** for dropshipping. |

---

## Detailed Category Audits & Technical Evaluation

### Category A: EU IOSS & Low-Value Import Rules

1. **IOSS Threshold (< €150):**
   - **Verification:** The European Union Import One Stop Shop (IOSS) applies to distance sales of goods imported from third territories or third countries in consignments of an intrinsic value not exceeding **€150**.
   - **Docs Assessment:** `Symmetrical_Governmental_Support_Protocol.md` (L131, L148, L232, L285) and `Cluster_Link_System_Specification.md` (L219, L225) correctly cite the < €150 threshold.

2. **OSS Threshold (€10,000 EU Cross-Border B2C):**
   - **Verification:** Under EU VAT rules (Council Directive 2006/112/EC as amended), an EU business selling B2C goods/services cross-border within the EU can charge domestic VAT only up to the EU-wide micro-business threshold of **€10,000** (approx. DKK 74,500). Above €10,000, VAT must be settled in the destination Member State via the Union One Stop Shop (OSS).
   - **Docs Assessment:** The documentation mentions the Danish domestic VAT registration threshold of DKK 50,000 (*momsregistreringsgrænse* under *Momsloven* § 48), but **omits the €10,000 EU OSS threshold**. This threshold must be added to the BDT Rule Compass logic.

3. **IOSS vs. OSS Settlement Frequency Inconsistency:**
   - **Verification:** Under EU VAT regulations:
     - **IOSS (Import scheme):** VAT returns and payments must be submitted **monthly** (by the end of the month following the reporting month).
     - **OSS (Union scheme):** VAT returns and payments must be submitted **quarterly** (by the end of the month following the calendar quarter).
   - **Docs Assessment:** `Symmetrical_Governmental_Support_Protocol.md` contains an internal contradiction:
     - Line 148 states: *"Automatic IOSS registration for quarterly settlement"* -> **INCORRECT**
     - Line 245 states: *"EUS (IOSS): pre-validated quarterly VAT settlement"* -> **INCORRECT**
     - Line 285 states: *"VAT on imports < €150 ... monthly settlement"* -> **CORRECT**
   - **Fix:** Update Lines 148 and 245 of the Symmetrical Protocol to clarify that **IOSS is settled monthly**, whereas **OSS is settled quarterly**.

4. **Member State VAT Rates:**
   - **Verification:** Standard VAT rates: Denmark = 25%, Germany = 19%, France = 20%.
   - **Docs Assessment:** All three rates are accurately cited in `TONE_PATENT_SPECIFICATION.md` (L63) and `Symmetrical_Governmental_Support_Protocol.md` (L70, L148, L325).

---

### Category B: Danish Sickness Benefits Act (*Sygedagpengeloven*) & NemRefusion

1. **Statutory Framework & Employer Period (*Arbejdsgiverperiode*):**
   - **Verification:** Under Denmark's Sickness Benefits Act (*Sygedagpengeloven* - LBK nr 1293 af 21/09/2021), sick leave reimbursement operates in two distinct legal phases:
     - **Days 1–30 (Employer Period / *Arbejdsgiverperioden*):** The employer pays full sickness benefits or salary. The municipality is not involved, and NemRefusion reimbursement cannot be claimed (except for employees under a § 56 agreement for chronic illness).
     - **Day 31+ (Municipal Takeover):** The municipality (*kommune*) assumes financial responsibility for sickness benefits. Employers who continue paying full salary during sick leave file for reimbursement through **NemRefusion**.
   - **Docs Assessment:** Both `TONE_PATENT_SPECIFICATION.md` (Section 2.5) and `CLAIMS_DRAFT.md` (Claim 8) reference NemRefusion as an automated sickness declaration channel, but **fail to cite *Sygedagpengeloven*** and **omit the 30-day employer period and Day 31+ municipal transition**.
   - **Fix:** Incorporate explicit citations of *Sygedagpengeloven* § 30 (employer period) and § 40+ (NemRefusion municipal reimbursement) in the patent background and specification.

2. **Critical Data Privacy & Statutory Violation in NemRefusion Payload:**
   - **Verification:** Under Denmark's Health Information Act (*Helbredsoplysningsloven* § 1 and § 2) and GDPR Article 9:
     - An employer is legally entitled to know **only** that an employee is unable to work due to illness (*uarbejdsdygtig pga. sygdom*).
     - An employer is **strictly prohibited** from asking for or receiving medical diagnoses, clinical symptoms, or disease classifications.
     - NemRefusion notifications to employers contain binary incapacity dates, NOT clinical diagnostic codes.
   - **Docs Assessment:** In `TONE_PATENT_SPECIFICATION.md` Section 2.5 (L154) and `DIAGRAMS_DESCRIPTION.md` FIG. 4 (L137), the NemRefusion payload specification explicitly includes:
     ```text
     3. A declaration type code (e.g., SICKNESS_FEBRILE)
     ```
   - **Severity:** **HIGH / REGULATORY VIOLATION**. Disclosing clinical indicators like `SICKNESS_FEBRILE` to an employer or employer-facing system breaches *Helbredsoplysningsloven* and GDPR Art. 9.
   - **Fix:** Remove diagnostic/clinical codes from the payload specification. Replace with a strictly binary incapacity status flag (`IS_INCAPACITATED = true`) and timestamp. Clinical telemetry must remain isolated within the PDT ZK Vault.

---

### Category C: GDPR Article 9 Compliance

1. **Processing Prohibition & Architectural Isolation:**
   - **Verification:** GDPR Art. 9(1) prohibits processing of biometric data for uniquely identifying a natural person and health data unless an Art. 9(2) exception applies (e.g., Art. 9(2)(b) employment/social security law).
   - **Docs Assessment:** The architecture effectively uses Zero-Knowledge proofs and local enclave execution (PDT) so that raw biometric state vectors (HRV, body temperature, SpO2, respiratory rate) never leave the local device boundary. Trust boundaries in FIG. 2, FIG. 4, and FIG. 6 correctly reflect this separation.

2. **Legal Classification of Hashed Identifiers (`cpr_zk_hash`):**
   - **Verification:** Under GDPR Recital 26 and CJEU precedent (*Breyer* C-582/14; *SRB v EDPS* C-413/21 P):
     - A simple deterministic hash of a static national identification number (e.g., Danish CPR number) is **pseudonymous personal data**, NOT anonymized data.
     - Because the CPR input domain is bounded (~10 million possible active CPRs), simple hashes without salt or ZK commitment schemes can be easily brute-forced.
   - **Docs Assessment:** `TONE_PATENT_SPECIFICATION.md` (L188-193) and `CLAIMS_DRAFT.md` (Claim 2) describe `cpr_zk_hash` as "anonymized" or "non-reversible hash".
   - **Fix:** Update legal descriptions in the Compliance Book and Patent Specification to classify `cpr_zk_hash` as **pseudonymous data under GDPR Article 4(5)**, protected by Article 25 (Privacy by Design) and Article 32 cryptographic measures, OR specify the use of a salted ZK-pedersen commitment / ZK-SNARK proof to achieve true non-linkability.

---

### Category D: EU AI Act (Regulation (EU) 2024/1689)

1. **High-Risk Classification Rationale:**
   - **Verification:** Under EU AI Act Annex III:
     - **Point 5(a):** AI systems evaluating eligibility of natural persons for public assistance benefits and services.
     - **Point 1:** AI systems performing biometric categorization or health risk detection.
   - **Docs Assessment:** `By_Sommer_Compliance_Book_Consolidated.md` Section 7.1 accurately classifies AURA/TONE as a High-Risk AI System under Annex III Point 5. This classification is sound and well-substantiated.

2. **Article Mapping Verification (Regulation (EU) 2024/1689):**
   - **Correct Mappings:**
     - **Art. 9 (Risk Management System):** Mapped to L-AURORA governance substrate.
     - **Art. 12 (Record-keeping / Logging):** Mapped to s.net 5-year immutable audit trail.
     - **Art. 14 (Human Oversight):** Mapped to L-ETH hard veto & Human-Oversight Matrix.
   - **Mapping Inaccuracy:** In `By_Sommer_Compliance_Book_Consolidated.md` Section 7.2:
     - Table row **Art. 16** is labeled *"Obligations of deployers"*.
     - **Correction:** Under the enacted EU AI Act Regulation (EU) 2024/1689:
       - **Article 16** defines the **Obligations of providers** of high-risk AI systems.
       - **Article 26** defines the **Obligations of deployers** of high-risk AI systems.

---

### Category E: Other Regulatory Citations

1. **NIS2 Directive (Directive (EU) 2022/2555) Incident Reporting Timelines:**
   - **Verification:** Under NIS2 Article 23(4):
     - **Early Warning:** within **24 hours** of becoming aware of the incident.
     - **Incident Notification:** within **72 hours** of becoming aware.
     - **Final Report:** within **1 month** (30 days) of the incident notification.
   - **Docs Assessment:** While Section 2.3 of the Compliance Book states the timeline correctly, **three other sections contain an error**:
     - Section 7.2 (Art. 73 row), Section 10 Checklist, and `L-LEG_Living_Legal_Operating_System.md` (L291) state: *"NIS2 incident reporting procedures operational (24h/72h/15-day timelines)"*.
   - **Correction:** The **15-day** deadline comes from **EU AI Act Article 73** (reporting of serious incidents), NOT NIS2. NIS2 requires a **1-month** final report. The docs conflate NIS2 and AI Act timelines.

2. **eIDAS 2 (Regulation (EU) 2024/1183):**
   - **Verification:** Regulation (EU) 2024/1183 entered into force in May 2024, establishing the European Digital Identity Framework (EUDI Wallet).
   - **Docs Assessment:** Cites eIDAS 2 and EUDI Wallet accurately in concept. Should explicitly add the formal citation: **Regulation (EU) 2024/1183**.

3. **Danish Bookkeeping Act (*Bogføringsloven*):**
   - **Verification:** Denmark's Bookkeeping Act (*Lov om bogføring* - LBK nr 700 af 24/05/2022 § 12) mandates a **5-year retention period** for accounting material from the end of the financial year.
   - **Docs Assessment:** Accurately cited in Section 2.5 of the Compliance Book and L-LEG (L253), correctly overriding short retention periods for financial/tax records.

4. **CE Marking & General Product Safety Regulation (GPSR):**
   - **Verification:** Dropshipping and cross-border e-commerce in physical goods must comply with EU product safety laws, specifically the new **General Product Safety Regulation (EU) 2023/988 (GPSR)**, which replaced Directive 2001/95/EC in December 2024, as well as CE directives such as **Low Voltage Directive 2014/35/EU** and **Radio Equipment Directive 2014/53/EU**.
   - **Docs Assessment:** Cites "CE Marking" and AI Act Art. 48, but omits GPSR Regulation (EU) 2023/988 and specific CE product directives.

---

## Detailed Audit Summary: Incorrect Citations & Corrections

| Document | Current Inaccurate Text | Correct Legal Information | Severity / Priority |
| :--- | :--- | :--- | :--- |
| `TONE_PATENT_SPECIFICATION.md` (L154) & `DIAGRAMS_DESCRIPTION.md` (L137) | `3. A declaration type code (e.g., SICKNESS_FEBRILE)` in NemRefusion payload | **Remove diagnostic code**. Payload must contain strictly binary status (`IS_INCAPACITATED = true`) per Danish *Helbredsoplysningsloven* § 1/2 & GDPR Art. 9. | **CRITICAL / HIGH** |
| `Symmetrical_Governmental_Support_Protocol.md` (L148, L245) | *"Automatic IOSS registration for quarterly settlement"* | **IOSS settlement is MONTHLY** (EU VAT Directive). OSS settlement is QUARTERLY. Update text to reflect monthly IOSS filing. | **MEDIUM** |
| `By_Sommer_Compliance_Book_Consolidated.md` (Section 7.2) | `Art. 16 \| Obligations of deployers` | Under EU AI Act Reg (EU) 2024/1689: **Art. 16 = Obligations of providers**. **Art. 26 = Obligations of deployers**. | **MEDIUM** |
| `By_Sommer_Compliance_Book_Consolidated.md` (L358, L464) & `L-LEG` (L291) | *"NIS2 incident reporting procedures operational (24h/72h/15-day timelines)"* | NIS2 final report is **1 month (30 days)** (Directive (EU) 2022/2555 Art. 23). The **15-day** deadline applies to **EU AI Act Art. 73** serious incident reports. | **MEDIUM** |
| `TONE_PATENT_SPECIFICATION.md` (L188-193) & `CLAIMS_DRAFT.md` (Claim 2) | Describes `cpr_zk_hash` as "anonymized" or "non-reversible hash" | Under GDPR Recital 26, a static ID hash is **pseudonymous personal data**. Frame as pseudonymous data protected under GDPR Art. 25/32 or specify salted ZK commitments. | **LOW / FORMAL** |

---

## Detailed Audit Summary: Missing Regulatory References

1. **Danish Sickness Benefits Act (*Sygedagpengeloven* - LBK nr 1293/2021):**
   - **Missing:** Must be cited in `TONE_PATENT_SPECIFICATION.md` (Section 2.5) and `By_Sommer_Compliance_Book_Consolidated.md` (Section 2.5).
   - **Details:** Must explain the **30-day employer period (*arbejdsgiverperiode*)** under § 30, and how NemRefusion is invoked for **Day 31+ municipal reimbursement** under § 40+.
2. **EU-Wide €10,000 OSS Threshold (Council Directive 2006/112/EC):**
   - **Missing:** Must be added to `Symmetrical_Governmental_Support_Protocol.md` (Section 3 & Section 8).
   - **Details:** Explain that intra-EU B2C cross-border sales exceeding €10,000 annually trigger destination VAT registration via Union OSS.
3. **General Product Safety Regulation (GPSR Regulation (EU) 2023/988):**
   - **Missing:** Must be cited in `IP_Anti_Counterfeiting_Protocol.md` (Section 2) and `Symmetrical_Governmental_Support_Protocol.md` (Section 3).
   - **Details:** Replaced Directive 2001/95/EC in Dec 2024. Governs BDT product safety verification and responsible person requirements for EU dropshipping.
4. **Formal eIDAS 2 Regulation Citation:**
   - **Missing:** Add full citation **Regulation (EU) 2024/1183** to Compliance Book Section 2.4.

---

## Actionable Recommended Fixes (Remediation Plan)

### Fix 1: Fix NemRefusion Payload Privacy Violation
- **File:** `bysommer_archive/patent/TONE_PATENT_SPECIFICATION.md`
- **Location:** Section 2.5 (Line 154)
- **Change:**
  ```markdown
  - OLD: 3. A declaration type code (e.g., SICKNESS_FEBRILE)
  + NEW: 3. A binary incapacity status flag (IS_INCAPACITATED = TRUE) and timestamp (without clinical diagnosis indicators, preserving compliance with Danish Helbredsoplysningsloven § 1/2 and GDPR Art. 9)
  ```
- **File:** `bysommer_archive/patent/DIAGRAMS_DESCRIPTION.md`
- **Location:** FIG. 4 description (Line 137, Line 143)
- **Change:** Remove references to `SICKNESS_FEBRILE` and replace with `IS_INCAPACITATED`.

### Fix 2: Incorporate *Sygedagpengeloven* Framework
- **Files:** `bysommer_archive/patent/TONE_PATENT_SPECIFICATION.md` (Section 2.5) & `bysommer_archive/03_Compliance_Legal/By_Sommer_Compliance_Book_Consolidated.md` (Section 2.5)
- **Action:** Add subsection describing the two-stage sick leave model under *Sygedagpengeloven*:
  1. Days 1–30: Employer period (*arbejdsgiverperiode*). Local PDT generates private sickness notice for employer.
  2. Day 31+: Municipal takeover (*kommune*). NemRefusion bridge transmits authenticated `cpr_zk_hash` payload for municipal reimbursement.

### Fix 3: Correct IOSS Settlement Frequencies & Add €10,000 OSS Threshold
- **File:** `bysommer_archive/01_Core_Architecture_Protocols/Symmetrical_Governmental_Support_Protocol.md`
- **Location:** Lines 148, 231, 245, 284–285
- **Action:** 
  - Change "IOSS quarterly settlement" to "IOSS monthly settlement".
  - Add explicit rule for the **€10,000 EU-wide cross-border B2C OSS threshold** alongside the domestic DKK 50,000 Danish VAT registration threshold.

### Fix 4: Correct EU AI Act Article Mapping
- **File:** `bysommer_archive/03_Compliance_Legal/By_Sommer_Compliance_Book_Consolidated.md`
- **Location:** Section 7.2 Table
- **Action:**
  - Update row `Art. 16` to read: `Art. 16 | Obligations of providers of high-risk AI systems`.
  - Add row: `Art. 26 | Obligations of deployers of high-risk AI systems | By Sommer / client deployer operational obligations`.

### Fix 5: Disambiguate NIS2 and AI Act Incident Reporting Timelines
- **Files:** `bysommer_archive/03_Compliance_Legal/By_Sommer_Compliance_Book_Consolidated.md` (L358, L464) & `bysommer_archive/03_Compliance_Legal/L-LEG_Living_Legal_Operating_System.md` (L291)
- **Action:** Replace conflated "NIS2 (24h/72h/15-day)" text with distinct dual-track timelines:
  - **NIS2 Track (Directive (EU) 2022/2555 Art. 23):** 24h Early Warning -> 72h Incident Notification -> 1 Month Final Report.
  - **EU AI Act Track (Regulation (EU) 2024/1689 Art. 73):** Serious incident reporting without delay and no later than 15 days after awareness.

---

*Report compiled and verified against current Danish legislation (Retsinformation.dk) and EU Regulations (EUR-Lex) as of August 2026.*
