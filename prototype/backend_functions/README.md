# BDT+ Compliance Engine — Location-Aware Rule Matching

## Overview

The `supportObligationRuleMatcher` is a location-aware compliance engine that implements the SOMMER Compliance Book's three-tier jurisdictional filtering architecture. It determines which legal rules apply to a given transaction based on the physical location of the citizen, applying a **stricter-rule-wins** conflict resolution principle.

## Architecture

```
Citizen Request (user_id)
       │
       ▼
┌──────────────────────────┐
│  1. Location Telemetry   │  ← PDT GPS or device telemetry
│  (lat/long coordinates)   │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│  2. Reverse Geocode       │  ← DAWA API in production
│  → Danish Kommune         │     (mock lookup in prototype)
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│  3. Jurisdiction Filter   │  EU + NATIONAL_DK + MUNICIPAL_<code>
│  (three-tier hierarchy)   │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│  4. Rule Matching         │  IOSS · VAT · CE Marking ·
│  (compliance checks)      │  Env Zone · Noise · Water Quality
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│  5. Compliance Verdict    │  VALIDATED | PENDING_IOSS | BLOCKED
│  + Advisory Class (I-IV) │
│  + s.net audit log entry  │
└──────────────────────────┘
```

## Jurisdiction Hierarchy

| Tier | Jurisdiction Format | Scope | Example Rules |
|------|-------------------|-------|---------------|
| 1 (Supranational) | `EU` | Cross-border B2C | IOSS threshold (EUR 150) |
| 2 (National) | `NATIONAL_DK` | Country-wide | VAT 25% standard, 12% reduced |
| 3 (Municipal) | `MUNICIPAL_<KOMMUNE_CODE>` | Local kommune | Environmental zones, noise ordinances, water quality |

**Conflict Resolution:** Stricter-rule-wins. Municipal overrides national, national overrides EU. Core ethical constraints are inviolable in all jurisdictions.

## Seeded Municipal Rules

### Aarhus (MUNICIPAL_AARHUS)
- **Environmental Zone (ULEZ):** Euro 6+ diesel required in inner ring. Fine: 1,500 DKK.
- **PDT+ block:** Vehicle twin must verify emissions class before entering zone.

### København (MUNICIPAL_KOBENHAVN)
- **Noise Ordinance:** Construction/delivery 07:00-18:00 weekdays, 09:00-15:00 Saturday. No Sunday.
- **Harbor Bathing Zone:** Water quality monitored at 14 stations. Swimming blocked when E. coli > 500 CFU/100ml. Linked to Planetary Shield biosafety protocol.

## API Reference

### Endpoint
```
POST https://solas-7221afc1.base44.app/functions/supportObligationRuleMatcher
```

### Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | Citizen ID (triggers location telemetry) |
| `buyer_id` | string | No | Defaults to `user_id` |
| `business_id` | string | No | Business entity ID |
| `total_amount_dkk` | number | Yes | Transaction amount in DKK |
| `vat_rate_applied` | number | Yes | VAT rate (0.0 - 1.0) |
| `product_category` | string | No | e.g. "electronics", "food", "construction" |
| `has_ce_marking` | boolean | No | CE compliance for regulated categories |
| `is_cross_border` | boolean | No | Triggers IOSS check |
| `is_ioss_registered` | boolean | No | IOSS registration status |

### Response

| Field | Description |
|-------|-------------|
| `compliance_status` | `VALIDATED` \| `PENDING_IOSS` \| `BLOCKED_MISSING_CE` |
| `matched_rules` | Array of all applicable rules with jurisdiction |
| `advisory_class` | `I` (pass) \| `II` (pending) \| `III` (blocked) |
| `jurisdiction_context` | Per-layer rule counts + municipality info |
| `location_telemetry` | Coordinates, municipality name/code, rules loaded |
| `logged_to_snet` | Immutable decision ledger entry flag |

## Database Schema

Entity: `SupportObligationRules`

| Field | Type | Description |
|-------|------|-------------|
| `jurisdiction` | string | `EU`, `NATIONAL_DK`, or `MUNICIPAL_<CODE>` |
| `entitlement_text` | string | Human-readable rule description |
| `obligation_reservation_text` | string | Enforcement reservation |
| `trigger_criteria` | object | Machine-readable conditions (type, thresholds) |
| `is_active` | boolean | Rule active flag |

Rule registry is **append-only** (superseded, not deleted) for full audit traceability.
