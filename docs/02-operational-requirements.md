# 02 — Operational Requirements

**Document ID:** TKI-30-66 / DOC-02  
**Version:** 0.3.0  
**Status:** Conceptual

Full KPP tables: [Annex B — KPP Targets](../annexes/B-kpp-targets.md)

---

## Primary Mission

Provide dismounted squad and SOF elements with a **reliable**, man-portable capability to defeat small-to-medium UAS at close-to-mid range — guided rounds that function when fired, with failed rounds caught before launch.

---

## Key Performance Parameters (KPPs)

### Must-Have (Threshold)

| Parameter | Threshold | Rationale |
|-----------|-----------|-----------|
| Launcher mass (empty, with tracker) | ≤ 8.5 kg | Single gunner carry with standard combat load |
| Ready round mass | ≤ 3.0 kg | Ammo bearer carries 2–4 rounds in assault pack |
| Ready round length | 285–320 mm | ~1 ft; compatible with standard pack configuration |
| Nominal caliber | 40–66 mm envelope (50 mm baseline) | Balance of KE, mass, and backblast |
| Effective range vs. 2–25 kg UAS | ≥ 150 m (min) / ≥ 600 m (design) | Close-in terminal layer |
| Guidance | Launcher IR + quad-cell round IR (LOBL) + pre-fire BIT | No-fire on BIT fail |
| Round guidance reliability at launch | ≥ 98% | Failed rounds caught by BIT before fire |
| Pre-fire BIT catch rate | 100% | No launch on seeker fail |
| Fin deployment success | ≥ 99% | Dual springs per fin |
| Launcher MRBF (critical failure) | ≥ 300 rounds | Field-replaceable tracker module |
| Rear danger zone (backblast) | ≤ 40 m | Safer than Gustaf class for routine employment |
| Cost per round (production goal) | ≤ $500 | Secondary to reliability; reject lowest bidder |
| Launcher service life | ≥ 500 rounds | Reusable economics require durability |
| Lock-on before launch | Required | Gunner confirms seeker lock via launcher sight |

### Should-Have (Objective)

| Parameter | Objective | Rationale |
|-----------|-----------|-----------|
| Launcher mass (empty) | ≤ 8.0 kg | Reduce gunner fatigue |
| Ready round mass | ≤ 2.5 kg | Increase rounds per bearer |
| Effective range | ≥ 800 m (cooperative target, clear conditions) | Extended envelope when geometry permits |
| Single-shot Pk (hovering target) | ≥ 0.60 | Primary engagement mode |
| Single-shot Pk (crossing target, 90°) | ≥ 0.35 | Harder geometry; honest target |
| Time to first shot | ≤ 15 s from ready carry | Ambush responsiveness |
| Reload time | ≤ 10 s (trained gunner) | Volume of fire |
| Sustained rate of fire | 4–6 rounds / 2 min (2-man team) | Swarm response |
| Rear danger zone | ≤ 30 m | Gustaf-class improvement |
| Cost per round | ≤ $350 | Reliability-qualified supplier |
| Round guidance reliability | ≥ 99.5% | Lot acceptance testing |
| Mini radar seeker (Phase 2) | **Deprioritized** | Reliability review gate required |

---

## Secondary Requirements

| Requirement | Description |
|-------------|-------------|
| Night employment | IR tracker and seeker provide inherent night capability vs. thermal UAS signature |
| Training burden | Qualification course ≤ Carl Gustaf basic duration |
| Tracker interface | Integrated in launcher; no external designator |
| Environmental | Operate -25 to +45 °C (objective: -30 to +50 °C) |
| Storage / shelf life | ≥ 10 years sealed round storage; small-arms logistics chain |
| Maintenance | Unit-level launcher maintenance; round is sealed consumable |
| Safety | No fire-from-enclosure capability assumed or required |
| Signature | Passive IR tracker on launcher; active radar seeker (Phase 2 only) emits |

---

## Target Set Definition

| Target Class | Mass | Examples | Engagement Priority |
|--------------|------|----------|---------------------|
| Group 1 (small) | < 9 kg | Commercial quadcopters, FPV racing drones | Primary |
| Group 2 (medium) | 9–25 kg | Military ISR platforms, larger FPV | Primary |
| Group 3 (large) | > 25 kg | Tactical UAS | Secondary / opportunistic |
| Fixed-wing fast | Any | Racing-wing, cruise-type | Limited (crossing Pk low) |

TKI-30-66 is optimized for Groups 1–2 at moderate range. Group 3 and fast fixed-wing targets are not primary design drivers.

---

## Measures of Effectiveness (MOE)

| MOE | Metric | Notional Target |
|-----|--------|-----------------|
| Threat neutralization | UAS structurally defeated or mission-killed | 1 UAS per successful engagement |
| Engagement timeline | Detection cue to first round fired | ≤ 30 s with pre-cueing |
| Ammunition efficiency | Rounds expended per kill (trained team) | ≤ 2 avg. vs. cooperative hover |
| Collateral risk | Hazard radius vs. HE alternative | Significantly reduced (kinetic rod) |
| Operational availability | Mission-capable rate | ≥ 93% (≥ 97% objective) |

---

## Measures of Suitability (MOS)

| MOS | Metric | Target |
|-----|--------|--------|
| Carry burden | Total 2-man load (launcher + 4 rounds) | ≤ 24 kg |
| Setup time | Movement to ready posture | ≤ 30 s |
| Training retention | 6-month recertification pass rate | ≥ 80% |
| Safety | Catastrophic launcher failure rate | Zero in acceptance testing |

---

## Assumptions

1. Two-man team minimum: gunner + ammo bearer.
2. Target is visually or acoustically cued before engagement; launcher tracker does not autonomously search the battlespace.
3. UAS presents sufficient thermal contrast for IR lock (motor, battery, or airframe).
4. Engagement occurs in ROE-permitted kinetic environment.
5. No validated Pk data exists; all effectiveness figures are analytic placeholders.

---

## Related Documents

| Document | Purpose |
|----------|---------|
| [03 — Design Constraints](03-design-constraints.md) | Physical and logistics limits |
| [04 — CONOPS / Use Cases](04-conops-use-cases.md) | Operational scenarios |
| [Annex B — KPP Targets](../annexes/B-kpp-targets.md) | Full KPP/KSA tables |

---

[← Concept Overview](01-concept-overview.md) | [Next: Design Constraints →](03-design-constraints.md)
