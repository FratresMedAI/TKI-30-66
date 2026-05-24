# Annex B — Key Performance Parameter (KPP) Targets

**Document ID:** TKI-30-66 / ANX-B  
**Version:** 0.3.0  
**Status:** Conceptual — not validated

Traceability: [02 — Operational Requirements](../docs/02-operational-requirements.md)

**Design priority:** Reliability thresholds take precedence over cost and peak performance when in conflict.

---

## KPP Summary Table

| ID | Parameter | Threshold (T) | Objective (O) | Unit | Verification Method |
|----|-----------|---------------|---------------|------|---------------------|
| KPP-01 | Launcher mass (empty, with tracker) | ≤ 8.5 | ≤ 8.0 | kg | Weighing / design review |
| KPP-02 | Ready round mass | ≤ 3.0 | ≤ 2.5 | kg | Weighing / design review |
| KPP-03 | Ready round overall length | 285–320 | ~305 | mm | Dimensional inspection |
| KPP-04 | Nominal caliber | 40–66 envelope | 50 | mm | Design review |
| KPP-05 | Effective range vs. 2–25 kg UAS | ≥ 150 / ≥ 600 | ≥ 800 | m | Live fire / simulation |
| KPP-06 | Single-shot Pk vs. cooperative hover | ≥ 0.40 | ≥ 0.60 | — | Live fire test series |
| KPP-07 | Single-shot Pk vs. crossing target | ≥ 0.20 | ≥ 0.35 | — | Live fire test series |
| KPP-08 | Time to first shot from ready carry | ≤ 20 | ≤ 15 | s | Timed field drill |
| KPP-09 | Reload time (trained gunner) | ≤ 15 | ≤ 10 | s | Timed field drill |
| KPP-10 | Sustained rate of fire (2-man team) | ≥ 3 | ≥ 4–6 | rounds / 2 min | Field exercise |
| KPP-11 | Rear danger zone (backblast) | ≤ 40 | ≤ 30 | m | Safety test / analysis |
| KPP-12 | Guidance mode | Launcher IR + quad-cell round IR (LOBL) | No dual-mode | — | Design review / test |
| KPP-13 | Round seeker mass | ≤ 300 | ≤ 200 | g | Weighing |
| KPP-14 | Cost per round (production) | ≤ $500 | ≤ $350 | USD | Cost analysis (secondary to reliability) |
| KPP-15 | Launcher service life | ≥ 500 | ≥ 1000 | rounds | Endurance test |
| KPP-16 | LOBL lock time | ≤ 8 | ≤ 5 | s | Timed test vs. representative UAS |
| KPP-17 | Operating temperature | -25 to +45 | -30 to +50 | °C | Environmental test |

---

## Reliability KPPs (Primary)

| ID | Parameter | Threshold (T) | Objective (O) | Unit | Verification Method |
|----|-----------|---------------|---------------|------|---------------------|
| R-KPP-01 | Round guidance functional at launch | ≥ 98.0 | ≥ 99.5 | % | Sample BIT + live fire |
| R-KPP-02 | Pre-fire BIT blocks failed rounds | 100 | 100 | % | Fault injection test |
| R-KPP-03 | Fin deployment success | ≥ 99.0 | ≥ 99.5 | % | High-speed video / live fire |
| R-KPP-04 | Launcher MRBF (critical failure) | ≥ 300 | ≥ 500 | rounds | Reliability growth test |
| R-KPP-05 | Dud rate (no guidance / no propulsion) | ≤ 2.0 | ≤ 0.5 | % | Lot acceptance test |
| R-KPP-06 | Mission-capable rate (30-day field) | ≥ 93 | ≥ 97 | % | Field exercise |
| R-KPP-07 | Tracker module field replacement | ≤ 10 | ≤ 5 | min | Timed maintenance drill |
| R-KPP-08 | Round shelf life (guidance function) | ≥ 10 | ≥ 15 | years | Accelerated aging test |

---

## Key System Attributes (KSAs)

| ID | Attribute | Requirement | Notes |
|----|-----------|-------------|-------|
| KSA-01 | Man-portability | 2-man team: launcher + ≥ 4 rounds | Gunner + ammo bearer |
| KSA-02 | Training burden | Qualification ≤ Carl Gustaf basic duration | Emphasis on BIT and no-fire procedures |
| KSA-03 | Logistics footprint | Sealed factory rounds; no unit round repair | Bad rounds discarded |
| KSA-04 | Tracker integration | Field-replaceable module in launcher | Single LRU for guidance failures |
| KSA-05 | Night employment | IR tracker + quad-cell seeker | Passive thermal track |
| KSA-06 | Collateral effects | Kinetic rod: localized | ROE-dependent |
| KSA-07 | Maintenance echelon | Unit-level launcher BIT + module swap | Factory round QA only |
| KSA-08 | **Reliability philosophy** | **Simplicity over feature count** | Reject dual-mode / radar baseline |

---

## Measures of Effectiveness (MOE)

| MOE | Definition | Notional Target |
|-----|------------|-----------------|
| MOE-01 | Threat neutralization | 1 UAS per successful hit |
| MOE-02 | Engagement timeline | Cue-to-fire ≤ 30 s |
| MOE-03 | Ammunition efficiency | ≤ 2 rounds/kill (hover, trained team) |
| MOE-04 | **Guided shot reliability** | **≥ 98% of BIT-passed rounds guide to terminus** | 
| MOE-05 | Availability | ≥ 93% mission-capable rate |

---

## Reliability Verification Plan

| Phase | Activity |
|-------|----------|
| Phase 1 | Fault injection on BIT; fin deployment stat sample (n ≥ 100) |
| Phase 2 | Launch shock survivability; environmental soak |
| Phase 3 | Guided live fire reliability growth (≥ 200 rounds) |
| Phase 4 | Field MTBF and dud-rate lot acceptance |

---

## Related Documents

- [02 — Operational Requirements](../docs/02-operational-requirements.md)
- [05 — Key Design Trades](../docs/05-key-design-trades.md)
- [07 — Limitations and Risks](../docs/07-limitations-and-risks.md)
