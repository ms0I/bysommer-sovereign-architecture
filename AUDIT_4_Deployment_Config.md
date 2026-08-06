# AUDIT REPORT 4: Environment & Deployment Configuration Readiness
**Target System:** By Sommer Sovereign Intelligence Architecture (TONE)  
**Audit Date:** August 6, 2026  
**Auditor:** Automated System Audit Agent  
**Scope:** Verification of Environment Variables, Database Connection Specs, API Mock Hooks, Deployment Environment Setup, and Master Specification Completeness for Zero-Friction Deployment.  
**Repository Location:** `bysommer_archive/`

---

## Executive Summary

An exhaustive audit of the **By Sommer TONE Architecture** repository was conducted to assess its readiness for zero-friction deployment. The audit evaluated 13 core files across system specifications, deployment roadmaps, backend functions, and edge worker prototypes.

### Core Finding
The repository exhibits **high-level conceptual sophistication**, but is **NOT currently ready for zero-friction deployment**. A developer attempting to deploy the system today would be forced to make numerous guesses regarding environment variables, entity schema naming conventions, database permission models, external API mocks, scheduled workflow triggers, and deployment steps.

### Deployment Readiness Scorecard Summary
* **Environment Variables & Secrets Management:** `1.5 / 5.0` (Critical Gap: Zero process.env usage or .env documentation; all parameters hardcoded)
* **Entity Schema & Database Specifications:** `2.0 / 5.0` (Incomplete: Disconnect between Base44 SDK entity names and legacy snake_case table names; field name mismatches; 0 RLS documentation)
* **External API Integrations & Mocks:** `2.0 / 5.0` (Partial: 4 of 6 external integrations lack mock stubs or API specifications)
* **Deployment Infrastructure & Automation:** `1.5 / 5.0` (Critical Gap: No local setup guides, no Base44 deployment CLI specs, no Docker container definitions, no CI/CD pipelines)
* **Master Spec Completeness (`SOMMER_FLAGSHIP_SPEC.md`):** `2.0 / 5.0` (Incomplete: Missing backend function listings, scheduled cron definitions, dashboard views, and test scenarios)
* **Overall Composite Deployment Score:** **`1.8 / 5.0` (UNPREPARED FOR DEPLOYMENT)**

---

## 1. Environment Variables & Secrets Configuration Audit

### 1.1 Documented vs. Implemented Environment Variables
A repository-wide inspection was conducted for environment variable patterns (`process.env`, `os.getenv`, `os.environ`, `.env` files, API keys, tokens, or vault secrets references).

* **Documented List of Required Environment Variables:** **ABSENT**. Neither `SOMMER_FLAGSHIP_SPEC.md`, `README.md`, nor `prototype/backend_functions/README.md` documents a single required environment variable.
* **Non-Production Defaults:** **ABSENT in documentation**. Non-production defaults exist solely as **hardcoded literals** inside source code files.
* **Secrets Handling Patterns:** **UNDOCUMENTED**. While `CADA_Sovereignty_Execution_Roadmap.md` discusses hardware-backed HSMs and hardware vaults for CADA sovereignty levels, application-level secret management patterns (e.g., Base44 Secret Manager, `.env.example`, JWT signing keys) are not specified.
* **Flagged Code vs. Spec Discrepancies:**
  * **Env vars referenced in code but not documented:** `0` (Source code files contain **zero calls** to `process.env` or `os.getenv`; all API endpoints, coordinates, thresholds, and economic rates are hardcoded).
  * **Env vars documented but not used in code:** `0` (Documentation does not mention any environment variables).

### 1.2 Table 1: Inventory of Implicit/Hardcoded Configuration Parameters Requiring Extraction to Environment Variables

To achieve zero-friction deployment, all hardcoded configuration parameters found in source code must be extracted into environment variables:

| Parameter / Variable Name | Description | Required | Default / Mock Value | Source File Reference |
| :--- | :--- | :---: | :--- | :--- |
| `BASE44_APP_URL` | Base44 Application Base Endpoint URL | **Yes** | `https://solas-7221afc1.base44.app` | `prototype/backend_functions/README.md:68`, `supportObligationRuleMatcher.ts:15`, `computeDailySurplus.ts:19` |
| `NON_PROFIT_BASELINE_DKK` | Monthly non-profit cost baseline | **Yes** | `225.0` | `computeDailySurplus.ts:38`, `dec10LedgerWorker.js:7` |
| `ESTIMATED_DAILY_OPERATING_COST_DKK` | Estimated daily system operating cost | **Yes** | `5.20` | `computeDailySurplus.ts:40`, `dec10LedgerWorker.js:8` |
| `DEFAULT_CITIZEN_LAT` | Fallback latitude coordinate for reverse geocoding | No | `55.6761` (København) | `supportObligationRuleMatcher.ts:48` |
| `DEFAULT_CITIZEN_LNG` | Fallback longitude coordinate for reverse geocoding | No | `12.5683` (København) | `supportObligationRuleMatcher.ts:48` |
| `DAWA_API_URL` | Danish Address Web API Endpoint | No | `https://dawa.aws.dk/kommuner` | `supportObligationRuleMatcher.ts:31` |
| `FLAT_CUSTOMS_DUTY_EUR` | EU 2026 Customs Reform flat duty per HS code | **Yes** | `3.00` | `bdtComplianceWorker.js:8` |
| `EUR_TO_DKK_RATE` | Currency conversion rate (EUR to DKK) | **Yes** | `7.46` | `bdtComplianceWorker.js:9` |
| `MONTHLY_MAINTENANCE_CAP_DKK` | Household asset twin monthly maintenance cap | No | `250.00` | `SOMMER_FLAGSHIP_SPEC.md:19`, `bdtComplianceWorker.js:10` |
| `ACTIVE_INFERENCE_ANOMALY_THRESHOLD` | Free energy divergence threshold for biological anomaly | **Yes** | `4.5` (JS Worker) / `2.5` (Python Engine) | `pdtInferenceWorker.js:23`, `active_inference_engine.py:27` |
| `WHO_WEBHOOK_SECRET` | Secret token/signature key for WHO telemetry authentication | **Yes** | *Missing* (Evaluated as `who_authenticated` boolean) | `planetaryShieldWorker.js:6` |
| `SNET_AUDIT_LOG_ENDPOINT` | s.net immutable decision ledger endpoint | No | *Hardcoded boolean* (`logged_to_snet: true`) | `supportObligationRuleMatcher.ts:221` |

---

## 2. Database Connection Specs & Entity Engine Audit

The system relies on Base44's native Entity Engine. However, a major architectural disconnect exists between the flagship specification, the Deno TypeScript backend functions, and the JavaScript worker files in `docs/`.

### 2.1 Table 2: Entity Schema Verification & Field Match Matrix

| Entity Name (Spec / SDK) | Fields in `SOMMER_FLAGSHIP_SPEC.md` | Fields in Source Code Files | Match Status | Discrepancies & Gaps |
| :--- | :--- | :--- | :---: | :--- |
| **`users`** / **`SommerUsers`** | `id`, `name`, `email`, `role`, `cpr_zk_hash`, `true_discretionary_income_dkk`, `dec_10_surplus_pool_dkk` | `role`, `name`, `dec_10_surplus_pool_dkk`, `true_discretionary_income_dkk`, `id` | **MISMATCH** | **Entity Name Mismatch:** Flagship spec and `dec10LedgerWorker.js` call it `users`. TS backend function `computeDailySurplus.ts` calls it `SommerUsers`. `cpr_zk_hash` and `email` missing in TS update calls. |
| **`pdt_active_inference_states`** / **`PdtActiveInferenceStates`** | `id`, `user_id`, `physiological_baseline`, `active_inference_delta`, `anomaly_flag` | `user_id`, `baseline_telemetry`, `active_inference_delta`, `anomaly_flag` | **MISMATCH** | **Field Name Mismatch:** Flagship spec specifies `physiological_baseline`. Worker script `pdtInferenceWorker.js` writes `baseline_telemetry`. Missing PascalCase SDK entity definition. |
| **`support_obligation_rules`** / **`SupportObligationRules`** | `id`, `jurisdiction`, `trigger_criteria`, `entitlement_text`, `obligation_reservation_text`, `is_active` | `is_active`, `jurisdiction`, `trigger_criteria`, `entitlement_text`, `obligation_reservation_text` | **MATCH** | **Field Alignment Correct.** However, spec uses snake_case (`support_obligation_rules`) whereas SDK code uses PascalCase (`SupportObligationRules`). |
| **`bdt_transactions`** / **`BdtTransactions`** | `id`, `business_id`, `buyer_id`, `total_amount_dkk`, `vat_rate_applied`, `compliance_status`, `timestamp` | `id`, `compliance_status`, `total_dkk`, `vat_rate` | **MISMATCH** | **Severe Field Discrepancy:** Code uses `total_dkk` instead of `total_amount_dkk`, and `vat_rate` instead of `vat_rate_applied`. Code omits `business_id`, `buyer_id`, and `timestamp`. |
| **`planetary_council_telemetry`** / **`PlanetaryCouncilTelemetry`** | `id`, `alert_status`, `pathogen_r0_vector`, `who_approved`, `affected_geographies` | `alert_status`, `pathogen_r0_vector`, `who_approved`, `affected_geographies` | **MATCH** | **Field Alignment Correct.** Naming convention mismatch (snake_case in spec/worker vs PascalCase required for SDK). |

### 2.2 Connection Pattern & Access Syntax Verification
* **TypeScript SDK Pattern (`prototype/backend_functions/*.ts`):** Uses modern Base44 SDK syntax:
  ```typescript
  import { createClientFromRequest } from 'npm:@base44/sdk@0.8.31';
  const base44 = createClientFromRequest(req);
  const rules = await base44.entities.SupportObligationRules.list({});
  ```
* **JavaScript Worker Pattern (`docs/*.js`):** Uses an outdated / mock MongoDB-style syntax:
  ```javascript
  await base44.db.bdt_transactions.create({...});
  const users = await base44.db.users.findMany();
  ```
* **Service Role Access Pattern (`base44.asServiceRole`):** **UNDOCUMENTED & UNIMPLEMENTED**.
  * Scheduled cron functions (such as `computeDailySurplus.ts` and `dec10LedgerWorker.js`) iterate over and update all user records across the tenant.
  * In Base44, unauthenticated background tasks or cross-user cron jobs require service role privileges (`base44.asServiceRole.entities.SommerUsers.list()`).
  * Neither code nor documentation references or utilizes `asServiceRole`, which will cause permission errors when RLS is enforced.

### 2.3 Row-Level Security (RLS) Settings
* **RLS Documentation Status:** **0% Documented**.
* None of the 5 entity schemas in `SOMMER_FLAGSHIP_SPEC.md` or any deployment guide specify Row-Level Security policies.
* **Missing Security Specs:** No definitions exist for citizen self-read/write rules, BDT merchant access rules, or regulator/council audit privileges.

---

## 3. External API Integrations & Mock Hooks Audit

The system architecture specifies integrations with six major Danish and European external platforms.

### 3.1 Table 3: External Integration Readiness & Mock Availability Matrix

| External System / Integration | Documented in Specs | Mock / Stub Provided | Auth Requirements Documented | Readiness Status | Summary & Missing Artefacts |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **1. Virk.dk API** (Danish Business Authority) | Conceptual | **No** | No | **CRITICAL GAP** | Mentioned in NAS interface diagrams (`BDT ⇄ NAS (Virk, SKAT, MitID)`). No API lookup stub, CVR verification function, or auth spec provided. |
| **2. SKAT API** (Danish Tax Agency) | Conceptual | Partial | No | **CRITICAL GAP** | Internal VAT math (25% standard / reduced rates) implemented in TS/JS. However, no SKAT API submission endpoints, TastSelv auth, or mock hooks exist. |
| **3. NemRefusion API** (Municipal Sick Leave) | Conceptual | **No** | No | **CRITICAL GAP** | Patent Claim 8 and `FIG_6` describe a ZK-CPR NemRefusion bridge. No API endpoint schemas, payload definitions, or mock stubs exist in code. |
| **4. EUR-Lex API** (EU Legal Rule Updates) | Conceptual | **No** | No | **CRITICAL GAP** | Union tier rule ingestion referenced in specifications. No CELLAR SPARQL/REST endpoint stubs, parser scripts, or auth specs exist. |
| **5. EU IOSS/OSS Portal** (Cross-Border VAT) | **Yes** | **Yes** | No | **PARTIAL** | Mock logic in `supportObligationRuleMatcher.ts` checks `is_cross_border`, threshold (< 1125 DKK / EUR 150), and `is_ioss_registered`. Lacks external VIES/IOSS portal auth specs. |
| **6. WHO Epidemiology API** (Pathogen $R_0$) | **Yes** | **Yes** | Partial | **PARTIAL** | `planetaryShieldWorker.js` provides a webhook handler `handlePlanetaryTelemetry` and `PLANETARY_SHIELD_SPEC.md` provides a Python engine. Auth uses a mock `who_authenticated` boolean instead of cryptographic signatures. |

---

## 4. Deployment Environment & Infrastructure Audit

### 4.1 Local Development Setup Instructions
* **Status:** **MISSING**.
* The repo contains no step-by-step instructions explaining how to set up the environment locally.
* Missing details: Node/Deno version requirements, local dependency installation (`npm install`), Deno execution commands (`deno run --allow-net`), database seeding commands, and environment variable initialization.

### 4.2 Production Deployment on Base44 Cloud
* **Status:** **INCOMPLETE / INCONSISTENT**.
* TS function header comments reference a deployed instance URL (`https://solas-7221afc1.base44.app/functions/...`).
* However, no instructions or scripts are provided explaining how to deploy backend functions to Base44 (e.g., Base44 CLI commands, dashboard upload steps, or manifest files).

### 4.3 Scheduled Job Configuration
* **Status:** **INCONSISTENT & UNDOCUMENTED**.
* **Cron Timing Mismatch:**
  * `computeDailySurplus.ts` header specifies: `Scheduled via Base44 Workflow: daily at 09:00 Europe/Copenhagen`.
  * `dec10LedgerWorker.js` header specifies: `Scheduled: Every day at 00:00 UTC`.
* **Missing Workflow Trigger Definition:** Neither `SOMMER_FLAGSHIP_SPEC.md` nor any configuration file provides the JSON/YAML workflow definition or trigger specification required to configure this scheduled job in Base44.

### 4.4 Runtime Architecture Mismatch
* **Status:** **SPLIT RUNTIME**.
* Prototype functions in `prototype/backend_functions/` are written for the **Deno runtime** using ES modules and `@base44/sdk@0.8.31`.
* Worker functions in `docs/` are written as **Node.js Express-style handlers** (`export async function handleX(req, res)`).
* No build pipeline or unified runtime configuration exists to deploy these two disparate paradigms.

### 4.5 Docker & Containerization Specs
* **Status:** **MISSING**.
* `Sovereign_Layer_Architecture_Specification.md` line 189 references a *"Sandboxed execution environment (containerized, per-tone scope)"*.
* However, no `Dockerfile`, `docker-compose.yml`, or container configuration files exist in the repository.

### 4.6 CI/CD Pipeline
* **Status:** **MISSING**.
* `CADA_Sovereignty_Execution_Roadmap.md` discusses automated compliance pipelines and attestation standards.
* However, no GitHub Actions workflows (`.github/workflows/`), GitLab CI definitions, or automated testing/deployment scripts exist.

---

## 5. Master Specification Completeness Audit (`SOMMER_FLAGSHIP_SPEC.md`)

`SOMMER_FLAGSHIP_SPEC.md` is designated as the master specification v2.0 for the flagship release. It was audited against the five mandatory deployment components:

| Requirement Area | Present in Flagship Spec? | Evaluation & Specific Deficiencies |
| :--- | :---: | :--- |
| **1. Full Entity Schema** | **Partial** | Documents 5 tables (`users`, `pdt_active_inference_states`, `support_obligation_rules`, `bdt_transactions`, `planetary_council_telemetry`). **Deficiencies:** Naming uses snake_case instead of PascalCase; field names conflict with worker code; field data types omit Base44 native primitives; primary/foreign keys and RLS policies are missing. |
| **2. Backend Functions & Config** | **NO** | **0% Present.** Does not list `supportObligationRuleMatcher`, `computeDailySurplus`, or worker functions. Provides zero deployment endpoints, HTTP verbs, or runtime requirements. |
| **3. Scheduled Job Config** | **NO** | **0% Present.** Mentions the December 10th dividend concept, but omits the daily 09:00 Copenhagen cron job specification, execution handler, and retry parameters. |
| **4. Four Dashboard Views** | **NO** | **0% Present.** Fails to document the 4 required governance dashboard views (Citizen Surplus Portal, BDT Compliance Sentinel, PDT Active Inference Monitor, Planetary Shield Command Center). |
| **5. Test Scenarios & Results** | **NO** | **0% Present.** Contains no sample test payloads, expected HTTP response bodies, or verification scenarios. |

---

## 6. Deployment Readiness Scorecard

| Dimension | Rating (1-5) | Key Justification |
| :--- | :---: | :--- |
| **1. Environment Variables & Secrets** | **1.5 / 5.0** | Zero `process.env` calls or `.env` templates. All endpoints, rates, coordinates, and thresholds are hardcoded in source files. |
| **2. Database Schema & Entity Specs** | **2.0 / 5.0** | Disconnect between Base44 SDK entity names (`SommerUsers`, `SupportObligationRules`) and spec table names (`users`, `support_obligation_rules`). Field name mismatches (`total_amount_dkk` vs `total_dkk`). Zero RLS policies documented. Unimplemented `asServiceRole`. |
| **3. External API Integrations & Mocks** | **2.0 / 5.0** | Stubs/mocks exist for IOSS and WHO telemetry, but Virk.dk, SKAT, NemRefusion, and EUR-Lex lack API specs and mock hooks. Auth is unauthenticated or mock boolean. |
| **4. Deployment Infrastructure & Automation** | **1.5 / 5.0** | Missing local setup guide, Base44 CLI deployment specs, Dockerfiles, and CI/CD pipelines. Mismatch in scheduled job execution timing (09:00 Copenhagen vs 00:00 UTC). |
| **5. Master Spec Completeness (`FLAGSHIP_SPEC`)** | **2.0 / 5.0** | Flagship spec lacks backend function registry, cron trigger specs, dashboard views, and test execution scenarios. |
| **OVERALL COMPOSITE SCORE** | **`1.8 / 5.0`** | **NOT DEPLOYMENT READY.** Requires mandatory configuration, schema alignment, and documentation remediation prior to release. |

---

## 7. Recommended Fixes & Actionable Remediation Plan

### Priority 1: Critical Deployment Blockers (Immediate Action Required)
1. **Create `.env.example` and Extract Configuration Parameters:**
   * Remove all hardcoded URLs, thresholds, currency rates, and coordinates from `supportObligationRuleMatcher.ts`, `computeDailySurplus.ts`, and `docs/*.js`.
   * Implement environment variable access using Deno/Node stdlib (`Deno.env.get()` / `process.env`).
2. **Standardize Base44 Entity Access & Implement Service Role Access:**
   * Migrate all `docs/*.js` worker files to use `@base44/sdk@0.8.31` entity syntax (`base44.entities.EntityName`).
   * Update `computeDailySurplus.ts` and `dec10LedgerWorker.js` to execute using `base44.asServiceRole.entities.SommerUsers` to bypass user-level RLS restrictions during background cron runs.
3. **Resolve Field Name & Entity Naming Mismatches:**
   * Align `bdtComplianceWorker.js` and flagship spec: change `total_dkk` to `total_amount_dkk`, and `vat_rate` to `vat_rate_applied`.
   * Align `pdtInferenceWorker.js` and flagship spec: change `baseline_telemetry` to `physiological_baseline`.
   * Standardize all SDK references to PascalCase (`SommerUsers`, `PdtActiveInferenceStates`, `SupportObligationRules`, `BdtTransactions`, `PlanetaryCouncilTelemetry`).

### Priority 2: Master Specification Consolidation
1. **Update `SOMMER_FLAGSHIP_SPEC.md` to Version 2.1:**
   * Add Section 3.1: **Row-Level Security (RLS) Policies** per entity.
   * Add Section 5: **Backend Functions & API Registry** documenting endpoints, parameters, runtimes, and deployment config.
   * Add Section 6: **Scheduled Jobs & Workflow Triggers** defining the 09:00 Europe/Copenhagen cron trigger in Base44 workflow format.
   * Add Section 7: **Governance Dashboard Views** defining the 4 core UI views.
   * Add Section 8: **End-to-End Test Scenarios & Verification Payload Suite**.

### Priority 3: External Integration Stubs & Security
1. **Implement Missing External API Mock Hooks:**
   * Create mock handlers for Virk.dk (CVR lookup), SKAT (Tax/VAT filing), NemRefusion (Sick leave ZK proof submission), and EUR-Lex (Legal rule sync).
2. **Upgrade Webhook Security:**
   * Replace the `who_authenticated` boolean flag in `planetaryShieldWorker.js` with HMAC signature verification (`x-who-signature` header) backed by a secret key stored in environment variables.

### Priority 4: Infrastructure & CI/CD Automation
1. **Create Deployment & Local Quickstart Documentation:**
   * Add `docs/DEPLOYMENT_GUIDE.md` with step-by-step commands for local setup (`deno task start`), database seeding (`deno run scripts/seed.ts`), and Base44 CLI cloud deployment commands.
2. **Provide Docker & CI/CD Artefacts:**
   * Add a root `Dockerfile` and `docker-compose.yml` for local containerized development.
   * Add `.github/workflows/deploy.yml` to automate linting, type-checking, and automated deployment to Base44.
