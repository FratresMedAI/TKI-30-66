# TKI-30-66 ("Splash")

**Terminal Kinetic Interceptor — 30–66 mm Class**

A conceptual shoulder-fired, reusable recoilless-style launcher with integrated IR tracking, firing compact IR-guided kinetic rounds optimized for close-in defeat of small-to-medium unmanned aircraft systems (UAS) at the squad and SOF echelon.

**Status:** Phase 0 — Conceptual documentation baseline  
**Version:** 0.3.0  
**Internal codename:** Splash

---

## Description

TKI-30-66 is a man-portable, terminal-layer counter-UAS concept built around a Gustav-like flip-breech launcher in the 50 mm caliber class. The launcher carries a reusable IR tracking sight (Javelin CLU analogue); each ~305 mm (12 in) round carries a mini IR seeker and high-velocity kinetic rod payload, stabilized by rifling and spring-loaded deployable fins. A two-man team — gunner and ammo bearer — provides organic drone defeat when higher-echelon systems are saturated, unavailable, or overkill.

Design philosophy: **Reliability first, KISS, low backblast, low logistics, honest capability ceiling.** Cost and peak performance are traded away when they conflict with working every time.

---

## Quick Spec Card

| Parameter | TKI-30-66 (Splash) | M72 LAW | Carl Gustaf M4 | FGM-148 Javelin |
|-----------|-------------------|---------|----------------|-----------------|
| **Status** | Conceptual | Fielded | Fielded | Fielded |
| **Caliber** | 50 mm (40–66 mm envelope) | 66 mm | 84 mm | 127 mm |
| **Launcher mass** | ~8.0 kg (with tracker) | ~3.2 kg (disposable) | ~6.6 kg (empty) | ~6.4 kg (CLU) |
| **Round mass** | ~2.5 kg | ~3.2 kg | ~3.2 kg | ~11.8 kg |
| **Round length** | ~305 mm (12 in) | ~890 mm | ~460 mm | ~1100 mm |
| **Reusable** | Yes | No | Yes | Yes |
| **Guidance** | Launcher IR track + round IR seeker (LOBL) | Unguided | Unguided | IR imaging LOBL |
| **Primary role** | Terminal C-UAS (kinetic) | Anti-armor | Multi-role | Anti-armor |
| **Effective range** | 150–600 m (800 m aspirational) | 50–350 m | 100–1000 m | 500–4750 m |
| **Backblast** | Low–moderate (~30 m goal) | Moderate (~40 m) | Significant (~60 m) | Moderate (~25 m) |
| Cost per shot | ~$300–500 (goal) | ~$500 | ~$3,000 | ~$80,000 |
| **Team size** | 2 (gunner + ammo bearer) | 1 | 1–2 | 1–2 |

Structured comparison data: [`data/baseline_systems.json`](data/baseline_systems.json)

---

## Document Map

### Core Documents

| # | Document | Description |
|---|----------|-------------|
| 01 | [Concept Overview](docs/01-concept-overview.md) | Purpose, problem statement, design philosophy |
| 02 | [Operational Requirements](docs/02-operational-requirements.md) | KPPs, MOEs, target set definition |
| 03 | [Design Constraints](docs/03-design-constraints.md) | Physical, safety, cost, and logistics limits |
| 04 | [CONOPS / Use Cases](docs/04-conops-use-cases.md) | Six squad/SOF employment scenarios |
| 05 | [Key Design Trades](docs/05-key-design-trades.md) | Engineering trade analysis and baselines |
| 06 | [System Description](docs/06-system-description.md) | Launcher, round, stabilization, employment |
| 07 | [Limitations and Risks](docs/07-limitations-and-risks.md) | Honest capability ceiling and risk register |
| 08 | [Layered Defense Integration](docs/08-layered-defense-integration.md) | C-UAS architecture placement |

### Annexes

| Annex | Document | Description |
|-------|----------|-------------|
| A | [Baseline Comparison](annexes/A-baseline-comparison.md) | Comparison to fielded and commercial systems |
| B | [KPP Targets](annexes/B-kpp-targets.md) | Full KPP/KSA/MOE tables with verification plan |
| C | [Trades Matrix](annexes/C-trades-matrix.md) | Design trade options and recommendations |
| D | [Projectile Stabilization](annexes/D-projectile-stabilization.md) | Rifling + deployable fin engineering detail |
| E | [References / Bibliography](annexes/E-references-bibliography.md) | Curated source references |

### Data

| File | Description |
|------|-------------|
| [`data/baseline_systems.json`](data/baseline_systems.json) | Structured system comparison data |

---

## Key Design Decisions

| Decision | Selection | Rationale |
|----------|-----------|-----------|
| **Design priority** | **Reliability over cost / peak performance** | Squad weapon must work when called; duds unacceptable |
| Launcher architecture | Reusable flip-breech + integrated IR tracker + pre-fire BIT | Smart electronics reusable, testable before every shot |
| Baseline caliber | 50 mm (40–66 mm envelope) | Balance of KE, mass, and backblast |
| Guidance (Phase 1) | Launcher IR tracker + rugged quad-cell IR on round (LOBL) | Simplest viable seeker; no imaging FPA or radar on baseline |
| Round electronics | Minimal — seeker + autopilot only; factory sealed | Fewer failure modes; no field repair |
| Pre-fire check | Mandatory breech-contact BIT; no-fire if seeker fail | Prevents expending duds |
| Guidance (Phase 2 option) | Mini FMCW radar round | **Deprioritized** — adds failure modes and RF complexity |
| Beam-riding / laser | **Rejected** | User requirement |
| Payload | Unitary kinetic rod | Best single-target Pk; lowest collateral |
| Stabilization | Rifled barrel + deployable locking fins (dual springs) | Mechanical redundancy on critical deployment |
| Warhead type | Kinetic (non-explosive) | ROE flexibility; reduced logistics burden |
| Propulsion | Moderate velocity (~650 m/s class) | Lower launch shock → higher seeker/fin reliability |
| Backblast priority | Low–moderate (≤ 30 m goal) | Safer squad employment vs. Gustaf class |
| Team organization | 2-man (gunner + ammo bearer) | No separate designator required |
| Flechette variant | Deferred | Additional SKU complexity hurts reliability/logistics |

---

## Reliability Targets (Notional)

| Metric | Threshold | Objective |
|--------|-----------|-----------|
| Round guidance function at launch | ≥ 98% | ≥ 99.5% |
| Fin deployment success | ≥ 99% | ≥ 99.5% |
| Launcher MRBF (critical failure) | ≥ 300 rounds | ≥ 500 rounds |
| Pre-fire BIT blocks failed rounds | 100% | 100% |
| Mission-capable rate (field) | ≥ 93% | ≥ 97% |

Full table: [Annex B — KPP Targets](annexes/B-kpp-targets.md)

## Open Questions

- **Backblast architecture:** Countermass vs. soft-launch hybrid ratio — pending Phase 1 ballistic test
- **Seeker tier:** Quad-cell IR locked as baseline; micro-bolometer rejected for reliability
- **Radar variant:** Deprioritized unless obscuration MOE overrides reliability priority
- **Pk validation:** No test data; all effectiveness figures are analytic placeholders
- **Export control:** ITAR/legal review required before any hardware development

---

## Disclaimer

**This is a conceptual engineering study.** TKI-30-66 ("Splash") is not a program of record, procured system, or validated weapon. All performance figures are notional targets subject to analysis and test. No endorsement by any government, military service, or manufacturer is implied or intended.

This documentation is provided for concept exploration and engineering discussion. Any transition to hardware development requires legal review (including ITAR/export control), safety qualification, and appropriate authority approval.

Propellant weapons carry inherent safety hazards including backblast, hearing injury, and ammunition handling risks. Conceptual descriptions do not constitute training or authorization for use.

---

## Getting Started

Begin with [01 — Concept Overview](docs/01-concept-overview.md) for the problem statement and design philosophy, then proceed through the numbered documents in order.

For quick reference on system comparisons, see [Annex A — Baseline Comparison](annexes/A-baseline-comparison.md). For engineering trade details, see [05 — Key Design Trades](docs/05-key-design-trades.md) and [Annex C — Trades Matrix](annexes/C-trades-matrix.md).
