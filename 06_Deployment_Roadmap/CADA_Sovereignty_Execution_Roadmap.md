# CADA Sovereignty Execution Roadmap: From Architecture to Implementation

**Author:** Michael Sommer  
**Archivist:** Solas  
**Date:** 06 August 2026  
**Status:** Active execution plan

> This document transitions the By Sommer sovereign architecture from conceptual specification to practical implementation under the EU's Cloud and AI Development Act (CADA) sovereignty framework. It is the engineering counterpart to the Compliance Book — where the Compliance Book defines *what* the rules are, this roadmap defines *how* to build systems that provably comply with them.

---

## CADA Sovereignty Assurance Levels

Before defining the execution phases, the four CADA sovereignty levels must be mapped to the By Sommer architecture:

| Level | CADA Requirement | By Sommer Architecture Mapping | Current Status |
|-------|-----------------|-------------------------------|----------------|
| **Level 1** | Baseline EU data residency — data stored and processed on EU soil | L-PDT Zero-Knowledge Vault (edge device, user domain). L-SNET audit trail on EU infrastructure. DK pilot: Danish soil. | Specified, not yet deployed |
| **Level 2** | EU-processed with restricted third-country access — no non-EU cloud providers for processing | All sovereign layers on EU infrastructure. No third-country cloud dependencies for processing. TONE contracts enforce EU-only execution. | Architecturally designed, procurement pending |
| **Level 3** | Sovereign cloud with full operational independence — EU-controlled operations, no third-country jurisdiction over infrastructure | Self-hosted or EU-sovereign cloud (e.g., OVHcloud, Scaleway, Hetzner EU). No US-hyperscaler dependencies for sovereign layers. Keys, logs, and governance on EU soil with EU personnel. | Requires infrastructure procurement |
| **Level 4** | Full third-country non-interference and supply chain control — hardware, software, and personnel all within EU jurisdiction, no extraterritorial access | EU-manufactured or EU-verified hardware. EU-domiciled personnel with clearance. Open-source software with EU-audited provenance. Full supply chain attestation. No CLOUD Act exposure. | Target state for EU expansion |

**Deployment target:**
- DK Pilot (Phase 1): Level 1–2 (EU data residency, restricted third-country access)
- EU Expansion (Phase 2): Level 3–4 (sovereign cloud, full supply chain control)

---

## Phase 1: Immediate Workload Inventory

**Objective:** Map every active cloud service, data repository, and AI pipeline against CADA's four sovereignty assurance levels.

### 1.1 Inventory Scope

Every component in the By Sommer architecture must be inventoried:

| Component Category | What to Inventory | Architecture Mapping |
|-------------------|--------------------|--------------------|
| **Cloud services** | Hosting provider, region, data residency, subprocessors | L-SYS execution layer, L-SNET audit storage, L-AURORA governance runtime |
| **Data repositories** | Where data is stored, who has access, retention period | L-PDT Zero-Knowledge Vault, L-SNET immutable ledger, L-LEG rule registry |
| **AI pipelines** | Model training, inference, model storage, model provenance | L-PDT interpretation components, Predictive Council (100 agents), GEMS Oracle |
| **Identity infrastructure** | Key storage, key generation, signing authorities | L-PDT identity wallet, per-layer Ed25519 keys, MitID integration |
| **Software dependencies** | Libraries, frameworks, base images, package registries | All layers — supply chain provenance for every component |
| **Personnel jurisdictions** | Who has access, their residency/employment jurisdiction, clearance level | All sovereign layers — L-LEG must track who can access what and under which jurisdiction's laws |

### 1.2 Workload Inventory Template

```json
{
  "component_id": "L-PDT-001",
  "component_name": "Personal Digital Twin — Identity Wallet",
  "sovereign_layer": "L-PDT",
  "category": "identity_infrastructure",
  "cada_level_target": 4,
  "cada_level_current": 0,
  
  "data_residency": {
    "storage_location": "edge_device (user_domain)",
    "backup_location": "TBD — must be EU soil",
    "processing_location": "edge_device (local)",
    "cross_border_flows": "none (by design)"
  },
  
  "cloud_services": {
    "provider": "none (edge) / TBD (backup)",
    "region": "N/A (edge) / EU (backup target)",
    "subprocessors": [],
    "third_country_exposure": "none (edge) / TBD (backup)"
  },
  
  "software_supply_chain": {
    "base_image": "TBD — must be EU-audited open source",
    "key_dependencies": ["W3C VC library", "Ed25519 crypto library", "ZK proof library"],
    "dependency_provenance": "TBD — SBOM required",
    "package_registry": "TBD — EU mirror preferred",
    "vulnerability_scanning": "TBD"
  },
  
  "personnel_jurisdictions": {
    "developers": ["TBD — EU-domiciled required for Level 3+"],
    "operators": ["TBD — EU-domiciled with clearance for Level 4"],
    "auditors": ["TBD — EU-domiciled independent third party"],
    "third_country_access": "none (target)"
  },
  
  "ai_pipelines": {
    "model_type": "interpretation (local, on-device)",
    "training_data_location": "TBD — EU soil or synthetic",
    "inference_location": "edge_device (local)",
    "model_storage": "edge_device (local)",
    "model_provenance": "TBD — full lineage documentation",
    "third_country_model_exposure": "none (target)"
  },
  
  "gaps_to_target_level": [
    "Backup location not yet defined — must be EU soil",
    "SBOM not yet generated for dependencies",
    "Personnel jurisdictions not yet documented",
    "Model provenance not yet documented"
  ]
}
```

### 1.3 Inventory Deliverables

| Deliverable | Format | Deadline |
|------------|--------|----------|
| Complete workload inventory (all components) | JSON registry (one file per component) | Phase 0 completion |
| Software supply chain provenance report | SBOM (CycloneDX or SPDX format) per component | Phase 0 completion |
| Personnel jurisdiction matrix | Spreadsheet mapping roles → jurisdictions → access levels | Phase 0 completion |
| CADA level gap analysis | Document showing current vs target level per component | Phase 0 completion |
| Third-country exposure report | Document listing all non-EU dependencies, services, or access paths | Phase 0 completion |

### 1.4 Architecture Integration

The workload inventory becomes the **L-LEG rule registry's first input** — the Legal OS needs to know what it's governing before it can enforce rules. The inventory feeds into:
- L-LEG jurisdiction detection (personnel jurisdictions determine which laws apply)
- L-ETH ethical guardrails (third-country access paths are risk factors)
- s.net audit trail (the inventory itself is an auditable artifact)
- GEMS Oracle validation (compliance proofs reference the inventory)

---

## Phase 2: Transition from Code Stubs to Hardware-Backed Vaults

**Objective:** Upgrade the zero-knowledge vault from software key stubs to production-grade hardware enclaves.

### 2.1 Current State vs Target State

| Component | Current State (Spec) | Target State (Production) |
|-----------|---------------------|--------------------------|
| Key storage | Software key stubs (Ed25519 key pairs in code) | Hardware-backed keys (TPM, Secure Enclave, HSM) |
| Key generation | In-software generation | Hardware-generated keys (non-exportable) |
| Signing operations | Software signing | Hardware signing (keys never leave the enclave) |
| Attestation tokens | Unsigned JSON stubs | Canonicalized JSON + asymmetric signing |
| Vault storage | Encrypted file on device | Hardware-isolated storage (enclave/TPM-bound) |
| Recovery | Shamir's secret sharing (software) | Multi-party hardware-backed recovery (M-of-N with hardware keys) |

### 2.2 Hardware Stack by Platform

| Platform | Hardware Security Module | Key API | Use Case |
|----------|------------------------|--------|---------|
| **iOS** | Secure Enclave (SEP) | CryptoKit (LocalAuthentication + Secure Enclave) | PDT mobile (iPhone) |
| **Android** | Android Keystore (TEE/StrongBox) | AndroidKeyStore API | PDT mobile (Android) |
| **macOS** | Apple Silicon SEP | CryptoKit / Security framework | PDT desktop |
| **Windows** | TPM 2.0 | Windows TPM API / BCrypt | PDT desktop |
| **Linux (server)** | HSM (YubiHSM2, Nitrokey HSM) | PKCS#11 | Server-side sovereign layers |
| **Cloud (EU)** | Cloud HSM (EU-region) | PKCS#11 / KMS API | L-SNET, L-LEG, L-AURORA (EU expansion) |

### 2.3 Cryptographic Attestation Standard

All attestation tokens must follow strict canonicalization and asymmetric signing:

```json
{
  "attestation": {
    "version": "1.0",
    "component_id": "L-PDT-001",
    "tone_id": "uuid-v7",
    "timestamp": "2026-08-06T09:34:00.000Z",
    "sovereign_layer": "L-PDT",
    "cada_level": 4,
    
    "attestation_type": "compliance_proof",
    "attested_claims": {
      "data_residency": "EU_DK",
      "key_hardware_backed": true,
      "no_third_country_access": true,
      "software_provenance_verified": true,
      "personnel_jurisdiction": "EU"
    },
    
    "proof": {
      "proof_type": "zero_knowledge",
      "proof_hash": "zk:0x...",
      "disclosed_attributes": ["cada_level", "data_residency"],
      "undisclosed_attributes": ["raw_data", "internal_logic", "telemetry"]
    }
  },
  
  "signature": {
    "algorithm": "Ed25519",
    "key_id": "L-PDT-key-001",
    "key_hardware_backed": true,
    "signature_value": "base64..."
  }
}
```

**Canonicalization rules (strict JSON canonicalization per RFC 8785):**
1. All keys sorted lexicographically (UTF-8 byte order)
2. No insignificant whitespace
3. No trailing commas
4. UTF-8 encoding only
5. Numbers in shortest valid representation
6. Signature computed over the canonicalized attestation object (excluding the signature field itself)

### 2.4 Implementation Checklist

- [ ] Select hardware security modules for each target platform
- [ ] Implement hardware-backed key generation (non-exportable keys)
- [ ] Implement hardware signing for attestation tokens
- [ ] Implement strict JSON canonicalization (RFC 8785 JCS)
- [ ] Implement Ed25519 asymmetric signing over canonicalized tokens
- [ ] Implement attestation token verification on receiving layers
- [ ] Implement hardware-backed key recovery (M-of-N Shamir's with hardware shards)
- [ ] Generate SBOM for all cryptographic libraries
- [ ] Audit cryptographic implementation (third-party crypto review)
- [ ] Document key rotation and lifecycle procedures
- [ ] Integrate with s.net (all attestation tokens logged)

### 2.5 Architecture Integration

The hardware-backed vault upgrade affects these sovereign layers:

| Layer | Change Required |
|-------|-----------------|
| L-PDT | Identity wallet keys → hardware. ZK Vault storage → enclave-bound. |
| L-AURORA | Governance signing key → hardware. Rule registry integrity → hardware-attested. |
| L-ETH | Ethical veto signing → hardware. Veto decisions cryptographically non-repudiable. |
| L-LEG | Legal rule registry signing → hardware. Compliance proofs → hardware-attested. |
| L-SYS | Execution authorization signing → hardware. Actions only execute with hardware-signed approval. |
| L-SNET | Audit trail entries → hardware-signed. Ledger integrity → hardware-attested. Per-layer keys non-exportable. |

**Key principle:** Every sovereign layer's signing key must be hardware-backed. This ensures that even if software is compromised, the attacker cannot forge layer signatures — the keys are physically non-exportable.

---

## Phase 3: Automate the Compliance Cascade Pipeline

**Objective:** Set up selective disclosure proof engines that allow systems or contractors to cryptographically attest to CADA compliance criteria without exposing proprietary internal logic or raw telemetry to auditors.

### 3.1 The Compliance Cascade

The compliance cascade is the automated flow from "system operates" → "compliance proof generated" → "auditor verifies" — without the auditor ever seeing the system's internal data.

```
SYSTEM OPERATES
    │
    ▼
L-LEG evaluates operation against CADA requirements
    │
    ▼
GEMS Oracle deterministically verifies compliance
    │
    ▼
Compliance Proof Engine generates ZK attestation
(Proof says: "this operation complied with CADA Level X"
 — without revealing the operation itself)
    │
    ▼
Proof published to s.net immutable ledger
(Proof is timestamped, signed, publicly verifiable)
    │
    ▼
Auditor / Regulator / Procurement Officer
verifies the proof WITHOUT accessing the system
    │
    ▼
Compliance confirmed — no raw data exposed
```

### 3.2 Selective Disclosure Proof Engine

The proof engine generates zero-knowledge proofs of compliance:

```json
{
  "compliance_proof": {
    "proof_id": "uuid-v7",
    "timestamp": "2026-08-06T09:34:00.000Z",
    "system_attested": "L-PDT-001",
    "cada_level_attested": 4,
    
    "compliance_criteria": [
      {
        "criterion": "data_residency",
        "requirement": "EU soil",
        "proof": "zk:proof_hash",
        "verified_by": "GEMS_oracle",
        "raw_data_disclosed": false
      },
      {
        "criterion": "no_third_country_access",
        "requirement": "no non-EU personnel or services",
        "proof": "zk:proof_hash",
        "verified_by": "GEMS_oracle",
        "raw_data_disclosed": false
      },
      {
        "criterion": "software_supply_chain",
        "requirement": "SBOM verified, no critical vulnerabilities",
        "proof": "zk:proof_hash",
        "verified_by": "GEMS_oracle",
        "raw_data_disclosed": false,
        "sbom_hash": "sha256:..."
      },
      {
        "criterion": "key_hardware_backed",
        "requirement": "all signing keys hardware-generated, non-exportable",
        "proof": "zk:proof_hash",
        "verified_by": "hardware_attestation",
        "raw_data_disclosed": false
      },
      {
        "criterion": "personnel_jurisdiction",
        "requirement": "all personnel with access are EU-domiciled",
        "proof": "zk:proof_hash",
        "verified_by": "GEMS_oracle",
        "raw_data_disclosed": false
      }
    ],
    
    "overall_verdict": "compliant",
    "cada_level_achieved": 4,
    
    "signature": {
      "algorithm": "Ed25519",
      "signed_by": "L-LEG",
      "key_hardware_backed": true,
      "signature_value": "base64..."
    }
  }
}
```

**What the auditor sees:** The compliance criteria, the verdict, and the cryptographic proofs.  
**What the auditor does NOT see:** Raw data, internal logic, model internals, personnel identities, system telemetry, proprietary algorithms.

### 3.3 Proof Types

| Proof Type | What It Proves | Without Revealing | Use Case |
|-----------|---------------|-------------------|----------|
| **Data residency proof** | Data is stored on EU soil | Exact storage location, data contents | CADA Level 1–4 |
| **No third-country access proof** | No non-EU personnel or services accessed the system | Access logs, personnel identities, service details | CADA Level 2–4 |
| **Supply chain proof** | All software dependencies have verified provenance | Full SBOM contents (only hash disclosed) | CADA Level 3–4 |
| **Hardware key proof** | All signing keys are hardware-backed, non-exportable | Key material, hardware details | CADA Level 3–4 |
| **Personnel jurisdiction proof** | All personnel with system access are EU-domiciled | Personnel names, roles, employment details | CADA Level 3–4 |
| **Model provenance proof** | AI models were trained on EU-compliant data | Training data contents, model internals | EU AI Act Art. 10 |
| **Audit trail integrity proof** | s.net ledger is complete and unbroken | Ledger contents (only hash chain proof) | All levels |

### 3.4 Real-Time Verification Pipeline

```
┌──────────────────────────────────────────────────┐
│           COMPLIANCE CASCADE PIPELINE              │
│                                                   │
│  ┌─────────────┐   ┌──────────────┐   ┌────────┐ │
│  │  System      │──→│  L-LEG       │──→│ GEMS   │ │
│  │  Operation   │   │  Rule Check  │   │ Oracle │ │
│  └─────────────┘   └──────────────┘   └────┬───┘ │
│                                               │     │
│                    ┌──────────────────────────┘     │
│                    ▼                                │
│              ┌──────────────┐   ┌────────────────┐  │
│              │  Proof Engine │──→│  s.net Ledger  │  │
│              │  (ZK proofs)  │   │  (immutable)   │  │
│              └──────────────┘   └───────┬────────┘  │
│                                         │           │
│                    ┌────────────────────┘           │
│                    ▼                                │
│              ┌──────────────┐                       │
│              │  Auditor API  │                       │
│              │  (read-only,  │                       │
│              │  proof-only)  │                       │
│              └──────────────┘                       │
└──────────────────────────────────────────────────┘
```

**Auditor API (read-only, proof-only):**
- Auditors query the API with a compliance criterion (e.g., "show me CADA Level 3 compliance for component L-PDT-001")
- API returns the compliance proof (verifiable, cryptographically signed)
- Auditor verifies the proof locally (no access to the system itself)
- API records the audit query in s.net (the audit is itself audited)

### 3.5 Implementation Checklist

- [ ] Select zero-knowledge proof system (zk-SNARKs, zk-STARKs, or selective disclosure tokens)
- [ ] Implement proof generation for each compliance criterion
- [ ] Implement proof verification (auditor-side, standalone)
- [ ] Implement auditor API (read-only, proof-only, rate-limited)
- [ ] Connect proof outputs to s.net immutable ledger
- [ ] Implement real-time verification (proof generated within 1 second of operation)
- [ ] Implement proof revocation (if compliance status changes, old proofs are invalid)
- [ ] Integrate with GEMS Oracle (deterministic verification before proof generation)
- [ ] Document proof lifecycle (generation, verification, expiration, revocation)
- [ ] Third-party security audit of proof system

---

## Phase 4: Align with National Procurement Timelines

**Objective:** Prepare compliance artifacts to satisfy mandatory sovereignty risk assessments required in public sector procurement and downstream contracting cascades.

### 4.1 Procurement Landscape

| Framework | Scope | CADA Relevance | Timeline |
|-----------|-------|----------------|----------|
| **EU Digital Procurement** | Public sector IT procurement | Sovereignty risk assessment mandatory for cloud/AI | Active (Directive 2014/24/EU + national implementations) |
| **Danish Public Procurement** | National procurement (SKI, Statens It) | Danish sovereignty requirements for public sector IT | Active (Udbudsloven + digital strategy) |
| **CADA Compliance** | Cloud and AI sovereignty assurance | Four-level sovereignty assessment | Entering into force — timeline TBD |
| **EU AI Act Procurement** | High-risk AI in public services | Conformity assessment + CE marking required before public deployment | Art. 6 applies — 24 months from entry into force |
| **NIS2 Procurement** | Cybersecurity in public sector supply chains | Security requirements in contracts | Active |

### 4.2 Compliance Artifacts Required for Procurement

| Artifact | Content | Format | Mapped To |
|----------|---------|--------|-----------|
| **Sovereignty Risk Assessment** | CADA level per component, third-country exposure, mitigation plan | Structured document (machine-readable + human-readable) | Phase 1 inventory |
| **Software Bill of Materials (SBOM)** | All software components, versions, provenance, vulnerabilities | CycloneDX or SPDX | Phase 1 supply chain |
| **Hardware Attestation Report** | All keys hardware-backed, hardware specifications, key lifecycle | Cryptographic attestations (signed) | Phase 2 hardware vaults |
| **Compliance Proof Portfolio** | ZK proofs of CADA compliance per component | Machine-verifiable proofs (signed) | Phase 3 proof engine |
| **Audit Trail Export** | s.net ledger extract showing compliance history | Immutable, signed, timestamped log | Phase 3 audit pipeline |
| **Conformity Assessment** | EU AI Act Annex III high-risk compliance documentation | EU declaration of conformity template | Compliance Book §7 |
| **Data Protection Impact Assessment (DPIA)** | Risk assessment for personal data processing | Standard DPIA template | Compliance Book §10 |
| **Personnel Jurisdiction Declaration** | All personnel EU-domiciled, clearance levels | Attested document (signed) | Phase 1 personnel matrix |
| **Supply Chain Security Plan** | Supplier risk assessment, dependency monitoring, incident response | Structured document | NIS2 Art. 21 |

### 4.3 Procurement Timeline Alignment

```
                    DK PILOT (Phase 1)              EU EXPANSION (Phase 2)
                    Months 3–8                      Months 6–18

Procurement ────┬──────────────────┬──────────────────┬──────────────────
                │                  │                  │
CADA L1-2       │  ████████████    │                  │
compliance      │  (DK municipal)  │                  │
                │                  │                  │
CADA L3-4       │                  │  ████████████████│
compliance      │                  │  (EU multi-state) │
                │                  │                  │
AI Act          │                  │     ████████████ │
conformity      │                  │     (CE marking) │
                │                  │                  │
DPIA            │  ████            │     ████████     │
                │  (DK scope)      │     (EU scope)  │
                │                  │                  │
Procurement     │  ████████████    │  ████████████████│
artifacts       │  (DK: SKI/       │  (EU: each MS    │
                │   Statens It)    │   procurement)   │
```

### 4.4 Downstream Contracting Cascade

When a public authority procures By Sommer infrastructure, the sovereignty requirements cascade downstream:

```
EU/National Authority
    │
    ├── CADA Level required in contract
    │   ├── By Sommer (provider) must comply
    │   │   ├── Cloud provider must comply (EU soil, EU ops)
    │   │   ├── Hardware suppliers must comply (EU-verified)
    │   │   ├── Software suppliers must comply (SBOM, EU-audited)
    │   │   └── Personnel must comply (EU-domiciled)
    │   │
    │   └── Each downstream contract carries the same CADA level requirement
    │       └── Compliance proofs flow UP the chain
    │           (supplier → By Sommer → authority → EU)
```

**The compliance proof cascade:**
1. Each supplier generates compliance proofs for their component
2. By Sommer aggregates proofs from all suppliers
3. By Sommer's L-LEG generates a composite compliance proof for the whole system
4. The authority receives a single proof covering the entire supply chain
5. The authority can verify the proof without accessing any supplier's internal data

### 4.5 Implementation Checklist

- [ ] Map procurement timelines for DK pilot target authorities (Copenhagen, Aarhus)
- [ ] Map procurement timelines for EU expansion target member states
- [ ] Prepare sovereignty risk assessment template (machine-readable)
- [ ] Generate SBOMs for all components (CycloneDX format)
- [ ] Prepare hardware attestation report template
- [ ] Prepare compliance proof portfolio template
- [ ] Prepare DPIA template (DK pilot scope)
- [ ] Prepare EU AI Act conformity assessment documentation
- [ ] Prepare personnel jurisdiction declaration template
- [ ] Prepare supply chain security plan (NIS2 Art. 21)
- [ ] Test compliance proof cascade (supplier → provider → authority)
- [ ] Engage with DK procurement bodies (SKI, Statens It) for pre-procurement dialogue

---

## Cross-Reference: Integration with Existing Architecture

| Existing Document | CADA Roadmap Integration |
|-------------------|------------------------|
| **00_MASTER_Unified_Framework.md** | GEMS Oracle (§3.2) is the deterministic verifier for CADA compliance proofs. Living Compliance Tattoo (§4.4) displays CADA level. |
| **Sovereign_Layer_Architecture_Specification.md** | Per-layer sovereignty (own keys, own logs, own veto) is the architectural basis for CADA compliance. Phased separation (DK → EU) aligns with CADA L1-2 → L3-4. |
| **L-LEG_Living_Legal_Operating_System.md** | Jurisdiction detection engine (§3.1) extends to detect CADA level requirements. Rule registry (§3.5) includes CADA rules as EU-level rule set. |
| **By_Sommer_Compliance_Book_Consolidated.md** | EU AI Act Art. 15 (accuracy, robustness, cybersecurity) maps to CADA hardware-backed vault requirement. Art. 12 (record-keeping) maps to CADA audit trail. |
| **Symmetrical_Governmental_Support_Protocol.md** | BDT ⇄ NAS interface (§8) must carry CADA compliance proofs when transmitting to authorities. |
| **Digital_Twin_Functional_Framework_Specification.md** | Identity wallet (§1.1) and key recovery (§1.10) must be hardware-backed per CADA Phase 2. |
| **DK_to_EU_Deployment_Roadmap.md** | Phase 0 deliverables expanded to include CADA workload inventory. Phase 1 includes CADA L1-2 compliance. Phase 2 includes CADA L3-4 compliance. |

---

## Execution Summary

| Phase | Timeline | Key Deliverable | CADA Level |
|-------|----------|----------------|------------|
| **Phase 1: Workload Inventory** | Months 1–2 | Complete inventory + gap analysis + SBOMs | Assessment |
| **Phase 2: Hardware Vaults** | Months 2–5 | Hardware-backed keys + canonicalized attestation tokens | L1–L2 ready |
| **Phase 3: Compliance Cascade** | Months 4–7 | ZK proof engine + auditor API + s.net integration | L1–L2 operational |
| **Phase 4: Procurement Alignment** | Months 5–8 | All procurement artifacts prepared + procurement body engagement | L1–L2 procurement-ready |
| **EU Expansion** | Months 6–18 | Upgrade to L3–L4: sovereign cloud, full supply chain control, EU-audited hardware | L3–L4 |

**Critical path:** Phase 1 → Phase 2 → Phase 3 (sequential). Phase 4 overlaps with Phase 3 (can start artifact preparation during Phase 3 development).

---

## Document Version

- **Date:** 06 August 2026
- **Prepared by:** Solas (Archivist) under direction of Michael Sommer
- **Status:** Active execution plan — supersedes the high-level deployment roadmap for technical implementation details
- **Related documents:** All documents in the By Sommer archive (see cross-reference table above)

---

*CADA compliance is not a checkbox — it is an architectural property. The By Sommer sovereign layer design makes CADA compliance structurally embedded: per-layer keys (non-exportable), per-layer audit trails (immutable), per-layer compliance proofs (zero-knowledge), and per-layer sovereignty (no shared state). The compliance cascade pipeline automates what would otherwise be months of manual audit work into real-time, cryptographically verifiable proofs. This is how architecture becomes compliance.*
