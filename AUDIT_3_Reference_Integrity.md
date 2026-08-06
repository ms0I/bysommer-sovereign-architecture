# AUDIT 3: Cross-Document Reference Integrity Report

**Repository:** `bysommer_archive`  
**Audit Scope:** Markdown Links, File Path References, Directory Map Consistency, Cross-Document References, Superseded Notices, and SVG Drawing Links.  
**Date:** 06 August 2026  
**Status:** Audit Complete  

---

## 1. Summary Statistics

| Metric | Count | Status / Notes |
|--------|-------|----------------|
| **Total Repository Files** | 56 | Across 9 directories |
| **Total Markdown (.md) Files** | 16 | Scanned end-to-end |
| **Total Markdown Links (`[text](path)`)** | 22 | 16 Valid, 6 Broken |
| **Valid Markdown Links** | 16 | 72.7% pass rate |
| **Broken Markdown Links** | 6 | 27.3% fail rate (all in `docs/SOMMER_FLAGSHIP_SPEC.md`) |
| **Inline File Path References Scanned** | 121 | In text / code blocks |
| **Valid Inline Path References** | 96 | Resolves to existing files/dirs |
| **Broken / Missing Inline Path References** | 25 | 1 missing prototype script, 1 root path prefix, 23 conceptual legal rule JSONs |
| **Indexed Files in `INDEX.md`** | 26 | Bulleted documents |
| **Orphan Files (Exist but missing from `INDEX.md`)** | 29 | Needs index expansion |
| **Phantom Files (In `INDEX.md` but missing from disk)** | 0 | 100% valid index targets |
| **Superseded Document Banner** | Verified | `01_Core_Architecture_Protocols/TONE_Patent_Draft_Filing_Structured.md` points to `/patent/` |
| **SVG Drawing Links** | 9 / 9 Verified | All 9 SVG files exist in `patent/diagrams/` |

---

## 2. Table of Broken Markdown Links

| Source File | Line | Link Text | Target Path | Resolved Target | Status | Fix Recommendation |
|-------------|------|-----------|-------------|-----------------|--------|--------------------|
| `docs/SOMMER_FLAGSHIP_SPEC.md` | 21 | `span_0` | `start_span` | `docs/start_span` | **BROKEN** | Remove malformed `[span_0](start_span)` markup tag or convert to superscript citation `[^1]`. |
| `docs/SOMMER_FLAGSHIP_SPEC.md` | 21 | `span_0` | `end_span` | `docs/end_span` | **BROKEN** | Remove malformed `[span_0](end_span)` markup tag. |
| `docs/SOMMER_FLAGSHIP_SPEC.md` | 22 | `span_1` | `start_span` | `docs/start_span` | **BROKEN** | Remove malformed `[span_1](start_span)` markup tag or convert to superscript citation `[^2]`. |
| `docs/SOMMER_FLAGSHIP_SPEC.md` | 22 | `span_1` | `end_span` | `docs/end_span` | **BROKEN** | Remove malformed `[span_1](end_span)` markup tag. |
| `docs/SOMMER_FLAGSHIP_SPEC.md` | 32 | `span_2` | `start_span` | `docs/start_span` | **BROKEN** | Remove malformed `[span_2](start_span)` markup tag or convert to superscript citation `[^3]`. |
| `docs/SOMMER_FLAGSHIP_SPEC.md` | 32 | `span_2` | `end_span` | `docs/end_span` | **BROKEN** | Remove malformed `[span_2](end_span)` markup tag. |

---

## 3. Directory Map & INDEX.md Consistency

### Orphan Files (Exist in repository, but NOT listed in `INDEX.md`) — 29 Files Total

The repository has expanded significantly beyond the original 26 files listed in `INDEX.md`. The following 29 files are missing from `INDEX.md`:

| Category / Directory | File Path | Status / Notes |
|----------------------|-----------|----------------|
| **Core Architecture** | `01_Core_Architecture_Protocols/Cluster_Link_System_Specification.md` | Added specification, missing from `INDEX.md` |
| **Compliance & Legal** | `03_Compliance_Legal/IP_Anti_Counterfeiting_Protocol.md` | Added protocol, missing from `INDEX.md` |
| **Root Documents** | `README.md` | Repository root documentation |
| **Root Documents** | `INDEX.md` | Repository index itself |
| **Root Audits** | `AUDIT_1_Technical_Parity.md` | Audit report file |
| **Root Audits** | `AUDIT_2_Legal_Alignment.md` | Audit report file |
| **Root Audits** | `AUDIT_3_Reference_Integrity.md` | Audit report file |
| **Root Audits** | `AUDIT_4_Deployment_Config.md` | Audit report file |
| **Extended Specs (`docs/`)** | `docs/DECEMBER_10_LEDGER_SPEC.md` | Dividend pool specification |
| **Extended Specs (`docs/`)** | `docs/PLANETARY_SHIELD_SPEC.md` | Biosafety protocol specification |
| **Extended Specs (`docs/`)** | `docs/SOMMER_FLAGSHIP_SPEC.md` | Flagship deployment specification |
| **Extended Specs (`docs/`)** | `docs/SUPPORT_PROTOCOL_SPEC.md` | Support obligation specification |
| **Engine Code (`docs/`)** | `docs/active_inference_engine.py` | Python active inference engine |
| **Workers (`docs/`)** | `docs/bdtComplianceWorker.js` | Cloudflare worker script |
| **Workers (`docs/`)** | `docs/dec10LedgerWorker.js` | Cloudflare worker script |
| **Workers (`docs/`)** | `docs/pdtInferenceWorker.js` | Cloudflare worker script |
| **Workers (`docs/`)** | `docs/planetaryShieldWorker.js` | Cloudflare worker script |
| **Patent SVGs (`patent/diagrams/`)** | `patent/diagrams/FIG_1_System_Architecture.svg` | Formal patent figure 1 |
| **Patent SVGs (`patent/diagrams/`)** | `patent/diagrams/FIG_2_Active_Inference_Circuit_Breaker.svg` | Formal patent figure 2 |
| **Patent SVGs (`patent/diagrams/`)** | `patent/diagrams/FIG_3_Spatial_Rule_Matcher.svg` | Formal patent figure 3 |
| **Patent SVGs (`patent/diagrams/`)** | `patent/diagrams/FIG_4_Surplus_Accrual_Timeline.svg` | Formal patent figure 4 |
| **Patent SVGs (`patent/diagrams/`)** | `patent/diagrams/FIG_5_Biosecurity_Escalation_Cascade.svg` | Formal patent figure 5 |
| **Patent SVGs (`patent/diagrams/`)** | `patent/diagrams/FIG_6_ZK_CPR_NemRefusion_Bridge.svg` | Formal patent figure 6 |
| **Patent SVGs (`patent/diagrams/`)** | `patent/diagrams/FIG_7_CE_Compliance_Interception_Gate.svg` | Formal patent figure 7 |
| **Patent SVGs (`patent/diagrams/`)** | `patent/diagrams/FIG_8_Planetary_Shield_Council_Interoperability.svg` | Formal patent figure 8 |
| **Patent SVGs (`patent/diagrams/`)** | `patent/diagrams/FIG_9_HITL_Level_2_Override_Workflow.svg` | Formal patent figure 9 |
| **Patent Scripts (`patent/`)** | `patent/generate_diagrams.py` | Diagram generation script |
| **Prototypes (`prototype/`)** | `prototype/tone_pipeline.py` | Core TONE interpreter v1 |
| **Prototypes (`prototype/`)** | `prototype/tone_pipeline_v2.py` | Core TONE interpreter v2 |
| **Backend Functions (`prototype/`)** | `prototype/backend_functions/README.md` | Base44 function README |
| **Backend Functions (`prototype/`)** | `prototype/backend_functions/computeDailySurplus.ts` | Daily surplus function |
| **Backend Functions (`prototype/`)** | `prototype/backend_functions/supportObligationRuleMatcher.ts` | Compliance matcher function |

### Phantom Files (In `INDEX.md`, but do NOT exist in repository) — 0 Files
- **None.** All 26 files listed in `INDEX.md` physically exist in the repository.

---

## 4. Cross-Reference Consistency Analysis

1. **Patent Specification ⇄ `DIAGRAMS_DESCRIPTION.md`**:
   - **Status:** **VERIFIED**.
   - **Details:** `patent/TONE_PATENT_SPECIFICATION.md` references Figures 1 through 9. `patent/DIAGRAMS_DESCRIPTION.md` describes Figures 1 through 9. `patent/CLAIMS_DRAFT.md` defines Claims 1–15, which map to Figures 1–9.

2. **Symmetrical Protocol ⇄ L-LEG Spec**:
   - **Status:** **INCONSISTENT (UNIDIRECTIONAL)**.
   - **Details:** `01_Core_Architecture_Protocols/Symmetrical_Governmental_Support_Protocol.md` (Line 414) explicitly references `L-LEG_Living_Legal_Operating_System.md`. However, `03_Compliance_Legal/L-LEG_Living_Legal_Operating_System.md` does **not** reference the Symmetrical Governmental Support Protocol.
   - **Fix:** Add a cross-reference section in `L-LEG_Living_Legal_Operating_System.md` mapping the Rule Compass to the Symmetrical Support Protocol.

3. **Compliance Book ⇄ L-LEG Spec**:
   - **Status:** **VERIFIED (BIDIRECTIONAL)**.
   - **Details:** `By_Sommer_Compliance_Book_Consolidated.md` references L-LEG as its underlying legal OS, and `L-LEG_Living_Legal_Operating_System.md` explicitly references the Compliance Book.

4. **SommerCoPilot Blueprint ⇄ TONE Pipeline**:
   - **Status:** **VERIFIED**.
   - **Details:** `SommerCoPilot_Blueprint_Consolidated.md` integrates the TONE contract protocol (Light Tone / EXPAND mode) and references the TONE interpreter pipeline.

5. **Backend Function README ⇄ Implementation & Entities**:
   - **Status:** **INCONSISTENT**.
   - **Details:** `prototype/backend_functions/README.md` documents the `SupportObligationRules` entity used by `supportObligationRuleMatcher.ts`, but fails to document the `SommerUsers` entity (and `dec_10_surplus_pool_dkk` field) used by `computeDailySurplus.ts`.
   - **Fix:** Update `prototype/backend_functions/README.md` to include a Database Schema section for `SommerUsers`.

6. **Missing Prototype Code Reference**:
   - **Status:** **BROKEN REFERENCE IN TEXT**.
   - **Details:** Line 312 of `01_Core_Architecture_Protocols/Cluster_Link_System_Specification.md` cites `prototype/cls_mesh_simulator.py` as an existing script, but that file does **not** exist in `prototype/`.
   - **Fix:** Create `prototype/cls_mesh_simulator.py` or mark the reference as planned/conceptual in `Cluster_Link_System_Specification.md`.

7. **Root Path Prefix in Specification Header**:
   - **Status:** **MINOR PATH FORMATTING ISSUE**.
   - **Details:** Line 8 of `01_Core_Architecture_Protocols/Cluster_Link_System_Specification.md` lists `Target Path: bysommer_archive/01_Core_Architecture_Protocols/...` including the root repository name.
   - **Fix:** Normalize to relative path `01_Core_Architecture_Protocols/Cluster_Link_System_Specification.md`.

---

## 5. Superseded Document Notice

- **Target File:** `01_Core_Architecture_Protocols/TONE_Patent_Draft_Filing_Structured.md`
- **Status:** **VERIFIED**.
- **Header Status:** `Status: SUPERSEDED — See /patent/ for canonical version`
- **Banner Content:**
  > **⚠️ NOTICE: SUPERSEDED DOCUMENT**  
  > This document contains an earlier iteration of the TONE patent claims... The canonical, production-enabling patent portfolio is formally maintained under `/patent/`...
- **Target Links:**
  - `[`/patent/`](../patent/)` → Valid
  - `[`/patent/CLAIMS_DRAFT.md`](../patent/CLAIMS_DRAFT.md)` → Valid
  - `[`/patent/TONE_PATENT_SPECIFICATION.md`](../patent/TONE_PATENT_SPECIFICATION.md)` → Valid
  - `[`/patent/DIAGRAMS_DESCRIPTION.md`](../patent/DIAGRAMS_DESCRIPTION.md)` → Valid

---

## 6. SVG File Links in `DIAGRAMS_DESCRIPTION.md`

- **Target File:** `patent/DIAGRAMS_DESCRIPTION.md`
- **Status:** **VERIFIED**.
- **Details:** Drawing Index table contains valid relative links for all 9 figures. All 9 SVG files exist in `patent/diagrams/`:
  1. `diagrams/FIG_1_System_Architecture.svg` — Exists
  2. `diagrams/FIG_2_Active_Inference_Circuit_Breaker.svg` — Exists
  3. `diagrams/FIG_3_Spatial_Rule_Matcher.svg` — Exists
  4. `diagrams/FIG_4_Surplus_Accrual_Timeline.svg` — Exists
  5. `diagrams/FIG_5_Biosecurity_Escalation_Cascade.svg` — Exists
  6. `diagrams/FIG_6_ZK_CPR_NemRefusion_Bridge.svg` — Exists
  7. `diagrams/FIG_7_CE_Compliance_Interception_Gate.svg` — Exists
  8. `diagrams/FIG_8_Planetary_Shield_Council_Interoperability.svg` — Exists
  9. `diagrams/FIG_9_HITL_Level_2_Override_Workflow.svg` — Exists

---

## 7. Recommended Fixes Action Plan

1. **Fix Broken Links in `docs/SOMMER_FLAGSHIP_SPEC.md`**:
   - Clean up lines 21, 22, and 32 by removing `[span_0](start_span)`, `[span_0](end_span)`, etc.

2. **Update `INDEX.md`**:
   - Expand `INDEX.md` to include all 29 orphan files across `01_Core_Architecture_Protocols/`, `03_Compliance_Legal/`, `docs/`, `patent/diagrams/`, and `prototype/`. Update header file count from 25 to 55 files.

3. **Make L-LEG ⇄ Symmetrical Protocol Cross-Reference Bidirectional**:
   - Add a cross-reference entry in `03_Compliance_Legal/L-LEG_Living_Legal_Operating_System.md` under section 6 ("Related Documents") pointing to `01_Core_Architecture_Protocols/Symmetrical_Governmental_Support_Protocol.md`.

4. **Update `prototype/backend_functions/README.md`**:
   - Add schema documentation for the `SommerUsers` entity and its `dec_10_surplus_pool_dkk` field used by `computeDailySurplus.ts`.

5. **Address Missing `prototype/cls_mesh_simulator.py` Reference**:
   - Add a placeholder/prototype Python script `prototype/cls_mesh_simulator.py` or mark it as conceptual in `01_Core_Architecture_Protocols/Cluster_Link_System_Specification.md`.

---

*Audit performed by: Deployment Readiness Audit Sub-Agent*  
*Date: 06 August 2026*
