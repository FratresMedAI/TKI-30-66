# 03 — Design Constraints

**Document ID:** RADR / DOC-03  
**Version:** 1.1.0  
**Status:** Conceptual

---

## Physical

| Constraint | Limit |
|------------|-------|
| Caliber | **60 mm** |
| Rocket OAL | **457 mm (18 in)** |
| Rocket mass | **≤ 3.5 kg** |
| Launcher OAL | **914 mm (36 in)** |
| Launcher mass (empty) | **≤ 5.5 kg** |
| System (launcher + 1 round) | **≤ 9.0 kg** |
| CoG | **Slightly rear-biased** |

---

## Warhead / Fuze

| Constraint | Requirement |
|------------|-------------|
| Fragments | **300 × 7 mm** dense alloy, **rough-edged** |
| Pattern | **Forward cone**, ~10–12 ft @ ~20 ft |
| Fuze | **Proximity primary + timed backup** |
| Burster | Disperser only |

---

## Flight / Guidance

| Constraint | Requirement |
|------------|-------------|
| Seeker | **100 mm** IR F&F |
| Canards | Small, movable, **near nose** |
| Fins | **4** swept spring-loaded at **base** |
| Motor | Progressive: **lower thrust 1–2 s**, then ramp |
| Off-boresight | **Not** high off-boresight |

---

## Launcher

| Item | Requirement |
|------|-------------|
| Round | **Ravioli-can** tube; **pull-off cap** removed by soldier on load |
| Breech | **Gustav-style flip**; spring-loaded bolt; **positive lock** |
| Triggers | Front = seeker + tone; rear = fire (front held) |
| Retention stop | Mechanical bore stop; release only when breech closed + front held + ready tone |
| Ergonomics | M1 Bazooka layout; foregrip forward of sight; pistol grip aft; **no shoulder stock** |
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
