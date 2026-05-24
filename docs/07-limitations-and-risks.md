# 07 — Limitations and Risks

**Document ID:** TKI-30-66 / DOC-07  
**Version:** 0.3.0  
**Status:** Conceptual

---

## Purpose

Honest assessment of what TKI-30-66 **cannot do well**, key risks, and vulnerability vectors.

---

## Capability Limitations

### Range and Target Set

| Limitation | Detail |
|------------|--------|
| Not a long-range interceptor | Effective envelope: 150–600 m; sharp drop-off beyond 800 m |
| Not effective vs. high-altitude UAS | Targets above ~500 m AGL with standoff are outside design center |
| Fast fixed-wing crossing targets | Low Pk (threshold 0.20); small seeker track rate limited |
| Group 3+ large UAS (> 25 kg) | Insufficient KE margin at range |
| Swarm saturation | One target per engagement cycle |

### Guidance and Environment

| Limitation | Detail |
|------------|--------|
| IR signature dependency | Low-thermal or cooled UAS difficult to lock; plastic airframes marginal |
| LOBL required before fire | Gunner must achieve lock; no snap-shot unguided mode in baseline |
| Not all-weather (IR baseline) | Heavy rain, fog, smoke degrade IR contrast and seeker performance |
| Mini seeker limitations | Not full imaging FPA; off-boresight and countermeasure discrimination limited |
| Phase 2 radar adds cost/signature | FMCW variant emits RF; vulnerable to EW and increases round cost |
| Flares / IR countermeasures | Simple flares may seduce cheap IR seeker (moderate CCM risk) |

### Physical and Safety

| Limitation | Detail |
|------------|--------|
| Backblast restricts employment | No enclosed-space fire |
| Direct hit required | Near-miss = no effect |
| Launcher tracker adds mass | ~8 kg vs. ~7 kg unguided tube |
| Tracker module failure | Grounds guided mode — field-replaceable LRU; ≤ 10 min swap |
| BIT false-pass / false-fail | Dud fired or good round discarded — factory QA + fault injection |
| Conservative velocity | Slightly reduced range vs. max propellant — accepted reliability trade |

### Logistics and Cost

| Limitation | Detail |
|------------|--------|
| Round cost vs. reliability spec | ~$250–500 per guided round at volume | Accepted — duds cost more than margin saved |
| No validated Pk data | All effectiveness bands are analytic placeholders |

---

## Risk Register

| ID | Risk | Likelihood | Impact | Mitigation |
|----|------|------------|--------|------------|
| R-01 | Fin deployment failure | Low | High (miss) | Redundant springs; QC; subscale test |
| R-02 | Seeker damage in bore | Low | High (miss) | Window protection; shock analysis |
| R-03 | Backblast injury | Medium | High | Training; SOP; danger zone enforcement |
| R-04 | IR lock failure (cold target) | Medium | Medium (miss) | Training; external cue; radar variant |
| R-05 | IR countermeasures (flares) | Medium | Medium (miss) | Seeker filtering; rapid TOF minimizes seduction window |
| R-06 | Obscuration degrades IR | Medium | Medium (miss) | EW layer; radar round variant (Phase 2) |
| R-07 | Swarm saturation | High | High (leakers) | Layered defense; multiple teams |
| R-08 | Launcher tracker module failure | Low | High (no guided fire) | Field-replaceable module; company-level spare LRU |
| R-13 | BIT false-pass (dud fired) | Low | High (miss + cost) | Factory 100% test; lot sample live fire |
| R-14 | BIT false-fail (good round discarded) | Low | Low (waste) | Threshold tuning; no operator override |
| R-09 | Cost per kill vs. small arms | Medium | Low | Volume procurement; training |
| R-10 | Rod collateral (urban) | Medium | Medium (ROE) | ROE restrictions |
| R-11 | Export control / ITAR | Medium | Medium (schedule) | Early legal review |

---

## Countermeasure Vulnerability

| Countermeasure | Effect | Severity |
|----------------|--------|----------|
| IR flares / hot decoys | Seeker break-lock or seduction | Moderate |
| Smoke / obscurants | Blocks IR contrast | High |
| Laser warning receiver | **Not applicable** (no laser guidance) | None |
| RF jamming (baseline IR round) | **Not applicable** to round | Low |
| RF jamming (Phase 2 radar round) | Degrades radar seeker | Moderate |
| Low-thermal airframe design | Difficult IR acquisition | Moderate |
| Swarm tactics | Exhausts ammunition | High |

---

## Related Documents

| Document | Purpose |
|----------|---------|
| [05 — Key Design Trades](05-key-design-trades.md) | Guidance architecture rationale |
| [08 — Layered Defense Integration](08-layered-defense-integration.md) | Complementary systems |

---

[← System Description](06-system-description.md) | [Next: Layered Defense Integration →](08-layered-defense-integration.md)
