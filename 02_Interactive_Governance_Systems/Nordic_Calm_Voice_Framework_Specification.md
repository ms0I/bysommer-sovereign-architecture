# Nordic Calm Voice Framework: Voice of By Sommer

**Structured Specification — 06 August 2026**  
**Status:** Draft for review  
**Source:** Voice_NordicCalm_Integration_Framework.pdf (3 pages)

---

## 1. Purpose

To establish the **Nordic Calm voice** as a living, audible layer of trust, accessibility, and symbolic continuity across all public-facing content, interfaces, and rituals on By Sommer.net and Imsor.com.

The voice is not a feature — it is a **trust signal**. When the system speaks in Nordic Calm, it signals that this is a By Sommer surface, operating within the Compliance Book's legal OS, and that the user is in a sovereign, compliant environment.

---

## 2. Architecture Position

The Nordic Calm voice serves two roles in the By Sommer architecture:

| Role | Where | Function |
|------|-------|----------|
| **Voice of the Future Self** | SommerCoPilot (experiential layer) | Narrates resonance forecasts and ripple prognoses to the user |
| **Voice of By Sommer** | Public-facing surfaces (bysommer.net, imsor.com) | Narrates compliance content, section intros, legacy archives |

Both roles use the same voice profile (Nordic Calm) for continuity — the user hears the same voice whether they're getting a resonance forecast or listening to a privacy policy.

---

## 3. Voice Profile

| Parameter | Value |
|-----------|-------|
| **Voice** | Microsoft Server Speech Text to Speech Voice (en-GB, ThomasNeural) |
| **Rate** | Medium |
| **Pitch** | -1st |
| **Tone** | Calm, measured, warm — Nordic aesthetic |
| **Format** | SSML (Speech Synthesis Markup Language) |
| **Rendering** | Azure TTS |
| **Hosting** | Secure CDN with WCAG-compliant playback |

---

## 4. Public-Facing Features

### 4.1 Voice-Guided Section Intros

Short, SSML-narrated greetings at the top of key sections:

- "Welcome to the Archive. Here, we preserve what matters."
- "This is the Studio. Where ideas become artifacts."
- "You've entered the Compliance Hub. Let's make trust audible."

**Trigger:** On scroll or via audio icon.  
**Optional:** Ambient background tone (low glacier wind or soft piano).

### 4.2 Voice-Guided Navigation

"Listen to this page" toggle on:
- Privacy Policies
- Terms of Use
- Research Abstracts
- Subscription Agreements

**Playback:** Nordic Calm SSML with section headers emphasized, strategic pauses and pacing.  
**Outro:** "You've reached the end of this section. Thank you for listening."

### 4.3 Symbolic Voice Glyphs

A glyph (ear, waveform, or listening face) signals "This section speaks."

- **Placement:** Top-right of sections, beside H2 headers
- **Tooltip:** "Listen in Nordic Calm voice"
- **Behavior:** Click to play pre-rendered audio; highlight section while playing; transcript toggle available

### 4.4 Voice of Legacy

Narrates archived projects and principles:
- "This was recorded in 2022, during our first AI ethics sprint."
- "We began with a question: what does it mean to build with care?"

Uses Nordic Calm to mark transitions:
- "This marks the close of our first compliance cycle. Let's reflect."

### 4.5 Multilingual Calm

Expansion of Nordic Calm to:
- Danish (da-DK, ChristelNeural)
- German (de-DE, ConradNeural)
- French (fr-FR, HenriNeural)

Users toggle language per section or site-wide. Tone, pacing, and clarity maintained across all languages.

### 4.6 Voice-Activated Search

Users can ask:
- "What's your AI policy?"
- "How do I request data deletion?"

Assistant responds in Nordic Calm with spoken summary, link to full section, and transcript view.

### 4.7 Seasonal Voice Rituals

Mark transitions with ambient voice messages:
- "Welcome to the Winter Release."
- "This is our Spring Ethics Update."
- "You're listening to the Solstice Reflection."

Embedded on homepage, podcast feed, or compliance hub.

---

## 5. Compliance Integration

The voice is not just UX — it is a **compliance accessibility feature**:

| Regulation | How Voice Helps |
|-----------|-----------------|
| **WCAG 2.1 AA** | Audio narration of text content for accessibility (screen reader alternative) |
| **GDPR Art. 12** | Information provided "in a concise, transparent, intelligible and easily accessible form" — voice narration makes policies accessible to non-readers |
| **EU AI Act Art. 13** | Transparency: users informed they're interacting with an AI system — voice narration of system status makes this audible and unmissable |
| **EU AI Act Art. 50** | Transparency obligations for AI systems — Nordic Calm voice can include AI disclosure in narration |

---

## 6. Implementation Notes

- All voice content authored in SSML
- Audio rendered via Azure TTS (en-GB, ThomasNeural base; multilingual expansion per §4.5)
- Hosted on secure CDN with WCAG-compliant playback
- Iconography and glyphs integrated into design system
- Pre-rendered audio for static content; dynamic SSML generation for Future Self narration

---

## 7. Relationship to Other Documents

| Document | Relationship |
|----------|-------------|
| SommerCoPilot Blueprint | Nordic Calm IS the Voice of the Future Self — same voice, different context |
| Consolidated Compliance Book | Voice narrates compliance content (privacy policy, terms of use) — makes trust audible |
| Sovereign Layer Architecture | Voice operates at the Operator Layer (L-OP) — it is how the system speaks TO the operator |
| Digital Twin Framework | Voice can narrate behavioral insights and recommendations (§1.8 of DT Framework) |

---

## Document Version

- **Source:** Voice_NordicCalm_Integration_Framework.pdf (3 pages)
- **This document:** Structured, annotated with compliance integration and architecture mapping
- **Date prepared:** 06 August 2026
- **Prepared by:** Solas (Archivist) under direction of Michael Sommer

---

*The Nordic Calm voice transforms By Sommer into a living, audible archive — where every section speaks, every policy breathes, and every user is heard. It is not a feature. It is a trust signal.*

---

## 8. GDPR Compliance for Voice Processing

### 8.1 Consent for Voice Playback (Art. 7)

All voice narration requires explicit user opt-in:
- **Public surfaces (bysommer.net, imsor.com):** Audio icon with tooltip "Listen in Nordic Calm voice." User must click to initiate playback. No auto-play.
- **SommerCoPilot (Future Self):** User is prompted "Would you like to hear from your future self?" before any voice narration. User must explicitly confirm.
- **Consent record:** Each playback session is logged to s.net with timestamp, user_ref, content reference, and consent status. Consent is revocable at any time.
- **Children:** No voice processing for users under 13 (COPPA/GDPR Art. 8 age threshold). Age verification via parent entity (SommerUsers.role).

### 8.2 Azure TTS as Third-Party Processor (Art. 28)

The Nordic Calm voice is rendered via Microsoft Azure Text-to-Speech (Cognitive Services). This constitutes a third-party data processing relationship:

| Art. 28 Requirement | Implementation |
|---------------------|----------------|
| **Data Processing Agreement (DPA)** | Azure Cognitive Services operates under Microsoft's standard DPA and EU Data Boundary. SSML text is processed in EU region. |
| **Processing scope** | Only SSML text strings are transmitted to Azure for rendering. No biometric data, no user identity, no audio recordings of the user. Azure processes the text → returns synthesized audio. |
| **Sub-processor disclosure** | Microsoft Azure disclosed as sub-processor in privacy policy. Listed in Compliance Book §3. |
| **Data residency** | Azure TTS processing pinned to EU region (West Europe) for DK pilot. No data leaves EU jurisdiction. |
| **Retention by processor** | Azure Cognitive Services does not retain SSML input or audio output beyond the rendering session (confirmed per Azure data residency documentation). |

**Key distinction:** The system sends *text* to Azure (SSML scripts), not *user voice data*. Azure TTS is a text-to-speech service, not a speech-to-text service. No user voice biometrics are collected, processed, or transmitted.

### 8.3 Voice Biometrics Clarification (Art. 9)

The Nordic Calm voice is **synthesized output**, not biometric identification:

- The system **does not** collect, process, or store user voice recordings.
- The system **does not** perform voice biometric identification or verification.
- The system **does not** perform speaker recognition or voice fingerprinting.
- The only voice is the *synthesized* Nordic Calm voice (ThomasNeural/ChristelNeural/etc.) — a synthetic TTS output, not a recording of any person.

**GDPR Art. 9 classification:** Not applicable. No special category biometric data is processed. The synthesized voice is generated output, not biometric input.

### 8.4 Accessibility Compliance (WCAG 2.1 AA)

| WCAG Criterion | Implementation | Verification |
|----------------|----------------|-------------|
| **1.2.2 Captions (AA)** | Voice-narrated content includes text transcript toggle | Manual audit per content section |
| **1.2.3 Audio Description (AA)** | Voice narration IS the audio description of visual content | Inherent — voice describes what's on screen |
| **1.4.2 Audio Control (A)** | Play/pause/stop controls visible; no auto-play; volume adjustable | UI component test |
| **1.4.7 Low Background Noise (AAA)** | No background music during voice narration (or ≥20dB SNR if ambient) | Audio QA per release |
| **2.1.1 Keyboard (A)** | All voice playback controls keyboard-accessible | Keyboard navigation test |
| **4.1.2 Name, Role, Value (A)** | ARIA labels on all audio controls ("Listen to this section," "Pause narration") | Screen reader test |

**Testing protocol:** WCAG compliance verified via automated scan (axe-core) + manual screen reader test (NVDA + VoiceOver) per content release cycle.

---

## 9. Data Retention for Voice Assets

| Asset | Retention | Basis |
|-------|-----------|-------|
| Pre-rendered audio (public surfaces) | Indefinite (content asset) | Art. 6(1)(f) — legitimate interest; publicly accessible content |
| Dynamic SSML scripts (SommerCoPilot) | Tied to glyph lifecycle (see SommerCoPilot §15) | Art. 5(1)(e) — storage limitation |
| Azure TTS processing logs | Not retained by By Sommer (Azure-side only) | Art. 28 — processor bound by DPA |
| Consent records (voice playback) | Duration + 3 years | Art. 7(1) — demonstrable consent |
| Transcript files | Same retention as associated audio | Tied to parent asset |

---

## Document Version (Updated)

- **Source:** Voice_NordicCalm_Integration_Framework.pdf (3 pages)
- **This document:** Structured, annotated with compliance integration, GDPR Art. 7/9/28, WCAG 2.1 AA testing, data retention, and architecture mapping
- **Status:** Execution-ready (Pass 3 consolidation — 06 August 2026)
- **Prepared by:** Solas (Archivist) under direction of Michael Sommer

---

## 10. SommerCoPilot Voice Integration (Updated per Pass 4)

### 10.1 On-Device Keyword Spotting

Per GDPR Art. 7 consent and Art. 5(1)(c) data minimization:

- **Raw audio buffering occurs locally** on the client device. No continuous audio streaming to servers.
- **Audio telemetry is only streamed upstream** upon detection of the local wake-word (keyword spotting model runs on-device).
- **Raw voice streams are discarded immediately** following acoustic-to-text transformation and pitch/tone inference.
- **Only abstract vector features** (pitch drift, cadence delta) are retained for emotional resonance modeling — no raw audio, no voice biometrics, no speaker identification.

### 10.2 Voice Processing Consent Schema

Stored on user profile as timestamped proof:

```json
{
  "voice_processing_consent": true,
  "consent_timestamp": "2026-08-06T14:42:00Z",
  "consent_scope": "nordic_calm_playback + future_self_narration",
  "withdrawable": true,
  "snet_log_ref": "snet:0x8b4c...f2a1"
}
```

### 10.3 Edge Fallback TTS

For high-privacy or offline scenarios, a local edge TTS model is available:
- No data transmitted to any external processor when edge model is active
- Same Nordic Calm voice profile, rendered locally
- Quality slightly reduced vs. Azure TTS but maintains compliance posture for air-gapped deployments
