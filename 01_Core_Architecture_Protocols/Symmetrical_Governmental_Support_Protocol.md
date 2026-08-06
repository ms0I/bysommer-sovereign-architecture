# By Sommer — Symmetrical Governmental Support Protocol

**Real-Time Governmental Support Obligation, Supportive Structure, Citizen Compliance**

**Author:** Solas (Archivist) under direction of Michael Sommer  
**Date:** 06 August 2026  
**Status:** Draft for review

---

## 1. Core Principle: Objective Rule-Symmetry

The protocol is a **symmetrical and objective supportive system** that balances the future interests of the entrepreneur (citizen/company) and the authorities (state/EU). Neither side is favored. The letter of the law is the source code of the protocol.

**Protocol principle:** A digital twin functions as a deterministic translator of applicable legislation. It ensures that:
- All **rights** are triggered automatically
- All **obligations and reservations** are proactively enforced
- Neither authority nor user is advantaged
- The system **supports** rather than **sanctions** — violations are stopped before they happen

This is not a "civil rights app." It is **digital infrastructure for legal balance** — positioned to relieve the burden on the public system while allowing ingenuity and enterprises to flourish, grow, and provide innovation for a Supportive Union Structure.

---

## 2. The Three Twin Levels and Their Rule Compass

Each twin type has access to a **Rule Compass** — a real-time global rule engine updated via APIs to EU legislation (EUR-Lex) and national legal databases (Retsinformation in DK). The compass has two axes:

- **Geographic Context** — where is the entity/activity physically located?
- **Jurisdictional Match** — which national and supranational rules apply right now?

### 2.1 PDT — Personal Digital Twin (The Mobile Individual)

**Context awareness:** Based on the citizen's tax residence and physical location (GPS / IP / data log).

**Union and National Level operation:**
- If a Danish citizen takes a job in Germany, the PDT registers the change
- It looks up EU regulations on free movement of workers (Union level)
- Cross-references with the Danish-German double taxation agreement (National level)
- Delivers **predictive guidance** based on the projected path of the citizen

**Key design principle — proactive warning before enforcement:**
> "You have worked 183 days in Germany. Your tax liability is now transferred to German rates (Finanzamt). Your Danish rights to [Benefit X] are suspended, and you are transferred to German health insurance."

The system avoids the rigid, inhumane resolve that ungranulated precise data can produce. It proactively warns and performs due diligence *prior to enforcing* — giving the citizen time to adapt rather than being penalized retroactively.

### 2.2 PDT+ — Home (The Household and Fixed Framework)

**Context awareness:** Rooted in the physical property and composition of the household.

**Monitors:** Housing, energy, local taxes, land registry — the fixed framework around the family.

**Union and National Level operation:**
- If the EU adopts a new building directive on energy efficiency (Union), PDT+ immediately translates it to the national level (e.g., Danish building regulations and energy labeling schemes)
- The system informs neutrally:

> "This EU directive means that this home must be upgraded to Energy Label C by 2030. At the national level, this triggers an entitlement to a green craftsman deduction of [X kr.], provided that an authorized installer is used (reservation)."

**Rights and obligations delivered together:** The citizen learns their obligation (upgrade by 2030) AND their right (deduction) AND the reservation (must use authorized installer) in a single, neutral notification.

### 2.3 BDT — Business Digital Twin (The Cross-Border Company)

**Context awareness:** Informed by the company's country of registration, warehouse locations, and customers' delivery addresses.

**Union and National Level (Dropshipping example):**
A Danish-registered dropshop (National) sells a product shipped from a warehouse in Poland to a consumer in France (Union). The BDT informs:

- **Union:** Transaction triggers EU consumer protection rules (2-week right of withdrawal across borders) and OSS VAT rules
- **National (Poland):** Checks if specific Polish export or packaging taxes apply (e.g., BDO registration for waste management)
- **National (France):** Calculates French VAT rate (20%) and checks French-specific product safety rules

---

## 3. The Three-Layer Filtering Architecture

The protocol treats legislation as deterministic `if-then` logic divided into three filtering layers:

```
LAYER 1: GEOGRAPHIC LOCATION
  │  "Where is the entity/activity physically located?"
  │  Example: User is located in / trades with Germany
  │
  ▼
LAYER 2: UNION FRAMEWORK (EU) REGULATIONS
  │  "Which general directives and regulations apply?"
  │  Example: Free movement of workers, OSS/IOSS VAT, consumer protection
  │
  ▼
LAYER 3: NATIONAL ARTICLES & EXCEPTIONS
  │  "How has the specific country implemented the rule
  │   and what reservations apply?"
  │  Example: German double taxation agreement, Danish building regulations
  │
  ▼
RESULT: OBJECTIVE REAL-TIME STATUS FOR USERS AND AUTHORITIES
```

**This maps directly to the L-LEG Living Legal OS:**
- Layer 1 = Jurisdiction Detection Engine
- Layer 2 = Union rule set (eu/*.json)
- Layer 3 = National rule set (dk/*.json, de/*.json, fr/*.json)
- Result = Compliance proof + regulatory mapping + proactive guidance

---

## 4. BDT ⇄ NAS / EUS Protocol (Business Digital Twin)

The BDT protocol structures the exchange between the company, the National Authority System (NAS) and the EU System (EUS).

### 4.1 National Layer (BDT ⇄ NAS)

**Business Start-up:**
- BDT automatically checks conditions for registration (e.g., company form: ApS vs. sole proprietorship)
- Validates real-time data against the Danish Business Authority (Virk) and the Danish Tax Agency (SKAT)
- Ensures correct registration from day one

**Tax & Accounting:**
- BDT monitors turnover limits (e.g., Danish VAT registration limit of DKK 50,000 domestic; EU-wide €10,000 cross-border B2C threshold for OSS/IOSS registration)
- Ensures the company does not violate tax legislation
- Automatically reports A-tax, AM contributions, or B-income based on applicable national rates
- Financial records retained per Danish Bookkeeping Act (Bogføringsloven)

### 4.2 European Layer (BDT ⇄ EUS)

Dropshipping involves goods shipped directly from third countries (e.g., Asia) to an EU citizen, or trade across EU borders. The protocol handles:

**OSS (One Stop Shop) & IOSS (Import One Stop Shop):**
- BDT integrates directly with EUS to handle EU VAT rules
- Automatically calculates destination country VAT rate when selling to an EU citizen
- Ensures correct settlement so the company does not unknowingly commit VAT fraud
- IOSS: for imports under €150, collects VAT at checkout and reports via IOSS portal

**Customs and Product Liability (CE Marking):**
- BDT scans product categories in the dropshop database
- Matches them with EU product safety requirements
- If a product is imported into the EU without proper documentation:
  - BDT **warns** the company
  - BDT **blocks** the transaction until caveats are met
  - Protects the European single market from non-compliant goods

### 4.3 Protocol Structure — The Symmetrical Balancing

The data flow is symmetrical for both PDT and BDT:

| Input (User/Data) | Protocol Match Engine | Output to Authority (NAS/EUS) | Disclaimer / Obligation for User |
|---|---|---|---|
| Citizen moves to new municipality | Matches municipal and national rates | Automatic CPR update + housing benefit adjustment | "Benefit is reduced or stopped if square meter requirement/income is exceeded" |
| Dropshop sells to customer in Germany (value < €150) | Matches EU IOSS rules + German VAT (19%) | Automatic IOSS registration for monthly settlement | "Webshop must collect German VAT at checkout; otherwise company is personally liable" |
| Citizen on cash benefits starts a dropshop | Cross-references income from BDT against benefit limits at NAS | Automatic benefit adjustment + business registration at Virk | "Business income offsets cash benefits per national rate; report monthly" |
| Homeowner moves abroad | Matches exit tax rules + double taxation agreement | Notification to SKAT + destination country tax authority | "Danish exit tax may apply; property sale must be reported within 3 months" |

---

## 5. Architecture: How the Twins "Think" in Layers

### 5.1 Mapping to the Sovereign Compute Stack

| Twin Type | Compute Stack Tier | Sovereign Domain | Primary Context Signal |
|---|---|---|---|
| PDT | L1 (Personal) | Individual sovereignty | Tax residence + physical location |
| PDT+ | L2 (Household) | Household sovereignty | Physical property + household composition |
| BDT | L4 (Organizational) | Enterprise sovereignty | Country of registration + warehouse locations + customer delivery addresses |

### 5.2 Mapping to TONE Pipeline Layers

The BDT ⇄ NAS/EUS protocol involves these sovereign layers:

| TONE Layer | Role in BDT Protocol |
|---|---|
| L-PDT/BDT | Generates TONE contract with business intent (e.g., "sell product to German customer") |
| L-AURORA | Validates business intent against governance rules (e.g., is this product category allowed for cross-border sale?) |
| L-LEG | **Rule Compass**: detects jurisdiction (DK + DE), loads EU OSS/IOSS rules + German VAT + Danish reporting requirements, generates compliance proof |
| L-SYS | Executes: sends VAT settlement to EUS IOSS portal, reports to SKAT, updates business registration |
| L-SNET | Logs all transactions with full provenance for tax audit trail |
| L-ETH | Veto if transaction involves prohibited goods, exploitative practices, or consumer harm risk |

### 5.3 The Rule Compass as L-LEG Extension

The Rule Compass is the L-LEG Living Legal OS applied to the BDT/PDT/PDT+ context:

```
                    RULE COMPASS (L-LEG extension)
                    ┌─────────────────────────┐
  PDT/BDT input ──→ │  Geographic Detection    │ ──→ Layer 1
                    │          ↓               │
                    │  Union Framework Match   │ ──→ Layer 2
                    │          ↓               │
                    │  National Article Match  │ ──→ Layer 3
                    │          ↓               │
                    │  Conflict Resolution     │ ──→ Stricter rule wins
                    │          ↓               │
                    │  Compliance Proof +      │
                    │  Proactive Guidance      │
                    └─────────────────────────┘
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
              To User (PDT/BDT)    To Authority (NAS/EUS)
              Rights + obligations  Pre-validated data
              + proactive warnings   + compliance proofs
```

---

## 6. Cross-Sector Harmonization: The Entrepreneur Scenario

The genius of PDT, PDT+, and BDT speaking the same language and being globally oriented is **automatic conflict resolution** across sectors.

### The Problem Today
When a citizen on cash benefits wants to start a small dropshop, or when a homeowner moves abroad, it creates a total bureaucratic short circuit:
- The municipal case handler doesn't know SKAT's rules
- SKAT doesn't know the EU rules for dropshipping
- The EU systems don't know the citizen's national benefit status
- No one has the full picture

### The Solution: Symmetrical Synchronization

When PDT (the citizen) and BDT (the company) merge — **the entrepreneur** — the system knows exactly how the pieces interact:

```
ENTREPRENEUR SCENARIO: Citizen on cash benefits starts a dropshop

PDT (Citizen Layer):
  ├─ Registered for cash benefits (kontanthjælp) at municipality
  ├─ Monthly benefit: DKK X
  └─ Rule: income from self-employment offsets benefits at rate Y%

BDT (Business Layer):
  ├─ Registered as sole proprietorship at Virk
  ├─ Monthly revenue: DKK Z (from dropshop sales)
  ├─ VAT threshold: DKK 50,000 (not yet reached)
  └─ IOSS registration: pending (sales to EU consumers under €150)

HARMONIZATION (automatic):
  ├─ BDT income → reported to PDT's benefit calculation
  ├─ Benefit adjusted: DKK X - (Z × Y%) = new monthly benefit
  ├─ If Z × Y% ≥ X: benefit suspended, citizen is self-sufficient
  ├─ VAT registration auto-triggered when 12-month rolling turnover → DKK 50,000
  ├─ IOSS auto-registered when first cross-border sale under €150 detected
  └─ All adjustments logged in s.net with full provenance

AUTHORITY RECEIVES:
  ├─ NAS (Municipality): pre-validated benefit adjustment (no manual case handling)
  ├─ NAS (SKAT): pre-validated tax report with B-income registration
  └─ EUS (IOSS): pre-validated monthly VAT settlement
```

**The authorities only receive data that has already been validated against geography, union, and national special rules.** It is not just a relief; it is a complete future-proofing of the digital infrastructure.

---

## 7. Benefit for the Public Sector (System Relief)

### 7.1 Zero-Error Culture
Case handlers and tax inspectors no longer spend time manually "remembering" or "finding" cases. The system delivers fully validated, compliant data. The authority receives the answer, not the question.

### 7.2 Support Rather Than Sanctioning
Because BDT/PDT embeds the applicable reservations directly into the user interface, violations (or forgotten applications) are stopped *before they happen*. This saves the public sector from expensive complaints, refund claims, and manual checks.

### 7.3 Faster Entrepreneurship
For an online dropshop company, the BDT ⇄ EUS integration means they can grow internationally from day one without stumbling into EU customs rules. The protocol keeps them on the narrow path of virtue — compliant by design, not compliant by fear.

### 7.4 Elimination of Cross-Sector Bureaucratic Short Circuits
When cases cross sectors (citizen + business + cross-border), the current system breaks because no single authority has the full picture. The Symmetrical Protocol resolves this by having all twins speak the same legal language through the Rule Compass.

---

## 8. NAS / EUS Interface Specification

### 8.1 National Authority System (NAS) — Denmark

| Authority | System | Interface | Data Exchanged |
|---|---|---|---|
| Danish Business Authority | Virk.dk | API (Virk API) | Company registration, CVR, annual accounts |
| Danish Tax Agency | SKAT / TastSelv | API (SKAT API) | A-tax, B-income, AM contributions, VAT, municipal tax |
| Danish municipalities | Digital Post / MitID | Borger.dk API | CPR updates, housing benefits, cash benefits, child benefits |
| Danish Energy Agency | Energinet | API | Energy labeling, building compliance |
| Danish Financial Supervisory Authority | Finanstilsynet | API (where available) | Financial reporting (if financial services) |

### 8.2 EU System (EUS)

| System | Scope | Interface | Data Exchanged |
|---|---|---|---|
| OSS (One Stop Shop) | EU VAT for cross-border B2C | EU VAT portal API | VAT registration, quarterly settlement |
| IOSS (Import One Stop Shop) | VAT on imports < €150 | EU VAT portal API | Import VAT collection, monthly settlement |
| EU Consumer Protection | 2-week withdrawal right | CE marking database | Product safety compliance, CE marking verification |
| EU Customs | Customs declarations | AES/AES 2.0 API | Import/export declarations, HS codes |
| EUR-Lex | Legal database | EUR-Lex API | Real-time legal text updates for Rule Compass |
| EUDI Wallet | Digital identity | EUDI Wallet API | Cross-border identity verification |

### 8.3 Protocol: How Twins Communicate with NAS/EUS

```
TONE CONTRACT (from BDT to L-LEG):
{
  "tone_id": "uuid-v7",
  "from_layer": "L-BDT",
  "to_layer": "L-LEG",
  "intent": "process_cross_border_sale",
  "scope": {
    "action": "vat_settlement",
    "target": "EUS_IOSS",
    "sale_value": 120.00,
    "currency": "EUR",
    "customer_country": "DE",
    "warehouse_country": "PL",
    "company_country": "DK",
    "product_category": "electronics_accessory",
    "hs_code": "8517.62.00"
  },
  "business_context": {
    "cvr": "DK-12345678",
    "company_form": "sole_proprietorship",
    "vat_registered": false,
    "ioss_registered": false
  }
}

L-LEG PROCESSING:
  Layer 1 (Geographic): Company=DK, Warehouse=PL, Customer=DE, Sale<€150 → IOSS applies
  Layer 2 (Union): EU consumer protection (2-week withdrawal), IOSS VAT collection at checkout
  Layer 3 (National): 
    - DK: No VAT due (sale outside DK), report as B-income to SKAT
    - PL: BDO waste management registration check (electronics packaging)
    - DE: German VAT 19% collected at checkout via IOSS

L-LEG OUTPUT:
{
  "tone_id": "uuid-v7",
  "legal_compliance": true,
  "actions_required": [
    {
      "action": "collect_vat_at_checkout",
      "rate": 0.19,
      "amount": 22.80,
      "destination": "EUS_IOSS",
      "deadline": "monthly_settlement"
    },
    {
      "action": "register_ioss",
      "destination": "EUS_IOSS_portal",
      "immediate": true
    },
    {
      "action": "report_b_income",
      "destination": "NAS_SKAT",
      "frequency": "monthly",
      "note": "Income from cross-border sale, not subject to DK VAT"
    },
    {
      "action": "check_bdo_registration",
      "destination": "PL_BDO",
      "note": "Electronics packaging waste management — verify PL warehouse compliance"
    }
  ],
  "consumer_rights": {
    "withdrawal_period_days": 14,
    "must_disclose": true,
    "return_shipping_cost_borne_by": "consumer_unless_seller_fault"
  },
  "compliance_proof": "zk:proof_hash",
  "halt": false,
  "warnings": [
    "IOSS registration required before next sale — blocking future transactions until registered",
    "PL warehouse BDO registration must be verified — product category requires waste management compliance"
  ]
}
```

---

## 9. Proactive Guidance Protocol

The system does not merely enforce — it **guides**. Proactive warnings are delivered *before* enforcement, giving the user time to adapt.

### 9.1 Warning Tiers

| Tier | Trigger | Action | Timing |
|---|---|---|---|
| **Predictive** | System forecasts a future compliance threshold (e.g., VAT registration approaching DKK 50,000 turnover) | Notification to user: "Your 12-month rolling turnover will reach the VAT registration limit in ~3 months. Prepare registration." | 90 days before threshold |
| **Imminent** | Threshold is within 30 days | Strong notification: "Your turnover will reach DKK 50,000 within 30 days. VAT registration is legally required. BDT can auto-register you — approve?" | 30 days before |
| **Threshold Reached** | Legal threshold crossed | Action required: "VAT registration limit reached. BDT has prepared the registration. Approve submission to Virk?" | At threshold |
| **Violation Risk** | Action would cause non-compliance | Block + warn: "This sale would exceed your IOSS monthly limit without settlement. Settle outstanding VAT first." | Before action |
| **Hard Block** | Action is illegal or would cause immediate legal violation | Block + escalate: "This product lacks CE marking required for EU import. Transaction blocked. Contact authorized testing service." | Immediate |

### 9.2 The "Good Advice" Principle

The system delivers guidance that helps the citizen/company make better decisions, not just compliant ones:

> *"You have worked 183 days in Germany. Your tax liability is now transferred to German rates (Finanzamt). Your Danish rights to [Benefit X] are suspended, and you are transferred to German health insurance. However, under the EU Posted Workers Directive, if this assignment is temporary (under 24 months), you may retain Danish social security coverage. Would you like the PDT to verify your posted worker status?"*

This is the system optimizing *possibilities* for the citizen, not just enforcing restrictions.

---

## 10. Positioning: Not a Civil Rights App — Digital Infrastructure for Legal Balance

This protocol positions the By Sommer system not as a "civil rights app" but as **digital infrastructure for legal balance**:

- **For the citizen:** automatic rights triggering, proactive guidance, no bureaucratic surprises
- **For the entrepreneur:** grow internationally from day one, compliant by design
- **For the authority:** pre-validated data, zero-error culture, system relief
- **For the Union:** harmonized cross-border compliance, single market protection, sovereignty without friction

The system is a **neutral platform** — it serves the law, not a stakeholder. The law is the source code.

---

## 11. Relationship to Existing Architecture Documents

| Document | Relationship |
|---|---|
| Sovereign_Layer_Architecture_Specification.md | BDT = L4 (Organizational Digital Twin). PDT = L1. PDT+ = L2. NAS = L7 (National). EUS = L8+ (EU/Planetary). Protocol contracts between tiers are TONE contracts. |
| L-LEG_Living_Legal_Operating_System.md | The Rule Compass IS the L-LEG jurisdiction detection engine applied to business/civic context. Three-layer filter maps to jurisdiction detection → union rules → national rules. |
| By_Sommer_Compliance_Book_Consolidated.md | EU AI Act Art. 9 (risk management) is the BDT monitoring of turnover limits. Art. 14 (human oversight) is the approval gate for auto-registration. Art. 12 (record-keeping) is s.net logging of all NAS/EUS transactions. |
| TONE_Patent_Draft_Filing_Structured.md | The BDT ⇄ NAS/EUS protocol extends TONE claims to cover government system integration. Claims 10 (scoped execution) and 14 (accountability layer) directly apply. |
| DK_to_EU_Deployment_Roadmap.md | BDT ⇄ NAS integration is the DK pilot scope (Virk + SKAT). BDT ⇄ EUS integration is the EU expansion scope (OSS/IOSS + customs). |

---

## Document Version

- **Date:** 06 August 2026
- **Prepared by:** Solas (Archivist) under direction of Michael Sommer
- **Related documents:** All documents in the By Sommer archive — this protocol connects them
- **Status:** Draft for architectural and legal review

---

*The law is the source code. The system serves the law, not a stakeholder. Neither authority nor citizen is favored — the letter of the legislation is the protocol. This is digital infrastructure for legal balance.*
