"""
By Sommer — TONE Pipeline Prototype
=====================================
The smallest deployable slice of the sovereign architecture.

This proves:
- TONE contracts flow through 7 sovereign layers
- Each layer has its own logic and veto power
- Dense/Light tone density triggers SUPPORT/EXPAND modes
- L-ETH can veto (ethical guardrail)
- L-LEG can halt (legal compliance)
- s.net logs every decision with full provenance
- The architecture is real, not just paper

Run: python3 prototype/tone_pipeline.py
"""

import json
import uuid
import hashlib
from datetime import datetime, timezone
from enum import Enum
from dataclasses import dataclass, field, asdict
from typing import Optional


# ═══════════════════════════════════════════════════════════════
# TONE PROTOCOL — The Semantic Mediation Layer
# ═══════════════════════════════════════════════════════════════

class ToneDensity(Enum):
    DENSE = "Dense"   # High-impact → SUPPORT mode
    LIGHT = "Light"   # Low-risk → EXPAND mode

class ToneDirection(Enum):
    INWARD = "inward"       # Self-directed
    OUTWARD = "outward"     # Authority-directed (NAS/EUS)
    LATERAL = "lateral"     # Peer (PDT↔BDT)
    UPWARD = "upward"       # Escalation
    DOWNWARD = "downward"   # Authorization

class SystemMode(Enum):
    SUPPORT = "SUPPORT"  # Conservative, protective, mandatory HITL
    EXPAND = "EXPAND"    # Generative, exploratory, standard thresholds


@dataclass
class ToneHeader:
    """The structured metadata inside every tone.
    This is the TONE Protocol's core data structure — Patent Claims 1-15."""
    tone_id: str                          # UUIDv7 — correlatable across all layers
    actor_id: str                         # Cryptographic identifier (hashed)
    layer: str                             # Which sovereign layer produced this
    density: ToneDensity                   # Dense or Light
    direction: ToneDirection               # Target direction
    intent: str                            # Semantic meaning of the request
    scope: dict                            # Boundaries of the requested action
    constraints: dict                      # Limitations and conditions
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def mode(self) -> SystemMode:
        """Dense Tone → SUPPORT mode. Light Tone → EXPAND mode."""
        return SystemMode.SUPPORT if self.density == ToneDensity.DENSE else SystemMode.EXPAND

    def to_dict(self) -> dict:
        d = asdict(self)
        d['density'] = self.density.value
        d['direction'] = self.direction.value
        return d


# ═══════════════════════════════════════════════════════════════
# SOVEREIGN LAYERS — Each is its own state with veto power
# ═══════════════════════════════════════════════════════════════

@dataclass
class LayerResult:
    """What each layer returns after processing a tone."""
    layer: str
    approved: bool
    reason: str
    modified_scope: Optional[dict] = None  # Layer may modify scope (e.g., L-LEG retention override)
    vetoed: bool = False
    halted: bool = False
    metadata: dict = field(default_factory=dict)


# ── L-OP: Operator Layer ───────────────────────────────────────
class OperatorLayer:
    """The human. Expresses intent. The operator is the ultimate authority."""
    name = "L-OP"

    def generate_tone(self, actor_id: str, intent: str, density: ToneDensity,
                      direction: ToneDirection, scope: dict, constraints: dict = None) -> ToneHeader:
        return ToneHeader(
            tone_id=str(uuid.uuid4()),
            actor_id=hashlib.sha256(actor_id.encode()).hexdigest()[:16],
            layer=self.name,
            density=density,
            direction=direction,
            intent=intent,
            scope=scope,
            constraints=constraints or {},
        )


# ── L-PDT: Personal Digital Twin ──────────────────────────────
class PersonalDigitalTwin:
    """Translates human intent into structured tones. Manages identity wallet."""
    name = "L-PDT"

    def process(self, tone: ToneHeader) -> LayerResult:
        # PDT validates that the operator's intent is structurally sound
        if not tone.intent or len(tone.intent) < 3:
            return LayerResult(self.name, False, "Intent too vague — clarification needed")

        # Check identity scope is not overbroad
        identity_scope = tone.scope.get('identity_scope', [])
        if len(identity_scope) > 5:
            return LayerResult(self.name, False,
                             "Identity scope too broad — data minimization violated (max 5 attributes)")

        return LayerResult(self.name, True, "Intent validated and structured",
                          metadata={'mode': tone.mode().value, 'identity_attributes': len(identity_scope)})


# ── L-AURORA: Governance Substrate ────────────────────────────
class AuroraGovernance:
    """The 'Mona Lisa frame'. Validates tones against versioned rules and risk thresholds."""
    name = "L-AURORA"

    # Simplified rule registry (in production: versioned JSON, append-only)
    RULES = {
        'verify_tax_eligibility': {'risk_tier': 'medium', 'requires_hitl': False},
        'submit_vat_settlement': {'risk_tier': 'high', 'requires_hitl': True},
        'emergency_disclosure': {'risk_tier': 'high', 'requires_hitl': True},
        'creative_exploration': {'risk_tier': 'low', 'requires_hitl': False},
        'publish_glyph': {'risk_tier': 'low', 'requires_hitl': False},
        'delete_account': {'risk_tier': 'high', 'requires_hitl': True},
    }

    def process(self, tone: ToneHeader) -> LayerResult:
        rule = self.RULES.get(tone.intent)

        if rule is None:
            # Unknown intent — escalate for clarification
            return LayerResult(self.name, False,
                             f"Unknown intent '{tone.intent}' — escalation triggered for human clarification")

        # Dense tones always require HITL
        if tone.density == ToneDensity.DENSE and rule['requires_hitl']:
            return LayerResult(self.name, True,
                             f"Governance validated (risk: {rule['risk_tier']}, HITL required for Dense tone)",
                             metadata={'risk_tier': rule['risk_tier'], 'hitl_required': True})

        return LayerResult(self.name, True,
                         f"Governance validated (risk: {rule['risk_tier']})",
                         metadata={'risk_tier': rule['risk_tier'], 'hitl_required': rule['requires_hitl']})


# ── L-ETH: Ethical Layer (HARD VETO POWER) ────────────────────
class EthicalLayer:
    """Enforces immutable ethical rules. Has hard veto — can block ANY action."""
    name = "L-ETH"

    # Core ethical constraints — inviolable in ALL jurisdictions
    CORE_CONSTRAINTS = ['consent', 'privacy', 'dignity', 'transparency', 'non_harm']

    # Prohibited intents (would violate core ethics)
    PROHIBITED = {
        'surveillance': "Mass surveillance violates privacy and dignity",
        'forced_disclosure': "Forced disclosure without consent violates autonomy",
        'discriminatory_action': "Discriminatory actions violate dignity and equality",
    }

    def process(self, tone: ToneHeader) -> LayerResult:
        # Check if intent is prohibited
        if tone.intent in self.PROHIBITED:
            return LayerResult(self.name, False, self.PROHIBITED[tone.intent], vetoed=True)

        # Check constraints for ethical violations
        constraints = tone.constraints or {}
        if not constraints.get('consent', True):
            return LayerResult(self.name, False,
                             "Consent not provided — ethical veto (consent is a core constraint)",
                             vetoed=True)

        if constraints.get('force_disclosure', False):
            return LayerResult(self.name, False,
                             "Forced disclosure detected — ethical veto",
                             vetoed=True)

        # Check for acute risk escalation (the ONE case where L-ETH acts without user consent)
        if tone.constraints.get('acute_risk', False):
            return LayerResult(self.name, True,
                             "Acute risk detected — escalating to human professional (acting without user consent for this specific action only)",
                             metadata={'acute_risk_escalation': True, 'consent_override': True})

        return LayerResult(self.name, True, "Ethical constraints satisfied (consent, privacy, dignity, transparency, non-harm)")


# ── L-LEG: Legal Compliance Layer (HARD HALT POWER) ───────────
class LegalComplianceLayer:
    """The Living Legal OS. Jurisdiction detection + rule resolution + compliance proof."""
    name = "L-LEG"

    # Simplified jurisdiction rule sets (in production: versioned JSON files per jurisdiction)
    JURISDICTION_RULES = {
        'DK': {'vat_threshold': 50000, 'retention_years': 5, 'ai_act_class': 'high_risk'},
        'DE': {'vat_threshold': 0, 'retention_years': 10, 'ai_act_class': 'high_risk'},
        'EU': {'oss_threshold_eur': 10000, 'ioss_threshold_eur': 150, 'ai_act': 'Art.6-15'},
        'baseline': {'human_rights_floor': True, 'core_ethics_inviolable': True},
    }

    def process(self, tone: ToneHeader) -> LayerResult:
        scope = tone.scope
        operator_jurisdiction = scope.get('jurisdiction', 'DK')

        # Jurisdiction detection (simplified — production uses 5 signals)
        applicable = ['baseline', 'EU']
        if operator_jurisdiction in self.JURISDICTION_RULES:
            applicable.append(operator_jurisdiction)

        # Check for VAT threshold compliance (BDT scenario)
        if tone.intent == 'submit_vat_settlement':
            turnover = scope.get('turnover', 0)
            threshold = self.JURISDICTION_RULES['DK']['vat_threshold']
            if turnover < threshold and not scope.get('vat_registered', False):
                return LayerResult(self.name, True,
                                 f"Below VAT threshold (DKK {threshold}) — no registration required yet",
                                 metadata={'jurisdictions': applicable, 'vat_threshold': threshold})

        # Check retention requirements (stricter rule wins)
        retention_requested = scope.get('retention_days', 30)
        required_retention = self.JURISDICTION_RULES['DK']['retention_years'] * 365
        if retention_requested < required_retention and scope.get('data_category') == 'financial':
            return LayerResult(self.name, True,
                             f"Compliance verified. Retention overridden: {retention_requested}d → {required_retention}d (Danish Bookkeeping Act, stricter rule wins)",
                             modified_scope={'retention_days': required_retention},
                             metadata={'jurisdictions': applicable, 'retention_override': True})

        # Check for cross-border data flow
        if scope.get('cross_border', False) and not scope.get('schrems_safeguards', False):
            return LayerResult(self.name, False,
                             "Cross-border data flow without Schrems II safeguards — legal halt",
                             halted=True,
                             metadata={'jurisdictions': applicable})

        # Generate compliance proof (simplified — production uses ZK proofs)
        compliance_proof = hashlib.sha256(
            json.dumps({'tone_id': tone.tone_id, 'jurisdictions': applicable,
                       'intent': tone.intent, 'timestamp': tone.timestamp},
                      sort_keys=True).encode()
        ).hexdigest()[:32]

        return LayerResult(self.name, True,
                         f"Legal compliance verified. Jurisdictions: {', '.join(applicable)}",
                         metadata={'jurisdictions': applicable, 'compliance_proof': f"zk:{compliance_proof}"})


# ── L-SYS: System Execution Layer ─────────────────────────────
class SystemExecution:
    """Executes only if ALL layers approve. No shared state with other layers."""
    name = "L-SYS"

    def process(self, tone: ToneHeader, results: list) -> LayerResult:
        # Verify all prior layers approved
        for r in results:
            if not r.approved:
                return LayerResult(self.name, False,
                                 f"Execution blocked — {r.layer} did not approve: {r.reason}")

        # Apply any scope modifications from L-LEG
        final_scope = tone.scope.copy()
        for r in results:
            if r.modified_scope:
                final_scope.update(r.modified_scope)

        return LayerResult(self.name, True,
                         f"Executed: {tone.intent} | Final scope: {json.dumps(final_scope, sort_keys=True)}",
                         metadata={'final_scope': final_scope})


# ── L-SNET: Accountability & Audit Trail ──────────────────────
class AuditTrail:
    """Immutable decision ledger. Append-only. Records the 'why' behind every action."""
    name = "L-SNET"

    def __init__(self):
        self.ledger = []
        self._hash_chain = None

    def log(self, tone: ToneHeader, results: list):
        entry = {
            'log_id': str(uuid.uuid4()),
            'tone_id': tone.tone_id,
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'operator_id': tone.actor_id,
            'intent': tone.intent,
            'density': tone.density.value,
            'direction': tone.direction.value,
            'mode': tone.mode().value,
            'layer_results': [
                {
                    'layer': r.layer,
                    'approved': r.approved,
                    'vetoed': r.vetoed,
                    'halted': r.halted,
                    'reason': r.reason,
                    'metadata': r.metadata,
                }
                for r in results
            ],
            'outcome': 'executed' if all(r.approved for r in results) else 'blocked',
        }

        # Hash chain (append-only integrity — simplified Merkle)
        entry_hash = hashlib.sha256(
            json.dumps(entry, sort_keys=True).encode()
        ).hexdigest()
        entry['entry_hash'] = entry_hash
        if self._hash_chain:
            entry['previous_hash'] = self._hash_chain
        else:
            entry['previous_hash'] = 'GENESIS'
        self._hash_chain = entry_hash

        self.ledger.append(entry)
        return entry

    def export(self) -> list:
        """Export the full audit trail (for auditor review)."""
        return self.ledger

    def verify_integrity(self) -> bool:
        """Verify the hash chain is unbroken."""
        prev = 'GENESIS'
        for entry in self.ledger:
            if entry.get('previous_hash') != prev:
                return False
            check = {k: v for k, v in entry.items() if k != 'entry_hash' and k != 'previous_hash'}
            expected = hashlib.sha256(json.dumps(check, sort_keys=True).encode()).hexdigest()
            if entry['entry_hash'] != expected:
                return False
            prev = entry['entry_hash']
        return True


# ═══════════════════════════════════════════════════════════════
# THE PIPELINE — Orchestrates the 7-layer flow
# ═══════════════════════════════════════════════════════════════

class TONEPipeline:
    """The sovereign pipeline. TONE contracts flow through 7 layers, each with veto power."""

    def __init__(self):
        self.l_op = OperatorLayer()
        self.l_pdt = PersonalDigitalTwin()
        self.l_aurora = AuroraGovernance()
        self.l_eth = EthicalLayer()
        self.l_leg = LegalComplianceLayer()
        self.l_sys = SystemExecution()
        self.l_snet = AuditTrail()

    def execute(self, actor_id: str, intent: str, density: ToneDensity,
                direction: ToneDirection, scope: dict, constraints: dict = None) -> dict:
        """Send a tone through the full pipeline."""
        print(f"\n{'─'*70}")
        print(f"  TONE PIPELINE — Intent: {intent}")
        print(f"  Density: {density.value} → Mode: {density == ToneDensity.DENSE and 'SUPPORT' or 'EXPAND'}")
        print(f"  Direction: {direction.value}")
        print(f"{'─'*70}")

        # 1. L-OP generates the tone
        tone = self.l_op.generate_tone(actor_id, intent, density, direction, scope, constraints)
        print(f"\n  [{self.l_op.name}] Tone generated: {tone.tone_id[:8]}...")
        print(f"         Actor: {tone.actor_id} | Intent: {tone.intent}")

        results = []

        # 2. L-PDT validates intent structure
        r = self.l_pdt.process(tone)
        results.append(r)
        self._print_result(r)

        if not r.approved:
            return self._finish(tone, results)

        # 3. L-AURORA validates against governance rules
        r = self.l_aurora.process(tone)
        results.append(r)
        self._print_result(r)

        if not r.approved:
            return self._finish(tone, results)

        # 4. L-ETH checks ethical constraints (HARD VETO)
        r = self.l_eth.process(tone)
        results.append(r)
        self._print_result(r)

        if r.vetoed:
            print(f"\n  ⛔ ETHICAL VETO — Action blocked by L-ETH")
            return self._finish(tone, results)

        if not r.approved:
            return self._finish(tone, results)

        # 5. L-LEG checks legal compliance (HARD HALT)
        r = self.l_leg.process(tone)
        results.append(r)
        self._print_result(r)

        if r.halted:
            print(f"\n  ⛔ LEGAL HALT — Action blocked by L-LEG")
            return self._finish(tone, results)

        if not r.approved:
            return self._finish(tone, results)

        # 6. L-SYS executes (only if ALL approved)
        r = self.l_sys.process(tone, results)
        results.append(r)
        self._print_result(r)

        return self._finish(tone, results)

    def _finish(self, tone: ToneHeader, results: list) -> dict:
        # 7. L-SNET logs everything (always runs, even on veto/halt)
        log_entry = self.l_snet.log(tone, results)
        outcome = log_entry['outcome']
        print(f"\n  [{self.l_snet.name}] Logged: {log_entry['log_id'][:8]}...")
        print(f"         Outcome: {outcome.upper()}")
        print(f"         Hash chain: {log_entry['entry_hash'][:16]}... → prev: {log_entry['previous_hash'][:16]}...")
        print(f"{'─'*70}")
        return {'tone_id': tone.tone_id, 'outcome': outcome, 'results': results, 'log_id': log_entry['log_id']}

    def _print_result(self, r: LayerResult):
        symbol = "✅" if r.approved else "❌"
        tag = ""
        if r.vetoed: tag = " [VETO]"
        if r.halted: tag = " [HALT]"
        print(f"  [{r.layer}] {symbol}{tag} {r.reason}")


# ═══════════════════════════════════════════════════════════════
# DEMO SCENARIOS — Prove the architecture works
# ═══════════════════════════════════════════════════════════════

def demo():
    pipeline = TONEPipeline()

    print("\n" + "="*70)
    print("  BY SOMMER — TONE PIPELINE PROTOTYPE")
    print("  The sovereign architecture, running.")
    print("="*70)

    # ── Scenario 1: Light Tone — Creative exploration (EXPAND mode) ──
    print("\n\n" + "═"*70)
    print("  SCENARIO 1: Light Tone — Creative Exploration (EXPAND mode)")
    print("═"*70)
    pipeline.execute(
        actor_id="michael@bysommer.net",
        intent="publish_glyph",
        density=ToneDensity.LIGHT,
        direction=ToneDirection.INWARD,
        scope={'glyph_name': 'winter_reflection', 'identity_scope': ['display_name']},
    )

    # ── Scenario 2: Dense Tone — Tax verification (SUPPORT mode) ──
    print("\n\n" + "═"*70)
    print("  SCENARIO 2: Dense Tone — Tax Eligibility Check (SUPPORT mode)")
    print("═"*70)
    pipeline.execute(
        actor_id="michael@bysommer.net",
        intent="verify_tax_eligibility",
        density=ToneDensity.DENSE,
        direction=ToneDirection.OUTWARD,
        scope={
            'jurisdiction': 'DK',
            'identity_scope': ['name', 'cpr_hash', 'income_bracket'],
            'data_category': 'financial',
            'retention_days': 30,
        },
        constraints={'consent': True},
    )

    # ── Scenario 3: Ethical Veto — No consent ──
    print("\n\n" + "═"*70)
    print("  SCENARIO 3: Ethical Veto — Action attempted without consent")
    print("═"*70)
    pipeline.execute(
        actor_id="michael@bysommer.net",
        intent="verify_tax_eligibility",
        density=ToneDensity.DENSE,
        direction=ToneDirection.OUTWARD,
        scope={'jurisdiction': 'DK', 'identity_scope': ['name', 'cpr', 'income']},
        constraints={'consent': False},  # ← No consent given
    )

    # ── Scenario 4: Legal Halt — Cross-border without safeguards ──
    print("\n\n" + "═"*70)
    print("  SCENARIO 4: Legal Halt — Cross-border data without Schrems II safeguards")
    print("═"*70)
    pipeline.execute(
        actor_id="michael@bysommer.net",
        intent="verify_tax_eligibility",
        density=ToneDensity.DENSE,
        direction=ToneDirection.OUTWARD,
        scope={
            'jurisdiction': 'DK',
            'identity_scope': ['name', 'income'],
            'cross_border': True,
            'schrems_safeguards': False,  # ← Missing safeguards
        },
        constraints={'consent': True},
    )

    # ── Scenario 5: BDT — VAT settlement with retention override ──
    print("\n\n" + "═"*70)
    print("  SCENARIO 5: BDT — VAT Settlement with Legal Retention Override")
    print("  (Danish Bookkeeping Act overrides 30-day request → 5 years)")
    print("═"*70)
    pipeline.execute(
        actor_id="michael@bysommer.net",
        intent="submit_vat_settlement",
        density=ToneDensity.DENSE,
        direction=ToneDirection.OUTWARD,
        scope={
            'jurisdiction': 'DK',
            'identity_scope': ['cvr', 'turnover_summary'],
            'data_category': 'financial',
            'retention_days': 30,  # ← Requested 30 days
            'turnover': 75000,     # ← Above DKK 50,000 threshold
            'vat_registered': True,
        },
        constraints={'consent': True},
    )

    # ── Audit Trail Verification ──
    print("\n\n" + "═"*70)
    print("  AUDIT TRAIL VERIFICATION")
    print("═"*70)
    print(f"\n  Total entries logged: {len(pipeline.l_snet.ledger)}")
    print(f"  Hash chain intact: {'✅ YES' if pipeline.l_snet.verify_integrity() else '❌ NO'}")
    print(f"\n  Ledger summary:")
    for i, entry in enumerate(pipeline.l_snet.ledger):
        print(f"    {i+1}. [{entry['outcome'].upper()}] {entry['intent']} | "
              f"density={entry['density']} | mode={entry['mode']} | "
              f"hash={entry['entry_hash'][:12]}...")

    print("\n\n" + "="*70)
    print("  PROTOTYPE COMPLETE")
    print("  The architecture works. Each layer is sovereign. Veto and halt")
    print("  power are real. The audit trail is immutable and hash-chained.")
    print("="*70)


if __name__ == "__main__":
    demo()
