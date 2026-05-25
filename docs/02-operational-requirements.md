# 02 — Operational Requirements

**Document ID:** RADR / DOC-02  
**Version:** 1.2.0  
**Status:** Conceptual

Annex B: [KPP Targets](../annexes/B-kpp-targets.md)

---

## Primary Mission

Provide **squad and SOF** units a **terminal-layer** defeat capability against **Group 1–2 UAS** at **150–1000 m** using a **speed-first** guided flak rocket.

---

## Threat Requirements

The system shall be designed to engage:

| ID | Threat | Priority |
|----|--------|----------|
| TH-01 | FPV kamikaze drones | High |
| TH-02 | Small-to-medium quadcopters | High |
| TH-03 | Loitering munitions | High |
| TH-04 | Terrain-matching / GPS-denied gliding UAS (Hornet / “Martian” class) | High |
| TH-05 | Other Group 1–2 UAS in swarm / interdiction roles | High |

**Out of threat set:** Group 3+ UAS, fixed-wing aircraft, armored ground targets.

---

## Locked KPPs

| Parameter | Threshold | Objective |
|-----------|-----------|-----------|
| Caliber | 60 mm | Locked |
| Rocket OAL | 457 mm (18 in) | Locked |
| Rocket mass | ≤ 3.5 kg | Locked |
| Launcher OAL | 1016 mm (40 in) | Locked |
| Launcher mass (empty) | ≤ 5.5 kg | Locked |
| System mass (launcher + 1 round) | ≤ 9.0 kg | Locked |
| Warhead | 300 × 7 mm dense alloy cubes | Locked |
| Pattern | Forward cone @ ~20 ft | ~10–12 ft wide |
| Fuze | Radar or mm-wave proximity + timed backup | Locked |
| Seeker | 100 mm IR F&F | Lock before launch |
| Guidance | Low-maneuver nose canards | Not high OBA |
| Fins | 4 spring-loaded swept | Deploy on exit |
| Motor | Evolution Space propellant; progressive burn (low 1–2 s, ramp) | Locked |
| Range | ≥ 800 m | **1000 m** effective |
| Backblast | ≤ 10 yd (30 ft) | Locked |
| Tube | Ravioli-can, pull-off cap | Locked |
| Breech | Gustav flip + positive lock | Locked |
| Controls | Dual-trigger + lock tone | Locked |
| CoG | Rear-biased | Locked |
| Rocket retention stop | Engaged when not armed; releases per interlock table | Locked |
| One-person reload | Required | — |
| Cost per rocket | ≤ $500 | ≤ $300 |

---

## Safety Requirements

| ID | Requirement | Verification (concept) |
|----|-------------|--------------------------|
| SAF-01 | Rocket shall not slide forward in bore during carry/sling unless retention stop is intentionally released | Mechanical stop + logic |
| SAF-02 | Retention stop shall disengage only when breech fully closed **and** front trigger held **and** seeker ready tone active | Interlock table — Annex F |
| SAF-03 | Retention stop shall re-engage when front trigger is released | Annex F |
| SAF-04 | Rear trigger shall not initiate launch without lock tone | Annex F |
| SAF-05 | Seeker shall not arm until tube seated (pressure + contacts) | Annex F |
| SAF-06 | Backblast danger zone ≤ 10 yd (30 ft) — cleared before fire and breech open | Locked |

---

## Employment Sequence (Required)

| Step | Gunner action | System response |
|------|---------------|-----------------|
| 1 | Open breech (pull spring bolt, swing open) | Rear trigger disabled; retention stop **engaged** |
| 2 | Remove pull-off cap from protective tube | Round exposed outside bore |
| 3 | Load tube into launcher | — |
| 4 | Close breech | Deadbolt locks; seat confirm |
| 5 | Hold front trigger | Seeker on; tone at lock; retention stop **disengages** |
| 6 | Pull rear trigger (front held) | Launch |
| 7 | Open breech after safe interval | Empty tube drops |

**Authoritative interlocks:** [Annex F](../annexes/F-employment-and-breech.md) — [Gunner sequence](../annexes/F-employment-and-breech.md#loading-and-firing--gunners-sequence) · [Retention stop](../annexes/F-employment-and-breech.md#rocket-retention-stop) · [Breech](../annexes/F-employment-and-breech.md#breech-mechanism)

---

## MOEs (Notional)

| MOE | Target |
|-----|--------|
| Mission kill vs. TH-01–TH-05 at 1000 m | TBD live fire |
| Fuze function (proximity primary or timed backup) | ≥ 99% |
| Time threat → fire | Minimize |
| Rockets per kill (hover quadcopter) | ≤ 2 (trained) |
| One-person carry/reload | ≤ 9.0 kg system |

---

## Assumptions

- Gunner can rough-aim within seeker FOV  
- Progressive motor achieves 1000 m class closure speed  
- Radar or mm-wave proximity + timed backup covers fuze reliability for forward-cone geometry at ~20 ft  

---

[← Concept Overview](01-concept-overview.md) | [Next: Design Constraints →](03-design-constraints.md)
