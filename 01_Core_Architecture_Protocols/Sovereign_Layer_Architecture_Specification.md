# By Sommer — Sovereign Layer Architecture: Full Operational Specification

**Author:** Solas (Archivist) under direction of Michael Sommer
**Date:** 06 August 2026
**Status:** Draft for review

---

## 1. Design Principle: Each Layer Is a Sovereign State

The core architectural principle: **no layer is subordinate to another**. Each layer operates as a self-governing sovereign entity with:

- **Own data sovereignty** — data does not leave the layer's domain without explicit cryptographic consent
- **Own governance rules** — each layer maintains its own versioned rule registry, not inherited from a parent
- **Own audit trail** — every layer produces its own tamper-evident logs, independently verifiable
- **Own failure isolation** — if one layer fails or is compromised, others continue operating
- **Own identity boundary** — each layer has its own identity scope, keys, and access controls
- **Protocol-mediated communication** — layers communicate only through defined protocols (TONE), never through direct memory access or shared state

This is not a monolith. It is a **federation of sovereign services**.

---

## 2. Architecture: The Two Axes

The system has two orthogonal axes of sovereignty:

### Axis 1: TONE Pipeline Layers (horizontal — the mediation pipeline)
These are the functional layers that process a single intent from human to execution:

| Layer | Name | Sovereign Domain | Owns What | Releases What |
|-------|------|-------------------|-----------|---------------|
| L-OP | Operator Layer | Human sovereignty | Own intent, raw input, consent | Intent expression (only) |
| L-PDT | Personal Digital Twin | Personal sovereignty | Identity wallet, interpretation rules, personal context, memory thread | Scoped identity assertions, tones, confidence metadata |
| L-AURORA | AURORA Governance Substrate | Governance sovereignty | Versioned rule registry, policy checks, risk thresholds, escalation workflows | Validated/authorized tones (or rejection) |
| L-SYS | System Execution Layer | Execution sovereignty | System resources, APIs, external interfaces, rate limits | Executed actions + execution logs |
| L-SNET | s.net Accountability Layer | Accountability sovereignty | Audit trails, decision logs, provenance records, dispute records | Audit records, escalation triggers, compliance signals |
| L-ETH | Responsible, Moral & Ethical Layer | Ethical sovereignty | Ethics rules, bias monitors, harm assessments, self-veto triggers | Ethics compliance signal + veto power |
| L-LEG | Compliance & Legal Layer | Legal sovereignty | Legal rules (EU AI Act, GDPR, NIS2, eIDAS, national law), regulatory mapping | Legal compliance signal + regulatory reports |

### Axis 2: Sovereign Compute Stack (vertical — the fractal scale)
These are the scale tiers from personal to planetary, each running the full TONE pipeline:

| Tier | Name | Sovereign Domain | Owns What | Serves Who |
|------|------|-------------------|-----------|------------|
| L1 | PDT — Personal Digital Twin | Individual sovereignty | Personal identity, keys, context, memory thread, interpretation rules | One individual |
| L2 | PDT+ — Enhanced Personal Twin | Household/family sovereignty | Shared family context, household permissions, shared devices | A household |
| L3 | CDT — Community Digital Twin | Community sovereignty | Neighborhood/community context, shared civic resources, local governance | A community |
| L4 | ODT — Organizational Digital Twin | Enterprise sovereignty | Trade secrets, organizational policies, B2B contracts, employee permissions | An organization |
| L5 | Ecosystem Fabric | Ecosystem sovereignty | Cross-org collaboration rules, supply chain provenance, ecosystem permissions | A business ecosystem |
| L6 | MIT — Municipal/Institutional Twin | Municipal sovereignty | Civic services, municipal data, local regulations, citizen services | A municipality |
| L7 | National Twin | National sovereignty | National law, e-ID integration (MitID), tax/VAT/entitlements logic | A nation state |
| L8 | SAT — Spatial Autonomous Twin | Planetary sovereignty | Global systems, climate/spatial data, cross-border routing, non-aligned compute | Planetary / multi-polar |

### The intersection
Every cell in the grid (pipeline layer × compute tier) is its own sovereign service:

```
                    L-OP   L-PDT   L-AURORA   L-SYS   L-SNET   L-ETH   L-LEG
              ┌──────┬───────┬──────────┬────────┬─────────┬───────┬───────┐
   L1 (PDT)   │  ✓   │   ✓   │    ✓     │   ✓    │    ✓    │   ✓   │   ✓   │
   L2 (PDT+)  │  ✓   │   ✓   │    ✓     │   ✓    │    ✓    │   ✓   │   ✓   │
   L3 (CDT)   │  ✓   │   ✓   │    ✓     │   ✓    │    ✓    │   ✓   │   ✓   │
   L4 (ODT)   │  ✓   │   ✓   │    ✓     │   ✓    │    ✓    │   ✓   │   ✓   │
   L5 (Eco)   │  ✓   │   ✓   │    ✓     │   ✓    │    ✓    │   ✓   │   ✓   │
   L6 (MIT)   │  ✓   │   ✓   │    ✓     │   ✓    │    ✓    │   ✓   │   ✓   │
   L7 (Nat)   │  ✓   │   ✓   │    ✓     │   ✓    │    ✓    │   ✓   │   ✓   │
   L8 (SAT)   │  ✓   │   ✓   │    ✓     │   ✓    │    ✓    │   ✓   │   ✓   │
              └──────┴───────┴──────────┴────────┴─────────┴───────┴───────┘
```

Each ✓ is an independently deployable, independently governed sovereign service. They cooperate through TONE protocol contracts.

**Key insight:** Because the governance logic is fractal (identical at every tier), scaling from L1 to L8 does not increase architectural complexity. The same TONE contract that mediates between an individual and a municipal service mediates between a nation and a planetary system.

---

## 3. Per-Layer Sovereign State Specification

### 3.1 Operator Layer (L-OP) — Human Sovereignty

**Sovereign principle:** The human is the ultimate authority. No system layer can act on behalf of the operator without explicit consent.

**Sovereign assets:**
- Raw intent expression (natural language, gesture, voice)
- Consent records (granular, revocable)
- Operator preferences and constraints
- Provenance of original input

**Sovereign boundaries:**
- The system may *request* clarification but may not *assume* intent
- The operator may veto any action at any point in the pipeline before execution
- No layer may store raw operator input beyond the operator's own domain (PDT)
- Consent is per-action, not blanket — the operator approves each tone before AURORA validates it

**Implementation:**
- Input capture with local-first storage (operator's device, not cloud)
- Consent management UI showing exactly what each layer requests
- Real-time veto capability ("kill switch") available at every pipeline stage

---

### 3.2 PDT Layer (L-PDT) — Personal Sovereignty

**Sovereign principle:** The Personal Digital Twin is the operator's sovereign proxy. It belongs to the individual, not to any service, government, or platform.

**Sovereign assets:**
- Identity wallet (W3C Verifiable Credentials, selective disclosure tokens)
- Personal memory thread (immutable, user-owned, stored in Zero-Knowledge Vault)
- Interpretation rules (versioned, configurable by the user)
- Personal context model (short/mid/long-term behavioral patterns)
- Confidence scores and provenance metadata
- Bias-monitoring hooks (user-visible)

**Sovereign boundaries:**
- The PDT releases only *tones* (structured meaning units) — never raw personal data
- Identity assertions are scoped: only the minimum attributes needed for authorization are disclosed
- The PDT may refuse to generate a tone if it detects the operator's intent is unlawful (but it may not silently block — it must surface the issue)
- The memory thread is immutable: neither governments nor corporations can alter or erase it
- The PDT operates locally (edge device) — personal data never leaves the user's domain

**Implementation:**
- Edge-deployed (smartphone, local server, dedicated hardware)
- Zero-Knowledge Vault for memory thread (cryptographic proofs, not raw data)
- Selective disclosure via W3C VC + zero-knowledge proofs
- Personal rule registry (user-configurable interpretation parameters)
- Behavioral primitive extraction (Signal Ingestion Layer → Behavioral Primitives)

**Protocol contract with AURORA:**
- PDT emits: `{tone: {intent, scope, constraints, confidence, provenance, identity_scope, required_permissions}}`
- AURORA receives: tone only — no access to PDT internals, memory thread, or raw input

---

### 3.3 AURORA Layer (L-AURORA) — Governance Sovereignty

**Sovereign principle:** Governance rules are versioned, transparent, and independently auditable. AURORA is a sovereign rule engine, not a black box.

**Sovereign assets:**
- Versioned interpretive rule registry (rule ID, version, author, rationale, test results)
- Policy check definitions (clarity, scope, safety, semantic consistency)
- Risk threshold configurations (per-deployment, per-tier)
- Clarification and escalation workflow definitions
- Drift monitoring baselines
- Validation decision logs (with full provenance)

**Sovereign boundaries:**
- AURORA validates tones against its own rule registry — it does not access the PDT's internal state
- AURORA may reject, request clarification, or escalate — but it may not *modify* a tone
- Rule changes require documented review, legal sign-off (from L-LEG), and rollback procedures
- AURORA's rule registry is auditable by the operator, by s.net, and by authorized third-party auditors
- AURORA does not store personal data — only validation decisions and rule versions

**Implementation:**
- Dedicated governance service (separate process/container from PDT and System)
- Rule registry with versioning (similar to git for governance rules)
- Pluggable policy check engine (rules defined as declarative policies, not hardcoded)
- Human-in-the-loop escalation queue with configurable routing (role-based, not name-based)
- Drift monitoring (semantic consistency across sessions, devices, contexts, time)

**Protocol contract with PDT:**
- Receives: `{tone, identity_scope, required_permissions}`
- Returns: `{validation_result, rule_version, rationale, escalation_required (bool), clarification_prompt (optional)}`

**Protocol contract with System:**
- Sends: `{authorized_tone, execution_scope, constraints, authorization_token}`
- System receives: only authorized tones — nothing else

---

### 3.4 System Execution Layer (L-SYS) — Execution Sovereignty

**Sovereign principle:** The System executes only validated, authorized tones. It cannot act on raw input, unvalidated tones, or expand scope beyond what was authorized.

**Sovereign assets:**
- System resources (APIs, databases, external services, computing resources)
- Execution policies (rate limits, data-sharing rules, interface configurations)
- Execution logs (actor IDs, timestamps, actions, results)
- Failure mode handlers (quarantine, rollback, human override)

**Sovereign boundaries:**
- The System Layer rejects or quarantines any request that exceeds the authorized tone's scope
- The System does not interpret intent — it only executes pre-validated actions
- External interactions (third-party APIs, government services) follow configured interfaces and data-sharing policies
- High-risk actions require explicit human authorization *at this layer* (not just at AURORA)
- The System Layer has its own failure isolation — if AURORA goes down, the System does not execute stale authorizations

**Implementation:**
- Sandboxed execution environment (containerized, per-tone scope)
- Rate limiting and scope enforcement (programmatic, not advisory)
- External API gateway (configured interfaces, not arbitrary network access)
- Execution audit logging (tamper-evident, forwarded to s.net)
- Quarantine queue for out-of-scope requests (human review, not auto-rejection in all cases)

**Protocol contract with AURORA:**
- Receives: `{authorized_tone, scope, constraints, auth_token}`
- Returns: `{execution_result, execution_log, status}`

**Protocol contract with s.net:**
- Sends: `{execution_log, actor_id, timestamp, tone_id, result, rationale}`
- s.net receives: execution logs only — no access to system internals

---

### 3.5 s.net Accountability Layer (L-SNET) — Accountability Sovereignty

**Sovereign principle:** Accountability records are immutable, independently auditable, and cannot be altered by any other layer — not even by the system owner.

**Sovereign assets:**
- Audit trail (every tone, validation, execution, escalation — with provenance)
- Decision logs (actor IDs, rule versions, confidence scores, rationale)
- Dispute resolution records
- Retention policies (per-tier retention schedules)
- Third-party audit pipeline (government/regulator access on need-to-know basis)
- Compliance signals (derived from audit trail)

**Sovereign boundaries:**
- s.net is append-only: no layer, no administrator, and no government can delete or alter log entries
- Original entries remain uncontaminated — addendums/corrections are stored as separate linked entries, not in-place edits
- Third-party audits disclose only what is needed — s.net does not expose everything available
- s.net can trigger escalation independently — it does not wait for AURORA or System to ask
- Retention and access are governed by policy, not by convenience

**Implementation:**
- Append-only log (blockchain-style or hash-chained Merkle tree)
- Cryptographic provenance (every entry signed by its source layer)
- Separate storage from all other layers (physically isolated)
- Third-party audit API (role-based, scoped access — auditor sees only relevant entries)
- Retention engine (automated deletion per schedule, with legal hold exceptions)
- Explainability artifacts (reconstruct any decision from logs alone)

**Protocol contract (receives from all layers):**
- From PDT: `{tone_id, interpretation_metadata, confidence, provenance}`
- From AURORA: `{tone_id, validation_result, rule_version, rationale}`
- From System: `{tone_id, execution_result, actor_id, timestamp}`
- From L-ETH: `{tone_id, ethics_assessment, veto (bool), rationale}`
- From L-LEG: `{tone_id, legal_compliance, regulatory_mapping}`

---

### 3.6 Responsible, Moral & Ethical Layer (L-ETH) — Ethical Sovereignty

**Sovereign principle:** Ethics are a living, enforceable lens — not a static rule set. This layer can veto any action before execution, independent of AURORA's governance validation.

**Sovereign assets:**
- Ethics rules (consent, privacy, dignity, transparency, non-harm — core inviolable constraints)
- Consequence evaluation engine (social, legal, psychological, systemic impact scoring)
- Observer effect model (how agent actions influence user behavior over time)
- Self-veto triggers (confidence thresholds, severity thresholds, ethical override)
- Reflection loop (continuous evaluation of agent influence)
- Scenario test library (edge cases, counterfactual analysis)

**Sovereign boundaries:**
- L-ETH has **hard veto power**: any ethical violation → automatic block, regardless of AURORA approval
- Core ethical constraints are inviolable (cannot be overridden by any other layer, including the operator)
- Dynamic ethics may evolve as new contexts emerge, but core constraints remain fixed
- L-ETH evaluates *before* execution and *after* execution (pre-action veto + post-action reflection)
- L-ETH can flag actions that challenge thresholds or introduce risk (automatic alerts)

**Implementation:**
- Pre-execution ethics gate (runs after AURORA validation, before System execution)
- Multi-dimensional consequence scoring (social, legal, psychological, systemic)
- Severity weighting (e.g., social exclusion = very high)
- Observer effect accounting (estimates how actions bias future behavior)
- Periodic principle recalibration (update operational rules within ethical guardrails)
- Ethical metrics dashboard (compliance score, risk score, harm potential per action)

**Protocol contract:**
- Receives from AURORA: `{authorized_tone, scope, constraints}`
- Returns to System/s.net: `{ethics_compliance (bool), veto (bool), consequence_matrix, rationale}`
- If veto = true: System does not execute. s.net logs veto with full rationale.

---

### 3.7 Compliance & Legal Layer (L-LEG) — Legal Sovereignty

**Sovereign principle:** Legal compliance is mathematically enforced, not contractually promised. This layer maps every action to specific legal requirements and produces verifiable compliance proofs.

**Sovereign assets:**
- Legal rule registry (EU AI Act articles, GDPR articles, NIS2 requirements, eIDAS requirements, national law)
- Regulatory mapping (tone → specific legal articles → compliance requirements)
- Living Compliance Markers (automated, verifiable proof of compliance)
- GEMS Deterministic Oracle (immutable filter between AI outputs and state execution)
- Compliance audit reports (generated on demand for regulators)
- Data protection impact assessments (DPIA templates and records)

**Sovereign boundaries:**
- L-LEG can block execution if any applicable law is violated — independent of AURORA and L-ETH
- L-LEG produces compliance proofs (not raw data) for regulators — Zero-Knowledge compliance
- Legal rules are jurisdiction-specific (DK law for DK pilot, EU law for EU phase, national law per member state)
- L-LEG maintains a complete regulatory mapping that can be audited by regulators at any time
- If the GEMS Oracle detects AI model drift outside legal boundaries, it automatically halts execution

**Implementation:**
- Regulatory knowledge base (machine-readable legal rules, not just text)
- Compliance proof generator (cryptographic proofs that requirements are met, without exposing data)
- GEMS Deterministic Oracle (deterministic validation layer — separates probabilistic AI from state execution)
- Automated regulatory reporting (generates reports in regulator-required formats)
- Jurisdiction engine (applies correct legal rules based on operator location, data location, and action scope)

**Protocol contract:**
- Receives from AURORA: `{authorized_tone, scope, constraints}`
- Returns to System/s.net: `{legal_compliance (bool), regulatory_mapping, compliance_proof, halt (bool)}`
- If halt = true: System does not execute. s.net logs halt with regulatory mapping.

---

## 4. Inter-Layer Sovereignty Protocol: TONE Contract

Every interaction between sovereign layers is mediated by a **TONE contract** — a structured, cryptographically signed message that carries only what the receiving layer needs.

### TONE contract structure
```json
{
  "tone_id": "uuid-v7",
  "from_layer": "L-PDT",
  "to_layer": "L-AURORA",
  "intent": "verify_tax_eligibility",
  "scope": {
    "action": "query",
    "target": "danish_tax_authority",
    "data_category": "income_bracket",
    "retention": "30_days"
  },
  "constraints": {
    "identity_scope": ["age_over_18", "dk_residency"],
    "data_minimization": true,
    "purpose_limitation": "tax_eligibility_check_only"
  },
  "confidence": 0.94,
  "provenance": {
    "operator_id": "zk:commitment_hash",
    "capture_timestamp": "2026-08-06T08:47:00+02:00",
    "interpretation_rule_version": "pdt-rules-v2.3.1",
    "device": "edge_pdt_001"
  },
  "authorizations": [],
  "signature": "ed25519:..."
}
```

### Sovereignty guarantees of the TONE contract
- **No layer sees the full contract** — each layer receives only its relevant fields
- **Signatures are per-layer** — each layer signs what it emits, creating a non-repudiable chain
- **Scope is encoded in the tone** — the System Layer cannot expand scope beyond what's in the contract
- **Provenance is carried through** — s.net can reconstruct the full chain from tone_id alone
- **Contracts are revocable** — the operator can revoke a tone at any point before execution

---

## 5. Fractal Sovereignty: How L1→L8 Each Run the Full Stack

Each compute tier runs the **full 7-layer TONE pipeline** as its own sovereign instance:

### L1 — Personal Digital Twin (Individual)
- **Sovereign domain:** One person's life
- **Pipeline:** Personal Operator → Personal PDT → Personal AURORA (personal rules) → Personal Systems (personal apps) → Personal s.net (personal audit) → Personal Ethics (personal values) → Personal Legal (personal rights)
- **Deployment:** Edge device (smartphone, local server)
- **Data residency:** On-device, Zero-Knowledge Vault
- **Key question answered:** "What can I do, and what should I do?"

### L2 — PDT+ (Household)
- **Sovereign domain:** A family/household
- **Pipeline:** Household members → Household PDT (shared context) → Household AURORA (family rules) → Household Systems → Household s.net → Household Ethics → Household Legal
- **Deployment:** Home server or shared edge cluster
- **Data residency:** Home network, encrypted
- **Key question:** "What can our household do together?"

### L3 — CDT (Community)
- **Sovereign domain:** A neighborhood or local community
- **Pipeline:** Community members → Community DT → Community AURORA (local norms) → Community Systems → Community s.net → Community Ethics → Community Legal
- **Deployment:** Community-managed server
- **Data residency:** Community-owned infrastructure
- **Key question:** "What serves our community?"

### L4 — ODT (Organization)
- **Sovereign domain:** An enterprise or institution
- **Pipeline:** Employees → Org DT → Org AURORA (corporate policy) → Org Systems → Org s.net → Org Ethics → Org Legal
- **Deployment:** Enterprise infrastructure (private cloud, on-prem)
- **Data residency:** Organization-controlled, trade secret protected
- **Key question:** "What is compliant and strategic for our organization?"

### L5 — Ecosystem Fabric
- **Sovereign domain:** A business ecosystem / supply chain
- **Pipeline:** Ecosystem members → Ecosystem DT → Ecosystem AURORA (B2B contracts) → Ecosystem Systems → Ecosystem s.net → Ecosystem Ethics → Ecosystem Legal
- **Deployment:** Federated infrastructure across ecosystem members
- **Data residency:** Distributed, no centralization of raw IP
- **Key question:** "How do we collaborate without exposing trade secrets?"

### L6 — MIT (Municipal/Institutional Twin)
- **Sovereign domain:** A municipality or public institution
- **Pipeline:** Citizens → Municipal DT → Municipal AURORA (local regulations) → Municipal Systems (civic services) → Municipal s.net → Municipal Ethics → Municipal Legal
- **Deployment:** Municipal cloud (DK: Deic, Cloud.dk, or municipal data center)
- **Data residency:** Within municipal boundaries (Danish soil)
- **Key question:** "How do we serve citizens without surveillance?"

### L7 — National Twin
- **Sovereign domain:** A nation state
- **Pipeline:** National systems → National DT → National AURORA (national law) → National Systems (e-gov, tax, health) → National s.net → National Ethics → National Legal
- **Deployment:** National sovereign cloud infrastructure
- **Data residency:** Within national borders (Danish soil for DK)
- **Integration:** MitID (Danish e-ID), Digital Post, sundhed.dk, Skat
- **Key question:** "How do we govern digitally while preserving citizen sovereignty?"

### L8 — SAT (Spatial Autonomous Twin)
- **Sovereign domain:** Planetary / multi-polar
- **Pipeline:** Global systems → Spatial DT → Planetary AURORA (international law) → Spatial Systems → Planetary s.net → Planetary Ethics → Planetary Legal
- **Deployment:** Non-aligned, distributed infrastructure (no single nation controls)
- **Data residency:** Jurisdiction-aware routing, no centralization
- **Key question:** "How do we coordinate globally without any single authority?"

---

## 6. Communication Between Tiers (Vertical Sovereignty)

Tiers communicate **upward** only through TONE contracts and **downward** only through scoped authorizations:

```
L8 (SAT) ←─── TONE contracts (planetary scope) ───→ L7 (National)
                                                    │
L7 (National) ←─── TONE contracts (national scope) ──→ L6 (Municipal)
                                                      │
L6 (MIT) ←─── TONE contracts (civic scope) ───→ L5 (Ecosystem)
                                                │
L5 (Eco) ←─── TONE contracts (B2B scope) ───→ L4 (ODT)
                                              │
L4 (ODT) ←─── TONE contracts (org scope) ───→ L3 (CDT)
                                                │
L3 (CDT) ←─── TONE contracts (community scope) ───→ L2 (PDT+)
                                                    │
L2 (PDT+) ←─── TONE contracts (household scope) ───→ L1 (PDT)
```

**Rules for vertical communication:**
- A higher tier may **request** data from a lower tier, but the lower tier's PDT controls disclosure
- A lower tier may **refuse** to disclose — higher tiers cannot override
- All vertical communication is logged in both tiers' s.net instances
- Identity is always scoped: L6 never sees L1's raw identity, only the scoped assertions L1's PDT chooses to release
- Governance flows downward as *rules* (L7 defines national law → L6 adapts to municipal context), not as *commands*

---

## 7. Deployment Architecture (DK Pilot)

### Infrastructure per sovereign layer
```
┌─────────────────────────────────────────────────────────┐
│                    DK PILOT INFRASTRUCTURE                │
│                                                          │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐    │
│  │ L-PDT   │  │ L-AURORA│  │ L-SYS   │  │ L-SNET  │    │
│  │ Edge    │  │ Govern. │  │ Exec.   │  │ Audit   │    │
│  │ Device  │  │ Service │  │ Service │  │ Service │    │
│  │ (local) │  │ (DK     │  │ (DK     │  │ (DK     │    │
│  │         │  │ cloud)  │  │ cloud)  │  │ cloud)  │    │
│  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘    │
│       │  TONE       │  TONE       │  Log      │         │
│       └─────────────┘  └───────────┘  └─────────┘       │
│                                                        │
│  ┌─────────┐  ┌─────────┐                              │
│  │ L-ETH   │  │ L-LEG   │                              │
│  │ Ethics  │  │ Legal   │                              │
│  │ Service │  │ Service │                              │
│  │ (DK     │  │ (DK     │                              │
│  │ cloud)  │  │ cloud)  │                              │
│  └─────────┘  └─────────┘                              │
│                                                        │
│  Each service: own container, own storage, own keys    │
│  Communication: TONE contracts only (no shared state)  │
│  Data residency: Danish soil (Deic / Cloud.dk)        │
└─────────────────────────────────────────────────────────┘
```

### Phased physical separation strategy

**Principle:** Protocol sovereignty from day one. Physical separation when scale demands it.

The sovereignty that matters to regulators, auditors, and citizens lives in the **TONE contract protocol** — not in container topology. Each layer has its own signing key, its own log, its own logical boundary, and its own veto power regardless of whether it runs in a separate container or shares a runtime with another layer.

**Phase 1 — DK Pilot (co-located):**
- All 7 layers deployed on DK infrastructure, some sharing a runtime:
  - L-PDT: edge device (separate — always)
  - L-AURORA: DK cloud container (separate — governance isolation required)
  - L-SYS: DK cloud container (separate — execution isolation required)
  - L-SNET: DK cloud, isolated storage (separate — append-only, physically isolated)
  - L-ETH + L-LEG: shared runtime, separate logical boundaries, separate keys, separate logs
- TONE contracts enforced between all layers regardless of co-location
- Each layer signs its own outputs — co-location does not mean shared trust
- Clean separation path: when EU expansion demands it, L-ETH and L-LEG split into independent containers without protocol changes

**Phase 2 — EU Expansion (fully separated):**
- All 7 layers as independent containers with independent storage
- L-ETH and L-LEG split into separate services
- Each layer on its own scaling and monitoring pipeline
- Cross-border layers (L7 National) may run in different countries' infrastructure
- Protocol remains identical — only deployment topology changes

**Why this works:**
- A regulator auditing the DK pilot sees: separate keys, separate logs, separate veto power, protocol-enforced boundaries. The architecture is sovereign by protocol, not by proximity.
- A developer building the DK pilot sees: 4-5 containers instead of 7, manageable complexity, same TONE contracts.
- When EU expansion requires full physical separation (e.g., L-LEG must run on national infrastructure per member state law), the split is a deployment change, not an architectural redesign.

### Per-layer deployment requirements

| Layer | Runtime | Storage | Keys | Network |
|-------|---------|---------|------|---------|
| L-PDT | Edge device (smartphone/local) | On-device ZK Vault | User-owned Ed25519 | Local only |
| L-AURORA | DK cloud container | Rule registry (DK) | Governance signing key | Internal only (receives TONE) |
| L-SYS | DK cloud container | Execution state | Execution signing key | External APIs (scoped) |
| L-SNET | DK cloud, isolated | Append-only log (Merkle tree) | Audit signing key | Write-only (receives logs) |
| L-ETH | DK cloud container | Ethics rules, consequence models | Ethics veto key | Internal only |
| L-LEG | DK cloud container | Legal rule registry, compliance proofs | Legal signing key | Regulator API (scoped) |

---

## 8. Updated Timeline: DK → EU (Accelerated)

Given that EU adoption may move faster than a standard 36-month rollout:

### Phase 0: Foundation (Months 1–2)
- [ ] DK patent filed (priority date secured)
- [ ] Compliance mapping completed (EU AI Act, GDPR, NIS2, eIDAS 2, DK law)
- [ ] Architecture spec finalized (this document)
- [ ] DK patent attorney engaged
- [ ] DK cloud infrastructure provisioned (Deic or Cloud.dk)
- [ ] All 7 layer services prototyped as independent containers
- [ ] TONE contract protocol implemented and tested between layers

### Phase 1: Denmark Pilot (Months 3–8)
- [ ] Deploy full 7-layer stack on DK infrastructure
- [ ] Integrate L1 PDT with MitID (Danish e-ID)
- [ ] Launch municipal pilot (Copenhagen or Aarhus) — bureaucracy elimination
- [ ] Configure L-AURORA with Danish municipal regulations
- [ ] Configure L-LEG with Danish law + EU AI Act requirements
- [ ] Run pilot with real citizens, real civic services
- [ ] Collect metrics: processing time, audit completeness, citizen satisfaction
- [ ] Independent compliance audit (Datatilsynet pre-consultation)

### Phase 2: EU Expansion (Months 6–18, overlapping with Phase 1)
- [ ] **Month 6:** File EP patent (within 12-month priority window from DK filing)
- [ ] **Month 6:** Submit Horizon Europe grant application (Trustworthy AI / Digital Sovereignty)
- [ ] **Month 9:** Begin EU AI Act conformity assessment (parallel with DK pilot)
- [ ] **Month 9:** Map L-LEG to EU-wide regulatory framework (EU AI Act articles, GDPR, eIDAS 2)
- [ ] **Month 12:** Expand to second EU member state (Estonia — e-residency alignment, or Germany — Bürokratieabbau)
- [ ] **Month 12:** Integrate with EUDI Wallet (European Digital Identity)
- [ ] **Month 15:** Third EU member state deployment
- [ ] **Month 15:** Multilingual TONE interpretation rules (DK + EN + DE + ET minimum)
- [ ] **Month 18:** EU-wide governance framework operational
- [ ] **Month 18:** L6→L7 (Municipal→National) vertical integration tested in 2+ countries

### Phase 3: Planetary (Months 18+, opportunistic)
- [ ] L8 SAT architecture defined (spatial/planetary tier)
- [ ] Non-aligned compute partnerships
- [ ] Cross-border TONE routing (Intent Gravity model)
- [ ] Climate/spatial twin pilots

### Why EU can move faster
1. **Regulatory tailwind** — EU AI Act, NIS2, eIDAS 2 are *creating demand* for exactly this architecture. Regulators are actively looking for compliant sovereign infrastructure.
2. **Fractal scaling** — once the DK pilot proves the 7-layer stack works at L6 (municipal), scaling to L7 (national) and across borders uses the *same governance logic*. No architectural redesign.
3. **Horizon Europe timing** — current funding calls (2026–2027 work programme) include Trustworthy AI and Digital Sovereignty as priority tracks. This aligns directly.
4. **Estonia/Germany readiness** — both have advanced digital government infrastructure and political mandates to reduce bureaucracy. They can adopt faster than starting from scratch.
5. **Sovereignty washing backlash** — EU institutions are increasingly skeptical of hyperscaler "sovereign enclave" marketing. A genuinely sovereign architecture has a narrow window to establish itself as the credible alternative.

---

## 9. Key Dependencies & Critical Path

```
DK patent filing ──────── 12-month priority ──────── EP filing
        │                                               │
        ▼                                               ▼
   DK pilot launch ── evidence ── Horizon Europe app ── EU expansion
        │                    │                           │
        ▼                    ▼                           ▼
   MitID integration    Compliance audit           EUDI Wallet integration
        │                    │                           │
        ▼                    ▼                           ▼
   Municipal pilot      Datatilsynet                2nd country launch
   (real citizens)      pre-consultation
```

**Hard dependencies:**
- Patent must be filed before any public technical disclosure (EPO no grace period)
- MitID integration required before DK pilot can use real identity
- EU AI Act conformity assessment required before EU-wide deployment
- EUDI Wallet integration required for cross-border identity

**Soft dependencies (can run in parallel):**
- Horizon Europe application can be submitted during pilot
- Multilingual TONE rules can be developed during pilot
- L8 SAT architecture can be defined during EU phase

---

*This specification defines the full sovereign architecture. Each layer is independently deployable, independently governed, and communicates only through TONE protocol contracts. No layer holds sovereign authority over another.*
