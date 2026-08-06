# By Sommer — Danish Municipal Pilot Strategy: Aarhus / Copenhagen Deployment Plan

**Document Identifier:** DK_MUNICIPAL_PILOT_STRATEGY.md
**Date Prepared:** 06 August 2026
**Prepared By:** Solas (Archivist) under direction of Michael Sommer
**Status:** Draft for review
**Repository:** [MSDK0I/bysommer-sovereign-architecture](https://github.com/MSDK0I/bysommer-sovereign-architecture)
**Related:** EIC_Accelerator_Application_Framework.md (WP4), DK_to_EU_Deployment_Roadmap.md (Phase 1)

---

## Executive Summary

This document defines the operational rollout plan for deploying the TONE Sovereign Architecture in a Danish municipal pilot targeting **10,000 citizens** in Aarhus or Copenhagen. The pilot validates three core systems: (1) the Active Inference Circuit Breaker (𝓕Δ ≥ 3.0) via NemRefusion sickness benefit integration, (2) Zero-Knowledge CPR hash compliance matching with municipal spatial rules, and (3) the Autonomous Surplus Dividend Ledger with December 10th payout epoch.

**Pilot Duration:** 12 months (Months 6–20 of EIC project timeline)
**Target Citizens:** 10,000 (tiered onboarding: 500 → 2,000 → 10,000)
**Target Municipalities:** Aarhus (primary) or Copenhagen (backup)

---

## 1. Municipal Partner Selection

### 1.1 Primary Target: City of Aarhus

| Criterion | Aarhus | Copenhagen |
|-----------|--------|------------|
| Population | ~350,000 | ~660,000 |
| Digital maturity | High — Digital Aarhus strategy since 2015 | High — Copenhagen Solutions Lab |
| Existing ULEZ/zones | Low Emission Zone (LEZ) active for heavy vehicles | Low Emission Zone (LEZ) + environmental zones |
| NemRefusion integration | Via Udbetaling Danmark (national) | Via Udbetaling Danmark (national) |
| Academic partner proximity | Aarhus University (Computer Science, IT) | IT University of Copenhagen, DTU |
| Pilot scalability | Manageable scale (10K = ~3% of population) | Small fraction (~1.5% of population) |
| Municipal innovation culture | Strong — Aarhus has piloted multiple digital initiatives | Strong — Copenhagen Solutions Lab active |
| Political alignment | Danish digital government strategy alignment | Same |

### 1.2 Engagement Strategy

**Phase A — Pre-Application (August–September 2026):**
- Contact Aarhus Kommune Digital Transformation Office (Digitalisering og IT)
- Present TONE Architecture as alignment with Aarhus's digital strategy
- Frame pilot as: bureaucracy elimination + citizen health protection + cost savings
- Leverage Digitaliseringsstyrelsen as national-level sponsor

**Phase B — Letter of Intent (by October 2026):**
- Secure formal LoI from municipal CIO/Digital Director
- Define pilot scope, citizen recruitment plan, municipal API access
- Establish data processing agreement (Databehandleraftale) per GDPR Art. 28

**Phase C — Partnership Agreement (by Month 6 of project):**
- Formal municipal partnership agreement signed
- Pilot deployment plan finalized with municipal IT team
- DPIA (Data Protection Impact Assessment) completed and approved by Datatilsynet

### 1.3 Key Stakeholders

| Stakeholder | Role | Engagement |
|-------------|------|------------|
| Aarhus Kommune (Digitalisering og IT) | Pilot host, municipal rule provider | LoI → Partnership Agreement |
| Digitaliseringsstyrelsen | National digital government sponsor | Letter of Support |
| Datatilsynet | Data protection authority | Pre-consultation on ZK-CPR pseudonymization |
| Udbetaling Danmark (NemRefusion) | Sickness benefit API provider | Technical Partnership |
| Sundhedsdatastyrelsen | Health data authority | Advisory (Planetary Shield data governance) |
| Aarhus University (Dept. of Computer Science) | Independent academic evaluator | Subcontract / LoI |
| DAWA (Danmark Adressers Web API) | Address/municipal geocoding | Public API integration |
| CPR-kontoret (Danish Civil Registration) | CPR number verification (ZK hash) | Pre-consultation on cpr_zk_hash approach |

---

## 2. Citizen Onboarding Flow

### 2.1 Three-Tier Onboarding Strategy

```
Tier 1: Beta Cohort (Month 9-12)
  │  500 citizens — municipal employees + recruited volunteers
  │  Focus: Functional testing, consent flow, 𝓕Δ calibration
  │
  ▼
Tier 2: Early Access (Month 12-15)
  │  2,000 citizens — open enrollment with targeted recruitment
  │  Focus: Scale testing, NemRefusion integration, ULEZ rules
  │
  ▼
Tier 3: Full Pilot (Month 15-20)
  │  10,000 citizens — open enrollment, public outreach
  │  Focus: Metrics collection, independent evaluation, case study
  │
  ▼
Evidence Dossier (Month 20)
```

### 2.2 Citizen Onboarding Pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│                    CITIZEN ONBOARDING FLOW                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. DISCOVERY                                                   │
│     └─ Municipal portal / app store / community outreach        │
│                                                                  │
│  2. IDENTITY VERIFICATION (ZK-CPR)                              │
│     └─ Citizen presents CPR number                              │
│     └─ System computes cpr_zk_hash (zero-knowledge)             │
│     └─ Hash verified against municipal CPR register             │
│     └─ NO raw CPR number stored or transmitted                  │
│                                                                  │
│  3. GDPR CONSENT (Art. 7 Explicit Consent)                      │
│     └─ Consent screen: "I consent to processing of my          │
│        pseudonymized health telemetry for automated             │
│        sickness benefit declarations and financial safety"      │
│     └─ Granular toggles:                                        │
│        [✓] Active inference (𝓕Δ anomaly detection)             │
│        [✓] NemRefusion integration (sick leave automation)      │
│        [✓] Surplus dividend accrual                            │
│        [✓] SommerCoPilot advisory interface                     │
│        [ ] Planetary Shield (anonymous epidemiological signal)   │
│     └─ Withdrawal protocol documented (GDPR Art. 7(3))         │
│                                                                  │
│  4. BASELINE CALIBRATION (7-day)                                │
│     └─ 7-day physiological baseline collection                  │
│     └─ Heart rate variability (HRV), temperature, SpO₂         │
│     └─ Baseline stored locally on edge device                    │
│     └─ 𝓕Δ = 0 at baseline (no anomaly detected)                 │
│                                                                  │
│  5. WALLET ACTIVATION                                           │
│     └─ Citizen digital wallet activated                         │
│     └─ Surplus dividend accrual begins (2.30 DKK/day)           │
│     └─ Transaction pre-booking enabled (with 𝓕Δ circuit breaker)│
│                                                                  │
│  6. SOMMERCOPILOT ONBOARDING                                    │
│     └─ Nordic Calm Voice framework activated                    │
│     └─ Advisory-only interface (no automated decisions)         │
│     └─ GDPR Art. 22 HITL confirmation screen                    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 2.3 Consent Management Architecture

**Consent Record Structure (pseudonymized):**
```json
{
  "user_id": "cpr_zk_hash:0x7a3f...e9b2",
  "consent_timestamp": "2026-09-15T10:30:00Z",
  "consent_version": "1.0",
  "consent_grants": {
    "active_inference": true,
    "nemrefusion_integration": true,
    "surplus_dividend": true,
    "sommercopilot": true,
    "planetary_shield": false
  },
  "withdrawal_protocol": "available_via_app_settings",
  "retention": "5_years_post_withdrawal_bogforingsloven"
}
```

**Consent Withdrawal Flow:**
1. Citizen opens app → Settings → Privacy → Withdraw Consent
2. System confirms withdrawal scope (which features will be disabled)
3. All active processing stops immediately
4. Surplus dividend accrual pauses
5. Historical data retained for 5 years (Bogføringsloven) then cryptographically erased
6. cpr_zk_hash remains on record for audit trail (pseudonymous, non-identifying)

### 2.4 Recruitment Strategy

| Channel | Target | Method |
|---------|--------|--------|
| Municipal employee program | 200 | Internal email, intranet, town hall presentation |
| Aarhus University students | 100 | Computer Science department partnership |
| General public — digital channels | 3,000 | MitDigital.dk platform, municipal app, social media |
| General public — physical outreach | 1,700 | Libraries, Borgerservice centers, community events |
| Targeted demographics (diversity) | 4,000 | Senior citizens (65+), self-employed, families with children |
| Total | 10,000 | |

**Diversity Requirements:**
- Age: 18-30 (20%), 31-50 (35%), 51-65 (25%), 65+ (20%)
- Gender: approximately 50/50
- Employment: employed (50%), self-employed (15%), students (15%), retired (15%), unemployed (5%)
- Geographic: central Aarhus (40%), suburban (40%), rural municipality (20%)

---

## 3. NemRefusion API Integration Plan

### 3.1 NemRefusion Overview

NemRefusion is Denmark's national digital infrastructure for sickness benefit processing, operated by Udbetaling Danmark. The system connects:
- **Employers** (reporting sick days via digital forms)
- **Municipalities** (administering sickness benefits after Day 31)
- **Udbetaling Danmark** (national processing)
- **Citizens** (receiving benefits)

### 3.2 TONE-NemRefusion Integration Flow

```
┌─────────────────────────────────────────────────────────────────┐
│              TONE-NEMREFUSION INTEGRATION FLOW                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  EDGE DEVICE (PDT)                                              │
│  ┌───────────────┐                                              │
│  │ Physiological  │  HRV, T, SpO₂ → local computation          │
│  │ telemetry     │  𝓕Δ = divergence from 7-day baseline       │
│  │ (local only)  │  IF 𝓕Δ ≥ 3.0 AND thermal_drift ≥ 1.5°C:    │
│  │               │    → Status: IS_INCAPACITATED = true        │
│  │               │    → NO diagnostic strings transmitted      │
│  └───────┬───────┘                                              │
│          │                                                       │
│          ▼                                                       │
│  ZERO-KNOWLEDGE BRIDGE                                           │
│  ┌───────────────┐                                              │
│  │ ZK Proof      │  cpr_zk_hash → identity proof                │
│  │ Generation    │  IS_INCAPACITATED → status proof              │
│  │               │  Timestamp → temporal proof                  │
│  │               │  Signature → authenticity proof              │
│  └───────┬───────┘                                              │
│          │                                                       │
│          ▼                                                       │
│  NEMREFUSION API                                                 │
│  ┌───────────────┐                                              │
│  │ Declaration   │  Payload: {                                  │
│  │ Submission    │    cpr_zk_hash: "0x7a3f...e9b2",             │
│  │               │    status: "IS_INCAPACITATED",               │
│  │               │    timestamp: "2026-09-20T08:00:00Z",        │
│  │               │    jurisdiction: "DK_AARHUS",                │
│  │               │    signature: "ed25519:0x..."                │
│  │               │  }                                           │
│  │               │  NO diagnostic codes (Helbredsoplysningsloven)│
│  └───────┬───────┘                                              │
│          │                                                       │
│          ▼                                                       │
│  EMPLOYER NOTIFICATION                                           │
│  ┌───────────────┐                                              │
│  │ Day 1-30:     │  Employer receives: "IS_INCAPACITATED"       │
│  │ Employer      │  (binary status only — no diagnosis)         │
│  │ Period        │  Sygedagpengeloven LBK nr 1293 §4:          │
│  │               │  Employer pays sick pay for first 30 days    │
│  └───────┬───────┘                                              │
│          │                                                       │
│          ▼                                                       │
│  MUNICIPAL TAKEOVER                                              │
│  ┌───────────────┐                                              │
│  │ Day 31+:      │  Aarhus Kommune receives:                    │
│  │ Municipal     │  IS_INCAPACITATED + cpr_zk_hash              │
│  │ Period        │  Municipal sickness benefit (sygedagpenge)   │
│  │               │  No clinical data transmitted ( GDPR Art. 9) │
│  └───────────────┘                                              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 3.3 Sygedagpengeloven Compliance Matrix

| LBK nr 1293 Provision | TONE Implementation | Verification |
|------------------------|---------------------|-------------|
| §4: Employer sick pay (Day 1-30) | Automatic declaration to employer on Day 1 | IS_INCAPACITATED binary status |
| §5: Municipal takeover (Day 31+) | Automatic transfer to Aarhus Kommune on Day 31 | Timestamp-based handoff |
| §7: Medical certificate | HITL Level 2 — doctor confirms if 𝓕Δ sustained >7 days | Human override required |
| §9: Gradual return | 𝓕Δ recovery tracking (passive: 𝓕Δ < 1.0 unlocks) | Edge device monitoring |
| §10: Fit-for-work assessment | SommerCoPilot advisory (non-binding) | Advisory-only, HITL confirmed |
| §54: Reporting | s.net immutable audit log of all declarations | Append-only ledger |

### 3.4 Helbredsoplysningsloven Compliance

| Requirement | TONE Implementation |
|-------------|---------------------|
| §1: Health information may only be processed for explicit purpose | Purpose: automated sickness benefit declaration (consented) |
| §2: Health data must not be disclosed to unauthorized parties | Zero-knowledge proofs — no health data leaves edge device |
| §3: Processing requires informed consent | GDPR Art. 7 explicit consent with granular toggles |
| §6: Data minimization | IS_INCAPACITATED binary — no diagnostic codes transmitted |
| §10: Right to information | SommerCoPilot transparency interface |

### 3.5 API Integration Timeline

| Month | Milestone |
|-------|-----------|
| M1-M3 | Pre-consultation with Udbetaling Danmark on API access |
| M4-M6 | Technical API integration (sandbox/testing environment) |
| M7-M9 | Beta testing with 500 citizens (Tier 1) |
| M10-M12 | Scale testing with 2,000 citizens (Tier 2) |
| M13-M15 | Full integration validation with 10,000 citizens (Tier 3) |
| M16-M20 | Production monitoring and metrics collection |

---

## 4. ULEZ Spatial Rule Testing Plan

### 4.1 Municipal Geofencing Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                  SPATIAL RULE ENGINE                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  GPS COORDINATES (from BDT transaction)                         │
│  ┌───────────────┐                                              │
│  │ lat: 56.1629  │  → DAWA API reverse geocode                  │
│  │ lon: 10.2039  │  → Municipal boundary detection              │
│  └───────┬───────┘  → Zone classification                       │
│          │                                                       │
│          ▼                                                       │
│  THREE-TIER RULE MATCHING                                        │
│  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐      │
│  │ Tier 1: EU    │→ │ Tier 2: DK     │→ │ Tier 3: Aarhus │      │
│  │ (IOSS, CE)    │  │ (VAT, national)│  │ (ULEZ, local)  │      │
│  └───────┬───────┘  └───────┬───────┘  └───────┬───────┘      │
│          └────────────────────┴────────────────────┘             │
│                              │                                   │
│                              ▼                                   │
│  ZK PROOF GENERATION                                           │
│  ┌───────────────┐                                              │
│  │ cpr_zk_hash   │  → Identity verified                          │
│  │ spatial_match │  → Location verified                          │
│  │ rule_outcome  │  → VALIDATED / BLOCKED / PENDING              │
│  └───────────────┘                                              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 4.2 Aarhus Spatial Rules to Test

| Rule | Type | Zone Definition | Enforcement |
|------|------|-----------------|-------------|
| Low Emission Zone (LEZ) | Environmental | Central Aarhus — Diesel restriction (Euro 6+) | BLOCK non-compliant vehicle transactions |
| Noise ordinance | Time-based | Residential zones — 22:00-06:00 | ADVISORY (SommerCoPilot notification) |
| Municipal parking zones | Spatial | Zone 1 (center), Zone 2 (mid), Zone 3 (outer) | VALIDATE parking fee compliance |
| School zone speed limits | Time + Spatial | 500m radius, 07:00-16:00 school days | ADVISORY (speed reminder) |
| Construction permits | Spatial + Temporal | Designated construction zones | VALIDATE permit-linked transactions |
| Local tax rules | Spatial | Aarhus Kommune municipal boundary | VALIDATE municipal tax (kommuneskat) |

### 4.3 DAWA API Integration

| Parameter | Value |
|-----------|-------|
| API | Danmark Adressers Web API (DAWA) |
| Endpoint | `https://dawa.aws.dk/adgangsadresser` |
| Purpose | Reverse geocoding: GPS → municipal boundary → zone classification |
| Data returned | Municipality code, street, postal code, zone designation |
| Rate limit | Public API, no authentication required (fair use) |
| Integration | Backend function `reverseGeocode(lat, lon) → municipality, zone` |

### 4.4 ULEZ Testing Protocol

**Test Scenario 1 — Valid LEZ Entry:**
1. BDT transaction initiated at GPS within LEZ zone
2. DAWA reverse geocode confirms Aarhus central zone
3. Vehicle compliance verified (Euro 6+ via Danish Motorregister lookup)
4. ZK proof generated: VALIDATED
5. Transaction authorized

**Test Scenario 2 — Non-Compliant LEZ Entry:**
1. BDT transaction initiated at GPS within LEZ zone
2. DAWA reverse geocode confirms Aarhus central zone
3. Vehicle compliance check fails (Euro 5 or below)
4. ZK proof generated: BLOCKED
5. Transaction blocked + SommerCoPilot advisory notification

**Test Scenario 3 — Cross-Border (Aarhus → Copenhagen):**
1. Citizen travels from Aarhus to Copenhagen
2. GPS re-geocoding detects municipal boundary change
3. Rule engine switches from Aarhus rules to Copenhagen rules
4. Copenhagen LEZ rules applied (potentially stricter)
5. Stricter-rule-wins principle applied

**Test Scenario 4 — EU Cross-Border (DK → DE):**
1. BDT transaction initiated from DK in German border zone
2. Tier 1 (EU) rules: IOSS VAT validation
3. Tier 2 (National) rules: German VAT (19%) replaces Danish VAT (25%)
4. Tier 3 (Municipal): No Danish ULEZ rules apply
5. ZK proof: VALIDATED with German jurisdiction

---

## 5. Pilot Metrics & Evaluation

### 5.1 Success Metrics (from Deployment Roadmap)

| Metric | Target | Measurement Method | Frequency |
|--------|--------|-------------------|-----------|
| Administrative processing time reduction | >60% | Before/after comparison on pilot services | Quarterly |
| Citizen-reported friction (UX) | >70% reduction | Survey / NPS scores | Monthly |
| Audit trail completeness | 100% of decisions logged | Automated log verification | Continuous |
| HITL escalations resolved within SLA | >95% | SLA monitoring dashboard | Weekly |
| ZK verification success rate | >99% | Cryptographic proof validation rate | Continuous |
| Misinterpretation firewall accuracy | <5% false positive rate | Measured against ground truth | Monthly |
| GDPR compliance violations | 0 | Independent DPIA audit | End of pilot |
| 𝓕Δ circuit breaker false positive rate | <5% | Clinical validation | Monthly |
| 𝓕Δ circuit breaker false negative rate | <2% | Clinical validation | Monthly |
| NemRefusion declaration accuracy | >98% | Cross-reference with municipal records | Monthly |
| Surplus dividend distribution accuracy | 100% | Financial audit | December 10th |
| Citizen retention (active after 3 months) | >80% | App engagement metrics | Monthly |

### 5.2 Independent Academic Evaluation

| Parameter | Value |
|-----------|-------|
| Evaluator | IT University of Copenhagen OR Aarhus University (Dept. Computer Science) |
| Scope | Technical accuracy, privacy compliance, social impact, citizen satisfaction |
| Methodology | Mixed-methods: quantitative metrics + qualitative interviews (N=200 sample) |
| Deliverable | Independent Pilot Evaluation Report (D4.3, Month 22) |
| Budget | €30,000 (subcontracted from WP4) |

### 5.3 Citizen Feedback Channels

- **In-app feedback:** Weekly pulse survey (3 questions, <30 seconds)
- **Monthly deep survey:** NPS + friction questions + open text (N=500 random sample)
- **Quarterly focus groups:** 15 citizens per group, 4 groups total
- **Exit interviews:** All citizens who withdraw consent (GDPR Art. 7(3) withdrawal)
- **Continuous dashboard:** Real-time engagement metrics (DAU, MAU, session length)

---

## 6. Technical Infrastructure

### 6.1 Deployment Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                  PILOT INFRASTRUCTURE                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  EDGE DEVICES (10,000)                                          │
│  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐      │
│  │ Smartphone    │  │ Wearable      │  │ Edge gateway  │      │
│  │ (TONE app)    │  │ (HRV, T, SpO₂)│  │ (home hub)    │      │
│  │ 𝓕Δ local     │  │ BT/ANT+       │  │ Aggregation   │      │
│  │ ZK proof gen  │  │               │  │               │      │
│  └───────┬───────┘  └───────┬───────┘  └───────┬───────┘      │
│          └─────────────────┴─────────────────┘                 │
│                              │                                   │
│          (TLS 1.3 — ZK proofs only, no raw telemetry)          │
│                              │                                   │
│          ▼                                                       │
│  DK-HOSTED CLOUD (Data Sovereignty)                             │
│  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐      │
│  │ Base44        │  │ NemRefusion   │  │ DAWA API      │      │
│  │ Backend       │  │ Integration   │  │ Geocoding     │      │
│  │ (9 entities)  │  │ Bridge        │  │ Service       │      │
│  └───────┬───────┘  └───────┬───────┘  └───────┬───────�      │
│          └─────────────────┴─────────────────┘                 │
│                              │                                   │
│          ▼                                                       │
│  s.net AUDIT LEDGER                                             │
│  ┌───────────────┐                                              │
│  │ Immutable     │  All decisions logged with provenance        │
│  │ Append-only   │  5-year retention (Bogføringsloven)          │
│  │ Cryptographic │  Independent verification capability        │
│  └───────────────┘                                              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 6.2 Infrastructure Requirements

| Component | Specification | Provider |
|-----------|--------------|----------|
| Cloud hosting | DK-hosted, EU data boundary | Deic / Cloud.dk / Scalingo DK |
| Edge app | iOS + Android (React Native) | By Sommer |
| Wearable integration | Bluetooth HRV, temperature, SpO₂ | Open APIs (Garmin, Polar, Apple Health) |
| Backend | Base44 managed (9 entities, 4+ backend functions) | Base44 platform |
| s.net audit | Append-only, cryptographically signed | PostgreSQL + cryptographic chain |
| API gateway | NemRefusion, DAWA, CPR verification | Danish government APIs |
| Monitoring | Real-time dashboards, alerting | Grafana / Prometheus |

### 6.3 Data Sovereignty Guarantees

- **All processing within EU:** DK-hosted cloud, no non-EU data transfers
- **Raw telemetry stays on edge:** Only ZK proofs and 𝓕Δ values transmitted
- **CPR numbers never stored:** Only cpr_zk_hash (pseudonymous, GDPR Recital 26)
- **Audit trail:** s.net immutable ledger with 5-year retention (Bogføringsloven)
- **Right to erasure:** Cryptographic erasure of consent records after retention period

---

## 7. Regulatory Compliance Checklist

| Requirement | Authority | Status | Action |
|-------------|-----------|--------|--------|
| DPIA (Data Protection Impact Assessment) | Datatilsynet | ☐ | Draft before pilot launch |
| Data Processing Agreement (Art. 28) | Aarhus Kommune | ☐ | Sign before pilot launch |
| Explicit consent (Art. 7) | Internal | ☐ | Consent UI implemented |
| Automated decision-making (Art. 22) | Internal | ✅ | HITL Level 2 override implemented |
| Helbredsoplysningsloven compliance | Datatilsynet | ☐ | Pre-consultation on ZK-CPR approach |
| Sygedagpengeloven compliance | Udbetaling Danmark | ☐ | NemRefusion API integration agreement |
| Bogføringsloven 5-year retention | Internal | ✅ | s.net audit ledger configured |
| EU AI Act conformity (Annex III) | Notified Body | ☐ | Conformity assessment in WP4 |
| eIDAS 2 alignment | Digitaliseringsstyrelsen | ☐ | EUDI Wallet mapping |
| NIS2 incident reporting | CSIRT | ☐ | Register as essential entity if scaling |

---

## 8. Pilot Timeline

| Month | Phase | Key Activities |
|-------|-------|---------------|
| M6 | Setup | Municipal partnership signed, DPIA completed, infrastructure deployed |
| M7 | Setup | NemRefusion sandbox access, DAWA integration, consent UI built |
| M8 | Setup | Beta testing infrastructure, edge device deployment |
| M9 | Tier 1 (500) | Beta cohort onboarded, 𝓕Δ calibration begins |
| M10 | Tier 1 | NemRefusion integration tested with beta cohort |
| M11 | Tier 1 | ULEZ spatial rules tested with beta cohort |
| M12 | Tier 1 | First metrics collection, 𝓕Δ calibration validated |
| M13 | Tier 2 (2,000) | Early access enrollment opens |
| M14 | Tier 2 | NemRefusion scale testing |
| M15 | Tier 2 | ULEZ cross-border testing |
| M16 | Tier 3 (10,000) | Full pilot enrollment opens |
| M17 | Tier 3 | Surplus dividend accrual monitoring |
| M18 | Tier 3 | Full metrics collection begins |
| M19 | Tier 3 | Independent evaluation begins |
| M20 | Wrap-up | Case study published, evidence dossier compiled |

### December 10th Payout Epoch

The pilot's first surplus dividend distribution is scheduled for **December 10, 2026** (or December 10 of the first full pilot year). Citizens onboarded before this date will receive a pro-rated dividend based on their accrual period:

- Onboarded at M9 (September 2026): ~3 months × 2.30 DKK/day × 30 = ~207 DKK
- Onboarded at M13 (January 2027): N/A (first payout is Dec 10, 2026)
- Subsequent payout: December 10, 2027 (full year: 839.50 DKK/citizen)

---

## 9. Risk Register (Pilot-Specific)

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|-----------|
| Aarhus Kommune declines partnership | Medium | Critical | Copenhagen as backup; leverage Digitaliseringsstyrelsen |
| NemRefusion API access denied | Low | High | Pre-consultation M1-M3; Udbetaling Danmark engagement |
| Datatilsynet objects to cpr_zk_hash | Medium | High | Pre-consultation; frame as GDPR Recital 26 pseudonymization |
| 𝓕Δ threshold too aggressive (false positives) | Medium | Medium | 7-day baseline calibration; clinical validation in Tier 1 |
| Citizen recruitment shortfall | Low | Medium | Multi-channel recruitment; municipal employee program |
| Edge device hardware failures | Medium | Medium | Device warranty; replacement pool (5% spare) |
| Consent withdrawal rate >15% | Medium | Medium | User experience optimization; SommerCoPilot engagement |
| Budget overrun | Low | Medium | 70% co-funding; EUopSTART pre-financing |

---

## Document Version

- **Version:** 1.0
- **Status:** Draft for review
- **Next action:** Begin Aarhus Kommune engagement (Phase A pre-application)
- **Repository:** [MSDK0I/bysommer-sovereign-architecture](https://github.com/MSDK0I/bysommer-sovereign-architecture)
