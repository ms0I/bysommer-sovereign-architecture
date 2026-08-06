#!/usr/bin/env python3
"""
TONE Patent Diagram Generator
Produces 9 USPTO-grade SVG diagrams for the TONE Architecture patent portfolio.
"""

import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "diagrams")

def esc(text):
    """Escape XML special characters in text content."""
    return str(text).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


# ── Shared style constants ──────────────────────────────────────────
FONT = "Arial, Helvetica, sans-serif"
FONT_MONO = "Courier New, monospace"
COLOR_INK = "#1a1a1a"
COLOR_ACCENT = "#2563eb"
COLOR_RED = "#dc2626"
COLOR_GREEN = "#16a34a"
COLOR_AMBER = "#d97706"
COLOR_BG_BOX = "#ffffff"
COLOR_BG_BOX_LIGHT = "#f8f8f8"
COLOR_BG_DECISION = "#fffde7"
COLOR_BG_BOUNDARY = "#f0f4ff"
COLOR_BORDER = "#666666"
COLOR_BORDER_LIGHT = "#cccccc"
COLOR_ARROW = "#444444"
COLOR_MUTED = "#888888"

def svg_header(width=960, height=640):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" font-family="{FONT}">
'''

def svg_footer():
    return "</svg>\n"

def defs():
    return f'''
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L9,3 L0,6 Z" fill="{COLOR_ARROW}"/>
    </marker>
    <marker id="arrow-accent" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L9,3 L0,6 Z" fill="{COLOR_ACCENT}"/>
    </marker>
    <marker id="arrow-red" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L9,3 L0,6 Z" fill="{COLOR_RED}"/>
    </marker>
    <marker id="arrow-dashed" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L9,3 L0,6 Z" fill="{COLOR_MUTED}"/>
    </marker>
  </defs>
'''

def box(x, y, w, h, label, sublabel=None, ref=None, fill=COLOR_BG_BOX, border=COLOR_BORDER, rx=4):
    elements = [f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" ry="{rx}" fill="{fill}" stroke="{border}" stroke-width="1.5"/>']
    mid_y = y + h/2
    if sublabel:
        elements.append(f'  <text x="{x+w/2}" y="{mid_y-8}" text-anchor="middle" font-size="14" font-weight="600" fill="{COLOR_INK}">{esc(label)}</text>')
        elements.append(f'  <text x="{x+w/2}" y="{mid_y+12}" text-anchor="middle" font-size="11" fill="{COLOR_MUTED}">{esc(sublabel)}</text>')
    else:
        elements.append(f'  <text x="{x+w/2}" y="{mid_y+5}" text-anchor="middle" font-size="14" font-weight="600" fill="{COLOR_INK}">{esc(label)}</text>')
    if ref:
        elements.append(ref_num(x + w - 18, y + 16, ref))
    return "\n".join(elements)

def decision_diamond(cx, cy, w, h, label, ref=None):
    points = f"{cx},{cy-h/2} {cx+w/2},{cy} {cx},{cy+h/2} {cx-w/2},{cy}"
    elements = [
        f'  <polygon points="{points}" fill="{COLOR_BG_DECISION}" stroke="{COLOR_BORDER}" stroke-width="1.5"/>',
        f'  <text x="{cx}" y="{cy-4}" text-anchor="middle" font-size="12" font-weight="600" fill="{COLOR_INK}">{esc(label)}</text>',
    ]
    if ref:
        elements.append(ref_num(cx + w/2 - 12, cy - h/2 + 14, ref))
    return "\n".join(elements)

def arrow(x1, y1, x2, y2, label=None, color=COLOR_ARROW, dashed=False, marker="arrow"):
    dash = ' stroke-dasharray="5,3"' if dashed else ''
    marker_id = marker
    if color == COLOR_ACCENT:
        marker_id = "arrow-accent"
    elif color == COLOR_RED:
        marker_id = "arrow-red"
    elif dashed:
        marker_id = "arrow-dashed"
    elements = [f'  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="1.5"{dash} marker-end="url(#{marker_id})"/>']
    if label:
        mx, my = (x1+x2)/2, (y1+y2)/2
        elements.append(f'  <text x="{mx}" y="{my-6}" text-anchor="middle" font-size="10" fill="{COLOR_MUTED}">{esc(label)}</text>')
    return "\n".join(elements)

def ref_num(x, y, num):
    return f'''  <g>
    <circle cx="{x}" cy="{y}" r="10" fill="{COLOR_ACCENT}" stroke="none"/>
    <text x="{x}" y="{y+4}" text-anchor="middle" font-size="10" font-weight="700" fill="#ffffff">{num}</text>
  </g>'''

def title(text, num, x=480, y=28):
    return f'  <text x="{x}" y="{y}" text-anchor="middle" font-size="16" font-weight="700" fill="{COLOR_INK}">FIG. {num} — {esc(text)}</text>'

def zone_label(x, y, w, label, color=COLOR_BORDER_LIGHT):
    return f'  <text x="{x+w/2}" y="{y-8}" text-anchor="middle" font-size="11" font-weight="600" fill="{COLOR_MUTED}" letter-spacing="1">{esc(label)}</text>'

def trust_boundary(x, y, w, h, label):
    return f'''  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" ry="6" fill="none" stroke="{COLOR_ACCENT}" stroke-width="1.5" stroke-dasharray="6,4"/>
  <text x="{x+8}" y="{y+18}" font-size="10" font-weight="600" fill="{COLOR_ACCENT}">{label}</text>'''

def pill(x, y, label, color=COLOR_BORDER):
    w = len(label) * 8 + 20
    return f'''  <rect x="{x}" y="{y}" width="{w}" height="24" rx="12" ry="12" fill="{color}" stroke="none"/>
  <text x="{x+w/2}" y="{y+16}" text-anchor="middle" font-size="11" font-weight="600" fill="#ffffff">{label}</text>'''

def text_line(x, y, text, size=12, weight="400", color=COLOR_INK, anchor="middle"):
    return f'  <text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{weight}" fill="{color}">{esc(text)}</text>'

# ═══════════════════════════════════════════════════════════════════════
# FIG. 1 — System Architecture Overview
# ═══════════════════════════════════════════════════════════════════════
def fig1():
    s = svg_header(960, 700)
    s += defs()
    s += "  " + title("System Architecture Overview", "1") + "\n"
    
    # L1 block: Edge Physiological Sensors
    s += box(310, 60, 340, 70, "Edge Physiological Sensors", "HRV · Core Temp · Resp Rate · SpO₂", ref="100") + "\n"
    
    # Arrow down
    s += arrow(480, 130, 480, 165, "ZK Proof Transmission", color=COLOR_ACCENT) + "\n"
    
    # L2: Active Inference Engine
    s += box(310, 170, 340, 70, "Active Inference Engine", "Variational Free-Energy Divergence (FΔ)", ref="102") + "\n"
    
    # Arrow down
    s += arrow(480, 240, 480, 275, "Anomaly Signal", color=COLOR_RED) + "\n"
    
    # Side branch: Circuit Breaker
    s += box(620, 170, 240, 70, "Circuit Breaker Module", "Transaction Freeze + Cap → 0 DKK", ref="104") + "\n"
    s += arrow(650, 205, 560, 205, color=COLOR_RED) + "\n"
    
    # L3: ZK Compliance Engine
    s += box(310, 280, 340, 70, "ZK Compliance Engine (BDT+)", "Multi-Tier Jurisdictional Rule Matcher", ref="106") + "\n"
    
    # Side: ZK Vault
    s += box(620, 280, 240, 70, "Zero-Knowledge Vault", "cpr_zk_hash · Identity Verification", ref="108") + "\n"
    s += arrow(650, 315, 560, 315, "ZK Hash Verify", dashed=True) + "\n"
    
    # Arrow down
    s += arrow(480, 350, 480, 385, "Compliance Verdict", color=COLOR_ACCENT) + "\n"
    
    # L4: Planetary Shield + Surplus Ledger (side by side)
    s += box(140, 390, 300, 70, "Planetary Shield", "R₀ Monitoring · Micro-Quarantine", ref="110") + "\n"
    s += box(520, 390, 300, 70, "Non-Profit Surplus Ledger", "Δ_surplus Accrual · Dec 10 Epoch", ref="112") + "\n"
    
    # Arrows from compliance engine to both
    s += arrow(400, 350, 290, 385, color=COLOR_ACCENT) + "\n"
    s += arrow(560, 350, 670, 385, color=COLOR_ACCENT) + "\n"
    
    # Cross link: Circuit breaker to surplus ledger
    s += arrow(740, 240, 670, 385, "Suspend Credit", dashed=True, color=COLOR_RED) + "\n"
    
    # Bottom: s.net ledger spanning
    s += f'  <rect x="80" y="500" width="800" height="50" rx="4" ry="4" fill="{COLOR_BG_BOX_LIGHT}" stroke="{COLOR_BORDER}" stroke-width="1.5"/>' + "\n"
    s += text_line(480, 530, "s.net — Immutable Append-Only Decision Ledger", 14, "600") + "\n"
    s += ref_num(860, 515, "114") + "\n"
    
    # Arrows to s.net
    for x in [200, 480, 740]:
        s += arrow(x, 460, x, 495, "Audit Log", dashed=True) + "\n"
    
    # Right side: Sovereign Governance / HITL
    s += box(820, 170, 120, 380, "Sovereign Governance", "HITL Override\nEthical Guardrails", ref="116") + "\n"
    s += text_line(880, 360, "HITL", 10, "600", COLOR_MUTED) + "\n"
    s += text_line(880, 375, "Level 2", 10, "600", COLOR_MUTED) + "\n"
    s += arrow(820, 205, 860, 205, dashed=True) + "\n"
    s += arrow(820, 315, 860, 315, dashed=True) + "\n"
    
    # Left side labels for layers
    for y, lbl in [(95, "L1 — PDT"), (205, "L2 — PDT+"), (315, "L4 — BDT+"), (425, "L6-L8"), (525, "L7 — s.net")]:
        s += text_line(50, y, lbl, 10, "600", COLOR_MUTED, "start") + "\n"
    
    s += svg_footer()
    return s

# ═══════════════════════════════════════════════════════════════════════
# FIG. 2 — Active Inference Circuit Breaker Flowchart
# ═══════════════════════════════════════════════════════════════════════
def fig2():
    s = svg_header(960, 780)
    s += defs()
    s += "  " + title("Active Inference Circuit Breaker — State Transition Flowchart", "2") + "\n"
    
    # Step 1: Telemetry ingestion
    s += box(340, 60, 280, 55, "Telemetry Stream Ingestion", "Anonymized physiological state vectors", ref="200") + "\n"
    s += arrow(480, 115, 480, 145) + "\n"
    
    # Step 2: ZK validation
    s += box(340, 150, 280, 55, "ZK Proof Validation", "GEMS Oracle verifies attestation", ref="202") + "\n"
    s += arrow(480, 205, 480, 235) + "\n"
    
    # Step 3: FΔ computation
    s += box(300, 240, 360, 70, "Variational Free-Energy Computation", "FΔ = Σᵢ ‖oᵢ − μᵢ‖ / σᵢ", ref="204") + "\n"
    s += arrow(480, 310, 480, 340) + "\n"
    
    # Decision: threshold check
    s += decision_diamond(480, 390, 280, 100, "FΔ ≥ 3.0 or\nΔT ≥ 1.5°C ?", ref="206") + "\n"
    
    # No branch (left)
    s += arrow(340, 390, 220, 390, "No") + "\n"
    s += box(80, 365, 220, 50, "NORMAL OPERATION", "Spending cap: 250 DKK/mo", ref="208", fill="#f0fdf4", border=COLOR_GREEN) + "\n"
    s += arrow(190, 365, 190, 330, "", dashed=True) + "\n"
    s += text_line(190, 320, "Continue autonomous\npre-bookings", 10, "400", COLOR_GREEN) + "\n"
    
    # Yes branch (down)
    s += arrow(480, 440, 480, 470, "Yes", color=COLOR_RED) + "\n"
    
    # Emit anomaly signal
    s += box(340, 475, 280, 50, "Emit Anomaly State Signal", ref="210", fill="#fef2f2", border=COLOR_RED) + "\n"
    s += arrow(480, 525, 480, 555, color=COLOR_RED) + "\n"
    
    # Circuit breaker action
    s += box(300, 560, 360, 70, "Circuit Breaker: Hard Lock", "Cap → 0 DKK · All pre-bookings frozen", ref="212", fill="#fef2f2", border=COLOR_RED) + "\n"
    s += arrow(480, 630, 480, 660, color=COLOR_RED) + "\n"
    
    # Audit + escalation
    s += box(300, 665, 360, 50, "Log to s.net + Escalate to Planetary Shield", ref="214") + "\n"
    
    # Unlock conditions (right side)
    s += box(700, 475, 220, 50, "Unlock Condition A", "Passive: FΔ < 1.0", ref="216", fill="#f0fdf4", border=COLOR_GREEN) + "\n"
    s += box(700, 560, 220, 50, "Unlock Condition B", "HITL Level 2 Override", ref="218", fill="#f0fdf4", border=COLOR_GREEN) + "\n"
    s += arrow(700, 500, 660, 500, "", color=COLOR_GREEN, dashed=True) + "\n"
    s += arrow(700, 585, 660, 585, "", color=COLOR_GREEN, dashed=True) + "\n"
    s += arrow(700, 500, 700, 460, "", dashed=True) + "\n"
    s += text_line(800, 450, "Recovery → Resume", 10, "600", COLOR_GREEN) + "\n"
    
    s += svg_footer()
    return s

# ═══════════════════════════════════════════════════════════════════════
# FIG. 3 — Spatial Rule Matcher Pipeline
# ═══════════════════════════════════════════════════════════════════════
def fig3():
    s = svg_header(960, 680)
    s += defs()
    s += "  " + title("Spatial Rule Matcher — Multi-Tier Jurisdictional Pipeline", "3") + "\n"
    
    # Step 1: GPS
    s += box(350, 60, 260, 50, "GPS Telemetry Capture", "lat/lng from PDT", ref="300") + "\n"
    s += arrow(480, 110, 480, 140) + "\n"
    
    # Step 2: Reverse geocode
    s += box(350, 145, 260, 50, "Municipal Reverse Geocoding", "→ MUNICIPAL_CODE", ref="302") + "\n"
    s += arrow(480, 195, 480, 225) + "\n"
    
    # Three-tier rule loading (parallel boxes)
    s += text_line(480, 240, "Rule Lookup — Three-Tier Hierarchy", 13, "600") + "\n"
    
    # EU box
    s += box(80, 250, 250, 60, "Supranational Rules", "EU · IOSS · Cross-border", ref="304") + "\n"
    # National box
    s += box(355, 250, 250, 60, "National Rules", "NATIONAL_DK · VAT 25% · CE Mark", ref="306") + "\n"
    # Municipal box
    s += box(630, 250, 250, 60, "Municipal Rules", f"MUNICIPAL_<CODE> · Env Zone · Noise", ref="308") + "\n"
    
    # Converge arrows
    s += arrow(205, 310, 380, 340) + "\n"
    s += arrow(480, 310, 480, 340) + "\n"
    s += arrow(755, 310, 580, 340) + "\n"
    
    # ZK-CPR validation
    s += box(300, 345, 360, 60, "ZK-CPR Identity Validation", "Verify cpr_zk_hash — no PII transmitted", ref="310") + "\n"
    s += arrow(480, 405, 480, 435) + "\n"
    
    # Decision matrix
    s += decision_diamond(480, 485, 300, 100, "Rule Matching\n+ Conflict Resolution\n(stricter-rule-wins)", ref="312") + "\n"
    
    # Three output states
    s += arrow(330, 485, 200, 485, "All pass") + "\n"
    s += box(60, 460, 220, 50, "VALIDATED", "Advisory Class I", ref="314", fill="#f0fdf4", border=COLOR_GREEN) + "\n"
    
    s += arrow(480, 535, 480, 565, "Missing doc", color=COLOR_AMBER) + "\n"
    s += box(350, 570, 260, 50, "PENDING", "Advisory Class II", ref="316", fill="#fffbeb", border=COLOR_AMBER) + "\n"
    
    s += arrow(630, 485, 760, 485, "Violation", color=COLOR_RED) + "\n"
    s += box(680, 460, 220, 50, "BLOCKED", "BLOCKED_MISSING_CE · Class III", ref="318", fill="#fef2f2", border=COLOR_RED) + "\n"
    
    # Audit
    s += arrow(480, 620, 480, 650, "→ s.net", dashed=True) + "\n"
    
    s += svg_footer()
    return s

# ═══════════════════════════════════════════════════════════════════════
# FIG. 4 — Surplus Accrual Timeline
# ═══════════════════════════════════════════════════════════════════════
def fig4():
    s = svg_header(960, 720)
    s += defs()
    s += "  " + title("Surplus Accrual Timeline — December 10th Protocol", "4") + "\n"
    
    # Formula box
    s += box(250, 55, 460, 55, "Daily Surplus Formula", "Δ_surplus = (225.00 / 30) − 5.20 = 2.30 DKK/day", ref="400") + "\n"
    
    # State machine labels
    s += text_line(180, 165, "STATE MACHINE", 12, "700", COLOR_MUTED) + "\n"
    
    # Accumulating state
    s += box(80, 180, 200, 60, "ACCUMULATING", "Pool_t+1 = Pool_t + 2.30", ref="402", fill="#f0fdf4", border=COLOR_GREEN) + "\n"
    
    # Suspended state
    s += box(80, 290, 200, 60, "SUSPENDED", "Circuit breaker active\nFΔ > 3.0", ref="404", fill="#fef2f2", border=COLOR_RED) + "\n"
    
    # Distributing state
    s += box(80, 400, 200, 60, "DISTRIBUTING", "Dec 10: Pool → Citizen", ref="406", fill="#fffbeb", border=COLOR_AMBER) + "\n"
    
    # State transitions
    s += arrow(180, 240, 180, 285, "Anomaly\nflag", color=COLOR_RED) + "\n"
    s += arrow(180, 350, 180, 395, "Dec 10", color=COLOR_AMBER) + "\n"
    s += arrow(180, 460, 180, 510, "Complete\n→ Reset") + "\n"
    s += text_line(180, 530, "Pool = 0", 10, "600", COLOR_MUTED) + "\n"
    s += arrow(180, 535, 180, 580, "", dashed=True) + "\n"
    
    # Recovery arrow (suspended back to accumulating)
    s += arrow(280, 320, 280, 210, "Recovery\nFΔ < 1.0", color=COLOR_GREEN, dashed=True) + "\n"
    
    # Right side: Timeline
    s += text_line(650, 165, "CALENDAR TIMELINE", 12, "700", COLOR_MUTED) + "\n"
    
    # Timeline line
    s += f'  <line x1="350" y1="200" x2="880" y2="200" stroke="{COLOR_BORDER}" stroke-width="2"/>' + "\n"
    
    # Month markers
    months = [("Jan 1", 360), ("Mar", 440), ("Jun", 540), ("Sep", 640), ("Dec 10", 780), ("Dec 31", 870)]
    for label, x in months:
        s += f'  <line x1="{x}" y1="195" x2="{x}" y2="210" stroke="{COLOR_BORDER}" stroke-width="2"/>' + "\n"
        s += text_line(x, 225, label, 10, "400", COLOR_MUTED) + "\n"
    
    # Increment bars
    for i in range(40):
        x = 360 + i * 13
        h = 20 + (i % 5) * 3
        s += f'  <rect x="{x}" y="{200-h}" width="8" height="{h}" fill="{COLOR_ACCENT}" opacity="0.3"/>' + "\n"
    
    # Epoch trigger
    s += f'  <line x1="780" y1="160" x2="780" y2="260" stroke="{COLOR_AMBER}" stroke-width="2" stroke-dasharray="4,3"/>' + "\n"
    s += text_line(780, 155, "EPOCH TRIGGER", 10, "700", COLOR_AMBER) + "\n"
    
    # Distribution arrow
    s += arrow(780, 260, 780, 300, "Pool_total → Citizen", color=COLOR_AMBER) + "\n"
    
    # Reset
    s += f'  <line x1="790" y1="200" x2="870" y2="200" stroke="{COLOR_GREEN}" stroke-width="3"/>' + "\n"
    s += text_line(830, 190, "Reset → 0", 10, "600", COLOR_GREEN) + "\n"
    
    # Accumulation curve annotation
    s += text_line(550, 175, "Accumulation: ~839.50 DKK/year", 10, "400", COLOR_ACCENT) + "\n"
    
    # Circuit breaker integration
    s += box(350, 600, 560, 50, "Circuit Breaker Integration (Claim 1)", "FΔ > 3.0 suspends crediting · HITL L2 to resume", ref="408") + "\n"
    s += arrow(180, 320, 350, 625, "", dashed=True, color=COLOR_RED) + "\n"
    
    s += svg_footer()
    return s

# ═══════════════════════════════════════════════════════════════════════
# FIG. 5 — Biosecurity Escalation Cascade
# ═══════════════════════════════════════════════════════════════════════
def fig5():
    s = svg_header(960, 700)
    s += defs()
    s += "  " + title("Biosecurity Escalation Cascade — 3-Layer Stack", "5") + "\n"
    
    # Layer 1: FΔ Anomaly Flag
    s += trust_boundary(80, 55, 800, 150, "LAYER 1 — Municipal Active Inference") + "\n"
    s += box(280, 75, 400, 55, "FΔ Anomaly Detection", "HRV/T/RR/SpO₂ → FΔ ≥ 3.0 or ΔT ≥ 1.5°C", ref="500") + "\n"
    s += box(280, 135, 400, 45, "Anomaly State Signal Emitted", ref="502", fill="#fef2f2", border=COLOR_RED) + "\n"
    
    # Arrow down to Layer 2
    s += arrow(480, 185, 480, 215, "Trigger", color=COLOR_RED) + "\n"
    
    # Layer 2: BDT+ Pre-Booking Freeze
    s += trust_boundary(80, 220, 800, 150, "LAYER 2 — BDT+ Compliance Execution") + "\n"
    s += box(280, 240, 400, 55, "Circuit Breaker Activation", "Spending cap → 0 DKK · Pre-bookings frozen", ref="504", fill="#fef2f2", border=COLOR_RED) + "\n"
    s += box(100, 240, 160, 55, "NemRefusion\nBridge", "ZK sick declaration", ref="506") + "\n"
    s += arrow(260, 267, 280, 267, "", dashed=True) + "\n"
    s += box(700, 240, 160, 55, "s.net\nAudit Entry", "FREEZE_EXECUTED", ref="508") + "\n"
    s += arrow(680, 267, 700, 267, "", dashed=True) + "\n"
    s += box(280, 305, 400, 45, "Queued Transactions: LOCKED", ref="510", fill="#fef2f2", border=COLOR_RED) + "\n"
    
    # Arrow down to Layer 3
    s += arrow(480, 375, 480, 405, "Escalate", color=COLOR_RED) + "\n"
    
    # Layer 3: Planetary Shield
    s += trust_boundary(80, 410, 800, 170, "LAYER 3 — Planetary Shield") + "\n"
    s += box(280, 430, 400, 55, "R₀ Correlation Engine", "WHO pathogen R₀ > 1.0 detected", ref="512") + "\n"
    
    # Graduated response
    s += arrow(480, 485, 480, 510) + "\n"
    
    s += box(100, 515, 220, 50, "Micro-Quarantine", "Local movement advisory", ref="514") + "\n"
    s += box(370, 515, 220, 50, "Supply Chain Redirect", "Diagnostic mfg request", ref="516") + "\n"
    s += box(640, 515, 220, 50, "Predictive Council", "In silico docking", ref="518") + "\n"
    
    s += arrow(350, 460, 210, 510, color=COLOR_ACCENT) + "\n"
    s += arrow(480, 510, 480, 510, color=COLOR_ACCENT) + "\n"
    s += arrow(610, 460, 750, 510, color=COLOR_ACCENT) + "\n"
    
    # Alert levels (right margin)
    s += text_line(910, 445, "REGIONAL", 9, "600", COLOR_AMBER, "middle") + "\n"
    s += text_line(910, 460, "WARNING", 9, "600", COLOR_AMBER, "middle") + "\n"
    s += text_line(910, 490, "↓", 12, "400", COLOR_MUTED, "middle") + "\n"
    s += text_line(910, 515, "GLOBAL", 9, "600", COLOR_RED, "middle") + "\n"
    s += text_line(910, 530, "DECREE", 9, "600", COLOR_RED, "middle") + "\n"
    
    s += svg_footer()
    return s

# ═══════════════════════════════════════════════════════════════════════
# FIG. 6 — ZK-CPR NemRefusion Bridge
# ═══════════════════════════════════════════════════════════════════════
def fig6():
    s = svg_header(960, 700)
    s += defs()
    s += "  " + title("ZK-CPR NemRefusion Bridge — Privacy-Preserving Sick Leave Declaration", "6") + "\n"
    
    # Three zones with trust boundaries
    # Zone A: PDT + Circuit Breaker
    s += trust_boundary(40, 55, 260, 380, "ZONE A: PDT + CIRCUIT BREAKER") + "\n"
    s += box(60, 80, 220, 50, "Biometric Sensor Array", "HRV · Temp · SpO₂ · RR", ref="600") + "\n"
    s += arrow(170, 130, 170, 155, color=COLOR_RED) + "\n"
    s += box(60, 160, 220, 50, "Anomaly Detected", "FΔ ≥ 3.0", ref="602", fill="#fef2f2", border=COLOR_RED) + "\n"
    s += arrow(170, 210, 170, 235) + "\n"
    s += box(60, 240, 220, 50, "Biosecurity Bridge Module", "Claims 1 + 8", ref="604") + "\n"
    s += arrow(170, 290, 170, 315) + "\n"
    s += box(60, 320, 220, 50, "Assemble Declaration", "Type: IS_INCAPACITATED", ref="606") + "\n"
    
    # Zone B: ZK Vault
    s += trust_boundary(340, 55, 260, 380, "ZONE B: ZERO-KNOWLEDGE VAULT") + "\n"
    s += box(360, 80, 220, 60, "ZK Hash Generation", "Hash(CPR) → cpr_zk_hash", ref="608") + "\n"
    s += arrow(470, 140, 470, 165) + "\n"
    
    # Payload assembly
    s += box(360, 170, 220, 140, "Declaration Payload", None, ref="610") + "\n"
    s += text_line(470, 195, "✅ cpr_zk_hash", 11, "400", COLOR_GREEN) + "\n"
    s += text_line(470, 215, "✅ Anomaly attestation", 11, "400", COLOR_GREEN) + "\n"
    s += text_line(470, 235, "✅ Declaration type code", 11, "400", COLOR_GREEN) + "\n"
    s += text_line(470, 255, "✅ Timestamp + signature", 11, "400", COLOR_GREEN) + "\n"
    s += f'  <line x1="370" y1="265" x2="570" y2="265" stroke="{COLOR_BORDER_LIGHT}" stroke-width="1"/>' + "\n"
    s += text_line(470, 282, "❌ Raw HRV/Temp/SpO₂", 11, "400", COLOR_RED) + "\n"
    s += text_line(470, 298, "❌ Real CPR number", 11, "400", COLOR_RED) + "\n"
    
    # Privacy boundary label
    s += f'  <line x1="620" y1="55" x2="620" y2="435" stroke="{COLOR_ACCENT}" stroke-width="2" stroke-dasharray="6,4"/>' + "\n"
    s += text_line(635, 240, "PRIVACY BOUNDARY", 10, "700", COLOR_ACCENT, "start") + "\n"
    s += text_line(635, 255, "(GDPR Art. 5,6,9,25)", 9, "400", COLOR_ACCENT, "start") + "\n"
    s += text_line(635, 270, "Only hash crosses", 9, "400", COLOR_ACCENT, "start") + "\n"
    
    # Zone C: NemRefusion
    s += trust_boundary(660, 55, 260, 380, "ZONE C: MUNICIPAL REIMBURSEMENT") + "\n"
    s += box(680, 80, 220, 60, "NemRefusion API", "Municipal reimbursement", ref="612") + "\n"
    s += arrow(790, 140, 790, 165) + "\n"
    s += box(680, 170, 220, 50, "Verify cpr_zk_hash", "Match against registry", ref="614") + "\n"
    s += arrow(790, 220, 790, 245) + "\n"
    s += box(680, 250, 220, 50, "Process Sick Leave", "Reimbursement approved", ref="616", fill="#f0fdf4", border=COLOR_GREEN) + "\n"
    s += arrow(790, 300, 790, 325) + "\n"
    s += box(680, 330, 220, 50, "Notify Employer", "Type + dates only — no biometrics", ref="618") + "\n"
    
    # Arrow from Zone A to Zone B
    s += arrow(280, 345, 360, 110, "Trigger", dashed=True) + "\n"
    # Arrow from Zone B to Zone C
    s += arrow(580, 240, 680, 110, "ZK Payload", color=COLOR_ACCENT) + "\n"
    
    # Bottom annotation
    s += box(200, 470, 560, 50, "Key Innovation (Claim 8)", "Sick-leave processed without employer seeing biometric sensor data", ref="620") + "\n"
    
    s += svg_footer()
    return s

# ═══════════════════════════════════════════════════════════════════════
# FIG. 7 — CE Compliance Interception Gate
# ═══════════════════════════════════════════════════════════════════════
def fig7():
    s = svg_header(960, 680)
    s += defs()
    s += "  " + title("CE Compliance Interception Gate — Customs & Product Conformity", "7") + "\n"
    
    # Start
    s += box(340, 60, 280, 50, "Transaction Request", "buyer_id · amount · product_category", ref="700") + "\n"
    s += arrow(480, 110, 480, 140) + "\n"
    
    # IOSS check
    s += decision_diamond(480, 190, 260, 90, "Cross-border &\namount < €150 ?", ref="702") + "\n"
    
    # Yes → IOSS check
    s += arrow(350, 190, 230, 190, "Yes") + "\n"
    s += decision_diamond(170, 190, 240, 90, "IOSS\nregistered?", ref="704") + "\n"
    
    # No IOSS → PENDING
    s += arrow(170, 145, 170, 110, "No", color=COLOR_AMBER) + "\n"
    s += arrow(170, 110, 340, 110, "", color=COLOR_AMBER) + "\n"
    # Actually let me simplify - PENDING goes right
    s += arrow(50, 190, 50, 250, "No IOSS", color=COLOR_AMBER) + "\n"
    s += box(20, 250, 160, 50, "PENDING", "PENDING_IOSS\nClass II", ref="706", fill="#fffbeb", border=COLOR_AMBER) + "\n"
    
    # Has IOSS → continue
    s += arrow(170, 235, 170, 280, "Yes", color=COLOR_GREEN) + "\n"
    s += arrow(170, 280, 340, 280, "", color=COLOR_GREEN) + "\n"
    
    # No cross-border → continue down
    s += arrow(480, 235, 480, 270, "No", color=COLOR_GREEN) + "\n"
    
    # CE marking check
    s += decision_diamond(480, 320, 300, 90, "Regulated category?\n(electronics, toys,\nmedical, machinery)", ref="708") + "\n"
    
    s += arrow(480, 365, 480, 395, "Yes") + "\n"
    
    # CE decision
    s += decision_diamond(480, 440, 220, 80, "CE marking\npresent?", ref="710") + "\n"
    
    # No CE → BLOCKED
    s += arrow(370, 440, 230, 440, "No", color=COLOR_RED) + "\n"
    s += box(50, 415, 200, 50, "BLOCKED", "BLOCKED_MISSING_CE\nClass III", ref="712", fill="#fef2f2", border=COLOR_RED) + "\n"
    
    # Has CE → continue
    s += arrow(480, 480, 480, 510, "Yes", color=COLOR_GREEN) + "\n"
    
    # Not regulated → skip to VAT
    s += arrow(630, 320, 720, 320, "No") + "\n"
    s += arrow(780, 320, 780, 510) + "\n"
    
    # VAT check
    s += box(340, 515, 280, 50, "VAT Rate Verification", "Expected 25% vs applied rate", ref="714") + "\n"
    s += arrow(480, 565, 480, 590) + "\n"
    
    # Final: VALIDATED
    s += box(340, 595, 280, 45, "VALIDATED", "Advisory Class I · → s.net", ref="716", fill="#f0fdf4", border=COLOR_GREEN) + "\n"
    
    s += svg_footer()
    return s

# ═══════════════════════════════════════════════════════════════════════
# FIG. 8 — Planetary Shield Council Interoperability
# ═══════════════════════════════════════════════════════════════════════
def fig8():
    s = svg_header(960, 720)
    s += defs()
    s += "  " + title("Planetary Shield Council Interoperability — Network Topology", "8") + "\n"
    
    # Municipal nodes (bottom layer)
    s += text_line(480, 60, "Municipal Active Inference Nodes", 13, "600", COLOR_MUTED) + "\n"
    
    node_positions = [(120, 90), (280, 90), (440, 90), (600, 90), (760, 90)]
    for i, (x, y) in enumerate(node_positions):
        s += box(x, y, 120, 50, f"Node {i+1}", "PDT FΔ sensor", ref=f"800{i}") + "\n"
    
    # Data types flowing up
    s += text_line(480, 175, "↑ Biometric anomalies · Wastewater signals · Clinical correlations", 10, "400", COLOR_ACCENT) + "\n"
    
    # Arrows from nodes to regional aggregator
    for x in [180, 340, 500, 660, 820]:
        s += arrow(x, 140, 480, 200, "", dashed=True, color=COLOR_ACCENT) + "\n"
    
    # Regional aggregator
    s += box(340, 205, 280, 60, "Regional Aggregation Engine", "Correlate FΔ anomalies across geography", ref="804") + "\n"
    s += arrow(480, 265, 480, 295) + "\n"
    
    # R₀ computation
    s += box(340, 300, 280, 60, "R₀ Transmission Vector Computation", "Effective reproduction number per region", ref="806") + "\n"
    s += arrow(480, 360, 480, 390) + "\n"
    
    # R₀ threshold decision
    s += decision_diamond(480, 440, 200, 80, "R₀ > 1.0 ?", ref="808") + "\n"
    
    # No → normal
    s += arrow(380, 440, 200, 440, "No", color=COLOR_GREEN) + "\n"
    s += box(80, 415, 200, 50, "NORMAL", "Continue monitoring", ref="810", fill="#f0fdf4", border=COLOR_GREEN) + "\n"
    
    # Yes → escalation
    s += arrow(480, 480, 480, 510, "Yes", color=COLOR_RED) + "\n"
    
    # WHO + Council (parallel)
    s += box(140, 515, 260, 60, "WHO Epidemiology Nodes", "Validate R₀ · Issue advisory", ref="812") + "\n"
    s += box(560, 515, 260, 60, "Predictive Council", "In silico docking requests", ref="814") + "\n"
    
    s += arrow(400, 510, 270, 510, color=COLOR_ACCENT) + "\n"
    s += arrow(560, 510, 690, 510, color=COLOR_ACCENT) + "\n"
    
    # Response actions
    s += arrow(270, 575, 270, 605, color=COLOR_AMBER) + "\n"
    s += arrow(690, 575, 690, 605, color=COLOR_AMBER) + "\n"
    
    s += box(140, 610, 260, 50, "Micro-Quarantine Rules", "Update municipal rules", ref="816") + "\n"
    s += box(560, 610, 260, 50, "Supply Chain Redirect", "Diagnostic mfg request", ref="818") + "\n"
    
    # Feedback to nodes
    s += arrow(270, 660, 180, 690, "Rule update", dashed=True, color=COLOR_AMBER) + "\n"
    s += text_line(220, 690, "↓", 10, "400", COLOR_MUTED) + "\n"
    
    s += svg_footer()
    return s

# ═══════════════════════════════════════════════════════════════════════
# FIG. 9 — HITL Level 2 Override Workflow
# ═══════════════════════════════════════════════════════════════════════
def fig9():
    s = svg_header(960, 720)
    s += defs()
    s += "  " + title("HITL Level 2 Override Workflow — Manual Circuit Breaker Resolution", "9") + "\n"
    
    # Start: Lock detected
    s += box(340, 60, 280, 50, "Circuit Breaker: LOCK ACTIVE", "FΔ ≥ 3.0 · Cap = 0 DKK", ref="900", fill="#fef2f2", border=COLOR_RED) + "\n"
    s += arrow(480, 110, 480, 140) + "\n"
    
    # Check: passive recovery?
    s += decision_diamond(480, 190, 280, 90, "Passive recovery?\nFΔ < 1.0", ref="902") + "\n"
    
    # Yes → auto-release
    s += arrow(340, 190, 200, 190, "Yes", color=COLOR_GREEN) + "\n"
    s += box(80, 165, 220, 50, "Auto-Release", "Resume operations", ref="904", fill="#f0fdf4", border=COLOR_GREEN) + "\n"
    s += arrow(190, 215, 190, 250, "", color=COLOR_GREEN) + "\n"
    
    # No → HITL escalation
    s += arrow(480, 235, 480, 265, "No", color=COLOR_AMBER) + "\n"
    s += box(340, 270, 280, 50, "Escalate to HITL Level 2", "Notify qualified authority", ref="906") + "\n"
    s += arrow(480, 320, 480, 350) + "\n"
    
    # HITL review
    s += box(320, 355, 320, 60, "HITL Level 2 Review", "Examine anomaly data · FΔ value\n· Threshold breached · Duration", ref="908") + "\n"
    s += arrow(480, 415, 480, 445) + "\n"
    
    # Decision: approve override?
    s += decision_diamond(480, 495, 260, 90, "Approve\noverride?", ref="910") + "\n"
    
    # No → maintain lock
    s += arrow(350, 495, 200, 495, "No", color=COLOR_RED) + "\n"
    s += box(80, 470, 220, 50, "Maintain Lock", "Continue freeze\nLog denial to s.net", ref="912", fill="#fef2f2", border=COLOR_RED) + "\n"
    s += arrow(190, 520, 190, 560, "", dashed=True) + "\n"
    s += text_line(190, 575, "Re-check in 24h", 10, "400", COLOR_MUTED) + "\n"
    s += arrow(190, 590, 190, 620, "", dashed=True) + "\n"
    # Loop back to review
    s += arrow(80, 495, 60, 495, "", dashed=True) + "\n"
    s += arrow(60, 495, 60, 385, "", dashed=True) + "\n"
    s += arrow(60, 385, 320, 385, "", dashed=True) + "\n"
    
    # Yes → release sequence
    s += arrow(480, 540, 480, 570, "Yes", color=COLOR_GREEN) + "\n"
    s += box(340, 575, 280, 50, "Log Override to s.net", "Authority · timestamp · rationale", ref="914") + "\n"
    s += arrow(480, 625, 480, 655) + "\n"
    
    # Update caps + resume
    s += box(300, 660, 360, 45, "Restore Spending Cap · Resume Pre-Booking Queue", "Cap → municipal default (250 DKK)", ref="916", fill="#f0fdf4", border=COLOR_GREEN) + "\n"
    
    # s.net audit for all paths
    s += arrow(190, 250, 190, 270, "", dashed=True) + "\n"
    s += text_line(190, 285, "→ s.net", 9, "400", COLOR_MUTED) + "\n"
    
    s += svg_footer()
    return s

# ═══════════════════════════════════════════════════════════════════════
# Main — write all SVGs
# ═══════════════════════════════════════════════════════════════════════

diagrams = {
    "FIG_1_System_Architecture.svg": fig1(),
    "FIG_2_Active_Inference_Circuit_Breaker.svg": fig2(),
    "FIG_3_Spatial_Rule_Matcher.svg": fig3(),
    "FIG_4_Surplus_Accrual_Timeline.svg": fig4(),
    "FIG_5_Biosecurity_Escalation_Cascade.svg": fig5(),
    "FIG_6_ZK_CPR_NemRefusion_Bridge.svg": fig6(),
    "FIG_7_CE_Compliance_Interception_Gate.svg": fig7(),
    "FIG_8_Planetary_Shield_Council_Interoperability.svg": fig8(),
    "FIG_9_HITL_Level_2_Override_Workflow.svg": fig9(),
}

os.makedirs(OUTPUT_DIR, exist_ok=True)
for filename, content in diagrams.items():
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"✓ {filename} ({len(content)} bytes)")

print(f"\nAll 9 SVG diagrams written to {OUTPUT_DIR}/")
