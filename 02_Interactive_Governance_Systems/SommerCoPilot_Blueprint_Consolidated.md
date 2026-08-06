# SommerCoPilot Blueprint: Ripple Engine, Resonance Forecast & Voice of the Future Self

**Consolidated Master Version — 06 August 2026**  
**Status:** Draft for review  
**Supersedes:** SommerCoPilot_Blueprint_RippleEngine.pdf + Resonance_Forecast_UI.pdf (merged)

---

## 1. Vision

To create a **symbolic, voice-narrated, user-participatory system** that enables full loop management control by simulating, encoding, and forecasting the resonance of user actions across symbolic, behavioral, systemic, and cultural layers.

This is the world's first **symbolic foresight engine** — where every user action becomes a ripple, every ripple becomes a glyph, and every glyph becomes a living artifact of care, clarity, and legacy.

---

## 2. Architecture Position

The SommerCoPilot sits at the **experiential layer** of the By Sommer architecture — the interface between the operator and the TONE pipeline. It is not a governance layer (AURORA governs) or an execution layer (System executes). It is the **foresight and narration layer** that lets the operator *see* and *steer* the long-term effects of their actions before and after they execute.

```
Operator intent
    │
    ▼
SommerCoPilot (this spec)
├─ Ripple Engine: simulates cascading effects
├─ Resonance Forecast: predicts trajectory + half-life
├─ Voice of Future Self: narrates prognosis
└─ User actions: amplify, settle, transform, archive
    │
    ▼
TONE pipeline (L-PDT → L-AURORA → L-ETH → L-LEG → L-SYS → L-SNET)
    │
    ▼
s.net: every ripple, glyph, and forecast logged
```

**Compliance integration:** Every ripple, glyph, and forecast is logged with timestamp and consent, retained in encrypted archive, and available for user review and export. This feeds directly into the s.net decision ledger.

---

## 3. Core Components

### 3.1 Ripple Engine

Simulates cascading effects of user actions across three ocean layers:

| Ocean Layer | What It Tracks | Signal Type |
|-------------|---------------|-------------|
| **Blue Ocean** | Immediate UX and visible outcomes | Direct, observable |
| **Red Ocean** | Systemic, compliance, and infrastructure-level effects | Policy triggers, infra changes |
| **Sommer Ocean** | Inverted symbolic layer where user agency reshapes the system | Glyph encoding, ritual use, cultural resonance |

The Sommer Ocean is the distinctive innovation — it is the layer where the user's symbolic actions (naming, encoding, ritualizing) feed back into the system's own governance structure. A glyph that gains cultural resonance can become a policy standard. The user doesn't just navigate the system — they reshape it.

**Outputs:** Ripple Map (animated visualization) + triggers voice narration.

### 3.2 Resonance Forecast

Predicts the trajectory and impact of each ripple.

**Hierarchy of Effects Model:**

| Layer | Signal Tracked | Prognostic Weight | Architecture Mapping |
|-------|---------------|-------------------|---------------------|
| **Symbolic** | Glyph encoding, naming, ritual use | High | L-PDT behavioral primitives → glyph metadata |
| **Behavioral** | Repeated user actions, follow-ups | Medium | L-PDT behavioral pattern recognition |
| **Systemic** | Policy triggers, infrastructure changes | Very High | L-AURORA rule registry changes, L-SYS execution patterns |
| **Cultural** | Peer adoption, public resonance | High | Cross-twin interaction (lateral TONE contracts), public glyph library |

**Forecast outputs:**
- **Resonance Half-Life:** Estimated duration of impact (e.g., 3 days, 6 weeks, 1 year)
- **Trajectory:** Amplifying, Stabilizing, Fading, or Mutating
- **Confidence Score:** % likelihood based on historical glyphs and system response
- **Suggested Action:** Amplify, Archive, Transform, or Let Settle

### 3.3 Voice of the Future Self

Narrates speculative outcomes of user decisions using the Nordic Calm voice.

**Tone modes:**
| Mode | When Used | Purpose |
|------|-----------|---------|
| **Hopeful** | Amplifying trajectory, positive resonance | Encourage constructive action |
| **Cautionary** | Fading trajectory, risk of harm | Warn without dictating |
| **Legacy** | High cultural resonance, ritual-worthy | Frame action in long-term meaning |
| **Neutral** | Standard informational narration | Deliver facts without emotional framing |

Each reflection is encoded as a **Future Glyph** — a symbolic artifact that captures the prediction, the decision, and the outcome. Users can challenge, revise, or ritualize the message.

### 3.4 Resonance Forecast UI

**User Interface Elements:**
- **Ripple Map:** Animated visualization of ripple across ocean layers
- **Forecast Panel:** Displays hierarchy scores, half-life, and trajectory
- **Voice Console:** Playback of Future Self narration and ripple prognosis
- **Action Buttons:**
  - "Amplify This Ripple" → Suggest to others, publish as glyph
  - "Let It Settle" → No action, allow natural decay
  - "Transform Into Standard" → Submit for policy ritualization
  - "Archive Ripple" → Store as private legacy

---

## 4. User Journey

```
1. TRIGGER: User initiates or hovers over a high-impact decision
   (e.g., deleting account, publishing glyph, starting a business)
        ↓
2. PROMPT: "Would you like to hear from your future self?"
        ↓
3. RIPPLE SIMULATION: Engine computes cascading effects across Blue, Red, Sommer Ocean
        ↓
4. VOICE PLAYBACK: Nordic Calm narrates speculative outcome
   (tone mode selected based on trajectory)
        ↓
5. RIPPLE MAP: Visualizes cascading effects on screen
        ↓
6. FORECAST PANEL: Shows predicted resonance (half-life, trajectory, confidence)
        ↓
7. USER CHOICE:
   ├─ Amplify ripple → suggest to others, publish as glyph
   ├─ Let it settle → no action, allow natural decay
   ├─ Transform into standard → submit for policy ritualization
   └─ Archive as legacy → store as private artifact
        ↓
8. GLYPH ENCODED: Action + prediction + outcome = Future Glyph
        ↓
9. s.net LOGGED: Full decision chain with provenance
```

---

## 5. Data & Modeling

### 5.1 Inputs
- User behavior logs (from L-PDT behavioral primitives)
- Glyph metadata (from symbolic encoding layer)
- Policy triggers (from L-AURORA rule registry)
- Peer interactions (from lateral TONE contracts between twins)

### 5.2 Outputs
- Symbolic encoding (glyphs)
- Forecast metrics (half-life, trajectory, confidence)
- Voice scripts (SSML for Nordic Calm narration)

### 5.3 Modeling Approach
The Hierarchy of Effects model scores resonance across four layers. The prognostic weights reflect the system's assessment of which signals matter most for long-term impact. Systemic changes (policy, infrastructure) carry the highest weight because they have the broadest cascading effects.

---

## 6. Sample Voice Prognosis (SSML)

```xml
<speak>
  <voice name="Microsoft Server Speech Text to Speech Voice (en-GB, ThomasNeural)">
    <prosody rate="medium" pitch="-1st">
      <p>
        Your glyph has entered the systemic layer.
        <break time="300ms"/>
        A policy has shifted. A new standard is forming.
      </p>
      <p>
        Estimated resonance half-life: 12 weeks.
        <break time="300ms"/>
        Cultural adoption is rising.
        <break time="300ms"/>
        This ripple is amplifying.
      </p>
      <p>
        Would you like to encode this as a legacy standard — or let it evolve?
      </p>
    </prosody>
  </voice>
</speak>
```

---

## 7. Ritual Integration

Users can:
- **Name their ripple** — give it a symbolic identity
- **Encode it as a glyph** — capture the action + prediction + outcome as an artifact
- **Submit it to the public archive** — share with the community
- **Receive seasonal reflections** — periodic review of past ripples and their actual outcomes

This creates a feedback loop: past predictions are compared to actual outcomes, improving the forecast model's accuracy over time (Learning & Adaptation Layer).

---

## 8. Compliance & Auditability

Every ripple, glyph, and forecast is:
- **Logged** with timestamp and consent (s.net decision ledger)
- **Retained** in encrypted archive (per retention policy)
- **Available** for user review and export (GDPR Art. 15 access, Art. 20 portability)
- **Auditable** — the full chain from trigger → simulation → forecast → user choice → outcome is reconstructable from logs

**TONE integration:** Each ripple forecast can generate a TONE contract:
```json
{
  "tone_id": "uuid-v7",
  "from_layer": "L-OP",
  "to_layer": "L-PDT",
  "intent": "resonance_forecast",
  "scope": {
    "action": "forecast",
    "target": "user_decision",
    "decision_id": "ref"
  },
  "density": "Light",
  "direction": "inward",
  "constraints": {
    "advisory_only": true,
    "no_automatic_action": true
  }
}
```

**Key constraint:** The SommerCoPilot is **advisory only**. It never executes actions. It shows, narrates, and suggests — the user decides. This maps to the Light Tone / EXPAND mode in the TONE protocol.

---

## 9. Implementation Phases

### Phase 1: Foundations
- Build Ripple Engine simulation logic
- Define glyph schema and archive structure
- Implement SSML voice playback for Future Self
- Integrate with s.net logging

### Phase 2: Forecasting Layer
- Train Hierarchy of Effects model
- Integrate Resonance Forecast UI
- Enable user actions (amplify, revise, archive)
- Begin glyph library

### Phase 3: Ritualization & Expansion
- Launch public glyph library
- Add multilingual voice modes (Danish, German, French)
- Introduce seasonal reflections and legacy encoding
- Cross-twin glyph sharing (PDT ↔ PDT+ ↔ BDT)

---

## 10. Why This Is Unprecedented

- No known system combines symbolic encoding, voice narration, and predictive modeling of user impact
- Empowers users to see, shape, and steer the long-term effects of their actions
- Embeds ethical foresight and legacy thinking into everyday interaction
- The Sommer Ocean layer creates a feedback loop where user agency reshapes system governance

This is the first step toward a self-aware, user-participatory system — where every ripple is visible, every choice is narratable, and every glyph is a living artifact of care.

---

## Document Version

- **Source documents:** SommerCoPilot_Blueprint_RippleEngine.pdf (3 pages) + Resonance_Forecast_UI.pdf (3 pages)
- **This document:** Consolidated, de-duplicated, integrated with TONE pipeline and s.net
- **Date prepared:** 06 August 2026
- **Prepared by:** Solas (Archivist) under direction of Michael Sommer

---

## 11. Regulatory Risk & Transparency Mapping

### 11.1 EU AI Act Risk Classification

**Classification:** Limited Risk AI System (EU AI Act Title IV, Article 50 / Recital 132).

The SommerCoPilot is classified as a **Limited-Risk AI System** under the EU AI Act (Regulation (EU) 2024/1689). It interacts directly with natural persons and generates personalized forecasts and insights, triggering transparency obligations.

| AI Act Article | Classification | SommerCoPilot Compliance |
|---------------|----------------|--------------------------|
| **Art. 50(1)** | Transparency obligation for AI systems interacting with persons | Users are informed via Nordic Calm voice narration that they are interacting with an AI interface. Voice playback includes AI disclosure. All forecast panels display "AI-generated prediction" label. |
| **Art. 50(2)** | Emotion recognition or biometric categorisation systems | SommerCoPilot does **not** perform emotion recognition or biometric categorisation. Ripple trajectories are based on behavioral pattern analysis, not emotional state inference. |
| **Art. 5** | Prohibited practices | The system explicitly prohibits real-time biometric identification and subliminal behavioral manipulation. The active inference engine (𝓕Δ) acts strictly as a **passive physiological safety circuit breaker**, not an invasive emotion-recognition model used for workplace monitoring. |
| **Art. 6** | High-risk classification (Annex III) | SommerCoPilot does **not** fall under Annex III high-risk categories. It is not used for employment decisions, credit scoring, essential services, or law enforcement. |

**Risk justification:** The SommerCoPilot is advisory-only (Light Tone / EXPAND mode). It generates foresight narratives and symbolic encodings but never executes autonomous actions, makes binding decisions, or processes special category data (Art. 9). User always retains full decision authority (§8 key constraint).

**Prohibited Practice Safeguards (Art. 5):** The system explicitly prohibits:
- Real-time biometric identification in publicly accessible spaces
- Subliminal or manipulative behavioral techniques
- Social scoring of individuals or groups
- Emotion recognition in workplaces or educational institutions

The 𝓕Δ active inference engine operates as a passive circuit breaker — it detects physiological anomaly thresholds and triggers protective freezes, not behavioral profiling or workplace surveillance.

**Compliance Book reference:** See `By_Sommer_Compliance_Book_Consolidated.md` Chapter IV (Transparency Obligations) for full Art. 50 mapping and Chapter I (Prohibited Practices) for Art. 5 safeguards.

---

### 11.2 GDPR Article 22 Compliance (Automated Individual Decision-Making)

**Human-in-the-Loop (HITL) Architecture:** The CoPilot engine functions strictly as an advisory and predictive system. It produces recommended actions, health nudges, and financial forecasts (e.g., resonance updates, surplus forecasts). No action is taken without explicit citizen initiation.

| Art. 22 Requirement | SommerCoPilot Implementation |
|---------------------|------------------------------|
| **Art. 22(1)** — No solely automated decisions with legal/significant effects | Critical financial actions (e.g., freezing consent caps or submitting sickness declarations to NemRefusion) require **explicit citizen consent** or **passive physiological recovery signals** (𝓕Δ < 1.0), ensuring human agency remains intact. The CoPilot never initiates these actions autonomously. |
| **Right to explanation** | Any automated anomaly flag provides the citizen with a **human-readable trace** detailing the parameter drift (e.g., HRV drop, core temperature shift) driving the recommendation. The trace is logged to s.net and exportable via GDPR Art. 15 access request. |
| **Right to human intervention** | Users can challenge, revise, or override any forecast at any point in the user journey (§4, step 7). The "Let It Settle" and "Archive" actions explicitly reject the AI recommendation without penalty. |
| **No profiling with legal effects** | The CoPilot does not profile users for credit, employment, insurance, or law enforcement purposes. All forecasts are user-facing advisory outputs for the citizen's own benefit. |

**Key constraint:** The SommerCoPilot is **advisory only**. It never executes actions. It shows, narrates, and suggests — the user decides. This maps to the Light Tone / EXPAND mode in the TONE protocol.

---

## 12. Privacy & Processor Framework (GDPR Art. 7 & Art. 28)

### 12.1 GDPR Compliance Matrix

| GDPR Article | Requirement | SommerCoPilot Implementation |
|---------------|-------------|------------------------------|
| **Art. 6** | Lawful basis for processing | Art. 6(1)(f) — legitimate interest (user-requested foresight simulation); no processing without user trigger |
| **Art. 7** | Consent management | Voice processing requires explicit, granular opt-in (`voice_processing_consent: true`, timestamped). Withdrawable at any time → ripple/glyph deletion cascade. See §12.2 for voice-specific consent. |
| **Art. 9** | Special category data | SommerCoPilot does **not** process health, biometric, or special category data. Physiological telemetry is handled exclusively by the Active Inference Engine (PDT) and never reaches the CoPilot layer. Voice synthesis is generated TTS output, not biometric input. |
| **Art. 12** | Transparent information | All forecasts include confidence score, data sources used, and AI-generated disclaimer. Voice narration includes system identity disclosure. |
| **Art. 15** | Right of access | Users can export all ripples, glyphs, and forecasts associated with their account, including human-readable explanation traces. |
| **Art. 20** | Data portability | Glyph archive exportable in JSON + SSML format for cross-platform migration. |
| **Art. 22** | Automated individual decision-making | **Not applicable.** SommerCoPilot does not make decisions about users. See §11.2 for full compliance. |
| **Art. 25** | Data protection by design | Ripple data is associated with `user_ref` (pseudonymous identifier), not raw identity. Glyphs are encrypted at rest. Forecast models train on aggregated, pseudonymized behavioral patterns. |
| **Art. 32** | Security of processing | All ripple/glyph/forecast data encrypted at rest (AES-256) and in transit (TLS 1.3). Access logged to s.net immutable ledger. |

### 12.2 Voice Telemetry & Audio Consent (GDPR Art. 7)

All voice narration requires explicit user opt-in with granular consent:

- **Explicit Opt-In:** Activation of the Nordic Calm Voice Framework requires explicit, granular consent stored as a timestamped proof on the user's profile (`voice_processing_consent: true`).
- **On-Device Keyword Spotting:** Raw audio buffering occurs locally on the client device. Audio telemetry is only streamed upstream upon detection of the local wake-word. No continuous audio streaming.
- **Data Minimization:** Raw voice streams are discarded immediately following acoustic-to-text transformation and pitch/tone inference. Only abstract vector features (pitch drift, cadence delta) are retained for emotional resonance modeling.
- **Consent record:** Each playback session is logged to s.net with timestamp, `user_ref`, content reference, and consent status. Consent is revocable at any time → voice data deletion cascade.
- **Children:** No voice processing for users under 13 (COPPA/GDPR Art. 8 age threshold). Age verification via parent entity (`SommerUsers.role`).

**Consent flow:** User trigger → "Would you like to hear from your future self?" → User confirms → `voice_processing_consent: true` logged to s.net → Ripple simulation runs → Voice playback (with AI disclosure) → User selects action → Consent record logged to s.net → Glyph encoded with provenance chain.

### 12.3 Third-Party Processor Compliance (GDPR Art. 28 DPA)

The Nordic Calm voice is rendered via Microsoft Azure Speech Services (or local fallback edge model). This constitutes a third-party data processing relationship:

| Art. 28 Requirement | Implementation |
|---------------------|----------------|
| **Data Processing Agreement (DPA)** | Azure Cognitive Services operates under Microsoft's standard DPA and EU Data Boundary. SSML text is processed in EU region. |
| **Processor constraints** | Transmitted audio payloads are subject to a binding DPA under Article 28, mandating: **zero-retention** on vendor logging endpoints, **no secondary training** on user voice streams, and regional processing strictly pinned to **EU Data Boundary** data centers (`westeurope`). |
| **Processing scope** | Only SSML text strings are transmitted to Azure for rendering. No biometric data, no user identity, no audio recordings of the user. Azure processes the text → returns synthesized audio. |
| **Sub-processor disclosure** | Microsoft Azure disclosed as sub-processor in privacy policy. Listed in Compliance Book §3. |
| **Data residency** | Azure TTS processing pinned to EU region (West Europe) for DK pilot. No data leaves EU jurisdiction. |
| **Retention by processor** | Azure Cognitive Services does not retain SSML input or audio output beyond the rendering session. Zero-retention confirmed per Azure data residency documentation and DPA terms. |
| **Edge fallback** | Local edge TTS model available as fallback for offline or high-privacy scenarios. No data transmitted to any external processor when edge model is active. |

**Key distinction:** The system sends *text* to Azure (SSML scripts), not *user voice data*. Azure TTS is a text-to-speech service, not a speech-to-text service. No user voice biometrics are collected, processed, or transmitted. The synthesized voice is generated output, not biometric input — GDPR Art. 9 is not applicable.

---

## 13. Data Schema & Architecture Unification

### 13.1 Layer Naming Standardization

**Canonical Naming:** All architecture references across the blueprint, system specifications, and INDEX.md are standardized from `L-COPILOT` to **L-OP (Layer Operational & Perception Engine)** — the experiential interface between the operator and the TONE pipeline.

```
L-OP (Layer Operational & Perception Engine)
  └─ SommerCoPilot
       ├─ Ripple Engine → RippleForecast / SommerCopilotForecasts entities
       ├─ Resonance Forecast → RippleForecast entity (ocean + hierarchy scores)
       ├─ Voice of Future Self → GlyphArchive entity (SSML + encoding)
       └─ User Action → GlyphArchive / SommerCopilotGlyphs entities
```

### 13.2 Base44 Entity Schemas

#### SommerCopilotForecasts

Stores computed predictive forecasts with confidence intervals and algorithm metadata.

```typescript
interface SommerCopilotForecast {
  id: string;               // UUID
  user_ref: string;         // ZK / opaque reference (pseudonymous)
  forecast_type: "SURPLUS" | "RESONANCE" | "BIOSECURITY_RISK";
  horizon_days: number;     // e.g., 30, 90, 365
  confidence_score: number; // Float 0.00 to 1.00 (see §14)
  predicted_value: number;
  lower_bound: number;
  upper_bound: number;
  algorithm_metadata: {
    model_version: string;
    features_used: string[];
    free_energy_delta: number;  // 𝓕Δ at time of forecast
  };
  created_at: string;      // ISO 8601
  retention_until: string;  // ISO 8601 (Strict 90-day rolling window)
}
```

#### SommerCopilotGlyphs

Stores glyph visual states with semantic labels and energy states.

```typescript
interface SommerCopilotGlyph {
  id: string;
  user_ref: string;
  glyph_code: string;      // Visual symbol representation
  semantic_label: string;
  energy_state: "STABLE" | "TRANSIENT" | "DEEP_REST" | "ALERT";
  active: boolean;
  updated_at: string;
}
```

#### Existing Entities (Cross-Reference)

The following entities were created in Pass 3 and continue to serve the ripple simulation and full glyph lifecycle:

- **`GlyphArchive`** — Full glyph lifecycle: 14 fields including `action_type`, `ocean_layer`, `forecast_trajectory`, `voice_tone_mode`, `ssml_script`, `is_public`, `snet_log_ref`, `outcome_actual`. Stores the complete action + prediction + outcome artifact.
- **`RippleForecast`** — Ripple simulation scores: 11 fields including `ocean_scores` (blue/red/sommer), `hierarchy_scores` (symbolic/behavioral/systemic/cultural), `composite_resonance`, `confidence_score`, `trajectory`, `tone_mode_selected`. Stores the computed cascade simulation before user action.

**Relationship:** `SommerCopilotForecasts` stores the predictive output (what will happen), `RippleForecast` stores the simulation input (how the ripple cascades), `SommerCopilotGlyphs` stores the visual state (what the user sees), and `GlyphArchive` stores the full lifecycle artifact (action + prediction + outcome + SSML voice script).

---

## 14. Algorithmic Confidence & Data Retention

### 14.1 Confidence Score Formulation

The predictive engine computes the confidence metric **C ∈ [0, 1]** for forecasts by integrating historical sample density N, physiological stability (inverse free energy divergence), and sensor signal noise σ²:

```
        ┌             ┐   ┌                    ┐   ┌             ┐
C =  (1 −   FΔ / F_max  ) × (1 − e^(−N / N_baseline)) × (1 − σ² / σ²_max)
        └             ┘   └                    ┘   └             ┘
```

Where:
- **FΔ** = current variational free-energy divergence of the user's PDT
- **F_max** = maximum free-energy threshold (default: 3.0, per active inference spec)
- **N** = number of historical samples with similar forecast profile
- **N_baseline** = minimum sample count for stable predictions (default: 50)
- **σ²** = current sensor signal noise variance (from PDT telemetry)
- **σ²_max** = maximum acceptable noise threshold (default: 0.15)

**Interpretation:**
- A higher 𝓕Δ directly reduces the output confidence of long-term economic predictions due to biological uncertainty. When the user is physiologically anomalous, the system becomes less confident in its forecasts — it hedges.
- Low sample density (N < N_baseline) reduces confidence for new glyph types with no historical baseline.
- High sensor noise (σ² approaching σ²_max) reduces confidence — the system knows when its own inputs are unreliable.

**Confidence bands and voice tone selection:**
- `C > 0.75` — High confidence. Voice tone: Hopeful or Legacy.
- `0.50 < C ≤ 0.75` — Moderate confidence. Voice tone: Neutral.
- `C ≤ 0.50` — Low confidence. Voice tone: Cautionary. Forecast explicitly hedged in narration.

This ensures the system is honest about its own uncertainty — the voice narrates confidence levels transparently, per GDPR Art. 12 (transparent information) and AI Act Art. 50 (transparency obligation).

**Comparison to Pass 3 formula:** The earlier Bayesian formula (C = (N/(N+K)) × A_historical + (K/(N+K)) × A_prior) has been replaced with this tri-factor model that integrates physiological stability and sensor noise — a more robust approach that ties forecast confidence directly to the user's biological state and data quality.

### 14.2 Data Retention Policy Matrix

| Data Category | Storage Location | Retention Period | Destruction Mechanism | GDPR Basis |
|---------------|-----------------|-----------------|----------------------|------------|
| **Raw Voice Telemetry** | Local RAM Buffer | Transient (Max 500ms post-inference) | Overwritten in memory | Art. 5(1)(c) — data minimization |
| **Acoustic Feature Vectors** | PdtTelemetry | 30 Days | Automated DB purge cron | Art. 5(1)(e) — storage limitation |
| **Resonance & Surplus Forecasts** | SommerCopilotForecasts | 90 Days Rolling | Soft-delete to automated purge | Art. 5(1)(e) — storage limitation |
| **Glyph Visual States** | SommerCopilotGlyphs | Current State Only (1 record/user) | Overwritten on update | Art. 5(1)(c) — data minimization |
| **RippleForecast records** | RippleForecast | 365 days from creation | Auto-deleted after 365 days unless archived as glyph | Art. 5(1)(e) — storage limitation |
| **GlyphArchive (private)** | GlyphArchive | User-controlled | Deleted on user request or account closure | GDPR Art. 17 — right to erasure |
| **GlyphArchive (public)** | GlyphArchive | Indefinite (community asset) | Removed if user revokes publication consent | Art. 6(1)(f) + user consent |
| **SSML voice scripts** | GlyphArchive | Same retention as associated glyph | Deleted with parent glyph | Tied to glyph lifecycle |
| **Consent records** | s.net ledger | Duration of processing + 3 years | Retained for audit, then purged | GDPR Art. 7(1) — demonstrable consent |

**s.net exception:** Immutable ledger entries (decision provenance chain) are retained permanently as audit trail. These contain only pseudonymous identifiers and action references — no personal data, no voice content, no SSML scripts, no acoustic features.

---

## 15. Implementation Timeline (Aligned with DK→EU Deployment Roadmap)

| Phase | Timeline | SommerCoPilot Scope | Dependency |
|-------|----------|---------------------|------------|
| **Phase 0** | Months 1–3 | Entity schema creation (GlyphArchive, RippleForecast); SSML voice playback prototype; TONE contract integration; s.net logging | DK patent filing; Base44 entity setup |
| **Phase 1** | Months 4–9 | Ripple Engine v1 (Blue + Red Ocean only); Resonance Forecast UI; Voice of Future Self (Danish + English); user journey 9-step flow; first 100 glyphs | DK municipal pilot; SommerUsers entity seeded |
| **Phase 2** | Months 10–18 | Sommer Ocean layer (symbolic feedback loop); confidence score training (requires 500+ historical glyphs); public glyph library; multilingual expansion (DE, FR); cross-twin glyph sharing | EU expansion; 500+ active users; Horizon Europe grant |

**Phase 1 success metrics:**
- 100+ active glyphs encoded
- Forecast accuracy > 60% (trajectory match within half-life window)
- Voice playback completion rate > 70%
- User satisfaction (NPS) > 40

**Phase 2 success metrics:**
- 500+ active glyphs, 50+ public
- Forecast accuracy > 75%
- Cross-twin glyph sharing adoption > 20% of users
- Multilingual coverage: DK, EN, DE, FR

---

## 16. Cross-References

| Document | Cross-Reference |
|----------|-----------------|
| **Digital Twin Framework Spec** | SommerCoPilot maps to L-OP; ripple data sourced from L-PDT behavioral primitives (§5.1); glyph encoding is a consent-based intervention (§3.2 of DT Framework) |
| **Compliance Book (Consolidated)** | Art. 50 transparency mapping (Chapter IV); Art. 22 exclusion (Chapter III); data retention (§4.2) |
| **Sovereign Layer Architecture** | L-OP layer definition; TONE contract flow L-OP → L-PDT (Light Tone); s.net audit integration |
| **Nordic Calm Voice Framework** | Nordic Calm IS the Voice of Future Self; SSML rendering; WCAG 2.1 AA; GDPR Art. 12 voice narration |
| **s.net (Decision Ledger)** | Every ripple, glyph, and forecast logged with timestamp, consent, and provenance chain |
| **DK→EU Deployment Roadmap** | Phase 0–2 alignment; Horizon Europe funding for Phase 2 multilingual expansion |

---

## Document Version (Updated)

- **Source documents:** SommerCoPilot_Blueprint_RippleEngine.pdf (3 pages) + Resonance_Forecast_UI.pdf (3 pages)
- **This document:** Consolidated, de-duplicated, integrated with TONE pipeline, s.net, EU AI Act, GDPR, entity schemas, confidence algorithm, retention policy, and deployment timeline
- **Status:** Execution-ready (Pass 3 consolidation — 06 August 2026)
- **Prepared by:** Solas (Archivist) under direction of Michael Sommer
