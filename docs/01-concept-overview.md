# 01 — Concept Overview

**Document ID:** TKI-30-66 / DOC-01  
**Version:** 0.3.0  
**Status:** Conceptual

---

## Purpose

TKI-30-66 (internal codename: **Splash**) is a conceptual shoulder-fired weapon system designed to provide squad- and SOF-level units with a man-portable, terminal-layer kinetic defeat capability against small-to-medium unmanned aircraft systems (UAS).

The system addresses a specific gap: when higher-echelon counter-UAS assets are saturated, unavailable, jammed, or overkill for the threat, dismounted teams need a low-logistics, high-volume-of-fire option that is more effective than small arms but cheaper and more portable than missile interceptors.

---

## Problem Statement

Modern conflicts demonstrate that small UAS are cheap, abundant, and difficult to counter at every echelon simultaneously. Squad and SOF elements face:

- **ISR drones** hovering or orbiting at low altitude, exposing position and movement
- **FPV and loitering munitions** conducting terminal attacks against personnel and vehicles
- **Swarm and high-volume threats** that exhaust limited SHORAD and EW resources
- **Electronic warfare saturation** that degrades RF-dependent defeat mechanisms
- **Logistics constraints** that prevent every patrol from carrying missile-class interceptors

Existing squad options are inadequate:

| Option | Limitation |
|--------|------------|
| Small arms (5.56 / 7.62) | Low Pk vs. maneuvering targets; high ammunition expenditure |
| MANPADS (Stinger-class) | Too heavy, too expensive per shot, wrong target set for small UAS |
| Vehicle SHORAD | Not always present; not dismount-portable |
| EW / jamming | Countered by autonomous or fiber-optic UAS; spectrum contested |
| Handheld jammers | Short range; power and legal constraints |

TKI-30-66 proposes a middle path: a **reusable, Gustav-like launcher** firing **IR-guided kinetic rounds** optimized for drone-class targets at close-to-mid range.

---

## Core Concept

### Launcher

A reusable, shoulder-fired, recoilless-style launcher with flip-open breech reloading—operationally familiar to users of the Carl Gustaf system but scaled down to the 40–66 mm class (50 mm nominal baseline).

The launcher carries a **compact integrated IR tracking sight** (Javelin CLU analogue): the reusable "brain and eyes" of the system. The gunner acquires and tracks the target through this sight before launch.

### Round

Approximately one foot long (~305 mm / 12 in), mass ~2.5 kg, containing:

- Propulsion system with low-to-moderate backblast mitigation
- High-velocity kinetic payload (unitary metal rod baseline; flechette pack variant)
- **Compact IR seeker** — rugged quad-cell detector only (no imaging focal-plane array)
- Spring-loaded deployable fins for post-launch stabilization

### Guidance

**No laser beam-riding.** Guidance uses a Javelin-like split architecture optimized for **reliability**:

1. **Launcher-mounted IR tracker** (reusable) — gunner acquires target; system runs pre-fire built-in test (BIT) on round seeker via breech contact
2. **Round-mounted quad-cell IR seeker** (expendable) — simplest viable homing head; terminal guidance only after LOBL

**Rejected for baseline (reliability):** imaging IR FPAs, FMCW radar seekers, dual-mode guidance, and flechette variant SKUs — each adds failure modes or logistics complexity.

**Phase 2 (only if required):** obscured-condition seeker study — radar or multi-band IR — subject to reliability review. Not default.

Expensive, testable electronics stay in the reusable launcher. The round carries the minimum sensor needed to finish the engagement.

### Stabilization

Rifled barrel imparts initial spin; umbrella-style mechanical fins deploy and lock after muzzle exit. See [Annex D — Projectile Stabilization](../annexes/D-projectile-stabilization.md).

---

## Design Philosophy

| Principle | Application |
|-----------|-------------|
| **Reliability first** | Pre-fire BIT; no shot unless seeker checks good; conservative propellant load |
| **KISS** | Quad-cell IR on round; mechanical fin lock; no radar, no imaging FPA on baseline |
| **Test before fire** | Launcher BIT on every round at breech contact; go/no-go indicator |
| **Man-portable** | Launcher ≤ 8.5 kg; 2-man team carries launcher + 4+ rounds |
| **Low logistics** | Sealed factory rounds; unit maintains launcher only |
| **Mechanical redundancy** | Dual springs per fin; mechanical breech interlock |
| **Low backblast** | Moderate muzzle velocity (~650 m/s class) reduces component shock |
| **Honest capability** | Terminal-layer, close-in; reliability over spec-sheet range |

---

## What TKI-30-66 Is

- A terminal kinetic effector for small-to-medium UAS at 150–600 m (800 m aspirational)
- A squad/SOF organic asset with integrated IR tracking — no separate designator required
- A complement to layered C-UAS architecture, not a replacement for SHORAD or EW
- A reusable system with reloadable rounds, reducing per-engagement waste vs. disposable tubes

## What TKI-30-66 Is Not

- A Stinger or MANPADS replacement
- A long-range area-defense interceptor
- A laser-designator-dependent beam-rider
- An all-weather, autonomous search-and-destroy system
- A swarm-defeat solution on its own
- A validated, fielded, or procurement-ready system

---

## Internal Codename

**Splash** is used informally within this project to refer to the TKI-30-66 concept. It is not a program of record designation.

---

## Related Documents

| Document | Purpose |
|----------|---------|
| [02 — Operational Requirements](02-operational-requirements.md) | KPPs and MOEs |
| [06 — System Description](06-system-description.md) | Hardware overview |
| [07 — Limitations and Risks](07-limitations-and-risks.md) | Honest capability ceiling |
| [Annex A — Baseline Comparison](../annexes/A-baseline-comparison.md) | System comparisons |

---

[Next: Operational Requirements →](02-operational-requirements.md)
