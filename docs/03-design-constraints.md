# 03 — Design Constraints

**Document ID:** TKI-30-66 / DOC-03  
**Version:** 0.3.0  
**Status:** Conceptual

---

## Overview

This document defines the physical, interface, environmental, cost, safety, and logistics constraints that bound TKI-30-66 design space.

---

## Physical / Form Factor

| Constraint | Limit | Notes |
|------------|-------|-------|
| Employment posture | Shoulder-fired, standing or kneeling | No tripod required for baseline |
| Launcher length (carry) | ≤ 950 mm | Includes IR tracker housing |
| Breech operation | Flip-open rear breech | Gustav-like reload sequence |
| Round packaging | ~305 mm OAL × ~50 mm diameter | Fits standard assault pack cells |
| Rounds per ammo bearer | ≥ 2 in pack + 1 ready | Without dedicated munitions carrier |
| Launcher + 4 rounds | ≤ 24 kg total team load | Tracker mass included in launcher |
| IR tracking sight | Integrated in launcher | Reusable; not a separate carry item |

---

## Interface / Compatibility

| Constraint | Requirement |
|------------|-------------|
| Round-launcher interface | Mechanical breech lock + brief electrical contact for LOBL cue |
| Squad communications | Optional radio cueing; not required for baseline fire |
| Vehicle integration | None required; system is dismount-native |
| Detection systems | May receive external cue (acoustic/optical); no hard interface required |
| Laser designator | **Not required** — system does not use beam-riding |

---

## Environmental Durability

| Parameter | Requirement | Design Impact |
|-----------|-------------|---------------|
| Operating temperature | -25 to +45 °C (objective: -30 to +50 °C) | IR sensor and battery materials |
| Storage temperature | -40 to +60 °C | Round seal integrity |
| Humidity / rain | Operable in light-to-moderate rain | Seeker window sealing; IR contrast may degrade |
| Dust / sand | Operable in arid conditions | Seeker window protection cap; breech seals |

**Known limitation:** Heavy rain, fog, and smoke degrade IR seeker performance. Phase 2 radar round variant addresses obscuration at additional cost.

---

## Cost and Producibility

| Constraint | Target |
|------------|--------|
| Round unit cost (10k+ qty) | ≤ $500 threshold; $350 objective (secondary to reliability) |
| Launcher unit cost | ≤ $10,000 (notional; includes IR tracker + BIT) |
| Round seeker cost | ≤ $180 at volume (reliability-qualified quad-cell) |
| Round QA | 100% factory BIT on every round |
| Launcher tracker | Field-replaceable LRU; ≤ 10 min unit-level swap |
| Manufacturing approach | Conventional rifled tube; reliability-screened IR components |
| Supply chain | NATO/US industrial base compatible |

---

## Safety / Backblast

| Constraint | Requirement |
|------------|-------------|
| Backblast class | Low-to-moderate (design priority) |
| Rear danger zone | ≤ 40 m threshold; ≤ 30 m objective |
| Fire from enclosure | **Not authorized** |
| Gunner positioning | Clear rear arc required |
| Ammo bearer positioning | Offset from backblast cone |

---

## Logistics / Training

| Constraint | Requirement |
|------------|-------------|
| Deployment echelon | Squad / fire team / SOF team |
| Crew size | 2 minimum (gunner + ammo bearer) |
| Qualification | Unit-level course; ≤ Gustaf basic duration |
| Round storage | With small-arms ammunition |
| Maintenance echelon | Unit-level for launcher and tracker calibration |
| ITAR / export | Legal review required before hardware development |

---

## Related Documents

| Document | Purpose |
|----------|---------|
| [02 — Operational Requirements](02-operational-requirements.md) | KPP targets |
| [05 — Key Design Trades](05-key-design-trades.md) | How constraints drive trades |

---

[← Operational Requirements](02-operational-requirements.md) | [Next: CONOPS / Use Cases →](04-conops-use-cases.md)
