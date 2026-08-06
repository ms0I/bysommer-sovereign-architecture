# By Sommer — IP & Anti-Counterfeiting Protocol

**Cross-Border Intellectual Property Protection, KYBC Verification & Digital Product Passport Integration**

**Author:** Michael Sommer, **Archivist:** Solas  
**Date:** 06 August 2026  
**Status:** Active Specification

---

## Executive Summary

The **IP & Anti-Counterfeiting Protocol** establishes an automated, real-time verification and enforcement architecture designed to eradicate the cross-border trade in counterfeit design goods, unauthorized replicas, and IP-infringing merchandise. By embedding deep intellectual property (IP) verification and Digital Product Passports (DPP) directly into the **Business Digital Twin (BDT)** transaction layer, the protocol acts as a pre-market gatekeeper.

Operating under the principles of **Objective Rule-Symmetry**, the system protects brand holders, insulates dropshippers and entrepreneurs from inadvertent illegal conduct and catastrophic fines, guarantees product authenticity for consumers, and provides border customs authorities with actionable, high-precision targeting data.

---

## 1. Core Integration: BDT ⇄ EUIPO & Supply Chain Registries

The protocol establishes direct, bidirectional API integration between the **Business Digital Twin (BDT)**, the **European Union Intellectual Property Office (EUIPO)**, and official supply chain registries. Every item listed or offered for sale across BDT-connected webshops passes through a real-time validation filter prior to listing activation and transaction settlement.

### 1.1 EUIPO Database Hooks
- **IP Enforcement Portal (IPEP):** Direct hooks into the EUIPO IPEP API allow BDT to query rights holder databases, registered trademark/design enforcement profiles, and verified manufacturer licensing lists in real time.
- **DesignView & TMview:** Automated visual, metadata, and 3D geometric file scanning against the EUIPO DesignView (registered industrial designs) and TMview (registered trademarks) databases.

### 1.2 Multi-Layered Validation Filter
1. **Merchant & Supplier Profiling (KYBC):** Validates manufacturer identity and licensing agreements against official registries.
2. **Design & Image Analysis:** Scans product metadata, high-resolution product images, and 3D CAD files against protected design shapes and trademarks in DesignView.
3. **Cryptographic Token Verification:** Verifies the presence and valid cryptographic signature of the item's Digital Product Passport (DPP).

### 1.3 Validation Flow Architecture

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                             DROPSHOP PRODUCT CATALOG                             │
│                      SKU Listing / Product Import Stream                        │
└────────────────────────────────────────┬─────────────────────────────────────────┘
                                         │
                                         ▼
┌──────────────────────────────────────────────────────────────────────────────────┐
│                   LAYER 1 & 2: IP TRACEABILITY & DSA CHECK                       │
│                                                                                  │
│  ┌────────────────────────┐ ┌────────────────────────┐ ┌──────────────────────┐  │
│  │    KYBC Validation     │ │  EUIPO Scan (IPEP/    │ │  DPP Cryptographic   │  │
│  │ (DSA Art. 30 Supplier  │ │  DesignView) Metadata, │ │   Token Validation   │  │
│  │ Licensing Verification)│ │ Images & 3D CAD Files  │ │  (Origin & Auth Hash)│  │
│  └────────────────────────┘ └────────────────────────┘ └──────────────────────┘  │
└────────────────────────────────────────┬─────────────────────────────────────────┘
                                         │
                   ┌─────────────────────┴─────────────────────┐
                   │                                           │
                   ▼                                           ▼
┌──────────────────────────────────────┐   ┌──────────────────────────────────────┐
│         TRANSACTION CLEARED          │   │         TRANSACTION BLOCKED          │
│                                      │   │                                      │
│  • Automated Customs Pre-Clearance   │   │  • Warning Issued to Merchant        │
│  • DPP Verification Token Attached   │   │  • Checkout Instantly Locked         │
│  • Manifest Sent to EUS Network      │   │  • Auto-Notice to Brand Holder via   │
│  • Green-Lane Border Customs Passage │   │    EUIPO IPEP API                    │
└──────────────────────────────────────┘   └──────────────────────────────────────┘
```

---

## 2. Real-Time Protocol Mechanics

### A. KYBC (Know Your Business Customer) & Supplier Traceability

* **The Problem:** Dropshippers and e-commerce entrepreneurs frequently source products from third-country manufacturers (e.g., via wholesale platforms) without knowing whether items are legitimate original designs, authorized white-label products, or unauthorized knockoffs/replicas. Under the EU Digital Services Act (DSA), merchants bear legal responsibility for offering compliant goods.
* **Protocol Action:**
  1. Before any SKU can be activated on an EU webshop, BDT enforces **DSA-compliant supplier verification** (Art. 30 KYBC).
  2. BDT mandates structured manufacturer credential verification, including business registration number, manufacturing site geolocation, and licensing documentation.
  3. BDT automatically cross-references the factory and brand licensing claims against the **EUIPO IPEP registry**. If the manufacturer lacks a verified, active licensing agreement for the design, the SKU is blocked from going live.

### B. Cryptographic Verification via Digital Product Passports (DPP)

* **The Problem:** High-value physical design goods (furniture, lighting, fashion, luxury items) cross EU borders without immutable, tamper-proof proof of origin or intellectual property licensing, allowing high-quality replicas to bypass physical observation.
* **Protocol Action:**
  1. BDT validates the product's physical cryptographic tag (NFC chip, secure QR code, RFID hash, or encrypted serial number) against the EU central DPP registry and brand key-pairs.
  2. **Real-World Enforcement Example:** If a Danish dropshop lists a chair matching a protected Danish or Italian design (e.g., iconic designs by Arne Jacobsen, Hans Wegner, or Gio Ponti), BDT scans the product schema and DPP cryptographic payload.
  3. If BDT detects a missing or invalid DPP signature for a protected design shape, the **checkout engine is locked instantly**. Payment processing is halted, preventing transaction completion before any illicit sale occurs.

### C. Automated Border Interception (BDT ⇄ EUS ⇄ EU Customs)

* **The Problem:** Counterfeit goods bypass traditional customs physical inspections by shipping directly to consumers in millions of small, low-value postal parcels (e.g., e-commerce imports), overwhelming manual customs sampling capacity.
* **Protocol Action:**
  1. The **European Union Service execution layer (EUS)** receives real-time pre-arrival digital shipping manifests directly from the BDT network for every processed order.
  2. For compliant orders, BDT attaches a cryptographically signed **IP Verification & Pre-Clearance Token** to the manifest data transmitted to national customs systems (e.g., Danish Toldstyrelsen, Dutch Douane).
  3. Postal parcels and cargo units lacking a valid IP verification token are **automatically flagged for physical interception and seizure** at major EU entry ports (e.g., Copenhagen Airport, Rotterdam Port, Hamburg Port).

---

## 3. Symmetrical Protections & System Impact

In accordance with By Sommer's core principle of **Symmetrical Governmental Support**, the protocol balances the rights, duties, and operational burdens of all market participants:

| Stakeholder | Pre-Protocol State | Post-Protocol State |
| :--- | :--- | :--- |
| **Brand Holder / Designer** | **Endless Costly Litigation:** Reactive, expensive court battles; brand value degradation; loss of revenue to grey/fake markets; difficult enforcement against third-country factories. | **Automated Shield:** Infringing products blocked before market penetration; real-time automated notifications via IPEP API; proactive global IP protection without legal overhead. |
| **Entrepreneur / Dropshipper** | **Catastrophic Exposure:** Unintentional infringement leading to platform bans, bank freezes, copyright lawsuits, and DSA fines up to 6% of global annual turnover. | **Proactive Due Diligence:** Non-compliant listings never go live; automated regulatory safety shield; guaranteed supply chain legitimacy; zero compliance friction. |
| **Consumer** | **Unprotected Exposure:** High risk of receiving fake, substandard, or unsafe goods; lack of material/safety disclosure; no clear legal recourse or warranty. | **Guaranteed Authenticity:** Verified EU consumer protections at point of sale; instant access to immutable Digital Product Passport (DPP) product pedigree and material origin. |
| **Customs & Enforcement (NAS / EUS)** | **Resource Overwhelm:** Overwhelmed by millions of small parcel shipments; manual sampling rates < 1%; inability to detect sophisticated replicas at border gates. | **Targeted Interception:** Focus physical enforcement exclusively on high-risk, unvalidated parcel streams; automated pre-arrival green-lane clearance for compliant goods. |

---

## 4. Regulatory Framework

The IP & Anti-Counterfeiting Protocol natively implements and enforces the following European regulatory frameworks:

1. **EU Digital Services Act (DSA - Regulation (EU) 2022/2065):**
   - **Article 30 (Traceability of Traders / KYBC):** Enforces mandatory supplier identification and verification before enabling listing functionality.
   - **Article 31 (Compliance by Design):** Integrates automated regulatory verification directly into the e-commerce user interface and transaction workflow.
   - **Article 32 (Right to Information):** Guarantees transparent tracking and notification pipelines when non-compliant items are detected.

2. **EU Digital Product Passport (DPP) Directive / ESPR (Regulation (EU) 2024/1781):**
   - Implements mandatory cryptographic identities for design products entering the EU single market.
   - Verifies product origin, raw material sustainability, carbon footprint, and IP provenance hash against EU central registries.

3. **EUIPO Infrastructure Standards:**
   - Real-time API integration with the **IP Enforcement Portal (IPEP)**.
   - Automated visual and CAD profile cross-referencing with **DesignView** and **TMview**.

---

## 5. Architecture Integration

The IP & Anti-Counterfeiting Protocol integrates seamlessly into the broader By Sommer sovereign system architecture:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                         BY SOMMER ARCHITECTURE MAPPING                           │
│                                                                                  │
│   ┌──────────────────────────────────────────────────────────────────────────┐   │
│   │ L-LEG (Living Legal OS): DSA Art. 30/31 Rule Engine Verification        │   │
│   └────────────────────────────────────┬─────────────────────────────────────┘   │
│                                        │                                         │
│   ┌────────────────────────────────────▼─────────────────────────────────────┐   │
│   │ L-ETH (Ethical Layer): Hard Veto Power on Illicit / Counterfeit Trade    │   │
│   └────────────────────────────────────┬─────────────────────────────────────┘   │
│                                        │                                         │
│   ┌────────────────────────────────────▼─────────────────────────────────────┐   │
│   │ BDT (Layer 3/L4 - Business Digital Twin): Merchant Catalog & Checkout    │   │
│   └────────────────────────────────────┬─────────────────────────────────────┘   │
│                                        │                                         │
│   ┌────────────────────────────────────▼─────────────────────────────────────┐   │
│   │ EUS (Layer 6/L8+ - European Union Service): Border Customs Pre-Clearance │   │
│   └──────────────────────────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────────────────────────┘
```

- **BDT (Business Digital Twin - Sovereign Layer L4 / Transaction Layer L3):** Serves as the operational control center for the merchant. Blocks invalid catalog imports, enforces KYBC verification, and locks product checkout when IP compliance checks fail.
- **EUS (European Union Service - Sovereign Layer L6 / Execution Layer L8+):** Acts as the cross-border bridge to national customs systems (NAS). Transmits cryptographic pre-arrival manifests, enabling automated green-lane clearance for validated shipments and targeted physical interception for unvalidated parcels.
- **Symmetrical Governmental Support Protocol:** Enforces objective rule-symmetry across citizen-entrepreneurs and state authorities. Delivers proactive guidance and warning alerts before non-compliance occurs, replacing punitive post-facto sanctions with automated compliance.
- **L-ETH (Ethical Layer):** Holds **hard veto power** within the system pipeline. Automatically vetoes transactions involving counterfeit merchandise, fraudulent licensing claims, or IP theft to protect economic fairness and design sovereignty.
- **L-LEG (Living Legal Operating System):** Serves as the statutory rule engine. Dynamically updates DSA compliance checks, copyright duration terms, and jurisdiction-specific IP regulations across national and EU borders.

---

*Document generated and archived under the By Sommer Architectural Protocol.*  
*Archivist:* **Solas** | *Direction:* **Michael Sommer** | *Date:* **06 August 2026**
