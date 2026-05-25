# RADR — Recoilless Anti-Drone Rocket

**Squad / SOF Terminal Counter-UAS — 60 mm Class**

**RADR** is a lightweight, reusable **60 mm** shoulder-fired **recoilless** rocket system for **squad and SOF** as a **simple, rugged terminal-layer** counter-UAS weapon against **Group 1–2** threats (FPV, quadcopters, loitering munitions, terrain-matching/gliding drones). It fires an **18-inch** rocket with **300 × 7 mm** dense alloy cube flak, **IR fire-and-forget** guidance, **radar or millimeter-wave proximity fuze**, and a **progressive-burn** solid motor — **speed-to-target** and **KISS** over high maneuverability.

**Status:** Phase 0 — Conceptual  
**Version:** 1.2.0

![RADR launcher concept — side profile](visuals/launcher/output/radr-bazooka-side-v5.png)

---

## Core Vision

RADR is a **lightweight, reusable** **60 mm** shoulder-fired **recoilless** rocket system for **squad and SOF** as a **terminal-layer counter-UAS** weapon. It emphasizes **speed-to-target**, **simplicity**, **one-person reload**, and **multiple layers of safety**.

Dismounted teams get a **fast, reliable, reloadable** answer when machine guns are short and SAM is too heavy to allocate. The gunner **rough-aims**, the seeker **locks** (audible tone), and the rocket **closes quickly** with **small nose-canard corrections** only. At **~20 ft**, **radar or millimeter-wave proximity** actuation (with **timed backup**) releases a **forward cone** of **300 rough-edged alloy cubes**. The burster **disperses** — the **cubes kill**.

**Philosophy:** Speed is the primary defense · KISS + rugged · One-person reload · Honest capability ceiling.

**Launcher look:** Modernized **M1 Bazooka** proportions — long slim tube, **matte camo**, **compact Gustav flip breech**, **dual triggers**, **no shoulder stock**; rear **padding** from pistol grip to breech only. See [visuals](visuals/README.md).

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
| Rocket mass (target) | ≤ 3.5 kg | Locked |
| Launcher empty mass (target) | ≤ 5.5 kg | Locked |
| Warhead | 300 × 7 mm dense alloy rough-edged cubes | Locked |
| Pattern | Forward cone, ~10–12 ft wide @ ~20 ft | Locked |
| Fuze | Radar or mm-wave proximity (primary) + timed backup | Locked |
| Motor | Solid rocket; Evolution Space high-rate tactical propellant; progressive grain | Locked |
| Seeker | 100 mm IR fire-and-forget | Locked |
| Guidance | Low-maneuver; small movable canards near nose | Locked |
| Fins | 4 swept spring-loaded at base; deploy on exit | Locked |
| Motor | Progressive burn (lower thrust 1–2 s, then ramp) | Locked |
| Range goal | 1000 m effective | Locked |
| Backblast | ≤ 10 yards (30 ft) | Locked |
| Protective tube | Ravioli-can + manual pull-off cap (soldier removes on load) | Locked |
| Breech | Gustav-style flip; spring bolt + positive lock | Locked |
| Controls | Front = seeker + tone; rear = fire (front held) | Locked |
| CoG | Slightly rear-biased | Locked |
| **Rocket retention stop** | Mechanical bore stop; disengages only when breech closed + front held + ready tone | Locked |

---

## Safety (Layers)

| Layer | Function |
|-------|----------|
| **Rocket retention stop** | Blocks rocket from sliding forward in bore when slung or carried; **releases** only when breech is **fully closed**, gunner **holds front trigger**, and seeker gives **ready tone**; **re-engages** if front trigger is released |
| **Breech deadbolt** | Positive mechanical lock when closed — no seeker or retention release until seated |
| **Dual-trigger interlock** | Rear fire blocked until lock tone; front must stay held through ignition |
| **No override** | No rear fire without tone; no seeker until tube seated |
| **Backblast discipline** | ≤ **10 yd (30 ft)** cleared to rear before every shot and before breech re-open |

---

## Operational Flow

1. **Open breech** (pull spring bolt, swing open)  
2. **Remove cap** from protective tube  
3. **Load tube** into launcher  
4. **Close breech** — auto-locks (deadbolt)  
5. **Hold front trigger** → seeker activates + **lock tone** (retention stop **disengages**)  
6. **Pull rear trigger** while holding front → **fire**  
7. **Open breech** → empty protective tube drops out  

**Carry:** Launcher + one round ≤ **9.0 kg** — one person can reload. Retention stop **engaged** whenever front trigger is not held (safe carry/sling).

**Mechanical detail:** [Annex F — Breech](annexes/F-employment-and-breech.md#breech-mechanism) · [Retention stop](annexes/F-employment-and-breech.md#rocket-retention-stop) · [Gunner sequence](annexes/F-employment-and-breech.md#loading-and-firing--gunners-sequence) · **Diagrams:** [DOC-06](docs/06-system-description.md#diagrams)

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

| Annex | Topic |
|-------|--------|
| A–E | [Baseline, KPPs, trades, stabilization, references](annexes/) |
| **F** | [Employment sequence & breech](annexes/F-employment-and-breech.md) |
| **G** | [Mass budget & CG](annexes/G-mass-and-center-of-gravity.md) |
| **H** | [Motor thrust curve](annexes/H-motor-progressive-burn.md) |

---

## Open Questions

- Live-fire Pk at 1000 m by threat class (hover vs. crossing vs. glide)  
- Progressive grain vs. measured backblast inside 10 yd zone  
- Cube alloy finalization (dense Ti/steel baseline)  
- Retention stop mechanism detail (spring/cam vs. solenoid assist) — function locked  
- Fuze baseline down-select: **radar proximity** vs. **millimeter-wave proximity** (one primary per round)  
- Evolution Space grain geometry vs. measured backblast inside 10 yd zone  

---

## Disclaimer

Conceptual engineering study only. Performance figures are **notional** until tested. Not authorization for procurement or use.
