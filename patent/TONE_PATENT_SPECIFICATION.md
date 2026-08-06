# TONE PATENT SPECIFICATION

**TITLE OF THE INVENTION:**  
System and Method for Telemetry-Driven Active Inference, Zero-Knowledge Jurisdictional Compliance, and Autonomous Dividend Accrual (TONE Architecture)

**APPLICANT:** By Sommer  
**DOCUMENT:** Full Patent Specification — Technical Background, Detailed Description, and Enablement  
**STATUS:** Draft for Filing  
**DATE:** 2026-08-06  

---

## CROSS-REFERENCE TO RELATED APPLICATIONS

Not applicable. This application claims the benefit of no prior provisional or non-provisional application.

---

## FIELD OF THE INVENTION

The present invention relates generally to sovereign digital infrastructure systems and, more specifically, to: (1) real-time physiological anomaly detection using active inference theory applied to zero-knowledge biometric telemetry; (2) autonomous financial circuit-breaking triggered by biosecurity threshold breaches; (3) location-aware multi-tier jurisdictional compliance verification using zero-knowledge identity proofs; and (4) decentralized non-profit surplus accrual and distribution mechanisms for citizen dividend systems.

---

## BACKGROUND OF THE INVENTION

### The Problem of Sovereign Digital Identity

Existing digital identity systems suffer from a fundamental tension: systems that provide robust compliance verification require access to personally identifiable information (PII), while systems that protect privacy cannot verify compliance. National civil registration systems (such as the Danish CPR system) provide unique citizen identification, but exposing CPR numbers to commercial compliance engines creates severe privacy and security risks under GDPR (General Data Protection Regulation, Regulation (EU) 2016/679).

No existing system provides a method for validating regulatory compliance (tax, trade, product safety) against a verified citizen identity without transmitting the underlying identity credential to the compliance verification system.

### The Problem of Autonomous Financial Safety

Autonomous financial agents acting on behalf of users (e.g., personal digital twins that pre-book maintenance, subscriptions, and discretionary purchases) create novel risks: if the user experiences a physiological emergency (fever, cardiac event, respiratory distress), the autonomous agent continues executing financial commitments without awareness of the user's physical state.

No existing system provides a mechanism for continuously monitoring physiological telemetry through zero-knowledge proofs and automatically freezing autonomous financial operations upon detecting a health anomaly, without requiring the financial system to access raw biometric data.

### The Problem of Jurisdictional Specificity

Modern regulatory compliance is not uniform. A transaction that is legal in one municipality may be restricted in another. Environmental zones, noise ordinances, water quality thresholds, and construction permits vary by local administrative jurisdiction. Existing compliance systems apply rules at the national level and cannot dynamically load municipal rules based on the physical location of the transacting party.

### The Problem of Non-Profit Operational Surplus Distribution

In sovereign digital infrastructure operated on a non-profit basis, the difference between a baseline operational allocation and actual operating cost produces a daily surplus. No existing system provides an automated mechanism for accruing this surplus in a zero-knowledge vault and distributing it as a non-taxable citizen dividend on a fixed calendar epoch.

---

## SUMMARY OF THE INVENTION

The present invention, referred to herein as the TONE Architecture (Telemetry-Driven Active Inference and Sovereign Privacy Protocol), addresses the foregoing problems through a unified system comprising three independent subsystems and a biosecurity escalation bridge:

### Subsystem 1: Biosecurity and Execution Circuit-Breaker (Claims 1, 4–8, 15)

A computer-implemented system that continuously receives anonymized physiological state vectors (heart rate variability, core body temperature, respiratory rate, blood oxygen saturation) from a personal digital twin via zero-knowledge proof transmission. An active inference computing module calculates the variational free-energy divergence (𝓕Δ) between an expected homeostatic baseline and the observed physiological state. When 𝓕Δ exceeds a safety threshold (≥3.0 or thermal drift ≥1.5°C), the system emits an anomaly state signal. A compliance execution engine receiving this signal automatically freezes all queued autonomous financial pre-bookings associated with the user by setting their monthly spending cap to zero DKK. Unlocking requires either passive homeostatic recovery (𝓕Δ < 1.0) or active Human-in-the-Loop (HITL) Level 2 override.

A biosecurity bridge module further transmits an authenticated digital sickness declaration to municipal reimbursement frameworks (e.g., NemRefund/NemRefusion in Denmark) using a zero-knowledge identity hash, enabling automated sick-leave processing without exposing biometric sensor data to employers.

A planetary shield telemetry engine correlates anomaly signals with WHO pathogen transmission coefficients (R₀), triggering micro-quarantine rule updates and diagnostic manufacturing requests when R₀ > 1.0.

### Subsystem 2: Location-Aware Zero-Knowledge Jurisdictional Compliance (Claims 2, 9–12)

A system that captures geographical coordinates from a personal digital twin's location telemetry, reverse-geocodes them to a municipal jurisdiction code, and loads applicable regulatory rules from a three-tier hierarchy: supranational (EU IOSS), national (Danish VAT 25%, CE marking), and municipal (environmental zones, noise ordinances, water quality). A zero-knowledge proof validator verifies the transaction principal's identity via a cryptographic hash of their CPR number without revealing the CPR number itself. The system produces a transaction authorization state (`VALIDATED`, `BLOCKED`, or `PENDING`) with specific compliance codes (e.g., `BLOCKED_MISSING_CE`).

### Subsystem 3: Autonomous Non-Profit Surplus Ledger (Claims 3, 13–14)

A system that maintains a non-custodial capital pool balance for each enrolled citizen, computes a daily surplus increment as the difference between a non-profit baseline allocation (225.00 DKK/month ÷ 30 days = 7.50 DKK/day) and the estimated actual daily operating cost (5.20 DKK/day), yielding a daily surplus of 2.30 DKK. This surplus is atomically credited to the citizen's pool each day. On December 10th of each year, the total accumulated pool is automatically distributed to the citizen as a non-taxable dividend, and the pool resets to zero.

---

## DETAILED DESCRIPTION

### 1. System Architecture Overview

The TONE Architecture is deployed as a multi-layer sovereign compute stack:

| Layer | Designation | Function |
|-------|------------|----------|
| L1 | Personal Digital Twin (PDT) | Biometric ingestion, location telemetry, ZK proof generation |
| L2 | PDT+ (Enhanced Twin) | Active inference computation, anomaly detection, circuit breaker |
| L3 | Business Digital Twin (BDT) | Transaction validation, compliance rule matching |
| L4 | BDT+ (Enhanced Business Twin) | Cross-border compliance, IOSS, CE marking |
| L5 | Support Obligation Protocol | Municipal rule loading, jurisdictional filtering |
| L6 | Planetary Shield | R₀ monitoring, micro-quarantine, WHO escalation |
| L7 | s.net (Decision Ledger) | Immutable audit trail, append-only decision logging |
| L8 | Sovereign Governance | HITL override, democratic validation, ethical guardrails |

### 2. Active Inference Telemetry Engine (Claim 1)

#### 2.1 Biometric Ingestion Interface

The biometric ingestion interface receives physiological state vectors from a personal digital twin (PDT). Each state vector comprises:

| Modality | Symbol | Unit | Normal Range |
|----------|--------|------|--------------|
| Heart Rate Variability | HRV | ms | 40–100 ms |
| Core Body Temperature | T | °C | 36.1–37.2 °C |
| Respiratory Rate | RR | breaths/min | 12–20 |
| Blood Oxygen Saturation | SpO₂ | % | 95–100% |

Each vector is associated with an opaque user identifier (`user_ref`) that does not reveal the citizen's real identity. The biometric signals are transformed via zero-knowledge proof generation within the PDT before transmission, ensuring that raw physiological measurements are never exposed to any external system.

The zero-knowledge proof produces a cryptographic attestation confirming:
1. The biometric signals originate from a verified source identity
2. The signals have not been tampered with in transit
3. The signals were generated within a configurable freshness window (e.g., 60 seconds)

A deterministic oracle (GEMS — Governance Engine for Mathematical Symmetry) validates each attestation before the signals are accepted by the active inference computing module, rendering "black-card" (unverified or opaque) execution paths structurally impossible.

#### 2.2 Free-Energy Divergence Calculation

The active inference computing module calculates the variational free-energy divergence (𝓕Δ) as:

> 𝓕Δ = Σᵢ ‖oᵢ − μᵢ‖ / σᵢ

where:
- oᵢ = observed value for biometric modality i
- μᵢ = expected baseline mean for modality i (derived from longitudinal temporal model)
- σᵢ = expected baseline standard deviation for modality i
- The summation is performed across all biometric modalities (HRV, T, RR, SpO₂)

The expected homeostatic baseline is continuously updated through a learning and adaptation layer that refines the baseline based on longitudinal telemetry. This adaptation is constrained by immutable ethical guardrails that prevent the baseline from being modified in a manner that would mask a genuine anomaly.

#### 2.3 Anomaly Threshold and Circuit Breaker

The system compares 𝓕Δ against a predefined safety threshold. The threshold is configurable but cannot be lowered below a minimum safety floor:

| Threshold Type | Value | Description |
|---------------|-------|-------------|
| Combined physiological anomaly | 𝓕Δ ≥ 3.0 | Multi-modal free-energy divergence |
| Thermal drift | ΔT ≥ 1.5°C | Core temperature deviation from baseline |

Upon threshold breach, the active inference computing module emits an anomaly state signal. The compliance execution engine receives this signal and performs the following actions atomically:

1. **Transaction freeze:** All queued autonomous financial pre-bookings associated with `user_ref` are locked. This includes maintenance scheduling, discretionary spending, and subscription renewals.
2. **Spending cap override:** The monthly consent spending cap associated with `user_ref` is set to zero DKK, overriding any municipal maintenance cap (e.g., the 250 DKK/month cap defined in municipal support obligation rules).
3. **Audit log entry:** The freeze event is logged to the s.net immutable decision ledger with timestamp, anomaly details, and system action taken.

#### 2.4 Unlock Conditions

The circuit breaker maintains the freeze until one of two conditions is met:

| Unlock Condition | Type | Description |
|-----------------|------|-------------|
| Passive recovery | Automatic | 𝓕Δ returns below 1.0, indicating homeostatic recovery. The system automatically releases the freeze and resumes autonomous operations. |
| Active HITL override | Manual | A Human-in-the-Loop (HITL) Level 2 authority reviews the anomaly data and explicitly approves resumption. The override is logged with authority level, timestamp, and rationale. |

#### 2.5 NemRefusion Biosecurity Bridge (Claim 8)

Upon anomaly detection, a biosecurity bridge module transmits an authenticated digital sickness declaration payload to a municipal reimbursement framework (in Denmark: NemRefusion). The payload contains:

1. The zero-knowledge identity hash (`cpr_zk_hash`) of the citizen
2. An anomaly attestation (signed, timestamped, containing 𝓕Δ value and threshold breached)
3. A declaration type code (e.g., `SICKNESS_FEBRILE`)

The payload does NOT contain:
- Raw biometric sensor data (HRV, temperature, SpO₂, respiratory rate)
- The citizen's real CPR number
- The citizen's employer identity

This enables automated sick-leave processing through the municipal reimbursement system without exposing biometric sensor telemetry to the employer, protecting the citizen's medical privacy.

### 3. Location-Aware Zero-Knowledge Jurisdictional Compliance (Claim 2)

#### 3.1 Spatial Receiver and Reverse Geocoding

The spatial receiver captures geographical location coordinates (latitude, longitude) from the personal digital twin's location telemetry stream. The municipal geofencing engine performs reverse geocoding to determine the local administrative jurisdiction:

```
Coordinates (lat, lng) → Reverse Geocode → MUNICIPAL_CODE
```

In the deployed embodiment, reverse geocoding is performed via the Danish Addresses Web API (DAWA: https://dawa.aws.dk/kommuner). The system maps coordinates to one of 98 Danish municipalities (kommuner), each with a unique code (e.g., `AARHUS`, `KOBENHAVN`, `ODENSE`).

In the prototype embodiment, a coordinate-range lookup table is used:
```
KOMMUNE_LOOKUP = [
  { code: 'AARHUS',    latRange: [56.0, 56.4],  lngRange: [9.8, 10.6] },
  { code: 'KOBENHAVN', latRange: [55.5, 55.8],  lngRange: [12.4, 12.8] },
  ...
]
```

#### 3.2 Zero-Knowledge Identity Validation

The cryptographic zero-knowledge proof validator verifies the transaction principal's identity without revealing PII:

1. The citizen's CPR number is hashed within a zero-knowledge vault to produce `cpr_zk_hash`
2. Only `cpr_zk_hash` is transmitted to the compliance engine
3. The compliance engine matches `cpr_zk_hash` against a registry of verified identity hashes
4. If matched, the transaction principal is verified without the CPR number ever leaving the vault

This architecture ensures that the compliance engine, the business digital twin, and any intermediary systems never have access to the citizen's real CPR number, satisfying GDPR Articles 5, 6, 9, and 25 (data minimization, lawfulness, special category data protection, and privacy by design).

#### 3.3 Multi-Tier Rule Execution Matcher

The multi-tiered rule execution matcher loads active regulatory rules from an append-only rule registry. The registry is organized by jurisdiction:

| Tier | Jurisdiction Format | Scope | Example Rules |
|------|-------------------|-------|---------------|
| 1 (Supranational) | `EU` | Cross-border B2C | IOSS threshold (EUR 150), low-value shipment regulations |
| 2 (National) | `NATIONAL_DK` | Country-wide | VAT 25% standard / 12% reduced, CE marking for regulated categories |
| 3 (Municipal) | `MUNICIPAL_<CODE>` | Local kommune | Environmental zones, noise ordinances, water quality, maintenance caps |

**Conflict resolution:** Stricter-rule-wins. A municipal rule overrides a national or supranational rule when the municipal rule imposes more restrictive conditions. The rule registry is append-only — superseded rules are retained for audit traceability but marked as inactive.

The matcher evaluates the transaction against the loaded rule set and produces an authorization state:

| State | Description | Advisory Class |
|-------|-------------|----------------|
| `VALIDATED` | All compliance checks passed | Class I |
| `PENDING` | Additional documentation required (e.g., IOSS registration) | Class II |
| `BLOCKED` | Transaction halted (e.g., missing CE marking) | Class III |
| — | Critical violation requiring regulatory escalation | Class IV |

Specific compliance codes include:
- `BLOCKED_MISSING_CE` — CE marking required for regulated product category (electronics, toys, medical devices, machinery, PPE)
- `PENDING_IOSS` — Cross-border transaction below EUR 150 threshold without IOSS registration

### 4. Autonomous Non-Profit Surplus Ledger (Claim 3)

#### 4.1 Daily Surplus Computation

The distributed ledger processing engine computes the daily discretionary dividend increment:

> Δ_surplus = (Monthly Baseline / 30) − Daily Operating Cost

In the deployed embodiment:
- Monthly Baseline = 225.00 DKK (midpoint of 200–250 DKK range)
- Daily Operating Cost = 5.20 DKK (estimated from infrastructure telemetry)
- Δ_surplus = (225.00 / 30) − 5.20 = 7.50 − 5.20 = **2.30 DKK/day**

The daily operating cost is dynamically computed from infrastructure telemetry including:
- Compute resource consumption (CPU-hours, memory-hours)
- Storage utilization (GB-hours)
- Network transfer metrics (ingress/egress GB)

#### 4.2 Atomic Increment and Epoch Distribution

Each day (at 09:00 Europe/Copenhagen in the deployed embodiment), the system atomically increments each citizen's non-custodial capital pool balance:

> Pool_{t+1} = Pool_t + Δ_surplus

The atomicity guarantee ensures that no surplus is lost, duplicated, or credited to the wrong citizen. The increment is logged to the s.net decision ledger.

On December 10th of each calendar year, the system:
1. Computes the total accumulated balance: Pool_total = Σ Δ_surplus for all days since last distribution
2. Transfers Pool_total to the citizen's verified discretionary balance
3. Resets the non-custodial capital pool to zero
4. Logs the distribution to the s.net decision ledger with distribution amount, date, and citizen identifier

The distribution is classified as a non-taxable citizen dividend derived from operational efficiency savings, not as employment income, capital gains, or social benefits.

#### 4.3 Circuit Breaker Integration

The surplus ledger is protected by the circuit breaker of Claim 1. When a citizen's PDT has an active anomaly flag (𝓕Δ > 3.0), the daily surplus crediting is suspended for that citizen. The suspension is logged to the s.net decision ledger. Upon recovery (𝓕Δ < 1.0) or HITL override, crediting resumes.

### 5. Planetary Shield Pathogen Telemetry (Claim 15)

#### 5.1 R₀ Monitoring and Correlation

The planetary shield telemetry engine receives pathogen transmission coefficients (R₀) from global epidemiology monitoring nodes (e.g., WHO disease outbreak data). When an active anomaly state signal from a municipal active inference node correlates with a regional R₀ > 1.0, the system initiates a graduated response:

| Alert Level | Condition | Response |
|-------------|-----------|----------|
| `REGIONAL_WARNING` | R₀ > 1.0, WHO validation pending | Municipal advisory, localized monitoring |
| `GLOBAL_DECREE` | R₀ > 1.0, WHO approved | Cross-border transit rule updates, micro-quarantine activation |

#### 5.2 Micro-Quarantine Activation

Upon `REGIONAL_WARNING` or `GLOBAL_DECREE`, the system:
1. Identifies geographic areas associated with anomalous active inference nodes
2. Activates hyper-localized movement advisories through PDTs of citizens in affected areas
3. Updates municipal support obligation rules to restrict non-essential services
4. Maintains essential service delivery (healthcare, food, energy)
5. Transmits automated diagnostic manufacturing requests to redirect supply chains

#### 5.3 Predictive Council Docking

The system assembles a pathogen profile from aggregated anomaly telemetry and transmits it to a plurality of specialized predictive agents. Each agent provides independent analysis. The system synthesizes these analyses through a validation, comparison, and synthesis process to produce a single bias-neutral advisory with transparent decision lineage.

### 6. Decision Ledger (s.net)

All decisions across all subsystems are logged to the s.net immutable, append-only decision ledger. Each entry contains:

| Field | Description |
|-------|-------------|
| Timestamp | ISO 8601 with timezone |
| Actor ID | Opaque identifier of the acting entity |
| Decision Type | `ANOMALY_DETECTED`, `FREEZE_EXECUTED`, `COMPLIANCE_CHECK`, `SURPLUS_CREDITED`, `QUARANTINE_ACTIVATED`, etc. |
| Input Data | Hashed reference to input data (not raw data) |
| Output | Decision result |
| Authority Level | `AUTONOMOUS`, `HITL_L1`, `HITL_L2`, `WHO_APPROVED` |
| Previous Hash | Cryptographic link to prior entry (chain) |

The ledger is append-only — entries cannot be modified or deleted. Superseded rules are marked inactive but retained. This ensures full forensic audit traceability for regulatory compliance and democratic oversight.

---

## BRIEF DESCRIPTION OF DRAWINGS

The accompanying drawings (to be prepared) illustrate embodiments of the invention:

- **FIG. 1:** System architecture overview showing the multi-layer sovereign compute stack (L1–L8) and data flow between subsystems.
- **FIG. 2:** Active inference telemetry flow — from biometric ingestion through ZK proof generation to 𝓕Δ calculation and anomaly threshold comparison.
- **FIG. 3:** Circuit breaker state diagram — normal operation → anomaly detection → transaction freeze → unlock conditions (passive recovery or HITL override).
- **FIG. 4:** NemRefusion biosecurity bridge — anomaly signal → ZK sickness declaration payload → municipal reimbursement framework, showing which data elements are and are not transmitted.
- **FIG. 5:** Jurisdictional compliance flow — GPS coordinates → reverse geocode → three-tier rule loading → matching → authorization state output.
- **FIG. 6:** Zero-knowledge identity validation — CPR number → ZK vault → hash → compliance engine → registry match, with data minimization boundary marked.
- **FIG. 7:** Surplus ledger state diagram — daily increment → atomic pool update → epoch trigger (Dec 10) → distribution → pool reset.
- **FIG. 8:** Planetary Shield escalation — anomaly correlation → R₀ threshold check → graduated alert → micro-quarantine + supply chain redirection.
- **FIG. 9:** s.net decision ledger — append-only chain structure with cryptographic linking and authority level tracking.

---

## DEPLOYED EMBODIMENT

The TONE Architecture has been deployed as a working prototype on the Base44 platform with the following components:

| Component | Implementation | Entity/Function |
|-----------|---------------|-----------------|
| Citizen registry | `SommerUsers` entity | Stores `cpr_zk_hash`, `true_discretionary_income_dkk`, `dec_10_surplus_pool_dkk` |
| Active inference states | `PdtActiveInferenceStates` entity | Stores `physiological_baseline` (HRV, T, RR, SpO₂), `active_inference_delta` (𝓕Δ), `anomaly_flag` |
| Support obligation rules | `SupportObligationRules` entity | Append-only rule registry with `jurisdiction`, `trigger_criteria`, `is_active` |
| Transaction records | `BdtTransactions` entity | Stores `buyer_id`, `business_id`, `compliance_status`, `total_amount_dkk`, `vat_rate_applied` |
| Planetary Shield telemetry | `PlanetaryCouncilTelemetry` entity | Stores `alert_status`, `pathogen_r0_vector`, `affected_geographies`, `who_approved` |
| Compliance engine | `supportObligationRuleMatcher` backend function | Location-aware rule matching with three-tier jurisdictional filtering |
| Surplus computation | `computeDailySurplus` backend function | Scheduled daily at 09:00 Europe/Copenhagen, credits 2.30 DKK/citizen/day |
| Dashboard | 4-panel artifact | Citizen view, Operations view, Compliance view, Planetary Shield view |

### Validated Test Results

1. **Febrile anomaly cascade (2026-08-06):** Injected physiological drift (T: 36.6°C → 38.4°C, 𝓕Δ: 0.15 → 3.10) for Sovereign User 01. System correctly:
   - Set `anomaly_flag` to true
   - Created `BLOCKED_MISSING_CE` transaction record (PDT pre-booking block)
   - Escalated to Planetary Shield (`REGIONAL_WARNING`, R₀ = 1.12, affected: DK)
   - WHO validation pending

2. **Location-aware compliance (2026-08-06):** Two citizens tested:
   - Sovereign User 01 in Aarhus (56.1629°N, 10.2039°E): loaded EU + NATIONAL_DK + MUNICIPAL_AARHUS rules → matched VAT (25%) + Environmental Zone (Euro 6 minimum, 1,500 DKK fine)
   - Michael in København (55.6761°N, 12.5683°E): loaded EU + NATIONAL_DK + MUNICIPAL_KOBENHAVN rules → matched VAT (25%) + Noise Ordinance (delivery permitted) + Water Quality (14 stations, E. coli < 500 CFU/100ml)

3. **Daily surplus computation (2026-08-06):** `computeDailySurplus` function executed successfully, crediting 2.30 DKK to each citizen's December 10th surplus pool.

---

## INDUSTRIAL APPLICABILITY

The TONE Architecture has industrial applicability in:

1. **Digital health infrastructure** — continuous physiological monitoring with privacy-preserving anomaly detection
2. **Autonomous financial systems** — safety circuit breakers for AI-driven financial agents
3. **E-commerce compliance** — automated cross-border regulatory verification without PII exposure
4. **Municipal governance** — location-aware rule enforcement for environmental, noise, and public health regulations
5. **Public health biosecurity** — early warning systems for pathogen spread through decentralized physiological monitoring
6. **Social welfare automation** — non-profit surplus distribution as citizen dividends
7. **Sick-leave automation** — privacy-preserving sickness declaration via ZK identity proofs

---

## INTERNATIONAL FILING STRATEGY & PRIORITY CLAIM

The deployment strategy is DK pilot → EU expansion. The patent filing strategy mirrors this phasing.

### Phase 1 — Denmark (DK) National Filing

- File a national DK patent application first via the Danish Patent and Trademark Office (DKPTO)
- DK national applications can be filed in Danish or English
- This secures the priority date while the DK pilot is operational
- The 12-month priority window is used to assess pilot results before committing to broader filings
- A DK national filing is fast and inexpensive (~3,000–5,000 DKK official fees) and gives immediate priority protection

### Phase 2 — European (EP) Filing Within 12 Months of DK Priority

- File a European patent application claiming priority from the DK national filing
- Via the European Patent Office (EPO) under the European Patent Convention (EPC)
- This covers all EPC contracting states (38+ countries including all EU member states)
- Claims must comply with the EPC's requirements for technical character (the "technical effect" doctrine — T 154/04, G 1/19)
- Governance/policy aspects must be framed to satisfy EPO exclusions (Art. 52(2)(c) EPC — "methods for doing business" / "programs for computers")
- Foreground the technical implementation: cryptographic identity proofs (ZK vault, cpr_zk_hash), free-energy divergence computation, circuit breaker mechanisms, immutable audit trail logging — these produce *further technical effects* beyond the normal interaction of software with hardware

### Alternative — PCT Route

- Instead of separate DK + EP filings, consider a PCT international application
- File within 12 months of the earliest priority date
- National phase entries: DK (Receiving Office), EP (EPO), and optionally US (USPTO) if US protection becomes relevant
- PCT gives flexibility to defer national-phase decisions by up to 30/31 months
- For a DK-first pilot, the direct DK + EP route may be simpler and faster, but PCT is recommended for broadest coverage if US market entry is anticipated

### Critical Pre-Filing Actions

1. **Prior art search** — Conduct a thorough prior art search covering: active inference biometric systems, zero-knowledge identity matching in compliance, autonomous circuit breakers for financial systems, non-profit surplus distribution mechanisms, and biosecurity pathogen telemetry architectures. Focus on EP, DK, and US patent databases.

2. **EPO technical character** — Under EPO practice, ensure each claim produces a *further technical effect*. The zero-knowledge identity mediation (cryptographic proofs), free-energy divergence computation (𝓕Δ), circuit breaker threshold gating, and append-only decision ledger with cryptographic chaining should be foregrounded as technical features. Pure governance/policy rules alone may be excluded under Art. 52(2) EPC.

3. **US § 101 eligibility** — Claims 1 and 2 recite specific structural components (biometric ingestion interface, active inference computing module, compliance execution engine, spatial receiver, municipal geofencing engine, ZK proof validator, rule execution matcher) — these should survive Alice/Mayo step two as concrete technological improvements. Claim 3 (surplus ledger) may face greater scrutiny — emphasize the atomic increment, epoch-triggered distribution, and circuit breaker integration as concrete technical implementation.

4. **Novelty grace period warning** — Denmark/EPO does NOT have a general novelty grace period (unlike US 35 U.S.C. § 102(b)(1)). Any public disclosure of the invention before the priority filing date could destroy novelty. If the bysommer.net website or any published material describes TONE in enabling detail, this may constitute prior disclosure. **Consult patent attorney urgently on this point.**

5. **Drawing formalization** — The 9 figure descriptions in `DIAGRAMS_DESCRIPTION.md` should be formalized into patent-style drawings with reference numerals (e.g., 100 = Active Inference Engine, 110 = Circuit Breaker, 120 = Compliance Engine, 130 = Surplus Ledger, 140 = Planetary Shield, 150 = s.net Ledger).

6. **Danish patent attorney** — Engage a DK-registered patent attorney (e.g., via Plougmann Vingtoft, Zacco, or Patrade) who can file nationally and handle the EP phase. They will also advise on whether Danish or English language is best for the initial filing.

### Filing Timeline

| Milestone | Target Date | Action |
|-----------|-------------|--------|
| Priority filing (DK) | Earliest feasible | File DK national application with Claims 1–15 |
| Priority window | 12 months from DK filing | Assess pilot results, refine claims |
| EP filing | Within 12 months of DK priority | File EP application claiming DK priority |
| PCT route (if elected) | Within 12 months of priority | File PCT application, national phases at 30/31 months |
| US filing (if applicable) | Within 12 months of priority | File US application (direct or via PCT national phase) |
| Divisional filings | As needed | File divisionals for GEMS, AURA Advisory Classes, Tone Density modes, incident hives, Living Compliance Tattoo |

---

## CLAIMS

See `CLAIMS_DRAFT.md` for the full text of Claims 1–15.
