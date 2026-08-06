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
