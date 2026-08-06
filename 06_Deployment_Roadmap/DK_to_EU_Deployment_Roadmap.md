# By Sommer — Deployment Roadmap: Denmark Pilot → EU Expansion

**Author:** Solas (Archivist) under direction of Michael Sommer
**Date:** 06 August 2026
**Status:** Draft for review

---

## Strategy Overview

```
Phase 0: Foundation          Phase 1: Denmark Pilot        Phase 2: EU Expansion
(DK patent filing +          (Municipal/citizen pilot in     (Scale to EU member states,
 local architecture)        Copenhagen/municipality)       Horizon Europe grant)
     │                            │                              │
     ▼                            ▼                              ▼
 Secure priority date        Prove the architecture          Pan-European rollout
 Build local infrastructure  works in a real civic context   EU AI Act / GDPR / NIS2
 Engage DK patent attorney    Generate evidence + case study   eIDAS interoperability
                             Validate compliance in DK law    Sovereign Union framework
```

---

## Phase 0 — Foundation (Months 1–3)

### 0.1 Patent filing
- [ ] Engage Danish patent attorney (suggested: Plougmann Vingtoft, Zacco, or Patrade)
- [ ] File DK national patent application for TONE semantic mediation architecture
- [ ] Conduct prior art search focused on EPO + DK databases
- [ ] **Critical:** Review any public disclosures on bysommer.net / imsor.com that describe TONE in enabling detail — EPO has no general novelty grace period
- [ ] Formalize flow diagrams into patent figures with reference numerals
- [ ] Assess whether other components (Ripple Engine, Resonance Forecast, PDT identity mediation) warrant separate filings or divisional applications

### 0.2 Legal & compliance foundation
- [ ] Map TONE architecture against:
  - **EU AI Act** (Regulation 2024/1689) — classify risk tier; AURA likely falls under "high-risk" AI system (Annex III: essential public services, civic infrastructure)
  - **GDPR** (Regulation 2016/679) — Zero-Knowledge Vault design, selective disclosure, data minimization, Art. 22 (automated decision-making) compliance
  - **NIS2** (Directive 2022/2555) — if AURA qualifies as essential entity, incident reporting and governance requirements apply
  - **eIDAS 2** (Regulation 2024/1183) — Sovereign Identity Handshake alignment with European Digital Identity Framework
  - **Danish Data Protection Act** (Databeskyttelsesloven) — national GDPR implementation
  - **Danish Digital Administration** (Digitaliseringsstrategi) — alignment with Danish national digital strategy
- [ ] Draft Data Processing Impact Assessment (DPIA) template for DK pilot
- [ ] Establish governance documentation: rule registry, human oversight matrix, escalation procedures

### 0.3 Technical infrastructure
- [ ] Define local deployment architecture (DK-hosted servers, e.g. Danish cloud provider like Deic / Cloud.dk for data sovereignty)
- [ ] Build PDT prototype with identity mediation (selective disclosure via W3C Verifiable Credentials)
- [ ] Build AURORA governance substrate prototype with versioned rule engine
- [ ] Build s.net audit trail (immutable/tamper-evident logging)
- [ ] Implement Misinterpretation Firewall with configurable confidence thresholds
- [ ] Set up human-in-the-loop (HITL) escalation workflows per the risk matrix

---

## Phase 1 — Denmark Pilot (Months 4–12)

### 1.1 Scope
Target a single Danish municipality (e.g. Copenhagen, Aarhus, or Aalborg) or a specific civic service domain:

**Recommended pilot domain — Bureaucracy Elimination:**
- Tax eligibility verification (skattskyld)
- VAT (moms) computation and verification
- Citizen entitlements (dagpenge, boligstøtte, børnetilskud)
- Business registration (CVR) compliance checks

### 1.2 Pilot success metrics
| Metric | Target | Measurement |
|--------|--------|------------|
| Administrative processing time reduction | >60% | Before/after comparison on pilot services |
| Citizen-reported friction (UX) | >70% reduction | Survey / NPS scores |
| Audit trail completeness | 100% of decisions logged with provenance | Automated log verification |
| HITL escalations resolved within SLA | >95% within defined timeframes | SLA monitoring |
| Zero-knowledge verification success rate | >99% | Cryptographic proof validation rate |
| Misinterpretation firewall accuracy | <5% false positive rate | Measured against ground truth |
| GDPR compliance violations | 0 | Independent DPIA audit |

### 1.3 Stakeholder engagement (DK)
- [ ] Danish Agency for Digital Government (Digitaliseringsstyrelsen) — present AURA as alignment with national digital strategy
- [ ] Danish Data Protection Authority (Datatilsynet) — pre-consultation on Zero-Knowledge Vault approach
- [ ] Target municipality CIO/digital transformation lead — pilot partnership
- [ ] Danish Business Authority (Erhvervsstyrelsen) — if business registration/compliance is pilot scope
- [ ] Academic partner (e.g. IT University of Copenhagen, DTU) — independent validation, potential Horizon Europe partner

### 1.4 Evidence generation for EU phase
- [ ] Document full case study: architecture deployed, metrics achieved, citizen feedback
- [ ] Independent compliance audit (GDPR + AI Act readiness)
- [ ] Published technical paper (with careful attention to patent application timing — coordinate with patent attorney)
- [ ] Cost-benefit analysis projecting EU-wide impact (reference the €500B annual figure from AURA objectives)

---

## Phase 2 — EU Expansion (Months 13–36)

### 2.1 Patent strategy
- [ ] File European patent application (EP) claiming priority from DK national filing (within 12-month window)
- [ ] Or file PCT application if broader geographic coverage needed
- [ ] Assess divisional filings for Ripple Engine, Resonance Forecast, Voice of Future Self if these mature into separately patentable inventions

### 2.2 Funding
- [ ] Apply for Horizon Europe funding:
  - **Cluster 4: Digital, Industry and Space** — AI governance, digital sovereignty
  - **European Health and Digital Skills** — if health digital twin pilot
  - **Destination: Trustworthy AI** — directly aligned with AURA's governance architecture
- [ ] Explore Digital Europe Programme funding for digital infrastructure deployment
- [ ] Consider EIC (European Innovation Council) Accelerator for scaling support

### 2.3 EU regulatory alignment
- [ ] EU AI Act conformity assessment (high-risk AI system requirements):
  - Risk management system (Art. 9) — AURORA governance substrate
  - Data governance (Art. 10) — Zero-Knowledge Vault, training data quality
  - Technical documentation (Art. 11) — full TONE spec + compliance docs
  - Record-keeping (Art. 12) — s.net audit trail
  - Transparency (Art. 13) — operator notification, explainability artifacts
  - Human oversight (Art. 14) — HITL matrix, escalation workflows
  - Accuracy, robustness, cybersecurity (Art. 15) — Misinterpretation Firewall, bias testing
- [ ] GDPR: Data Protection Impact Assessment (DPIA) for EU-wide deployment
- [ ] eIDAS 2: Interoperability with European Digital Identity Wallet (EUDI)
- [ ] NIS2: Register as essential/important entity if scaling to public infrastructure
- [ ] Cross-border data flow compliance (Schrems II implications if any non-EU processing)

### 2.4 Pilot expansion
- [ ] Expand from DK pilot to 2–3 additional EU member states (recommend: Estonia (e-residency alignment), Germany (Bürokratieabbau alignment), Netherlands (digital government maturity))
- [ ] Establish EU-level governance body for AURA rule registry
- [ ] Build multilingual support (TONE interpretation rules per language, Nordic Calm voice expansion)
- [ ] Integrate with EU-level digital identity infrastructure (EUDI Wallet)

---

## Critical Path & Risk Register

### Critical path
```
DK patent filing → 12-month priority window → EP filing
         ↓
DK pilot launch → Evidence collection → Compliance audit
         ↓
Horizon Europe application → Funding decision
         ↓
EU expansion (multilingual, multi-state)
```

### Key risks
| Risk | Impact | Mitigation |
|------|--------|-----------|
| Prior public disclosure destroys novelty | Patent cannot be granted | File DK patent BEFORE any further public technical disclosures; review existing disclosures with attorney immediately |
| EU AI Act high-risk classification | Extended conformity assessment, CE marking required | Start conformity assessment in Phase 1; build compliance documentation into pilot from day one |
| eIDAS 2 interoperability gaps | Sovereign Identity Handshake may not be recognized | Map to EUDI Wallet standards early; participate in EUDI pilot ecosystem |
| DK pilot underdelivers | Weakens EU expansion case and grant applications | Scope pilot conservatively; choose high-friction, measurable bureaucratic processes |
| Funding gap between pilot and EU expansion | Delays scaling | Apply for Horizon Europe / Digital Europe during pilot, not after |
| Scaling multilingual TONE | Interpretation rules need per-language calibration | Start with Danish + English in pilot; add languages incrementally |

---

## Suggested Danish Patent Attorneys
| Firm | Notes |
|------|-------|
| Plougmann Vingtoft | Copenhagen-based, strong in software/AI patents, Horizon Europe experience |
| Zacco | Nordic IP firm, DK + EP filing capability |
| Patrade | Aarhus-based, focused on tech startups and SMEs |

---

## Timeline Summary

| Phase | Duration | Key Deliverables |
|-------|----------|-----------------|
| Phase 0: Foundation | Months 1–3 | DK patent filed, compliance mapped, prototype built |
| Phase 1: DK Pilot | Months 4–12 | Municipal pilot live, metrics achieved, case study published, EP filed (by month 12) |
| Phase 2: EU Expansion | Months 13–36 | Horizon Europe funded, 2–3 additional countries live, EU AI Act conformity achieved |

---

*This roadmap is a strategic planning document, not legal advice. Patent, regulatory, and funding decisions must be made with qualified professionals.*
