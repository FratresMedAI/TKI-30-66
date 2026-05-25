# RADR — Recoilless Anti-Drone Rocket

**Squad / SOF Terminal Counter-UAS — 60 mm Class**

**RADR** is a lightweight, reusable **60 mm** shoulder-fired rocket system designed as a **squad and SOF terminal-layer** weapon. It fires an **18-inch** rocket with a **300 × 7 mm dense alloy cube flak** warhead, **onboard IR fire-and-forget** seeker, and **progressive-burn** motor optimized for **speed-to-target** rather than high off-boresight maneuvering.

**Status:** Phase 0 — Conceptual  
**Version:** 0.8.0

---

## Core Vision

RADR gives dismounted teams a **fast, reliable, reloadable** answer to close-in UAS threats when machine guns are short and SAM is too heavy to allocate. The gunner **rough-aims**, the seeker **locks** (audible tone), and the rocket **closes quickly** with **small nose-canard corrections** only. At **~20 ft**, **proximity fuze** actuation (with **timed backup**) releases a **forward cone** of **300 rough-edged alloy cubes**. The burster **disperses** — the **cubes kill**.

**Philosophy:** Speed is the primary defense · KISS + rugged · One-person reload · Honest capability ceiling.

---

## Primary Threats

| Threat class | Examples / notes |
|--------------|------------------|
| **FPV kamikaze drones** | Close-in terminal attack; high closure rate |
| **Small-to-medium quadcopters** | ISR, spotter, and light attack platforms |
| **Loitering munitions** | Orbiting or diving terminal engagement |
| **Terrain-matching / GPS-denied gliders** | Low-signature glide profiles (e.g. Hornet / “Martian” class) |
| **Group 1–2 UAS (general)** | Swarm and interdiction attacks in the close fight |

RADR is **not** sized for large Group 3+ platforms or long-range aircraft.

---

## Locked Specifications

| Item | Spec | Status |
|------|------|--------|
| Caliber | 60 mm | Locked |
| Rocket length | 18 in (457 mm) | Locked |
| Launcher length | 36 in (914 mm) | Locked |
| Rocket mass | ≤ 3.5 kg | Locked |
| Launcher empty mass | ≤ 5.5 kg | Locked |
| Warhead | 300 × 7 mm dense alloy rough-edged cubes | Locked |
| Pattern | Forward cone, ~10–12 ft wide @ ~20 ft | Locked |
| Fuze | Proximity primary + timed backup | Locked |
| Seeker | 100 mm IR fire-and-forget | Locked |
| Guidance | Low-maneuver; small movable canards near nose | Locked |
| Fins | 4 swept spring-loaded at base; deploy on exit | Locked |
| Motor | Progressive burn (lower thrust 1–2 s, then ramp) | Locked |
| Range goal | 1000 m effective | Locked |
| Backblast | ≤ 10 yards (30 ft) | Locked |
| Protective tube | Ravioli-can + pull-off cap (soldier removes on load) | Locked |
| Breech | Gustav-style flip; spring bolt + positive lock | Locked |
| Controls | Front = seeker + tone; rear = fire (front held) | Locked |
| CoG | Slightly rear-biased | Locked |

---

## Operational Flow

**Open breech** → **Pop cap off tube** → **Load tube** → **Close breech** → **Hold front trigger** (seeker tone at lock) → **Pull rear trigger** while holding front → **Fire** → **Open breech** → **Empty tube drops out**.

**Carry:** Launcher + one round ≤ **9.0 kg** — one person can reload.

---

## Comparison Snapshot

| | RADR | Carl Gustaf M4 | FIM-92 Stinger |
|--|------|----------------|----------------|
| Role | Terminal C-UAS flak | Multi-role | MANPADS |
| Launcher | ≤ 5.5 kg, 36 in | ~6.6 kg | ~15 kg |
| Round | ≤ 3.5 kg, 18 in | ~3.2 kg | ~10.1 kg |
| Guidance | IR F&F, low-maneuver | Unguided | High-agility IR |
| Range goal | 1000 m | ammo-dependent | 4000+ m |
| Backblast | 10 yd (30 ft) | ~60 m class | moderate |

Data: [`data/baseline_systems.json`](data/baseline_systems.json)

---

## Out of Scope (Removed Concepts)

Laser beam-riding · Launcher-tracked guidance · Kinetic penetrator rod · High off-boresight agility · General-issue every-rifleman distribution

---

## Document Map

| # | Document |
|---|----------|
| 01 | [Concept Overview](docs/01-concept-overview.md) |
| 02 | [Operational Requirements](docs/02-operational-requirements.md) |
| 03 | [Design Constraints](docs/03-design-constraints.md) |
| 04 | [CONOPS / Use Cases](docs/04-conops-use-cases.md) |
| 05 | [Key Design Trades](docs/05-key-design-trades.md) |
| 06 | [System Description](docs/06-system-description.md) |
| 07 | [Limitations and Risks](docs/07-limitations-and-risks.md) |
| 08 | [Layered Defense Integration](docs/08-layered-defense-integration.md) |

Annexes A–E: [`annexes/`](annexes/)

---

## Open Questions

- Live-fire Pk at 1000 m by threat class (hover vs. crossing vs. glide)  
- Progressive grain vs. measured backblast inside 10 yd zone  
- Cube alloy finalization (dense Ti/steel baseline)  
- Sight configuration (if added beyond iron/holo study)  

---

## Disclaimer

Conceptual engineering study only. Performance figures are **notional** until tested. Not authorization for procurement or use.
