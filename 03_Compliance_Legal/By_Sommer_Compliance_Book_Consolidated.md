# By Sommer Compliance Book: Legal, Ethical, and Operational Governance for Autonomous Systems

**Consolidated Master Version — 06 August 2026**
**Status:** Draft for legal review
**Supersedes:** BySommer_Compliance_Architecture.pdf + By_Sommer_Compliance_Book.pdf (merged)

> ⚠️ **NOTICE:** This document consolidates and extends prior compliance documents. It includes a preliminary mapping of EU AI Act articles to the By Sommer architecture. This mapping is architectural analysis, not legal advice. A qualified Danish/EU legal counsel must verify all regulatory mappings before deployment.

---

## Table of Contents

1. Introduction
2. Legal Foundations
   - 2.1 GDPR and Data Subject Rights
   - 2.2 EU AI Act — Article-by-Article Compliance Mapping
   - 2.3 NIS2 Cybersecurity Requirements
   - 2.4 eIDAS 2 and Digital Identity
   - 2.5 Danish National Law
3. Ethical Governance
   - 3.1 Responsible AI and HITL Oversight
   - 3.2 Bias Mitigation and Anti-Discrimination
   - 3.3 Transparency and Conduct
4. Intellectual Property and Digital Market Fairness
   - 4.1 IP Ownership and Licensing
   - 4.2 AI Training Prohibition
   - 4.3 Digital Commerce Compliance
5. Operational Compliance Protocols
   - 5.1 Contract Lifecycle Management
   - 5.2 Public LLM Usage Restrictions
   - 5.3 GDPR Rights Execution
6. Autonomous Agent Decision Logging Framework
   - 6.1 Purpose and Scope
   - 6.2 Logging Architecture
   - 6.3 Decision Categories and Metadata
   - 6.4 Auditability and Retention
   - 6.5 Contamination Prevention and Addendum Protocol
7. EU AI Act Compliance Architecture Mapping
   - 7.1 Risk Classification
   - 7.2 Article-by-Article Mapping (Art. 1–113)
   - 7.3 Conformity Assessment Pathway
   - 7.4 CE Marking and Registration
8. Public-Facing Legal Integration
9. Continuous Improvement and Governance Review
10. Deployment-Phase Compliance Checklist

---

## 1. Introduction

By Sommer is a research-driven innovation studio based in Copenhagen, Denmark, specializing in machine learning (ML), large language models (LLMs), and strategic design thinking. Operating within the European Union, the studio is committed to full compliance with the General Data Protection Regulation (GDPR), the EU AI Act, the NIS2 Directive, eIDAS 2, and other relevant European legal frameworks.

This Compliance Book codifies By Sommer's legal, ethical, and operational commitments, ensuring that all AI engagements — including those involving autonomous agents and the AURA/TONE architecture — are transparent, auditable, and aligned with EU law. It is designed to meet and exceed the legal, ethical, and operational standards required for Horizon Europe grant eligibility.

Compliance architecture is not bolt on. It is built into the system core foundation — a live, enforceable lens that continuously shapes agent decisions while preserving user sovereignty, trust, and dignity.

---

## 2. Legal Foundations

### 2.1 GDPR and Data Subject Rights

**Legal basis for processing:** consent, contract performance, legitimate interest.

**Data subject rights upheld:**
- Access (Art. 15)
- Rectification (Art. 16)
- Erasure (Art. 17)
- Restriction of processing (Art. 18)
- Data portability (Art. 20)
- Objection (Art. 21)
- Protection against automated decision-making (Art. 22)

**Architectural alignment:**
- Zero-Knowledge Vault ensures raw personal data never leaves the user's domain
- Selective disclosure via W3C Verifiable Credentials — only minimum attributes released
- TONE contract field scoping enforces data minimization at protocol level
- L-PDT (Personal Digital Twin) is the data controller boundary — downstream layers receive only scoped assertions
- s.net audit trail records all data access with provenance, enabling Art. 15 access requests via log queries
- Consent is per-action (per tone), not blanket — Art. 7 consent requirements met by design
- Deletion requests fulfilled within 30 days; financial records retained per Danish Bookkeeping Act

**Data Processing Agreements (DPAs):**
- By Sommer designated as Processor; data handled only under documented client instructions
- DPAs specify processors, subprocessors, purposes, retention, and security measures

**Contact:** privacy@bysommer.net (By Sommer), compliance@imsor.com (Imsor.com)

### 2.2 EU AI Act — Article-by-Article Compliance Mapping

*See Section 7 for the full article-by-article mapping.*

**Summary:**
- AURA/TONE architecture is classified as a **High-Risk AI System** (Annex III — essential public services, civic infrastructure)
- The architecture is designed to *exceed* AI Act requirements, not merely meet them
- Every AI Act obligation maps to a specific architectural component — compliance is structural, not procedural
- The GEMS Deterministic Oracle provides the deterministic verification layer required for high-risk AI outputs

### 2.3 NIS2 Cybersecurity Requirements

**Scope:** By Sommer aligns with NIS2 obligations for essential and important entities in the EU.

**Measures implemented:**
- Risk analysis and assessment
- Incident response procedures
- Business continuity planning
- Multi-factor authentication
- Network and system security monitoring
- Supply chain security assessment
- Vulnerability disclosure handling

**Architectural alignment:**
- Each sovereign layer has its own failure isolation — NIS2 Art. 21(1)(a) risk management by design
- s.net provides the audit trail required by NIS2 Art. 21(2)(d) logging and detection
- L-ETH self-veto mechanisms serve as automatic alerts per NIS2 Art. 21(2)(f)
- Cross-border layers (EU phase) must comply with NIS2 incident reporting timelines (24-hour early warning, 72-hour notification, 1-month final report)

### 2.4 eIDAS 2 and Digital Identity

**Alignment with European Digital Identity Framework (EUDI):**
- Sovereign Identity Handshake designed to interoperate with EUDI Wallet
- MitID integration (DK pilot) as national e-ID layer
- Cross-border identity recognition (EU phase) via eIDAS 2 mutual recognition
- Qualified Trust Services alignment for cryptographic proofs

### 2.5 Danish National Law

- **Danish Data Protection Act (Databeskyttelsesloven)** — national GDPR implementation
- **Danish Bookkeeping Act (Bogføringsloven)** — financial record retention requirements
- **Danish Digital Administration Strategy** — alignment with national digital priorities
- **MitID framework** — Danish e-ID integration requirements

---

## 3. Ethical Governance

### 3.1 Responsible AI and HITL Oversight

- HITL required for all high-stakes decisions (mapped to Human-Oversight Matrix, High risk tier)
- The L-ETH (Responsible, Moral & Ethical Layer) has **hard veto power** — can block any action even if AURORA approves
- Clients bear final responsibility for output verification (AI & IP Addendum)
- Augmentation over automation — the system assists, never replaces human judgment
- Periodic human review of agent decisions for alignment with intended ethics

**Architectural alignment:**
- The Human-Oversight Matrix (Low/Medium/High risk tiers) defines exactly which actions are automated and which require human sign-off
- Every escalation path is documented with roles (not names)
- The operator can veto any action at any point before execution ("kill switch")
- The L-ETH Reflection Loop evaluates the agent's influence on user behavior over time (Observer Effect Accounting)

### 3.2 Bias Mitigation and Anti-Discrimination

- Training datasets assessed for bias with documented mitigation strategies
- L-PDT interpretation components include bias-monitoring hooks and explainability metadata
- Periodic fairness tests run pre-deployment and on ongoing basis
- Right to terminate agreements if clients misuse AI for discriminatory, malicious, or unethical purposes

### 3.3 Transparency and Conduct

- Code of Conduct prohibits unlawful, harmful, or discriminatory behavior
- Compliance monitoring functions embedded into operations
- Every decision logged with provenance, rule version, actor ID, confidence score, and rationale
- Explainability artifacts sufficient to reconstruct any decision from logs alone

---

## 4. Intellectual Property and Digital Market Fairness

### 4.1 IP Ownership and Licensing

- Clients retain ownership of final deliverables upon payment
- By Sommer retains all proprietary methodologies, frameworks, and source code
- Contracts include disclaimers regarding copyrightability of AI-generated content
- TONE patent claims (1–15) are By Sommer proprietary IP

### 4.2 AI Training Prohibition

- Website Terms of Use explicitly prohibit use of any site content for training AI systems, ML models, or LLMs without express written consent
- This clause protects proprietary research and digital assets from unauthorized scraping
- Staff prohibited from inputting client data into public LLMs unless contractually authorized

### 4.3 Digital Commerce Compliance

- Subscription Agreement includes explicit waiver of 14-day withdrawal right for digital goods (EU consumer protection law)
- Subscriptions auto-renew monthly unless cancelled; fees non-refundable unless required by law
- Compliance with EU regulations targeting gatekeeper platforms (non-discrimination in data access, ranking, interoperability)

---

## 5. Operational Compliance Protocols

### 5.1 Contract Lifecycle Management

- All B2B engagements require e-signed MSA, AI & IP Addendum, and DPA before project initiation
- Documents integrated into onboarding workflows via secure e-signature platform
- Audit rights, liability allocation, and indemnity clauses defined per engagement

### 5.2 Public LLM Usage Restrictions

- Staff trained not to input client data into public LLMs (e.g., ChatGPT) unless explicitly authorized
- Enterprise-grade LLM instances used only under strict contractual and technical safeguards
- No personal data processed through third-party LLM APIs without DPA in place

### 5.3 GDPR Rights Execution

- Deletion requests fulfilled within 30 days
- Financial records retained per Danish Bookkeeping Act
- Data export and portability mechanisms provided consistent with law and policy
- Consent revocation triggers revalidation of dependent authorizations

---

## 6. Autonomous Agent Decision Logging Framework

### 6.1 Purpose and Scope

To ensure accountability and auditability of autonomous agent behavior in production and research environments. This framework implements the s.net (Responsibility & Accountability Layer) sovereign state.

### 6.2 Logging Architecture

- **Immutable, timestamped logs** stored in secure, access-controlled environments (append-only, Merkle tree or hash-chained)
- **Physically isolated storage** — separate from all other layers; no shared database
- **Cryptographic provenance** — every entry signed by its source layer's signing key
- Logs include: input prompts (hashed), model version, output, decision rationale, actor ID (human or automated), rule version used, confidence score, timestamp

### 6.3 Decision Categories and Metadata

**Categories:**
| Category | Description | Example |
|----------|-------------|---------|
| Data Access | Agent requests or retrieves data | PDT queries identity wallet |
| Content Generation | Agent produces output for user | Tone generation, clarification prompt |
| Escalation | Agent routes to human review | AURORA escalates ambiguous tone |
| Ethical Override | L-ETH vetoes an action | Bias detected, action blocked |
| Consent Handling | User consent captured or revoked | Operator approves scoped identity disclosure |
| Legal Halt | L-LEG blocks execution | GEMS Oracle detects regulatory violation |
| Execution | System layer executes authorized action | Tax eligibility query sent to authority |

**Metadata per entry:**
- tone_id (UUIDv7 — correlatable across all layers)
- user_id (hashed — not raw)
- session_id
- model confidence score
- HITL override status
- rule version(s) applied
- layer of origin (which sovereign layer produced this entry)
- signature (Ed25519 per-layer key)

### 6.4 Auditability and Retention

- Logs retained for 5 years (configurable per deployment, subject to minimum legal requirements)
- Accessible to compliance, legal, and DPO teams on role-based access (least privilege)
- Redaction protocols for sensitive data — auditor sees only what is needed, not everything available
- Third-party audit pipeline: government/regulator access via scoped API, not full log access
- Audit reports generated in regulator-required formats on demand

### 6.5 Contamination Prevention and Addendum Protocol

**Core principle:** The decision log is uncontaminated. Original entries are never modified or deleted.

- **Original entries remain immutable** — no edits, no deletions, even by system owner or administrator
- **Addendums are separate linked entries** — corrections, updates, or human/agent notes are stored as new entries linked to the original via tone_id
- **Addendums preserve the correction trail** — the agent can reflect on and comprehend addendums without losing the original context
- **Purpose:** Avoid memory lack or misalignment in decision structure; avoid hallucination; pinpoint the root of architectural error without branching or infection to the full system
- **Audit integrity:** During third-party audits, the original log and all addendums are disclosed as a chain — the auditor sees the full evolution of a decision, not just the final state

**Implementation:**
```
Original entry (immutable):
  {tone_id, timestamp, layer, decision, rationale, signature}

Addendum (linked, also immutable):
  {tone_id, addendum_id, timestamp, author, type: "correction"|"note"|"override",
   content, links_to: original_entry_id, signature}
```

---

## 7. EU AI Act Compliance Architecture Mapping

### 7.1 Risk Classification

**Classification: High-Risk AI System**

**Basis:** EU AI Act Annex III, points 5 and 6 — AI systems used in:
- Essential public services and civic infrastructure
- Law enforcement, migration, border control (potential future scope)
- Determination of eligibility for public benefits (bureaucracy elimination)

**AURA is classified as High-Risk, High-Trust** — compliant, transparent, and sovereign by design. This classification is not a liability; it is the trust signal that distinguishes AURA from non-compliant AI systems.

### 7.2 Article-by-Article Mapping

#### Chapter I — General Provisions

| Article | Requirement | By Sommer Architecture Mapping |
|---------|-------------|-------------------------------|
| Art. 1 | Subject matter and purpose | AURA is the constitutional substrate implementing the AI Act's purpose: protecting fundamental rights while enabling innovation |
| Art. 2 | Scope | AURA operates within scope — deployed in EU, serving EU citizens, by EU entity |
| Art. 3 | Definitions | TONE "tones" are AI system outputs; PDT is the AI system; AURORA is the governance mechanism |
| Art. 4 | AI literacy | Operator Layer provides clarification workflows ensuring operators understand system behavior and limitations |

#### Chapter II — Prohibited AI Practices

| Article | Requirement | By Sommer Architecture Mapping |
|---------|-------------|-------------------------------|
| Art. 5 | Prohibited practices | AURA is designed to **never** engage in: subliminal manipulation (L-ETH veto), social scoring (L-LEG blocks), real-time biometric identification (not in scope — would require separate L-LEG rule), exploitation of vulnerabilities (L-ETH core constraint) |

#### Chapter III — High-Risk AI Systems

| Article | Requirement | By Sommer Architecture Mapping |
|---------|-------------|-------------------------------|
| Art. 6 | Classification as high-risk | AURA classified under Annex III §5 (essential public services) — bureaucracy elimination, tax/VAT/entitlements |
| Art. 7 | Amendments to Annex III | L-LEG rule registry is versioned and updatable — new Annex III additions can be mapped without architectural changes |
| Art. 8 | Compliance with requirements | Compliance is structural: each requirement maps to a specific sovereign layer (see below) |
| Art. 9 | Risk management system | L-AURORA governance substrate IS the risk management system. Versioned rule registry, risk thresholds, escalation workflows. Risk identification → mitigation → evaluation → iteration. |
| Art. 10 | Data and data governance | L-PDT Zero-Knowledge Vault + selective disclosure. Training data quality ensured through bias monitoring hooks. Data minimization at protocol level (TONE contract scoping). |
| Art. 11 | Technical documentation | Full TONE specification + this Compliance Book + per-layer sovereign state specifications. Technical documentation maintained per-layer and versioned. |
| Art. 12 | Record-keeping (logging) | s.net (L-SNET) — append-only, immutable, timestamped, cryptographically signed audit trail. Logs include tone_id correlation across all layers. 5-year retention. |
| Art. 13 | Transparency and provision of information to deployers | Operator Layer provides real-time clarification. TONE contract provenance chain is the transparency mechanism. Operators informed of system capabilities, limitations, and expected output. |
| Art. 14 | Human oversight | L-ETH (Ethical Layer) with hard veto power. Human-Oversight Matrix (Low/Medium/High). HITL required for high-risk actions. Operator "kill switch" at every pipeline stage. **This is the strongest architectural alignment with the AI Act.** |
| Art. 16 | Obligations of providers | By Sommer as provider: ensures system meets Art. 9–15 requirements, technical documentation (Art. 11), quality management (Art. 17), automatic logging. L-AURORA governance substrate enforces provider obligations by design. |
| Art. 15 | Accuracy, robustness, cybersecurity | Misinterpretation Firewall (confidence thresholds, contextual heuristics). GEMS Deterministic Oracle (deterministic verification). Each layer has failure isolation (sovereign state). Per-layer failure does not cascade. |
| Art. 26 | Obligations of deployers | By Sommer as deployer: uses system per instructions, monitors operation, suspends if risk identified. L-ETH automatic alerts flag risk-threshold breaches. |
| Art. 17 | Representative | EU-based (Copenhagen) — representative requirement met by default. |
| Art. 18 | Information to be submitted to authorities | s.net generates compliance reports on demand. L-LEG produces regulatory mapping and compliance proofs. Zero-Knowledge compliance — proofs without raw data disclosure. |
| Art. 19 | CE marking and declaration of conformity | Required before EU-wide deployment. Conformity assessment pathway defined in §7.3 below. |
| Art. 20 | Presumption of conformity with requirements | If AURA is developed in conformity with harmonized standards (to be adopted by CEN/CENELEC/ETSI for AI Act), presumption of conformity applies. **Monitor standardization developments.** |

#### Chapter IV — Transparency Obligations

| Article | Requirement | By Sommer Architecture Mapping |
|---------|-------------|-------------------------------|
| Art. 50 | Transparency obligations for certain AI systems | AURA must inform users they are interacting with an AI system (Operator Layer clarification prompts). AI-generated content must be marked (TONE contract provenance metadata). |

#### Chapter V — Measures in Support of Innovation

| Article | Requirement | By Sommer Architecture Mapping |
|---------|-------------|-------------------------------|
| Art. 53 | AI regulatory sandboxes | DK pilot can operate within a national AI regulatory sandbox (Danish national sandbox for AI, if established). This aligns with the phased DK→EU deployment strategy. |

#### Chapter VI — Governance

| Article | Requirement | By Sommer Architecture Mapping |
|---------|-------------|-------------------------------|
| Art. 56–63 | EU AI Office, AI Board, Advisory Forum | By Sommer architecture designed for external audit. s.net provides the audit pipeline. GEMS Oracle provides deterministic verification for AI Office oversight. |

#### Chapter VII — EU Database

| Article | Requirement | By Sommer Architecture Mapping |
|---------|-------------|-------------------------------|
| Art. 71 | EU database for high-risk AI systems | AURA must be registered in the EU database before deployment. L-LEG maintains the regulatory mapping needed for registration. |

#### Chapter VIII — Post-Market Monitoring

| Article | Requirement | By Sommer Architecture Mapping |
|---------|-------------|-------------------------------|
| Art. 72 | Post-market monitoring by deployers | s.net continuous monitoring for drift, bias, safety incidents. L-AURORA drift mitigation flags semantic consistency issues. Periodic audits produce reports. |
| Art. 73 | Reporting of serious incidents | **AI Act:** serious incidents reported within 15 days (Art. 73). **NIS2 (separate directive):** 24-hour early warning, 72-hour notification, 1-month final report (Art. 23). s.net triggers automatic alerts for both reporting streams. Distinct timelines must not be conflated. |

#### Chapter IX — Penalties

| Article | Requirement | By Sommer Architecture Mapping |
|---------|-------------|-------------------------------|
| Art. 99 | Fines for non-compliance | Up to €35M or 7% of global turnover for prohibited practices violations; up to €15M or 3% for other obligations. **Compliance is not optional — it is architectural. The sovereign layer design makes violation structurally difficult.** |

### 7.3 Conformity Assessment Pathway

For AURA as a High-Risk AI System (Annex III):

1. **Internal compliance check** — verify all Art. 8–15 requirements are met (architectural compliance documented in this book)
2. **Conformity assessment** — Annex III high-risk systems require **internal control** (self-assessment) per Art. 43(2), unless the system falls under a sector requiring third-party assessment
3. **CE marking** — issue EU declaration of conformity (Art. 47) and affix CE marking (Art. 48)
4. **Registration** — register in EU database (Art. 49, Art. 71)
5. **Post-market monitoring** — continuous (Art. 72), with incident reporting (Art. 73)

**Timeline:** Conformity assessment can begin during DK pilot (Phase 1), with CE marking and registration before EU-wide deployment (Phase 2).

### 7.4 CE Marking and Registration

- EU declaration of conformity must include: provider name, system name/type, system description, intended purpose, Annex III classification, harmonized standards applied, statement of conformity
- Registration in EU database requires: provider info, system info, intended purpose, risk classification, member states of deployment
- L-LEG maintains all documentation needed for CE marking and registration as machine-readable regulatory mappings

---

## 8. Public-Facing Legal Integration

### 8.1 Website Legal Hub

- Global footer of bysommer.net links to Privacy Policy, Cookie Policy, and Website Terms of Use
- All forms include required checkbox for affirmative consent to these policies

### 8.2 Privacy Policy Requirements

- Enumerates GDPR rights for EEA/UK residents
- Provides contact emails for rights requests (privacy@bysommer.net, compliance@imsor.com)
- Describes data processing purposes, legal bases, retention periods, and third-party sharing
- AI-specific disclosures: use of AI systems, automated decision-making, right to human review

### 8.3 Terms of Use Clauses

- Asserts ownership of all site content and research methodologies
- Prohibits use of content for AI training without written consent
- User conduct expectations defined
- Limitation of liability for AI-assisted content

---

## 9. Continuous Improvement and Governance Review

- Annual review of all policies
- Stakeholder feedback loop (citizens, regulators, auditors, developers)
- Alignment with evolving EU and global standards
- Periodic principle recalibration — update operational rules while maintaining core ethical guardrails
- Dynamic ethics adjustment — principles evolve responsibly as new contexts emerge, core constraints remain inviolable

### User State Awareness

The system considers situational factors, vulnerabilities, and user preferences:
1. **Observer Effect Accounting** — recognize agent influence on behavior and adapt ethically
2. **Dynamic Ethics Adjustment** — principles evolve as contexts emerge, core constraints inviolable
3. **Scenario-Based Testing** — test under edge cases to detect ethical conflicts
4. **Counterfactual Analysis** — evaluate what might happen if actions were taken or withheld
5. **Ethical Metrics** — score actions for compliance, risk, and potential harm
6. **Continued Decision Log** — 3rd-party audit of log and addendums via pipeline to government, remaining uncontaminated at core
7. **Automatic Alerts** — flag actions that challenge thresholds or introduce risk
8. **Periodic Principle Recalibration** — update operational rules while maintaining ethical guardrails

### Scope Boundaries

- Define what domains the system can act in and where it must abstain
- Map each principle to explicit actions or non-actions (e.g., do not initiate contact without user permission)
- Define numerical or probabilistic boundaries for decisions (confidence thresholds)
- Self-veto mechanisms allow the agent to refuse an action if ethical conditions are not fully satisfied

---

## 10. Deployment-Phase Compliance Checklist

### Phase 0 — Foundation (Months 1–2)
- [ ] Engage Danish legal counsel for compliance review of this document
- [ ] Confirm AURA risk classification (High-Risk, Annex III §5)
- [ ] Map all applicable Danish national law (Databeskyttelsesloven, Bogføringsloven)
- [ ] Verify no prior public disclosure of TONE architecture details (patent novelty)
- [ ] Begin DPIA (Data Protection Impact Assessment) template

### Phase 1 — DK Pilot (Months 3–8)
- [ ] Complete DPIA for DK pilot scope
- [ ] Datatilsynet (Danish DPA) pre-consultation on Zero-Knowledge Vault approach
- [ ] Verify MitID integration compliance with Danish e-ID requirements
- [ ] Implement full s.net logging with per-layer cryptographic signatures
- [ ] Implement addendum protocol (no in-place edits to decision log)
- [ ] Configure Human-Oversight Matrix thresholds for pilot scope
- [ ] Begin EU AI Act conformity assessment (internal control)
- [ ] First compliance audit (internal)

### Phase 2 — EU Expansion (Months 6–18)
- [ ] Complete EU AI Act conformity assessment
- [ ] Issue EU declaration of conformity (Art. 47)
- [ ] Affix CE marking (Art. 48)
- [ ] Register in EU database (Art. 49, Art. 71)
- [ ] Cross-border DPIA for multi-state deployment
- [ ] eIDAS 2 / EUDI Wallet interoperability certification
- [ ] NIS2 incident reporting operational (24h/72h/1-month) AND AI Act Art. 73 serious incident reporting (15-day) — separate reporting streams, not conflated
- [ ] Independent third-party compliance audit
- [ ] Horizon Europe grant compliance verification

---

## Document Version

- **Source documents:** BySommer_Compliance_Architecture.pdf (4 pages) + By_Sommer_Compliance_Book.pdf (4 pages)
- **This document:** Consolidated, de-duplicated, extended with full EU AI Act article mapping, addendum protocol, and deployment compliance checklist
- **Date prepared:** 06 August 2026
- **Prepared by:** Solas (Archivist) under direction of inventor Michael Sommer
- **Supersedes:** Both source documents — they are retained in the repo for historical reference but this is now the canonical version

---

*This Compliance Book is a living document. It reflects By Sommer's commitment to building trustworthy, transparent, and legally resilient AI systems — and to leading by example in the responsible development of autonomous technologies. Compliance, legislation, guardrails, and ethics are built into the system core foundation, not perceived as a static ruleset but as a live, enforceable lens that continuously shapes agent decisions while preserving user sovereignty, trust, and dignity.*
