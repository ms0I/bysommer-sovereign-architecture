# EIC Accelerator Step 1 — Online Questionnaire Responses

**Project Acronym:** TONE-SOVEREIGN
**Call:** HORIZON-EIC-2025-ACCELERATOR-02-CHALLENGES-03 (GenAI4EU)
**Applicant:** BY SOMMER (Michael Sommer)
**Date:** 06 August 2026
**Repository:** [MSDK0I/bysommer-sovereign-architecture](https://github.com/MSDK0I/bysommer-sovereign-architecture)

---

## Section 1: The Breakthrough & Innovation

### Q1.1: What is the breakthrough innovation at the core of your project?

TONE-SOVEREIGN introduces the world's first privacy-preserving biosecurity circuit breaker that computes active inference (variational free-energy divergence, 𝓕Δ) entirely on edge devices, triggering hardware-level financial transaction freezes during physiological anomalies — without transmitting any raw health data to centralized servers.

The architecture unifies three mathematically grounded breakthroughs, each protected under DKPTO Priority Docket TONE-2026-PCT-01 (15 formal patent claims: 3 independent, 12 dependent):

1. **Active Inference Edge Engine (Patent Claim 1):** Raw biometric telemetry (heart rate variability, core temperature, blood oxygen saturation) is processed locally using Gaussian KL-divergence computation. When 𝓕Δ ≥ 3.0 or thermal drift ≥ 1.5°C above homeostatic baseline, physical hardware circuit breakers freeze all queued autonomous financial pre-booking transactions. Passive recovery unlocks automatically when 𝓕Δ returns below 1.0. This is a Friston active inference framework implemented at the silicon edge — not a cloud-based heuristic.

2. **Zero-Knowledge Jurisdictional Compliance Engine (Patent Claim 2):** Danish Civil Registration (CPR) numbers are hashed locally using salted SHA-256 (`cpr_zk_hash`), classified as pseudonymous under GDPR Recital 26. Municipal rules — from EU Low Emission Zones to Danish sickness benefit triggers — are verified cryptographically via a three-tier spatial matching engine (EU → National → Municipal) without exposing national identity numbers or medical diagnostics. The NemRefusion sickness benefit bridge transmits only a binary `IS_INCAPACITATED` status, fully compliant with Helbredsoplysningsloven §1/§2 (zero diagnostic strings).

3. **Autonomous Non-Profit Surplus Ledger (Patent Claim 3):** Daily civic efficiency accrues at exactly Δ_surplus = (225.00 DKK / 30) − 5.20 DKK = 2.30 DKK/citizen/day, compounding to 839.50 DKK/citizen/year. The surplus is distributed non-custodially on December 10th each year (atomic, idempotent payout epoch). At scale (5 million citizens, Year 5), this generates a ~4.20 billion DKK (~€562.7M) annual civic dividend pool funded entirely by administrative efficiency gains — not taxation.

### Q1.2: What is your current Technology Readiness Level (TRL)?

**Entry TRL: 5/6** — Technology validated in relevant environment (simulated operational).

Evidence:
- Complete Python integration test suite (77 test cases, 10 test classes, all passing) validating all 15 patent claims against the deployed prototype.
- 9 Base44 database entities deployed and seeded (SommerUsers, PdtActiveInferenceStates, SupportObligationRules, BdtTransactions, PlanetaryCouncilTelemetry, GlyphArchive, RippleForecast, SommerCopilotForecasts, SommerCopilotGlyphs).
- 4 deployed backend functions (rule matcher, surplus engine, daily inference, planetary shield).
- 4 dashboard views (Citizen, Operations, Compliance, Planetary Shield).
- Validated end-to-end febrile anomaly cascade: physiological anomaly → 𝓕Δ computation → circuit breaker → spending freeze → NemRefusion IS_INCAPACITATED declaration → Planetary Shield R₀ escalation.

### Q1.3: Why is this innovation unique — what distinguishes it from the state of the art?

No known system combines:
- **Edge-only active inference** (Friston free-energy computation at the silicon level, not cloud ML inference).
- **Zero-knowledge regulatory compliance** (pseudonymous identity proofs for municipal service delivery, GDPR Recital 26 classified).
- **Non-custodial civic dividends** (autonomous surplus distribution to citizens, not to intermediaries).

Existing AI compliance infrastructure (e.g., NeuralTrust, funded under this same GenAI4EU call at €2.36M) focuses on AI trust and verification in cloud environments. TONE-SOVEREIGN inverts the paradigm: raw data never leaves the edge, compliance is proven cryptographically, and citizens receive direct financial benefit from system efficiency. This is civic infrastructure, not surveillance infrastructure.

---

## Section 2: Market Opportunity & Impact

### Q2.1: What is the target market and scalability potential?

**Primary Market:** Danish municipal government services (Aarhus pilot: 10,000 citizens → Copenhagen: 100,000 → national: 500,000).

**Scale-Up Market:** European municipal governments via EU Data Spaces, IOSS spatial tax engine, and eIDAS 2.0 identity bridge.

**Revenue/Cost Structure:**
- Non-profit model: baseline 225.00 DKK/citizen/month operational cost, daily surplus 2.30 DKK/citizen/day.
- Year 1 (10K citizens): 8.395M DKK (~€1.12M) civic dividend pool.
- Year 3 (500K citizens): 419.75M DKK (~€56.3M) civic dividend pool.
- Year 5 (5M citizens): 4.20B DKK (~€562.7M) civic dividend pool.

**Administrative Savings:** ~€8B cumulative administrative expense reduction for European municipalities through automated sickness benefit verification (NemRefusion), ULEZ spatial compliance, and non-profit surplus distribution.

### Q2.2: How does your innovation create societal impact?

TONE-SOVEREIGN eliminates the false trade-off between privacy and civic efficiency:

- **Privacy:** Raw biometric data (HRV, temperature, SpO₂) is processed on edge devices. Municipalities and employers receive only binary `IS_INCAPACITATED` status — zero diagnostic strings, zero ICD-10 codes, zero clinical parameters. Compliant with GDPR Art. 9, Helbredsoplysningsloven §1/§2, and EU AI Act Title IV (Art. 50) transparency requirements.

- **Financial Inclusion:** Citizens receive direct non-custodial dividends (839.50 DKK/year) funded by administrative efficiency, not taxation. The surplus ledger is non-custodial — the platform cannot redirect or spend citizen pools.

- **Administrative Reduction:** Automated sickness benefit declarations (Sygedagpengeloven LBK nr 1293 §4/§5), three-tier spatial compliance matching (EU IOSS → National VAT → Municipal ULEZ), and immutable audit logging (Bogføringsloven §6, 5-year retention).

- **Democratic Oversight:** Human-in-the-Loop (HITL) Level 2 override keys ensure that automated decisions (circuit breaker engagement, transaction freezes) are always subject to human review per GDPR Art. 22.

### Q2.3: What are your commercialization and deployment plans?

- **2026:** DKPTO priority filing (TONE-2026-PCT-01) → 10,000-citizen Aarhus Municipal Sandbox pilot → EUopSTART pre-financing for EIC Step 2.
- **2027:** PCT international filing (RO/DK, ISA/EPO) → Copenhagen scale-up (100,000 citizens) → Danish EIC precedents (Skypuzzler, Hyme Energy) demonstrate national EIC track record.
- **2028–2029:** Pan-European expansion via EU Data Spaces & IOSS spatial tax engine → eIDAS 2.0 EUDI Wallet integration → 5 million citizen target.

---

## Section 3: Team & Capabilities

### Q3.1: Who is the founding team and what are their capabilities?

**Founder & Lead Inventor:** Michael Sommer — Architect of the TONE Sovereign Architecture. Responsible for:
- Full system architecture design (8-layer fractal sovereign substrate: L-PDT to L-SAT).
- Patent portfolio (15 claims, 9 technical diagrams, EPO Art. 52(2)(c) defense, USPTO §101 Alice/Mayo analysis).
- Deployed prototype implementation (9 Base44 entities, 4 backend functions, 77-test integration suite).
- Danish statutory compliance engineering (Sygedagpengeloven, Helbredsoplysningsloven, Bogføringsloven integration).

### Q3.2: What is your advisory ecosystem and consortium structure?

- **Municipal Pilot Host:** City of Aarhus (Digitalisering og IT) — 10,000-citizen urban sandbox, ULEZ zone definitions, NemRefusion API access.
- **Academic Partner:** Aarhus University, Dept. of Computer Science — Active inference formal verification, independent pilot evaluation.
- **National Digital Government:** Digitaliseringsstyrelsen — AI Regulatory Sandbox admission, eIDAS 2.0 alignment.
- **Data Protection Authority:** Datatilsynet — Pre-consultation on cpr_zk_hash pseudonymization and binary biosecurity status clearance.
- **Patent Counsel:** Plougmann Vingtoft / Zacco / Patrade — FTO assessment, DKPTO priority filing, PCT international prosecution.
- **Financial Audit:** Certified Public Accountant — Bogføringsloven compliance, 70% co-funding capacity documentation.

### Q3.3: What technical capabilities have you already demonstrated?

- 77-test Python integration suite validating 𝓕Δ computation (Gaussian KL-divergence), cpr_zk_hash (SHA-256 pseudonymization), surplus ledger (2.30 DKK/day, Dec 10 epoch), three-tier compliance, GDPR Art. 22 HITL, Bogføringsloven retention, and full febrile anomaly cascade.
- Deployed backend: rule matching engine (location-aware, DAWA geocoding), daily surplus computation (scheduled 09:00 Europe/Copenhagen), active inference worker, planetary shield telemetry.
- Fail-to-Sovereign-State (FSS) protocol: 3-tier deterministic fallback (Edge Circuit Lock → ZK State Lock → Accounting Backup) ensuring zero data exposure in all failure modes.

---

## Section 4: Risk Mitigation & Non-Bankability

### Q4.1: Why cannot this project be funded by private VC or commercial debt alone?

TONE-SOVEREIGN is non-bankable for four structural reasons:

1. **Regulatory Precedent Risk:** The architecture pioneers dual ZK/active inference compliance infrastructure — no existing regulatory framework has been tested for edge-computed biosecurity circuit breakers combined with non-custodial civic dividends. The Danish AI Regulatory Sandbox (Digitaliseringsstyrelsen/Datatilsynet) admission is required before commercial deployment. Private capital cannot underwrite this regulatory risk.

2. **Non-Profit Economic Model:** The surplus dividend (2.30 DKK/citizen/day) is distributed to citizens, not retained as profit. This eliminates the equity return mechanism that VC requires. The platform is civic infrastructure, not a SaaS company.

3. **Public Sector Procurement Dependency:** Deployment requires municipal partnership agreements (Aarhus Kommune), national API access (NemRefusion/Udbetaling Danmark, DAWA), and regulatory sandbox admission. These are government-gated milestones unsuitable for commercial debt servicing schedules.

4. **Deep-Tech Maturation Timeline:** TRL 5/6 → TRL 8 requires 24 months of hardware optimization (C++ edge kernels, Groth16 ZK circuit audits), municipal pilot deployment, and national qualification. The timeline exceeds typical VC fund return windows for pre-revenue deep-tech.

### Q4.2: What are the key technical and regulatory risks, and how are they mitigated?

**Technical Risks:**
- 𝓕Δ false positive rate: Mitigated by 7-day baseline calibration, clinical validation in Tier 1 pilot (target <5% false positive, <2% false negative).
- ZK prover performance: Mitigated by Groth16 circuit optimization in WP1 (C++ edge kernels, CIRCOM circuits).
- Edge device hardware failures: Mitigated by device warranty, 5% replacement pool, Fail-to-Sovereign-State Tier 1 (hardware circuit breaker is physical, not software-toggle).

**Regulatory Risks:**
- Datatilsynet objection to cpr_zk_hash: Mitigated by pre-consultation, GDPR Recital 26 pseudonymization classification, AI Regulatory Sandbox admission.
- EU AI Act Annex III conformity: Mitigated by Ethics Self-Assessment Matrix (4 risk dimensions), FΔ designed as passive safety circuit breaker (not autonomous decision-making), HITL Level 2 override implemented.
- NemRefusion API access denied: Mitigated by pre-consultation with Udbetaling Danmark (M1-M3), sandbox testing environment.

### Q4.3: What happens if the system fails?

The Fail-to-Sovereign-State (FSS) protocol ensures deterministic, legally compliant failure:

- **Tier 1 (Edge Circuit Lock):** 𝓕Δ ≥ 3.0 → hardware circuit breaker fires, all transactions freeze, raw biometrics stay on-device. Zero data leakage.
- **Tier 2 (ZK State Lock):** Network partition → offline cold queue, Ed25519-signed ZK proofs stored locally. When connectivity restores, proofs re-verify atomically. Zero raw CPR/health data re-transmission.
- **Tier 3 (Accounting Backup):** Ledger sync failure → local deterministic append-only ledger, Bogføringsloven §6 compliant (5-year retention). December 10th payouts recalculated against verified physical balance sheets. Zero double-counting or dividend loss.

**All failure modes result in zero data exposure.** The FSS protocol is tested and documented in `docs/SOVEREIGN_FALLBACK_PROTOCOL.md`.

---

## Document Version

- **Version:** 1.0
- **Status:** Ready for EIC Step 1 online submission
- **Cross-Reference Audit:** PASSED (100% traceable, `docs/AUDIT_REPORT.md`)
- **Repository:** [MSDK0I/bysommer-sovereign-architecture](https://github.com/MSDK0I/bysommer-sovereign-architecture)
