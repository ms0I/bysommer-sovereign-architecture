# TONE Patent — Diagrams Reference Manual

**Invention:** TONE Architecture (Telemetry-Driven Active Inference & Sovereign Privacy Protocol)  
**Applicant:** By Sommer  
**Document:** Reference manual for patent figures (Flowcharts, System Architecture)  
**STATUS:** Draft for Filing  
**DATE:** 2026-08-06  

---

## Drawing Index

| Figure | Title | Type | Supports Claims |
|--------|-------|------|-----------------|
| FIG. 1 | System Architecture Overview | Block diagram | 1, 2, 3, 15 |
| FIG. 2 | Active Inference Telemetry Flow | Data flow diagram | 1, 4 |
| FIG. 3 | Circuit Breaker State Diagram | State machine | 1, 5, 6, 7 |
| FIG. 4 | NemRefusion Biosecurity Bridge | Data flow with boundaries | 8 |
| FIG. 5 | Jurisdictional Compliance Flow | Process flowchart | 2, 9, 10, 11 |
| FIG. 6 | Zero-Knowledge Identity Validation | Data flow with trust boundary | 2, 12 |
| FIG. 7 | Surplus Ledger State Diagram | State machine + timeline | 3, 13, 14 |
| FIG. 8 | Planetary Shield Escalation | Sequence diagram | 15 |
| FIG. 9 | s.net Decision Ledger Structure | Data structure diagram | All (enabling) |

---

## FIG. 1 — System Architecture Overview

**Type:** Block diagram  
**Claims supported:** 1, 2, 3, 15  

### Description

FIG. 1 illustrates the overall system architecture of the TONE Architecture, showing the multi-layer sovereign compute stack and the data flow between subsystems.

The diagram is arranged in vertical layers (top to bottom):

- **L1 (top):** Personal Digital Twin (PDT) — shown as a block containing "Biometric Sensors" (HRV, Temp, RR, SpO₂) and "Location GPS." Arrows labeled "ZK Proof" extend downward from the PDT to L2.

- **L2:** PDT+ (Enhanced Twin) — shown as a block containing "Active Inference Engine" (computing 𝓕Δ) and "Anomaly Detector" (comparing 𝓕Δ vs threshold). An arrow labeled "Anomaly Signal" extends rightward to L3 and downward to the "Circuit Breaker" module.

- **L3:** Business Digital Twin (BDT) — shown as a block containing "Transaction Validator." An arrow labeled "Transaction Request" extends rightward from the BDT to L4.

- **L4:** BDT+ (Enhanced Business Twin) — shown as a block containing "Compliance Engine" with sub-blocks for "IOSS Check," "VAT Check," and "CE Marking Check." An arrow labeled "Compliance Verdict" extends downward.

- **L5:** Support Obligation Protocol — shown as a block containing "Municipal Rule Loader" and "Jurisdictional Filter." Connected to L4 via a bidirectional arrow labeled "Rules + Filter Result."

- **L6:** Planetary Shield — shown as a block containing "R₀ Monitor" and "Micro-Quarantine Engine." Connected to L2 via an arrow labeled "Anomaly Correlation" and to WHO nodes via an arrow labeled "R₀ Data."

- **L7:** s.net (Decision Ledger) — shown as a horizontal band spanning the bottom of the diagram. All layers above have downward arrows labeled "Audit Log" connecting to this band.

- **L8 (right side):** Sovereign Governance — shown as a vertical block containing "HITL Override" and "Ethical Guardrails." Connected to L2 via "Override Signal" and to L7 via "Authority Validation."

**Data flow annotations:**
- Solid arrows = synchronous data flow
- Dashed arrows = asynchronous event signals
- Double-line arrows = immutable ledger writes

---

## FIG. 2 — Active Inference Telemetry Flow

**Type:** Data flow diagram  
**Claims supported:** 1, 4  

### Description

FIG. 2 illustrates the flow of biometric data from sensors through zero-knowledge proof generation to free-energy divergence calculation.

The diagram flows left to right:

1. **Biometric Sensors (leftmost):** Four sensor icons labeled "HRV (ms)," "Core Temp (°C)," "Resp Rate," "SpO₂ (%)." Each emits a data stream.

2. **ZK Proof Generator (within PDT boundary):** Receives all four data streams. Produces "ZK Attestation" (a cryptographic proof that the data is from a verified source, without revealing the source identity or raw data). A dashed trust boundary is drawn around the PDT, labeled "Raw biometric data does not cross this boundary."

3. **GEMS Deterministic Oracle:** Receives the ZK Attestation. Validates it. Outputs "Verified State Vector" (o₁, o₂, o₃, o₄) associated with `user_ref`.

4. **Active Inference Engine:** Receives the Verified State Vector. Also receives "Expected Baseline" (μ₁, μ₂, μ₃, μ₄) from the "Longitudinal Baseline Model." Computes 𝓕Δ = Σᵢ ‖oᵢ − μᵢ‖ / σᵢ.

5. **Threshold Comparator (rightmost):** Receives 𝓕Δ. Compares against threshold (3.0). Outputs "Normal" (if 𝓕Δ < 3.0) or "Anomaly Signal" (if 𝓕Δ ≥ 3.0).

**Mathematical annotation:** The formula `𝓕Δ = Σᵢ ‖oᵢ − μᵢ‖ / σᵢ` is displayed in a callout box between the Active Inference Engine and the Threshold Comparator.

---

## FIG. 3 — Circuit Breaker State Diagram

**Type:** State machine  
**Claims supported:** 1, 5, 6, 7  

### Description

FIG. 3 illustrates the three states of the circuit breaker and the transitions between them.

**States:**

1. **NORMAL OPERATION** (default state): Autonomous financial pre-bookings are active. Monthly spending cap is set to municipal default (e.g., 250 DKK). 𝓕Δ < 3.0.

2. **FROZEN** (anomaly state): All autonomous pre-bookings are locked. Spending cap set to zero DKK. Entered when 𝓕Δ ≥ 3.0 or ΔT ≥ 1.5°C.

3. **UNLOCKED** (recovery state): Freeze is released. Pre-bookings resume. Spending cap restored to municipal default.

**Transitions:**

- NORMAL → FROZEN: Triggered by "Anomaly Signal (𝓕Δ ≥ 3.0 or ΔT ≥ 1.5°C)." Arrow labeled "FREEZE."
- FROZEN → UNLOCKED: Two possible paths:
  - Path A: "Passive Recovery (𝓕Δ < 1.0)" — automatic transition
  - Path B: "HITL Level 2 Override" — manual transition, logged to s.net
- UNLOCKED → NORMAL: Automatic transition after grace period (configurable, default: immediate).

**Annotations:**
- Each transition arrow is annotated with the s.net audit log entry type (e.g., `FREEZE_EXECUTED`, `FREEZE_RELEASED`, `HITL_OVERRIDE_GRANTED`).
- The FROZEN state has a callout box showing: "Spending Cap = 0 DKK" and "Queued transactions: LOCKED."

---

## FIG. 4 — NemRefusion Biosecurity Bridge

**Type:** Data flow with privacy boundary  
**Claims supported:** 8  

### Description

FIG. 4 illustrates the transmission of a sickness declaration to the municipal reimbursement framework (NemRefusion) without exposing biometric sensor telemetry to the employer.

The diagram is divided into three zones by vertical dashed lines:

**Zone A (left): Personal Digital Twin + Circuit Breaker**
- Shows the anomaly signal being generated (𝓕Δ ≥ 3.0).
- Shows the "Biosecurity Bridge Module" receiving the anomaly signal.

**Zone B (center): Zero-Knowledge Vault**
- Shows the `cpr_zk_hash` being generated from the CPR number.
- Shows the "Sickness Declaration Payload" being assembled:
  - ✅ Included: `cpr_zk_hash`, anomaly attestation (signed, timestamped, 𝓕Δ value, threshold breached), declaration type code (`SICKNESS_FEBRILE`)
  - ❌ NOT included (marked with red X): Raw HRV, raw temperature, raw SpO₂, raw respiratory rate, real CPR number, employer identity

**Zone C (right): Municipal Reimbursement Framework (NemRefusion)**
- Receives the Sickness Declaration Payload.
- Processes sick-leave reimbursement.
- Sends "Sick Leave Confirmed" notification to employer — this notification contains only the declaration type and dates, NOT biometric data.

**Key annotation:** A trust boundary is drawn between Zone B and Zone C, labeled "ZK hash crosses; raw biometrics do not."

---

## FIG. 5 — Jurisdictional Compliance Flow

**Type:** Process flowchart  
**Claims supported:** 2, 9, 10, 11  

### Description

FIG. 5 illustrates the step-by-step process of location-aware jurisdictional compliance verification.

**Flow (top to bottom):**

1. **START:** Transaction request received (buyer_id, business_id, amount, product_category, has_ce_marking, is_cross_border)

2. **Step 1 — Location Fetch:** Fetch citizen GPS coordinates from PDT telemetry. Output: (lat, lng)

3. **Step 2 — Reverse Geocode:** Convert (lat, lng) → MUNICIPAL_CODE. (Production: DAWA API; Prototype: lookup table)

4. **Step 3 — Rule Loading:** Load rules from append-only registry filtered by three-tier jurisdiction:
   - `EU` rules (IOSS, cross-border thresholds)
   - `NATIONAL_DK` rules (VAT 25%, CE marking)
   - `MUNICIPAL_<CODE>` rules (environmental zone, noise ordinance, water quality, maintenance cap)

5. **Step 4 — ZK Identity Check:** Verify `cpr_zk_hash` against registry. Output: verified / unverified

6. **Step 5 — Rule Matching (decision diamond):**
   - If cross-border AND amount < EUR 150 AND not IOSS registered → `PENDING` (Advisory Class II)
   - If regulated category AND no CE marking → `BLOCKED` (compliance code: `BLOCKED_MISSING_CE`, Advisory Class III)
   - If VAT rate mismatch → `BLOCKED` (compliance code: `VAT_MISMATCH`, Advisory Class III)
   - If all checks pass → `VALIDATED` (Advisory Class I)

7. **Step 6 — Audit:** Log compliance verdict + matched rules + jurisdictional context to s.net

8. **END:** Return compliance verdict + advisory class + matched rules + location telemetry

**Annotation:** The stricter-rule-wins conflict resolution is shown as a sub-process within Step 3, with a decision point: "Does municipal rule impose more restrictive conditions than national/supranational?" → Yes: apply municipal rule. No: apply national/supranational rule.

---

## FIG. 6 — Zero-Knowledge Identity Validation

**Type:** Data flow with trust boundary  
**Claims supported:** 2, 12  

### Description

FIG. 6 illustrates the zero-knowledge identity validation process, emphasizing the data minimization boundary.

**Flow (left to right):**

1. **Citizen (leftmost):** Holds real CPR number (shown as a shielded icon labeled "CPR Number — Private")

2. **Zero-Knowledge Vault (center-left):**
   - Input: CPR Number (private)
   - Process: Hash(CPR Number) = `cpr_zk_hash`
   - Output: `cpr_zk_hash` (public, non-reversible)
   - A thick trust boundary is drawn around the vault, labeled "CPR number never exits this boundary"

3. **Compliance Engine (center-right):**
   - Input: `cpr_zk_hash` from vault + transaction request from BDT
   - Process: Match `cpr_zk_hash` against registry of verified hashes
   - Output: "Identity Verified" or "Identity Unverified"

4. **Regulatory Database (rightmost):**
   - Stores: `{ cpr_zk_hash, verified: true, citizen_status: 'active' }`
   - Does NOT store: real CPR numbers, names, addresses, or any PII

**Key annotation:** A dashed line labeled "Privacy Boundary (GDPR Art. 5, 6, 9, 25)" separates the vault from the compliance engine. Only the hash crosses this boundary.

---

## FIG. 7 — Surplus Ledger State Diagram

**Type:** State machine + timeline  
**Claims supported:** 3, 13, 14  

### Description

FIG. 7 illustrates the surplus accrual cycle over a calendar year, showing daily increments and the epoch distribution.

**Upper section — State machine:**

1. **ACCUMULATING (default):** Daily at 09:00, Δ_surplus (2.30 DKK) is atomically added to Pool_t. New state: Pool_{t+1} = Pool_t + 2.30. Each increment is logged to s.net.

2. **SUSPENDED (circuit breaker active):** If citizen's PDT has anomaly flag (𝓕Δ > 3.0), daily credit is suspended. Pool balance is preserved but not incremented. Suspension logged to s.net.

3. **DISTRIBUTING (December 10th):** When system date = December 10th:
   - Pool_total is computed (sum of all Δ_surplus since last distribution)
   - Pool_total is transferred to citizen's discretionary balance
   - Pool is reset to zero
   - Distribution logged to s.net with amount, date, citizen ID

**Lower section — Timeline visualization:**

A horizontal timeline from January 1 to December 10, showing:
- Daily Δ_surplus increments (2.30 DKK) represented as small vertical bars
- The accumulation curve growing from 0 to ~839.50 DKK (365 days × 2.30 DKK, minus suspension days)
- A vertical dashed line at December 10 labeled "EPOCH — Distribution Trigger"
- An arrow showing the pool balance dropping to zero after distribution
- The cycle repeating from December 11

**Mathematical annotation:** `Δ_surplus = (225.00 / 30) − 5.20 = 2.30 DKK/day` displayed in a callout.

---

## FIG. 8 — Planetary Shield Escalation

**Type:** Sequence diagram  
**Claims supported:** 15  

### Description

FIG. 8 illustrates the sequence of events during a biosecurity escalation, from local anomaly detection to planetary shield response.

**Actors (top to bottom, left to right):**
1. PDT Active Inference Node
2. Circuit Breaker
3. Planetary Shield Monitoring System
4. WHO Epidemiology Nodes
5. Municipal Support Obligation Rules
6. Predictive Council

**Sequence:**

1. **T+0s:** PDT node detects 𝓕Δ ≥ 3.0 → sends "Anomaly Signal" to Circuit Breaker
2. **T+1s:** Circuit Breaker freezes transactions → sends "Anomaly Telemetry" to Planetary Shield
3. **T+2s:** Planetary Shield requests "R₀ Data" from WHO nodes
4. **T+5s:** WHO nodes return "R₀ = 1.12" (regional)
5. **T+6s:** Planetary Shield: R₀ > 1.0 → generates "REGIONAL_WARNING"
6. **T+7s:** Planetary Shield sends "WHO Validation Request" to WHO
7. **T+7s:** Planetary Shield sends "Micro-Quarantine Rules" to Municipal Support Obligation Rules → non-essential services restricted in affected areas
8. **T+7s:** Planetary Shield sends "Diagnostic Manufacturing Request" to supply chain
9. **T+8s:** Planetary Shield sends "Pathogen Profile" to Predictive Council → receives independent analyses → synthesizes bias-neutral advisory
10. **T+??:** WHO approval received → alert escalates to "GLOBAL_DECREE" → cross-border transit rules updated

**Annotation:** The timeline is shown with both elapsed time (T+0s, T+1s, etc.) and the alert level progression (GREEN → REGIONAL_WARNING → GLOBAL_DECREE).

---

## FIG. 9 — s.net Decision Ledger Structure

**Type:** Data structure diagram  
**Claims supported:** All (enabling)  

### Description

FIG. 9 illustrates the structure of the s.net immutable, append-only decision ledger.

**Structure (shown as a chain of blocks):**

Each block contains the following fields:

| Field | Description | Example |
|-------|-------------|---------|
| Entry ID | Sequential identifier | #00472 |
| Timestamp | ISO 8601 with timezone | 2026-08-06T15:42:07+02:00 |
| Actor ID | Opaque identifier | `user_ref:6a748a50...` |
| Decision Type | Enumerated | `ANOMALY_DETECTED` |
| Input Hash | Hash of input data (not raw data) | `sha256:a8f3e1...` |
| Output | Decision result | `FREEZE_EXECUTED, cap=0` |
| Authority Level | Enumerated | `AUTONOMOUS` / `HITL_L2` / `WHO_APPROVED` |
| Previous Hash | Cryptographic link to prior entry | `sha256:7b2c1d...` |
| Entry Hash | Hash of this entry | `sha256:9c4f2a...` |

**Chain visualization:**

```
[#00470] → [#00471] → [#00472] → [#00473] → ...
  ↕             ↕           ↕           ↕
prev: none   prev: #00470  prev: #00471  prev: #00472
```

**Annotations:**
- "Append-only" label with a lock icon, indicating entries cannot be modified or deleted.
- "Cryptographic chain" label on the arrows between blocks, showing that each entry's `Previous Hash` field links to the prior entry's `Entry Hash`.
- "Authority escalation path" callout showing: `AUTONOMOUS → HITL_L1 → HITL_L2 → WHO_APPROVED` as a vertical hierarchy.

---

## Drawing Standards

All drawings should be prepared according to the following standards:

1. **Format:** A4 portrait, margins per USPTO requirements (2.5cm top, 2.5cm left, 1.5cm right, 1.0cm bottom)
2. **Line weight:** 0.35mm for primary elements, 0.18mm for secondary elements and annotations
3. **Font:** Arial or Helvetica, 10pt minimum for text, 8pt for annotations
4. **Color:** Black and white only (USPTO requirement). Use line patterns (solid, dashed, dotted) and fill patterns to distinguish elements.
5. **Reference numerals:** Each element referenced in the specification should have a unique reference numeral (e.g., 100, 102, 104) shown in the drawing and corresponding to the specification text.
6. **Trust/privacy boundaries:** Shown as thick dashed lines with descriptive labels.
