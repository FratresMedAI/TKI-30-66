# 09 — Motor Vendor Brief (Evolution Space or equivalent)

**Document ID:** RADR / DOC-09  
**Version:** 1.0.0  
**Status:** Conceptual — for vendor / propulsion partner conversations

**Full technical basis:** [Annex H — Motor progressive burn](../annexes/H-motor-progressive-burn.md) (thrust table, grain sketch, engagement packet).

---

## What we need

A **60 mm × ~18 in** round solid motor that delivers **~330–350 m/s** at **1000 m** in RADR’s notional 2-D model, while keeping **recoilless backblast** inside a **≤ 10 yard (30 ft)** rear danger zone.

---

## Hard constraints (non-negotiable for baseline)

| Parameter | Locked band |
|-----------|-------------|
| Case OD | **60 mm** |
| Usable grain length | **~260 mm** |
| Propellant mass | **~1.20 kg** |
| Total impulse | **2950–3050 N·s** (nominal **3000**) |
| Burn time | **~3.3 s** |
| Initial thrust (first ~1–2 s) | **750–850 N** |
| Peak thrust | **1050–1150 N** |
| Thrust profile | **Mildly progressive** (low open → ramp → peak) — **not** boost-first |

---

## What we will share

- Thrust-time **design target** table (Annex H)  
- Script-calibrated trajectory band (**334.7 m/s @ 1000 m** nominal — notional until live fire)  
- Recoilless launcher context (M1 Bazooka class, squad carry)

---

## What we ask the vendor for (first meeting)

1. Feasibility letter for form factor + impulse band  
2. **Measured** static-test \(F(t)\), total \(I\), peak pressure  
3. Opening-segment thrust data relevant to **rear blast / plume** at **750–850 N** class  
4. Proposed **grain geometry** (sketch) showing mildly progressive burn  
5. Timeline and cost ROM for **grain development + static tests** (not full round)

---

## Out of scope (first call)

- IR seeker, fuze, warhead integration  
- Full round ballistics or Pk  
- Production line / qualification

---

## Honest status

All RADR motor numbers are **locked design baselines** aligned to repo scripts — **not** demonstrated KPPs. Ballistic test is Phase 2 (see [DOC-10 — Phase 1 prototype gates](10-phase-1-prototype-gates.md)).

---

[← Limitations](07-limitations-and-risks.md) · [Annex H](../annexes/H-motor-progressive-burn.md) · [Phase 1 gates →](10-phase-1-prototype-gates.md)
