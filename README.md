# TKI-30-66 ("Splash")

**Terminal Counter-UAS — 30–66 mm Class**

A conceptual shoulder-fired, reusable recoilless-style launcher firing lightweight guided rockets with **titanium BB flak** warheads and **onboard fire-and-forget IR** guidance, optimized for close-in defeat of small-to-medium unmanned aircraft systems (UAS) at the squad and SOF echelon.

**Status:** Phase 0 — Conceptual documentation baseline  
**Version:** 0.4.0  
**Internal codename:** Splash

---

## Description

TKI-30-66 is a man-portable, terminal-layer counter-UAS concept built around a Gustav-like flip-breech launcher in the 50 mm caliber class. Each lightweight rocket (up to ~457 mm / 18 in) carries an onboard IR seeker (baby Stinger / Igla class, drone-optimized) and a **Ti BB flak** warhead that disperses a cloud of titanium ball bearings near the target — rocket-delivered flak, not a kinetic rod or penetrator. A two-man team — gunner and ammo bearer — provides organic drone defeat when higher-echelon systems are saturated, unavailable, or overkill.

Design philosophy: **KISS, lightweight, man-portable, relatively cheap per shot, low backblast, honest capability ceiling.**

---

## Quick Spec Card

| Parameter | TKI-30-66 (Splash) | M72 LAW | Carl Gustaf M4 | FIM-92 Stinger |
|-----------|-------------------|---------|----------------|----------------|
| **Status** | Conceptual | Fielded | Fielded | Fielded |
| **Caliber** | 50 mm (40–66 mm envelope) | 66 mm | 84 mm | 70 mm |
| **Launcher mass** | ~7.0 kg (empty) | ~3.2 kg (disposable) | ~6.6 kg (empty) | ~15.2 kg (system) |
| **Rocket mass** | ~2.3 kg (goal) | ~3.2 kg | ~3.2 kg | ~10.1 kg |
| **Rocket length** | ≤ 457 mm (18 in max) | ~890 mm | ~460 mm | ~1520 mm |
| **Reusable** | Yes | No | Yes | No (tube) |
| **Guidance** | Onboard IR, fire-and-forget | Unguided | Unguided | IR homing |
| **Warhead** | Ti BB flak dispersal | HEAT | Multi-role | Blast-frag |
| **Primary role** | Terminal C-UAS (flak) | Anti-armor | Multi-role | MANPADS |
| **Effective range** | 150–600 m (800 m aspirational) | 50–350 m | 100–1000 m | 500–4800 m |
| **Backblast** | Low–moderate (~30 m goal) | Moderate (~40 m) | Significant (~60 m) | Moderate (~15 m) |
| **Cost per shot** | ~$200–400 (goal) | ~$500 | ~$3,000 | ~$120,000 |
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
| 06 | [System Description](docs/06-system-description.md) | Launcher, rocket, warhead, employment |
| 07 | [Limitations and Risks](docs/07-limitations-and-risks.md) | Honest capability ceiling and risk register |
| 08 | [Layered Defense Integration](docs/08-layered-defense-integration.md) | C-UAS architecture placement |

### Annexes

| Annex | Document | Description |
|-------|----------|-------------|
| A | [Baseline Comparison](annexes/A-baseline-comparison.md) | Comparison to fielded and commercial systems |
| B | [KPP Targets](annexes/B-kpp-targets.md) | Full KPP/KSA/MOE tables with verification plan |
| C | [Trades Matrix](annexes/C-trades-matrix.md) | Design trade options and recommendations |
| D | [Projectile Stabilization](annexes/D-projectile-stabilization.md) | Rocket fin stabilization and flight |
| E | [References / Bibliography](annexes/E-references-bibliography.md) | Curated source references |

### Data

| File | Description |
|------|-------------|
| [`data/baseline_systems.json`](data/baseline_systems.json) | Structured system comparison data |

---

## Key Design Decisions

| Decision | Selection | Rationale |
|----------|-----------|-----------|
| Launcher architecture | Reusable flip-breech recoilless tube | Gustav-familiar; no integrated tracker |
| Baseline caliber | 50 mm (40–66 mm envelope) | Smaller/lighter than 84 mm Gustaf |
| Rocket size | ≤ 457 mm (18 in) OAL; minimum mass | User requirement; pack-compatible upper bound |
| Guidance | **Onboard IR, fire-and-forget** | Baby Stinger/Igla class; drone-optimized; no laser |
| Warhead | **Ti BB flak dispersal** | Rocket-delivered flak cloud; not rod/penetrator |
| Beam-riding / laser | **Rejected** | Not in concept |
| Launcher-tracked guidance / BIT | **Removed** | Superseded by onboard F&F seeker |
| Kinetic rod / flechette | **Rejected** | Superseded by Ti BB flak |
| Stabilization | Fin-stabilized rocket (smoothbore baseline) | Conventional rocket architecture |
| Backblast priority | Low–moderate (≤ 30 m goal) | Squad-safe employment |
| Team organization | 2-man (gunner + ammo bearer) | SOF/squad doctrine |
| Philosophy | KISS, lightweight, cheap per shot | Terminal close-in UAS |

---

## Effectiveness Notes (Notional)

| Topic | Expectation |
|-------|-------------|
| Kill mechanism | BB cloud damages rotors/structure — proximity defeat, not single-point penetrator |
| Pk vs. hover target | Moderate; depends on cloud coverage and fuze timing |
| Pk vs. crossing target | Lower than hover |
| Collateral | Ti BB hazard footprint — ROE-sensitive in urban use |

Full KPP tables: [Annex B — KPP Targets](annexes/B-kpp-targets.md)

---

## Open Questions

- **Dispersal fuze:** Proximity IR vs. timed vs. seeker-gated — not selected in baseline
- **BB count / cloud diameter:** Analytic placeholder only
- **Seeker tier:** Simplified imaging IR vs. rosette — cost/Pk trade TBD
- **Smoothbore vs. rifled launch tube:** Engineering TBD (Annex D)
- **Pk validation:** No test data; all figures notional

---

## Disclaimer

**This is a conceptual engineering study.** TKI-30-66 ("Splash") is not a program of record, procured system, or validated weapon. All performance figures are notional targets subject to analysis and test. No endorsement by any government, military service, or manufacturer is implied or intended.

Propellant weapons carry inherent safety hazards including backblast and fragment hazard downrange. Conceptual descriptions do not constitute training or authorization for use.

---

## Getting Started

Begin with [01 — Concept Overview](docs/01-concept-overview.md), then proceed through numbered documents in order.
