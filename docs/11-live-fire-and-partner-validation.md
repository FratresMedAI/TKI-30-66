# 11 — Live-Fire and Partner Validation

**Document ID:** RADR / DOC-11  
**Version:** 1.0.0  
**Status:** Conceptual — **no physical test data in repo**; partner-ready plan

Traceability: [DOC-10 — Phase 1 gates](10-phase-1-prototype-gates.md) · [DOC-09 — Motor vendor brief](09-motor-vendor-brief.md) · [Annex I — Performance](../annexes/I-performance-modeling.md) · [Licensing & partnership](licensing-and-partnership.md)

---

## What “live-fire proof” means here

RADR does **not** claim live-fire validation until a partner or range records measured data. This document defines:

1. **What must be tested** (static motor, instrumented launch, warhead arena, seeker HIL)  
2. **Pass/fail metrics** aligned with locked specs  
3. **How results enter the repo** via [`data/live_fire_results.template.json`](../data/live_fire_results.template.json)

Repo scripts remain **notional** until `status` in that file moves from `pending` to `partial` or `complete`.

---

## Phase 2 validation gates (partner / range)

Phase 1 ([DOC-10](10-phase-1-prototype-gates.md)) proves launcher mechanics. Phase 2 proves **energy, ballistics, lethality, and guidance** — requires external facilities.

| Gate | ID | Proves | Does not prove |
|------|-----|--------|----------------|
| **Static motor** | **2A** | Measured \(F(t)\), total \(I\), peak pressure; opening thrust vs 10 yd backblast | Full round integration |
| **Instrumented launch** | **2B** | **v @ 1000 m** in **330–350 m/s** band; TOF; trajectory vs model | Pk on moving targets |
| **Warhead arena** | **2C** | Fragment cone **~10–12 ft** @ **~20 ft**; fuze timing | Full seeker loop |
| **Seeker HIL** | **2D** | Lock tone vs target class; crossing vs hover | Field swarm Pk |

### 2A — Motor static fire

| Item | Detail |
|------|--------|
| **Entry** | Grain vendor or partner static-test stand |
| **Procedure** | Fire motor in 60 mm fixture; record thrust trace, impulse, plume/rear overpressure at 10 yd equivalent |
| **Pass** | \(I \in\) **2950–3050 N·s**; opening **750–850 N** for first **1–2 s**; peak **1050–1150 N**; no case breach |
| **Fail** | Impulse out of band; opening thrust exceeds backblast SOP |
| **Artifacts** | \(F(t)\) CSV, impulse report, pressure at 10 yd |
| **JSON block** | `motor_static_fire` in live-fire results file |

### 2B — Instrumented launch

| Item | Detail |
|------|--------|
| **Entry** | 2A passed or waived with risk note; instrumented launcher + inert or live round per range rules |
| **Procedure** | Minimum **5** shots at **1000 m** downrange; Doppler or radar velocity at mark; TOF |
| **Pass** | **≥ 80%** of shots with **v @ 1000 m** in **330–350 m/s**; no structural failure |
| **Fail** | Systematic sub-330 or over-350; instability |
| **Artifacts** | Shot log, velocity table, high-speed video |
| **JSON block** | `instrumented_launches[]` |

### 2C — Warhead arena

| Item | Detail |
|------|--------|
| **Entry** | Inert or live fragment test per regulations |
| **Procedure** | Proximity or timed fuze at **~20 ft** standoff; measure cone footprint on paper/witness |
| **Pass** | Effective diameter **~10–12 ft** forward-biased; cube count intact |
| **Fail** | Omnidirectional burst; early/late fuze |
| **Artifacts** | Arena photos, timing log |
| **JSON block** | `warhead_arena` |

### 2D — Seeker hardware-in-the-loop

| Item | Detail |
|------|--------|
| **Entry** | Seeker module on track rig or HIL bench |
| **Procedure** | Hover vs crossing target sim; tone stability; lock time |
| **Pass** | Steady tone within spec FOV; abort on front release |
| **Fail** | False lock; no tone on valid target |
| **JSON block** | `seeker_hil` |

---

## Instrumentation (recommended)

| Measurement | Purpose |
|---------------|---------|
| Thrust stand / load cell | 2A impulse and \(F(t)\) |
| Doppler radar or sky-screen | 2B v @ downrange marks |
| Downrange timing gates | 2B TOF verification |
| Breech pressure transducer | Recoilless vent characterization |
| High-speed video | Fin deploy, tube separation |
| Arena witness sheets | 2C cone diameter |

---

## Data handoff (repo)

1. Copy [`data/live_fire_results.template.json`](../data/live_fire_results.template.json) → `data/live_fire_results.json` (do not commit classified partner data without approval).  
2. Set `status`: `pending` → `partial` → `complete`.  
3. Fill measured fields only — **no fabricated numbers**.  
4. Update [Annex I traceability](../annexes/I-performance-modeling.md#validated-vs-notional-traceability) row for live-fire when `complete`.

---

## Collaboration opportunities

RADR (concept + models + specs) pairs well with partners who have:

| Need from partner | RADR brings |
|-------------------|-------------|
| **Static motor test** (Evolution Space or equivalent) | Locked impulse/thrust bands, [DOC-09](09-motor-vendor-brief.md), Annex H |
| **Instrumented range** (1000 m validation) | Traceable 2-D model, MC envelope, open JSON schema |
| **Warhead / fuze arena** | 300-cube geometry, cone spec, Annex J |
| **Prime integrator** (launcher prototype) | Phase 1 gates, Annex F mechanics, IP framework |

**Inquiry:** [GitHub partnership issue template](https://github.com/FratresMedAI/RADR-mk.60/issues/new?template=partnership_inquiry.yml) · [Licensing & partnership](licensing-and-partnership.md)

---

## Honest limits

- This repo **cannot** substitute for range data.  
- Until `live_fire_results.json` is populated by a partner, all velocity and Pk claims remain **Modeled + CI** or **Notional** per Annex I.  
- 6-DOF and full IR seeker simulation stay deferred — see Annex I § Wind / Pk / 6-DOF.

---

[← Phase 1 gates](10-phase-1-prototype-gates.md) · [Motor vendor brief](09-motor-vendor-brief.md) · [Annex I](../annexes/I-performance-modeling.md)
