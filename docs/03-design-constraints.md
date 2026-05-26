# 03 — Design Constraints

**Document ID:** RADR / DOC-03  
**Version:** 1.6.0  
**Status:** Conceptual

---

## Physical

| Constraint | Limit |
|------------|-------|
| Caliber | **60 mm** |
| Rocket OAL | **457 mm (18 in)** |
| Rocket mass | **≤ 3.5 kg** |
| Launcher OAL | **1016 mm (40 in)** |
| Launcher mass (empty) | **≤ 5.5 kg** |
| System (launcher + 1 round) | **≤ 9.0 kg** |
| CoG | **Slightly rear-biased** |

---

## Warhead / Fuze

| Constraint | Requirement |
|------------|-------------|
| Fragments | **300 × 7 mm** dense alloy, **rough-edged** |
| Pattern | **Forward cone**, ~10–12 ft @ ~20 ft |
| Fuze | **Radar or millimeter-wave proximity (primary) + timed backup** |
| Burster | **Pyrotechnic dispersal charge** (forward-biased cone) |

---

## Flight / Guidance

| Constraint | Requirement |
|------------|-------------|
| Seeker | **100 mm** IR F&F |
| Guidance class | **Moderate-maneuver** (not high off-boresight) |
| Canards | Small, movable, **near nose** |
| Fins | **4** swept spring-loaded at **base**; **mechanical lock** once deployed |
| Motor | Solid rocket; **Evolution Space** high-rate tactical propellant; **mildly progressive** grain — **750–850 N** first **1–2 s**, ramp to **1050–1150 N**; **2950–3050 N·s** total impulse; **~3.3 s** burn; low-signature goal |
| Off-boresight | **Not** high off-boresight |

---

## Launcher

| Item | Requirement |
|------|-------------|
| Round | **Alloy** protective tube; **manual pull-off cap** removed by soldier on load |
| Breech | **Gustav-style flip**; spring-loaded bolt; **positive lock** |
| Triggers | Front = seeker + tone; rear = fire (front held) |
| Retention stop | Mechanical bore stop; release only when breech closed + front held + ready tone |
| Sight | Integrated **digital cam sight**; **smooth 1×–20×** zoom; fold-out **~4 in** display; **+ / −** on foregrip (wired to sight + screen) |
| Sighting employment | **RPG-style shouldering**; **no cheek weld**; front = seeker/tone, rear = fire | Locked |
| Ergonomics | M1 Bazooka layout; 40 in OAL; **no shoulder stock** |
| Backblast | **≤ 10 yards (30 ft)** rear |
| Seating confirmation | Pressure + electrical contacts |
| Post-fire | Empty tube drops on breech open |

Mechanical baseline: [Annex F](../annexes/F-employment-and-breech.md#breech-mechanism) · [Retention stop](../annexes/F-employment-and-breech.md#rocket-retention-stop)

---

## Threat-Driven Constraints

Design shall account for:

- High closure **FPV kamikaze** engagements  
- Small thermal signature **gliding** targets  
- Brief exposure windows in **swarm** scenarios  

---

[← Operational Requirements](02-operational-requirements.md) | [Next: CONOPS →](04-conops-use-cases.md)
