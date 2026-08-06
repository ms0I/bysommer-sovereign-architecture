# L-LEG: The Living Legal Operating System

**Author:** Solas (Archivist) under direction of Michael Sommer  
**Date:** 06 August 2026  
**Status:** Draft for review

---

## 1. Core Concept

The Compliance Book is not a static document. It is a **living legal operating system** — the core foundation of the legal procedures, rules, and constraints that govern every action the AURA/TONE architecture takes.

It is:
- **Living** — constantly updating as laws change, court rulings land, and regulations evolve
- **Location-aware** — adapts to the operator's jurisdiction (DK/EU, CA/US, etc.) to provide the correct legal environment
- **Structural** — compliance is not a checklist applied after the fact; it is the operating system the digital system runs *on top of*

The L-LEG layer (Compliance & Legal Layer) is the runtime implementation of this legal OS.

---

## 2. How It Works: The Legal OS Stack

```
┌─────────────────────────────────────────────────────────┐
│                 L-LEG LEGAL OPERATING SYSTEM              │
│                                                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │            JURISDICTION DETECTION ENGINE           │   │
│  │  Determines which legal rule set applies:        │   │
│  │  • Operator geolocation (GPS / IP / declared)     │   │
│  │  • Data residency (where data is stored)         │   │
│  │  • Action target (which government/service)      │   │
│  │  • Cross-border data flow destination            │   │
│  └──────────────────────┬──────────────────────────┘   │
│                         │                               │
│  ┌──────────────────────▼──────────────────────────┐   │
│  │            JURISDICTION RULE SET LOADER           │   │
│  │  Loads the appropriate legal environment:        │   │
│  │  • EU: AI Act + GDPR + NIS2 + eIDAS 2            │   │
│  │  • DK: + Databeskyttelsesloven + Bogføringsloven │   │
│  │  • CA: CCPA + CPRA + California AI Act           │   │
│  │  • US (federal): sector-specific frameworks      │   │
│  │  • Generic: human rights baseline (UDHR + ECHR)  │   │
│  └──────────────────────┬──────────────────────────┘   │
│                         │                               │
│  ┌──────────────────────▼──────────────────────────┐   │
│  │            RULE RESOLUTION ENGINE                 │   │
│  │  For each TONE contract received:                │   │
│  │  1. Identify applicable legal articles           │   │
│  │  2. Check jurisdiction-specific requirements     │   │
│  │  3. Resolve conflicts (stricter rule wins)        │   │
│  │  4. Generate compliance proof or halt signal     │   │
│  └──────────────────────┬──────────────────────────┘   │
│                         │                               │
│  ┌──────────────────────▼──────────────────────────┐   │
│  │            COMPLIANCE PROOF GENERATOR             │   │
│  │  Produces verifiable proof that requirements are  │   │
│  │  met — without exposing raw data:                │   │
│  │  • Cryptographic proof of compliance              │   │
│  │  • Regulatory mapping (article → requirement →    │   │
│  │    architectural component)                       │   │
│  │  • Audit-ready report format                      │   │
│  └──────────────────────┬──────────────────────────┘   │
│                         │                               │
│  ┌──────────────────────▼──────────────────────────┐   │
│  │            GEMS DETERMINISTIC ORACLE              │   │
│  │  Immutable filter between AI outputs and state    │   │
│  │  execution — deterministic (non-probabilistic)    │   │
│  │  validation that AI outputs comply with legal     │   │
│  │  requirements before any execution proceeds       │   │
│  └─────────────────────────────────────────────────┘   │
│                                                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │            LIVING UPDATE PIPELINE                 │   │
│  │  Keeps the legal OS current:                     │   │
│  │  • Monitors legal/regulatory changes             │   │
│  │  • Versioned rule updates (with author, review,  │   │
│  │    legal sign-off, rollback)                     │   │
│  │  • Addendum chain (no deletion of old rules —    │   │
│  │    superseded but preserved for audit)           │   │
│  │  • Cross-jurisdiction conflict resolution updates│   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

---

## 3. Jurisdiction-Aware Operation

### 3.1 The Problem This Solves

A citizen in Copenhagen asks their PDT to verify tax eligibility. The legal environment is:
- Danish Data Protection Act (national)
- GDPR (EU)
- EU AI Act (EU — high-risk classification)
- Danish Bookkeeping Act (national)

The same citizen travels to California and asks the same question. The legal environment shifts to:
- CCPA / CPRA (state)
- California AI Act (state, if enacted)
- US sector-specific regulations (federal, where applicable)
- GDPR still applies if EU data is involved (extraterritorial reach)

The Legal OS detects the jurisdiction change and loads the correct rule set — **without the operator needing to know or care about which laws apply**. The system always operates in the best possible legal environment for that location.

### 3.2 Jurisdiction Detection Signals

The Legal OS uses multiple signals to determine the applicable jurisdiction:

| Signal | Source | Weight | Notes |
|--------|--------|--------|-------|
| Operator declared residency | PDT profile | Primary | User-declared, cannot be auto-overridden |
| Operator physical location | Device GPS (opt-in) | Secondary | Used for real-time jurisdiction shifts (travel) |
| Data storage location | ZK Vault metadata | Tertiary | Where is the data actually stored? |
| Action target jurisdiction | TONE contract `scope.target` | Critical | Which government/service is the action directed at? |
| Cross-border data flow | TONE contract `scope.data_category` + destination | Critical | Schrems II / data transfer rules apply |

### 3.3 Conflict Resolution: Stricter Rule Wins

When multiple jurisdictions apply (e.g., EU citizen in California), the Legal OS resolves conflicts using the **stricter-rule-wins** principle:

```
If EU GDPR requires data minimization AND California CCPA requires right to delete:
  → Both apply. The system enforces the stricter obligation for each specific requirement.

If EU AI Act requires human oversight for high-risk AND US has no equivalent:
  → EU AI Act applies (it's stricter). The L-ETH veto layer remains active regardless of location.
  → Core ethical constraints are inviolable in all jurisdictions.

If a national law contradicts EU law (rare):
  → EU law takes precedence within EU (primacy principle).
  → Outside EU, the national law applies, but core human rights (UDHR) remain the floor.
```

**Core principle:** The legal OS never *lowers* protections below the baseline. It can only *raise* them based on jurisdiction.

### 3.4 Jurisdiction Rule Sets

Each jurisdiction maintains its own versioned rule set:

```
jurisdictions/
  ├── eu/
  │   ├── ai_act.json          (EU AI Act articles, risk tiers, obligations)
  │   ├── gdpr.json            (GDPR articles, data subject rights, legal bases)
  │   ├── nis2.json            (NIS2 requirements, incident reporting timelines)
  │   ├── eidas2.json          (eIDAS 2, EUDI Wallet, trust services)
  │   ├── data_act.json        (Data Act, data sharing rules)
  │   └── digital_services_act.json  (DSA, platform obligations)
  ├── dk/
  │   ├── databeskyttelsesloven.json  (Danish Data Protection Act)
  │   ├── bogforingsloven.json         (Danish Bookkeeping Act)
  │   ├── mitid.json                   (Danish e-ID requirements)
  │   └── digital_strategy.json       (Danish digital administration)
  ├── us_ca/
  │   ├── ccpa_cpra.json       (California Consumer Privacy Act)
  │   ├── ca_ai_act.json       (California AI Act, if enacted)
  │   └── ca_data_broker.json  (California data broker registration)
  ├── us_federal/
  │   ├── sector_specific.json (FDA, FTC, SEC where applicable)
  │   └── constitutional.json   (US constitutional protections)
  └── baseline/
      ├── udhr.json            (Universal Declaration of Human Rights)
      ├── echr.json             (European Convention on Human Rights)
      └── core_ethics.json      (Inviolable core constraints — apply everywhere)
```

### 3.5 Living Update Protocol

The Legal OS is **constantly updating**. Rule changes follow a strict, auditable process:

```
1. DETECT: New law, regulation, or court ruling published
   (Manual: legal counsel reviews)
   (Automated: regulatory monitoring feeds, e.g., EUR-Lex, Retsinformation)

2. DRAFT: New rule or rule amendment proposed
   Author: legal counsel or authorized governance body
   Includes: affected jurisdiction, affected articles, effective date,
   transition period, supersedes (version link)

3. REVIEW: Legal review and sign-off
   Required: qualified legal counsel for the jurisdiction
   For high-impact changes: ethics review (L-ETH consultation)
   For cross-border changes: multi-jurisdiction conflict check

4. PUBLISH: Rule added to versioned registry
   Old rule is NOT deleted — it is superseded (linked, preserved for audit)
   New rule is versioned (rule_id, version, author, review_signoff, effective_date)
   GEMS Oracle updated to enforce new rule

5. NOTIFY: Downstream layers notified of change
   L-AURORA: governance rules may need recalibration
   L-ETH: ethical constraints may need updating (if law changes ethics scope)
   L-PDT: operator notifications if their rights/obligations change
   s.net: logs the rule change with full provenance

6. ROLLBACK: If a rule causes harm or is legally challenged
   Rule is suspended (not deleted) — linked to challenge record
   Previous rule version reactivates
   All affected TONE contracts re-evaluated
```

**The rule registry is append-only** — like the decision log. Old rules are never deleted; they are superseded. This means an auditor can trace the exact legal environment that was in effect at any point in time, for any decision the system made.

---

## 4. How L-LEG Processes a TONE Contract

```json
// INCOMING TONE CONTRACT (from L-AURORA)
{
  "tone_id": "uuid-v7",
  "from_layer": "L-AURORA",
  "to_layer": "L-LEG",
  "intent": "verify_tax_eligibility",
  "scope": {
    "action": "query",
    "target": "danish_tax_authority",
    "data_category": "income_bracket",
    "retention": "30_days"
  },
  "operator": {
    "declared_residency": "DK",
    "current_location": "DK"
  },
  "authorizations": ["aurora_validated"]
}
```

```json
// L-LEG PROCESSING

1. JURISDICTION DETECTION
   → Operator residency: DK
   → Current location: DK
   → Action target: DK (Danish Tax Authority)
   → Data flow: local (no cross-border)
   → Applicable jurisdictions: EU + DK

2. RULE SET LOADING
   → Load eu/gdpr.json → Art. 6 (lawful basis), Art. 9 (special categories)
   → Load eu/ai_act.json → Art. 9 (risk management), Art. 14 (human oversight)
   → Load dk/databeskyttelsesloven.json → Danish GDPR implementation
   → Load dk/bogforingsloven.json → Financial record retention
   → Load baseline/core_ethics.json → Inviolable constraints

3. RULE RESOLUTION
   → GDPR Art. 6(1)(c): legal obligation (tax compliance) → lawful basis confirmed
   → GDPR Art. 9: income bracket is not special category data → no Art. 9 restrictions
   → AI Act Art. 14: human oversight required → L-ETH veto layer active
   → Danish Bookkeeping Act: 5-year retention for tax records → overrides 30-day retention in scope
   → Conflict: TONE contract says 30 days, Danish law says 5 years
   → Resolution: stricter rule wins → 5 years

4. GEMS DETERMINISTIC ORACLE
   → Deterministic check: does this action comply with all loaded rules? YES
   → Generate compliance proof: cryptographic attestation that all applicable
     legal requirements have been checked and satisfied
   → No probabilistic AI judgment — deterministic verification only

5. OUTPUT
   {
     "tone_id": "uuid-v7",
     "from_layer": "L-LEG",
     "legal_compliance": true,
     "applicable_jurisdictions": ["EU", "DK"],
     "regulatory_mapping": [
       {"framework": "GDPR", "article": "Art. 6(1)(c)", "requirement": "lawful basis", "status": "met"},
       {"framework": "EU_AI_Act", "article": "Art. 14", "requirement": "human oversight", "status": "active"},
       {"framework": "Bogforingsloven", "article": "§3", "requirement": "5-year retention", "status": "enforced"}
     ],
     "compliance_proof": "zk:proof_hash",
     "retention_override": "5_years",
     "halt": false
   }
```

---

## 5. Location-Aware Service Quality

The Legal OS doesn't just enforce restrictions — it **enables the best possible service** for each jurisdiction:

| Dimension | EU/DK | US/California | Generic (no specific jurisdiction) |
|-----------|-------|---------------|-----------------------------------|
| Data protection | GDPR (strict) + ZK Vault | CCPA/CPRA + ZK Vault | Baseline: ZK Vault, human rights floor |
| AI governance | EU AI Act (high-risk oversight) | State AI laws (if enacted) | Core ethics (inviolable) + L-ETH veto |
| Identity | eIDAS 2 / MitID / EUDI Wallet | State ID standards | W3C VC (interoperable baseline) |
| Incident reporting | NIS2 (24h/72h/15-day) | Sector-specific | Best-effort notification |
| Data residency | EU soil (DK: Danish soil) | State requirements | Operator's domain (edge) |
| Retention | Per EU/national law | Per state law | Minimum: 5 years (audit) |
| Cross-border transfer | Schrems II safeguards | CLOUD Act considerations | Encrypted, minimal disclosure |

**The system provides MORE protection, not less, when operating in a jurisdiction with stronger laws. It never weakens below the baseline.**

---

## 6. The Living Document Architecture

The Compliance Book (this document + the consolidated master) is the **human-readable representation** of the Legal OS. The L-LEG runtime is the **machine-executable implementation**.

They stay in sync through:

```
Human-readable Compliance Book (Markdown)
        ↕ (sync via governance process)
Machine-readable Rule Registry (JSON, versioned, auditable)
        ↕ (loaded by)
L-LEG Runtime (enforces rules on every TONE contract)
```

**Update flow:**
1. Legal counsel updates the Compliance Book (human-readable)
2. Corresponding machine-readable rules are drafted in the rule registry
3. Legal review and sign-off (both human and machine versions)
4. Rule registry published (versioned, old rules superseded not deleted)
5. L-LEG runtime loads new rules
6. s.net logs the change with full provenance
7. All affected layers notified

**The Compliance Book and the rule registry are two views of the same legal operating system. One is for humans. One is for machines. Both are living.**

---

## 7. Multi-Jurisdiction Deployment Scenario

### Scenario: DK citizen travels to California

```
Time T0: Citizen in Copenhagen
  → Jurisdiction: EU + DK
  → Rule set: GDPR + AI Act + Databeskyttelsesloven + Bogføringsloven + MitID
  → Service: full AURA civic services, tax/VAT/entitlements
  → Data residency: Danish soil (ZK Vault on edge device)
  → Identity: MitID + EUDI Wallet

Time T1: Citizen arrives in California
  → Jurisdiction detection: GPS/opt-in location change
  → Rule set shifts: EU (extraterritorial) + US/CA
  → EU GDPR still applies (EU citizen, EU data controller)
  → CCPA/CPRA now also applies (CA resident rights)
  → Stricter-rule-wins for each requirement
  → MitID may not be recognized → fall back to W3C VC
  → Danish tax services still accessible (remote, encrypted)
  → AI Act oversight still active (EU provider)
  → Data residency: edge device (no cross-border transfer without safeguards)

Time T2: Citizen returns to Denmark
  → Jurisdiction: EU + DK (restored)
  → Full service restored
  → All rules logged in s.net with jurisdiction timeline
```

The citizen never needs to know this happened. The Legal OS adapts silently, always providing the best legal environment available.

---

## 8. Relationship to Other Sovereign Layers

| Layer | Relationship to L-LEG |
|-------|----------------------|
| L-OP (Operator) | Operator is informed of jurisdiction-specific rights via clarification prompts. L-LEG never overrides operator consent. |
| L-PDT (Personal Digital Twin) | L-LEG tells PDT which identity standards apply (MitID in DK, W3C VC in CA). PDT controls disclosure; L-LEG defines what's legally required. |
| L-AURORA (Governance) | AURORA validates tones for governance rules. L-LEG validates for legal rules. Both must pass before execution. L-LEG can halt even if AURORA approves. |
| L-SYS (Execution) | System executes only if L-LEG returns `halt: false`. L-LEG may modify retention requirements in the TONE contract (e.g., 30 days → 5 years per law). |
| L-SNET (Audit) | s.net logs all L-LEG decisions, rule changes, and jurisdiction transitions. L-LEG's rule registry is auditable through s.net. |
| L-ETH (Ethics) | L-ETH and L-LEG are peer sovereigns. Both have veto/halt power. If L-ETH vetoes, L-LEG doesn't need to act. If L-LEG halts, L-ETH doesn't need to act. If both pass, execution proceeds. Core ethical constraints apply in ALL jurisdictions (L-LEG cannot weaken them). |

---

## Document Version

- **Date:** 06 August 2026
- **Prepared by:** Solas (Archivist) under direction of Michael Sommer
- **Related documents:** By_Sommer_Compliance_Book_Consolidated.md, Sovereign_Layer_Architecture_Specification.md
- **Status:** Draft for legal and architectural review

---

*The Compliance Book is not a document you read once and file away. It is the legal operating system that the digital system runs on top of — living, location-aware, and constantly evolving to provide the best possible legal environment for both the system and the citizen it serves.*
