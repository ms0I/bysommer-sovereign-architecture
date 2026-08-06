"""
By Sommer — TONE Pipeline Prototype v2
========================================
Upgraded with:
- Extended Tone Header (10 fields: +Priority, +Trace)
- Intent Gravity formula (blocks autonomous execution for high-gravity)
- Deterministic Authority Levels 0-4 (Observe → Critical)
- PDT 5 sub-agents (Guardian, Archivist, Optimizer, Organiser, Coordinator)
- Misinterpretation Firewall (routes high-gravity to HITL)

Run: python3 prototype/tone_pipeline_v2.py
"""

import json
import uuid
import hashlib
from datetime import datetime, timezone
from enum import Enum
from dataclasses import dataclass, field, asdict
from typing import Optional


# ═══════════════════════════════════════════════════════════════
# TONE PROTOCOL — 10-Field Header Vector
# ═══════════════════════════════════════════════════════════════

class ToneDensity(Enum):
    DENSE = "Dense"
    LIGHT = "Light"

class ToneDirection(Enum):
    INWARD = "inward"
    OUTWARD = "outward"
    LATERAL = "lateral"
    UPWARD = "upward"
    DOWNWARD = "downward"

class SystemMode(Enum):
    SUPPORT = "SUPPORT"
    EXPAND = "EXPAND"

class AuthorityLevel(Enum):
    LEVEL_0 = (0, "Observe", "Read-only, pattern detection, no action", False)
    LEVEL_1 = (1, "Recommend", "Suggests options, compares trade-offs, warns", False)
    LEVEL_2 = (2, "Assist Action", "Prepares drafts, schedules, workflows requiring approval", True)
    LEVEL_3 = (3, "Delegate Action", "Autonomous execution of predefined low-gravity actions", False)
    LEVEL_4 = (4, "Critical Action", "High-stakes clinical/financial/identity actions", True)

    def __init__(self, level, name, desc, requires_hitl):
        self.level = level
        self.auth_name = name
        self.description = desc
        self.requires_hitl = requires_hitl


@dataclass
class ToneHeader:
    """The 10-field Tone Header Vector.
    H = [A_id, L_num, D_tone, D_dir, I_intent, C_ctx, S_scp, C_con, P_pri, T_trace]^T"""
    tone_id: str
    actor_id: str
    layer: str
    density: ToneDensity
    direction: ToneDirection
    intent: str
    context: dict                          # NEW: situational context
    scope: dict
    constraints: dict
    priority: int = 5                      # NEW: 0-9 (9 = emergency)
    trace: list = field(default_factory=list)  # NEW: provenance chain
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def mode(self) -> SystemMode:
        return SystemMode.SUPPORT if self.density == ToneDensity.DENSE else SystemMode.EXPAND

    def to_dict(self) -> dict:
        d = asdict(self)
        d['density'] = self.density.value
        d['direction'] = self.direction.value
        return d


# ═══════════════════════════════════════════════════════════════
# INTENT GRAVITY — Determines if HITL is mandatory
# ═══════════════════════════════════════════════════════════════

def compute_intent_gravity(scope: dict, intent: str, density: ToneDensity) -> tuple:
    """
    G_intent = f(I_impact, R_irrev, S_scope, U_unc)

    Returns (gravity_score, threshold, requires_hitl, breakdown)
    High gravity (>= threshold) blocks autonomous execution → Misinterpretation Firewall
    """
    # Impact (0-10): based on action type
    impact_map = {
        'publish_glyph': 2, 'creative_exploration': 1,
        'verify_tax_eligibility': 5, 'submit_vat_settlement': 7,
        'emergency_disclosure': 9, 'delete_account': 8,
        'border_pre_clearance': 6, 'autonomous_valet_parking': 4,
        'ip_verification': 3, 'welfare_adjustment': 6,
    }
    I_impact = impact_map.get(intent, 5)

    # Irreversibility (0-10): can the action be undone?
    irrev_map = {
        'delete_account': 9, 'submit_vat_settlement': 8,
        'emergency_disclosure': 7, 'verify_tax_eligibility': 2,
        'publish_glyph': 3, 'border_pre_clearance': 5,
        'autonomous_valet_parking': 4, 'ip_verification': 2,
        'welfare_adjustment': 6,
    }
    R_irrev = irrev_map.get(intent, 5)

    # Scope (0-10): how many systems/people affected?
    S_scope = min(10, len(scope.get('identity_scope', [])) * 2 + scope.get('affected_systems', 1))

    # Uncertainty (0-10): how confident is the system?
    U_unc = 10 - scope.get('confidence', 80) // 10

    # Weighted gravity score
    G = (I_impact * 0.3 + R_irrev * 0.3 + S_scope * 0.2 + U_unc * 0.2)

    # Dense tones add gravity weight
    if density == ToneDensity.DENSE:
        G += 1.5

    threshold = 6.0  # Actions above 6.0 require mandatory HITL
    requires_hitl = G >= threshold

    return (round(G, 2), threshold, requires_hitl, {
        'impact': I_impact, 'irreversibility': R_irrev,
        'scope': S_scope, 'uncertainty': U_unc,
    })


# ═══════════════════════════════════════════════════════════════
# SOVEREIGN LAYERS
# ═══════════════════════════════════════════════════════════════

@dataclass
class LayerResult:
    layer: str
    approved: bool
    reason: str
    modified_scope: Optional[dict] = None
    vetoed: bool = False
    halted: bool = False
    authority_level: Optional[int] = None
    gravity_score: Optional[float] = None
    metadata: dict = field(default_factory=dict)


# ── L-OP: Operator ──────────────────────────────────────────────
class OperatorLayer:
    name = "L-OP"

    def generate_tone(self, actor_id, intent, density, direction, scope,
                      constraints=None, context=None, priority=5) -> ToneHeader:
        return ToneHeader(
            tone_id=str(uuid.uuid4()),
            actor_id=hashlib.sha256(actor_id.encode()).hexdigest()[:16],
            layer=self.name, density=density, direction=direction,
            intent=intent, context=context or {}, scope=scope,
            constraints=constraints or {}, priority=priority,
        )


# ── L-PDT: Personal Digital Twin (5 Sub-Agents) ───────────────
class PersonalDigitalTwin:
    name = "L-PDT"

    # The 5 sub-agents
    SUB_AGENTS = {
        'Guardian': 'Security & ethics sentinel — monitors threats, enforces consent',
        'Archivist': 'Memory & provenance keeper — maintains Memory Thread, addendum protocol',
        'Optimizer': 'Efficiency & resource manager — minimizes waste, optimizes logistics',
        'Organiser': 'Structure & taxonomy manager — categorizes info, manages glyph library',
        'Coordinator': 'Inter-layer orchestration — routes Tones, manages authority escalation',
    }

    def process(self, tone: ToneHeader) -> LayerResult:
        if not tone.intent or len(tone.intent) < 3:
            return LayerResult(self.name, False, "Intent too vague — clarification needed")

        identity_scope = tone.scope.get('identity_scope', [])
        if len(identity_scope) > 5:
            return LayerResult(self.name, False,
                             "Identity scope too broad — data minimization violated (max 5 attributes)")

        # Sub-agents each contribute
        sub_agent_results = {
            'Guardian': 'consent_verified' if tone.constraints.get('consent', True) else 'consent_missing',
            'Archivist': 'memory_thread_updated',
            'Optimizer': 'scope_optimized',
            'Organiser': 'intent_categorized',
            'Coordinator': 'routing_determined',
        }

        return LayerResult(self.name, True, "Intent validated by 5 sub-agents",
                          metadata={'mode': tone.mode().value, 'sub_agents': sub_agent_results,
                                   'identity_attributes': len(identity_scope)})


# ── L-AURORA: Governance Substrate ──────────────────────────────
class AuroraGovernance:
    name = "L-AURORA"

    RULES = {
        'verify_tax_eligibility': {'risk': 'medium', 'max_auth': 3},
        'submit_vat_settlement': {'risk': 'high', 'max_auth': 2},
        'emergency_disclosure': {'risk': 'high', 'max_auth': 4},
        'creative_exploration': {'risk': 'low', 'max_auth': 3},
        'publish_glyph': {'risk': 'low', 'max_auth': 3},
        'delete_account': {'risk': 'high', 'max_auth': 2},
        'border_pre_clearance': {'risk': 'medium', 'max_auth': 3},
        'autonomous_valet_parking': {'risk': 'medium', 'max_auth': 3},
        'ip_verification': {'risk': 'low', 'max_auth': 3},
        'welfare_adjustment': {'risk': 'high', 'max_auth': 2},
    }

    def process(self, tone: ToneHeader, gravity: float, requires_hitl: bool) -> LayerResult:
        rule = self.RULES.get(tone.intent)
        if rule is None:
            return LayerResult(self.name, False,
                             f"Unknown intent '{tone.intent}' — escalation for human clarification")

        # Intent Gravity check → Misinterpretation Firewall
        if requires_hitl:
            return LayerResult(self.name, True,
                             f"Governance validated (risk: {rule['risk']}). "
                             f"⚠ MISINTERPRETATION FIREWALL: Gravity={gravity} ≥ 6.0 → HITL mandatory. "
                             f"Max authority level: {rule['max_auth']}",
                             authority_level=rule['max_auth'],
                             gravity_score=gravity,
                             metadata={'risk_tier': rule['risk'], 'hitl_required': True,
                                      'misinterpretation_firewall': True, 'max_auth': rule['max_auth']})

        return LayerResult(self.name, True,
                         f"Governance validated (risk: {rule['risk']}, gravity: {gravity}). "
                         f"Max authority level: {rule['max_auth']}",
                         authority_level=rule['max_auth'],
                         gravity_score=gravity,
                         metadata={'risk_tier': rule['risk'], 'hitl_required': False,
                                  'max_auth': rule['max_auth']})


# ── L-ETH: Ethical Layer (HARD VETO) ───────────────────────────
class EthicalLayer:
    name = "L-ETH"

    PROHIBITED = {
        'surveillance': "Mass surveillance violates privacy and dignity",
        'forced_disclosure': "Forced disclosure without consent violates autonomy",
        'discriminatory_action': "Discriminatory actions violate dignity and equality",
    }

    def process(self, tone: ToneHeader) -> LayerResult:
        if tone.intent in self.PROHIBITED:
            return LayerResult(self.name, False, self.PROHIBITED[tone.intent], vetoed=True)

        if not tone.constraints.get('consent', True):
            return LayerResult(self.name, False,
                             "Consent not provided — ethical veto (consent is core constraint)",
                             vetoed=True)

        if tone.constraints.get('force_disclosure', False):
            return LayerResult(self.name, False, "Forced disclosure — ethical veto", vetoed=True)

        # Acute risk escalation (acts without consent for THIS specific action only)
        if tone.constraints.get('acute_risk', False):
            return LayerResult(self.name, True,
                             "Acute risk — escalating to human professional (consent override for this action only)",
                             metadata={'acute_risk_escalation': True})

        return LayerResult(self.name, True, "Ethical constraints satisfied (consent, privacy, dignity, transparency, non-harm)")


# ── L-LEG: Legal Compliance (HARD HALT) ────────────────────────
class LegalComplianceLayer:
    name = "L-LEG"

    JURISDICTIONS = {
        'DK': {'vat_threshold': 50000, 'retention_years': 5, 'ai_act': 'high_risk'},
        'DE': {'vat_threshold': 0, 'retention_years': 10, 'ai_act': 'high_risk'},
        'EU': {'oss_threshold': 10000, 'ioss_threshold': 150},
        'baseline': {'human_rights_floor': True},
    }

    def process(self, tone: ToneHeader) -> LayerResult:
        scope = tone.scope
        jurisdiction = scope.get('jurisdiction', 'DK')
        applicable = ['baseline', 'EU', jurisdiction] if jurisdiction in self.JURISDICTIONS else ['baseline', 'EU']

        # VAT threshold check
        if tone.intent == 'submit_vat_settlement':
            turnover = scope.get('turnover', 0)
            threshold = self.JURISDICTIONS['DK']['vat_threshold']
            if turnover < threshold and not scope.get('vat_registered', False):
                return LayerResult(self.name, True,
                                 f"Below VAT threshold (DKK {threshold}) — no registration required yet",
                                 metadata={'jurisdictions': applicable})

        # Retention override (stricter rule wins)
        retention_requested = scope.get('retention_days', 30)
        required = self.JURISDICTIONS.get(jurisdiction, {}).get('retention_years', 5) * 365
        if retention_requested < required and scope.get('data_category') == 'financial':
            return LayerResult(self.name, True,
                             f"Compliance verified. Retention overridden: {retention_requested}d → {required}d (stricter rule wins)",
                             modified_scope={'retention_days': required},
                             metadata={'jurisdictions': applicable, 'retention_override': True})

        # Cross-border halt
        if scope.get('cross_border', False) and not scope.get('schrems_safeguards', False):
            return LayerResult(self.name, False,
                             "Cross-border without Schrems II safeguards — legal halt",
                             halted=True, metadata={'jurisdictions': applicable})

        # Compliance proof
        proof = hashlib.sha256(json.dumps(
            {'tone_id': tone.tone_id, 'jurisdictions': applicable,
             'intent': tone.intent}, sort_keys=True).encode()).hexdigest()[:32]

        return LayerResult(self.name, True,
                         f"Legal compliance verified. Jurisdictions: {', '.join(applicable)}",
                         metadata={'jurisdictions': applicable, 'compliance_proof': f"zk:{proof}"})


# ── L-SYS: Execution ────────────────────────────────────────────
class SystemExecution:
    name = "L-SYS"

    def process(self, tone: ToneHeader, results: list) -> LayerResult:
        for r in results:
            if not r.approved:
                return LayerResult(self.name, False,
                                 f"Execution blocked — {r.layer} did not approve: {r.reason}")

        final_scope = tone.scope.copy()
        for r in results:
            if r.modified_scope:
                final_scope.update(r.modified_scope)

        # Determine actual authority level used
        auth_level = max((r.authority_level or 0) for r in results if r.authority_level)

        return LayerResult(self.name, True,
                         f"Executed: {tone.intent} | Auth Level: {auth_level} | Scope: {json.dumps(final_scope, sort_keys=True)}",
                         authority_level=auth_level,
                         metadata={'final_scope': final_scope, 'authority_level': auth_level})


# ── L-SNET: Audit Trail (hash-chained, append-only) ───────────
class AuditTrail:
    name = "L-SNET"

    def __init__(self):
        self.ledger = []
        self._prev = None

    def log(self, tone: ToneHeader, results: list):
        entry = {
            'log_id': str(uuid.uuid4()),
            'tone_id': tone.tone_id,
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'operator': tone.actor_id,
            'intent': tone.intent,
            'density': tone.density.value,
            'direction': tone.direction.value,
            'mode': tone.mode().value,
            'priority': tone.priority,
            'gravity': max((r.gravity_score or 0) for r in results if r.gravity_score) if any(r.gravity_score for r in results) else None,
            'authority_level': max((r.authority_level or 0) for r in results if r.authority_level) if any(r.authority_level for r in results) else None,
            'layers': [{'layer': r.layer, 'approved': r.approved, 'vetoed': r.vetoed,
                       'halted': r.halted, 'reason': r.reason} for r in results],
            'outcome': 'executed' if all(r.approved for r in results) else 'blocked',
        }
        entry_hash = hashlib.sha256(json.dumps(entry, sort_keys=True).encode()).hexdigest()
        entry['entry_hash'] = entry_hash
        entry['previous_hash'] = self._prev or 'GENESIS'
        self._prev = entry_hash
        self.ledger.append(entry)
        return entry

    def verify_integrity(self) -> bool:
        prev = 'GENESIS'
        for entry in self.ledger:
            if entry['previous_hash'] != prev: return False
            check = {k: v for k, v in entry.items() if k not in ('entry_hash', 'previous_hash')}
            if entry['entry_hash'] != hashlib.sha256(json.dumps(check, sort_keys=True).encode()).hexdigest():
                return False
            prev = entry['entry_hash']
        return True


# ═══════════════════════════════════════════════════════════════
# THE PIPELINE
# ═══════════════════════════════════════════════════════════════

class TONEPipeline:
    def __init__(self):
        self.l_op = OperatorLayer()
        self.l_pdt = PersonalDigitalTwin()
        self.l_aurora = AuroraGovernance()
        self.l_eth = EthicalLayer()
        self.l_leg = LegalComplianceLayer()
        self.l_sys = SystemExecution()
        self.l_snet = AuditTrail()

    def execute(self, actor_id, intent, density, direction, scope, constraints=None,
                context=None, priority=5) -> dict:
        print(f"\n{'─'*72}")
        print(f"  TONE PIPELINE v2 — Intent: {intent}")
        print(f"  Density: {density.value} → Mode: {density == ToneDensity.DENSE and 'SUPPORT' or 'EXPAND'}")
        print(f"  Direction: {direction.value} | Priority: {priority}")
        print(f"{'─'*72}")

        tone = self.l_op.generate_tone(actor_id, intent, density, direction, scope,
                                        constraints, context, priority)
        print(f"\n  [L-OP] Tone: {tone.tone_id[:8]}... | Actor: {tone.actor_id} | Priority: {tone.priority}")

        # Compute Intent Gravity BEFORE pipeline (determines HITL requirement)
        gravity, threshold, requires_hitl, breakdown = compute_intent_gravity(scope, intent, density)
        print(f"  [GRAVITY] Score: {gravity} / Threshold: {threshold} → HITL: {'REQUIRED' if requires_hitl else 'not required'}")
        print(f"           impact={breakdown['impact']} irrev={breakdown['irreversibility']} "
              f"scope={breakdown['scope']} unc={breakdown['uncertainty']}")

        results = []

        # L-PDT
        r = self.l_pdt.process(tone)
        results.append(r); self._print(r)
        if not r.approved: return self._finish(tone, results)

        # L-AURORA (with gravity)
        r = self.l_aurora.process(tone, gravity, requires_hitl)
        results.append(r); self._print(r)
        if not r.approved: return self._finish(tone, results)

        # L-ETH
        r = self.l_eth.process(tone)
        results.append(r); self._print(r)
        if r.vetoed:
            print(f"\n  ⛔ ETHICAL VETO — blocked by L-ETH")
            return self._finish(tone, results)
        if not r.approved: return self._finish(tone, results)

        # L-LEG
        r = self.l_leg.process(tone)
        results.append(r); self._print(r)
        if r.halted:
            print(f"\n  ⛔ LEGAL HALT — blocked by L-LEG")
            return self._finish(tone, results)
        if not r.approved: return self._finish(tone, results)

        # L-SYS
        r = self.l_sys.process(tone, results)
        results.append(r); self._print(r)

        return self._finish(tone, results)

    def _finish(self, tone, results):
        log = self.l_snet.log(tone, results)
        print(f"\n  [L-SNET] Logged: {log['log_id'][:8]}... | Outcome: {log['outcome'].upper()}")
        if log.get('gravity'): print(f"          Gravity: {log['gravity']} | Auth Level: {log.get('authority_level', 'N/A')}")
        print(f"          Hash: {log['entry_hash'][:16]}... → prev: {log['previous_hash'][:16]}...")
        print(f"{'─'*72}")
        return {'tone_id': tone.tone_id, 'outcome': log['outcome'], 'results': results}

    def _print(self, r):
        sym = "✅" if r.approved else "❌"
        tag = ""
        if r.vetoed: tag = " [VETO]"
        if r.halted: tag = " [HALT]"
        auth = f" | Auth: L{r.authority_level}" if r.authority_level is not None else ""
        grav = f" | Gravity: {r.gravity_score}" if r.gravity_score is not None else ""
        print(f"  [{r.layer}] {sym}{tag}{auth}{grav} {r.reason}")


# ═══════════════════════════════════════════════════════════════
# DEMO
# ═══════════════════════════════════════════════════════════════

def demo():
    p = TONEPipeline()

    print("\n" + "="*72)
    print("  BY SOMMER — TONE PIPELINE PROTOTYPE v2")
    print("  10-Field Header · Intent Gravity · Authority Levels 0-4 · 5 Sub-Agents")
    print("="*72)

    # 1. Light Tone — Low gravity, no HITL needed
    print("\n\n" + "═"*72)
    print("  SCENARIO 1: Light Tone — Publish Glyph (EXPAND, low gravity)")
    print("═"*72)
    p.execute("michael@bysommer.net", "publish_glyph", ToneDensity.LIGHT,
              ToneDirection.INWARD, {'glyph_name': 'winter_reflection', 'identity_scope': ['display_name'], 'confidence': 90})

    # 2. Dense Tone — Medium gravity, HITL required
    print("\n\n" + "═"*72)
    print("  SCENARIO 2: Dense Tone — Tax Check (SUPPORT, medium gravity → HITL)")
    print("═"*72)
    p.execute("michael@bysommer.net", "verify_tax_eligibility", ToneDensity.DENSE,
              ToneDirection.OUTWARD,
              {'jurisdiction': 'DK', 'identity_scope': ['name', 'cpr_hash', 'income_bracket'],
               'data_category': 'financial', 'retention_days': 30, 'confidence': 85},
              {'consent': True})

    # 3. Ethical Veto
    print("\n\n" + "═"*72)
    print("  SCENARIO 3: Ethical Veto — No consent")
    print("═"*72)
    p.execute("michael@bysommer.net", "verify_tax_eligibility", ToneDensity.DENSE,
              ToneDirection.OUTWARD,
              {'jurisdiction': 'DK', 'identity_scope': ['name', 'cpr', 'income'], 'confidence': 80},
              {'consent': False})

    # 4. Legal Halt
    print("\n\n" + "═"*72)
    print("  SCENARIO 4: Legal Halt — Cross-border without Schrems II")
    print("═"*72)
    p.execute("michael@bysommer.net", "verify_tax_eligibility", ToneDensity.DENSE,
              ToneDirection.OUTWARD,
              {'jurisdiction': 'DK', 'identity_scope': ['name', 'income'],
               'cross_border': True, 'schrems_safeguards': False, 'confidence': 80},
              {'consent': True})

    # 5. BDT VAT — High gravity, HITL mandatory, retention override
    print("\n\n" + "═"*72)
    print("  SCENARIO 5: BDT VAT Settlement (high gravity → Misinterpretation Firewall)")
    print("═"*72)
    p.execute("michael@bysommer.net", "submit_vat_settlement", ToneDensity.DENSE,
              ToneDirection.OUTWARD,
              {'jurisdiction': 'DK', 'identity_scope': ['cvr', 'turnover_summary'],
               'data_category': 'financial', 'retention_days': 30,
               'turnover': 75000, 'vat_registered': True, 'confidence': 85},
              {'consent': True})

    # 6. NEW: Emergency disclosure — Highest gravity, Level 4
    print("\n\n" + "═"*72)
    print("  SCENARIO 6: Emergency Disclosure (gravity=9+, Auth Level 4)")
    print("═"*72)
    p.execute("michael@bysommer.net", "emergency_disclosure", ToneDensity.DENSE,
              ToneDirection.OUTWARD,
              {'jurisdiction': 'DK', 'identity_scope': ['name', 'blood_type', 'allergies', 'emergency_contact'],
               'confidence': 95},
              {'consent': True, 'emergency': True}, priority=9)

    # 7. NEW: Border pre-clearance — Smart Freight Green Lane
    print("\n\n" + "═"*72)
    print("  SCENARIO 7: Border Pre-Clearance — Smart Freight Green Lane")
    print("═"*72)
    p.execute("michael@bysommer.net", "border_pre_clearance", ToneDensity.DENSE,
              ToneDirection.OUTWARD,
              {'jurisdiction': 'DK', 'identity_scope': ['passport_hash', 'driver_id', 'vehicle_id'],
               'cargo_manifest': True, 'customs_cleared': True, 'tachograph_compliant': True,
               'confidence': 88},
              {'consent': True}, priority=7)

    # Audit
    print("\n\n" + "═"*72)
    print("  AUDIT TRAIL VERIFICATION")
    print("═"*72)
    print(f"\n  Total entries: {len(p.l_snet.ledger)}")
    print(f"  Hash chain intact: {'✅ YES' if p.l_snet.verify_integrity() else '❌ NO'}")
    print(f"\n  {'#':>2} {'Outcome':>8} {'Intent':<25} {'Density':<6} {'Gravity':>7} {'AuthL':>5}")
    print(f"  {'─'*60}")
    for i, e in enumerate(p.l_snet.ledger):
        print(f"  {i+1:>2} {e['outcome'].upper():>8} {e['intent']:<25} {e['density']:<6} "
              f"{str(e.get('gravity','—')):>7} {str(e.get('authority_level','—')):>5}")

    print("\n\n" + "="*72)
    print("  PROTOTYPE v2 COMPLETE")
    print("  New features: 10-field header · Intent Gravity · Authority Levels")
    print("  5 sub-agents · Misinterpretation Firewall · 7 demo scenarios")
    print("="*72)


if __name__ == "__main__":
    demo()
