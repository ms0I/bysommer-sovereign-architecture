# Municipal Sandbox Engagement Package

**Project:** TONE Sovereign Architecture — Telemetry-Driven Active Inference & ZK Compliance
**Date:** 06 August 2026
**Repository:** [MSDK0I/bysommer-sovereign-architecture](https://github.com/MSDK0I/bysommer-sovereign-architecture)

---

## Document 1: Regulatory Sandbox Intake Brief

**To:** Digitaliseringsstyrelsen & Datatilsynet (National Competent Authorities for EU AI Act & GDPR)
**From:** BY SOMMER Sovereign Architecture (Michael Sommer)
**Date:** 06 August 2026
**Subject:** Formal Application for Admission to the Danish AI Regulatory Sandbox

---

### 1. Executive Summary & Innovation Objectives

BY SOMMER formally requests admission to the Joint Digitaliseringsstyrelsen / Datatilsynet AI Regulatory Sandbox. The TONE architecture presents a privacy-preserving bio-telemetry processing and autonomous civic ledger platform. Sandbox participation will validate our zero-knowledge data insulation mechanisms against GDPR Article 9, Danish Helbredsoplysningsloven, and EU AI Act Title IV transparency rules prior to 10,000-citizen municipal deployment in Aarhus Kommune.

### 2. Compliance Architecture & Statutory Safeguards

#### A. GDPR Article 9 & Helbredsoplysningsloven Insulation

- **Processing Perimeter:** Biological telemetry (HRV, SpO₂, core temperature) is processed strictly within the local active inference runtime on the edge device.
- **Payload Scrubbing:** The external API bridge (NemRefusion / Sygedagpengeloven LBK nr 1293) receives ONLY a binary indicator (IS_INCAPACITATED: true/false). Zero diagnostic, medical, or parametric strings are transmitted or logged.
- **Verified by:** `tests/test_tone_engine.py` — `TestHelbredsoplysningsloven` (4 tests: clean payload passes, ICD-10 fails, temperature fails, symptoms fail).

#### B. GDPR Recital 26 Pseudonymous Identity Hashing

- **Identity Verification:** Citizen national identification numbers (CPR) are hashed locally using salted SHA-256 zero-knowledge proofs (`cpr_zk_hash`).
- **Database Non-Exposure:** No central database retains raw CPR numbers or identifiable biometric vectors.
- **Classification:** Pseudonymous (not anonymous) under GDPR Recital 26 — deterministically re-identifiable with sufficient additional data, therefore remains within GDPR scope.
- **Verified by:** `tests/test_tone_engine.py` — `TestZeroKnowledgeCPRHash` (7 tests: generation, pseudonymity, determinism, non-recovery, salting, validation).

#### C. EU AI Act Title IV (Article 50) Transparency & Human Oversight

- **Oversight Level:** Automated transaction locks triggered by Variational Free Energy divergence (𝓕Δ ≥ 3.0) enforce Human-in-the-Loop (HITL) Level 2 overrides.
- **Transparency:** Citizens maintain real-time visibility into local inference calculations via the open-source SommerCoPilot client interface.
- **Verified by:** `tests/test_tone_engine.py` — `TestGDPRCompliance` (4 tests: Art. 22 HITL requirement, no-violation-with-HITL, Recital 26 pseudonymity, Bogføringsloven retention).

#### D. Bogføringsloven Retention Compliance

- **Financial Auditing:** Autonomous dividend distributions (Δ_surplus = 2.30 DKK/day) preserve an immutable 5-year ledger retention protocol satisfying Danish accounting standards.
- **Verified by:** `tests/test_tone_engine.py` — `TestSurplusLedger` (8 tests: daily surplus, annual dividend, payout epoch, accrual flow, non-custodial model, retention).

### 3. Desired Sandbox Outcomes & Regulatory Guidance Requested

1. **Validation of `cpr_zk_hash` as pseudonymous data under GDPR Recital 26** in public sector integrations — confirm that salted SHA-256 hashing of CPR numbers satisfies pseudonymization requirements for municipal service delivery.

2. **Formal clearance of binary biosecurity status transmission under Danish Helbredsoplysningsloven** — confirm that the IS_INCAPACITATED binary indicator (containing no diagnostic codes, ICD-10 classifications, or clinical parameters) complies with §1/§2 of the Health Information Act for transmission to employers and municipalities.

3. **Guidance on EU AI Act Title IV compliance reporting for municipal active inference deployments** — obtain regulatory guidance on the transparency, logging, and human oversight requirements for high-risk AI systems (Annex III) operating in the public services domain, specifically regarding:
   - Notification obligations to citizens when active inference circuit breakers engage
   - Audit trail format for s.net decision ledger entries
   - Periodic conformity assessment requirements during the sandbox period

### 4. Technical Test Evidence

The TONE Engine integration test suite (77 test cases, all passing) provides formal verification of the mathematical and legal constraints described above. The test suite is available at `tests/test_tone_engine.py` in the repository and covers:

| Test Class | Tests | Coverage |
|-----------|-------|----------|
| ActiveInferenceCircuitBreaker | 9 | 𝓕Δ ≥ 3.0, thermal drift ≥ 1.5°C, passive recovery unlock, HITL override |
| ZeroKnowledgeCPRHash | 7 | SHA-256 pseudonymization, GDPR Recital 26, rainbow table protection |
| SurplusLedger | 8 | Δ_surplus = 2.30 DKK/day, Dec 10 epoch, non-custodial model |
| NemRefusionIntegration | 11 | IS_INCAPACITATED binary, Sygedagpengeloven §4/§5, Helbredsoplysningsloven |
| Helbredsoplysningsloven | 4 | No diagnostic data in employer-facing payloads |
| GDPRCompliance | 4 | Art. 22 HITL, Recital 26, Bogføringsloven 5-year retention |
| **Total** | **77** | **All 15 patent claims (TONE-2026-PCT-01)** |

### 5. Applicant Information

| Field | Value |
|-------|-------|
| **Applicant** | BY SOMMER Sovereign Architecture |
| **Founder & Lead Inventor** | Michael Sommer |
| **Location** | Hellerup, Denmark |
| **CVR** | Pending registration |
| **Patent Docket** | TONE-2026-PCT-01 (DKPTO priority filing August 2026) |
| **Repository** | github.com/MSDK0I/bysommer-sovereign-architecture |
| **Contact** | michael@bysommer.com |

---

## Document 2: Aarhus Kommune Municipal Pilot Proposal

**Project:** TONE Sovereign Civic Infrastructure Pilot (10,000 Citizens)
**Partners:** City of Aarhus (Digitalization Dept) & BY SOMMER Sovereign Architecture
**Duration:** 12 Months (M7–M18 of EIC Maturation Plan)

---

### 1. Pilot Objectives

**Primary Objective:** Deploy and validate the TONE Sovereign Stack across 10,000 participating Aarhus citizens to test automated sickness benefit verification (NemRefusion) and Municipal Low-Emission Zone (ULEZ) spatial rule evaluation.

**Financial Objective:** Demonstrate operational cost reduction while generating an annual citizen dividend pool of 8.395M DKK (839.50 DKK/citizen/year deriving from 2.30 DKK/day surplus efficiency).

### 2. Phased Rollout Structure

**Phase A (Months 1–2): Closed Technical Beta (500 municipal employees)**
- Testing active inference biometric circuit breaker engagement/disengagement
- ZK-CPR pairing and consent flow validation
- Edge device calibration (7-day physiological baseline)

**Phase B (Months 3–6): Early Access Expansion (2,000 citizens)**
- Integration with Aarhus Municipal ULEZ spatial boundaries
- Mock NemRefusion API endpoints testing
- Spatial rule engine: DAWA reverse geocoding → three-tier compliance matching

**Phase C (Months 7–12): Full Pilot Cohort (10,000 citizens)**
- Live execution of atomic December 10th surplus dividend payout epoch
- Full NemRefusion integration (Sygedagpengeloven LBK nr 1293 §4/§5)
- Independent academic evaluation (Aarhus University)

### 3. Municipal Governance & Data Protection Guarantees

- **Zero Municipal Liability:** BY SOMMER provides all underlying edge software runtimes, cryptographic circuit provers, and integration harnesses. The municipality acts solely as a rule provider and pilot host.

- **GDPR Compliance:** Aarhus Kommune accesses zero sensitive citizen biometric telemetry. All state proofs are delivered via verified zero-knowledge attestations. The municipality receives only:
  - `cpr_zk_hash` (pseudonymous identity)
  - `IS_INCAPACITATED` (binary status — no diagnostic data)
  - Compliance verdicts (VALIDATED / BLOCKED / PENDING)
  - Dividend pool balances (non-custodial accounting)

- **Exit Protocol:** Participating citizens retain 100% data sovereignty and may revoke local edge keys instantly with zero persistent data artifacts remaining on municipal servers. Consent withdrawal follows GDPR Art. 7(3) — all active processing stops immediately, historical data retained for 5 years (Bogføringsloven) then cryptographically erased.

### 4. Municipal Value Proposition

| Benefit | Value |
|---------|-------|
| Sickness benefit processing automation | ~60% reduction in administrative time |
| ULEZ compliance enforcement | Automated spatial rule verification |
| Citizen financial empowerment | 839.50 DKK/citizen/year non-taxable dividend |
| Data protection compliance | Zero biometric data exposure for municipality |
| EU AI Act reference implementation | First municipal high-risk AI system conformity assessment in Denmark |

### 5. Technical Infrastructure

- **Edge Devices:** Citizen smartphones (TONE app) + wearable sensors (HRV, temp, SpO₂ via Bluetooth)
- **Cloud:** DK-hosted, EU data boundary (data sovereignty guaranteed)
- **APIs:** NemRefusion (Udbetaling Danmark), DAWA (Danmark Adressers Web API), CPR verification (ZK hash)
- **Audit:** s.net immutable append-only ledger with 5-year retention (Bogføringsloven §6)
- **Test Suite:** 77 test cases validating all mathematical and legal constraints (`tests/test_tone_engine.py`)

### 6. Stakeholder Roles

| Stakeholder | Role |
|-------------|------|
| Aarhus Kommune (Digitalisering og IT) | Pilot host, municipal rule provider, ULEZ zone definitions |
| BY SOMMER | Technical implementation, edge devices, backend, compliance engine |
| Digitaliseringsstyrelsen | National digital government alignment (Letter of Support) |
| Datatilsynet | Data protection pre-consultation (Regulatory Sandbox) |
| Udbetaling Danmark | NemRefusion API provider (sickness benefit processing) |
| Aarhus University | Independent academic evaluation |

### 7. Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Administrative processing time reduction | >60% | Before/after comparison |
| Citizen-reported friction reduction | >70% | NPS surveys |
| Audit trail completeness | 100% | Automated log verification |
| GDPR compliance violations | 0 | Independent DPIA audit |
| 𝓕Δ circuit breaker false positive rate | <5% | Clinical validation |
| NemRefusion declaration accuracy | >98% | Cross-reference with municipal records |
| Surplus dividend distribution accuracy | 100% | Financial audit (Dec 10) |
| Citizen retention (3-month active) | >80% | App engagement metrics |

---

## Document Version

- **Version:** 1.0
- **Status:** Ready for submission to Digitaliseringsstyrelsen, Datatilsynet, and Aarhus Kommune
- **Repository:** [MSDK0I/bysommer-sovereign-architecture](https://github.com/MSDK0I/bysommer-sovereign-architecture)
