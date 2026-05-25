# Annex H — Motor Progressive Burn Profile

**Document ID:** RADR / ANX-H  
**Version:** 1.1.0  
**Status:** Conceptual — notional ballistics

*Thrust, impulse, and range figures are analytic placeholders — not live-fire data.*

Traceability: [06 — System Description](../docs/06-system-description.md) · [05 — Key Design Trades](../docs/05-key-design-trades.md)

---

## Motor Summary (Locked Baseline)

| Parameter | Value |
|-----------|--------|
| Type | Progressive-burn solid grain |
| Motor bay length | ~297 mm |
| Usable grain length | ~260 mm |
| Propellant mass | ~1.20 kg |
| Burn time | ~3.2–3.4 s |
| Total impulse (notional) | **2800–3200 N·s** (nominal **~2900 N·s**) |
| Range goal | **1000 m** effective |

---

## Thrust-Time Profile (Notional)

Progressive burn: **lower thrust 0–2 s** (recoil/backblast control), **ramp 2–3.2 s** (range closure), **tail 3.2–3.4 s** (burnout).

| Time (s) | Thrust (N) | Phase |
|----------|------------|--------|
| 0.0 | 0 | Ignition start |
| 0.5 | 620 | Low plateau building |
| 1.0 | 680 | Low phase |
| 1.5 | 700 | Low phase |
| 2.0 | 720 | End low phase |
| 2.5 | 850 | Ramp |
| 3.0 | 1000 | Ramp peak approach |
| 3.2 | 1050 | Peak |
| 3.4 | 950 | Burnout tail |

### Phase Averages

| Phase | Duration (s) | Avg thrust (N) | Impulse contrib. (N·s) |
|-------|--------------|----------------|------------------------|
| Low (0–2.0) | 2.0 | ~700 | ~1400 |
| Ramp (2.0–3.2) | 1.2 | ~900 | ~1080 |
| Tail (3.2–3.4) | 0.2 | ~950 | ~190 |
| **Total** | **~3.4** | **~850 avg** | **~2670–2900** |

**Stated design band:** 2800–3200 N·s (conservative pad applied → **nominal ~2900 N·s**).

*Thrust rises from ~700 N (0–2 s) to ~1050 N peak at 3.2 s — see table for authoritative points.*

---

## Why Progressive (Not Neutral / Boost-First)

| Profile | Recoil / backblast | Range at 1000 m | RADR fit |
|---------|-------------------|-----------------|----------|
| **Progressive (low → ramp)** | Lower peak at launch | Good terminal velocity | **Selected** |
| Neutral burn | Higher initial peak | Moderate | Rejected — shoulder strain |
| Boost-first | Highest initial peak | Best short range | Rejected — 10 yd backblast SOP |

Low initial thrust keeps the **10 yard (30 ft)** rear danger zone manageable; ramp delivers **330–370 m/s** class terminal velocity at 1000 m (notional).

---

## Performance Bridge to 1000 m Goal

| Parameter | Notional value | Basis |
|-----------|----------------|-------|
| Total impulse | ~2900 N·s | Thrust-time integration |
| Launch mass | ~3.1 kg | Annex G |
| Burn time | ~3.4 s | Table above |
| Time of flight @ 1000 m | ~4.5–5.0 s | Ballistic estimate |
| Terminal velocity @ 1000 m | ~330–370 m/s | Drag + impulse placeholder |

**Honest limit:** No live motor test or trajectory radar validation. Range goal is a **design target**, not a demonstrated KPP.

---

## Comparison to Prior Program Estimates

| Metric | v0.5 notional | v0.9 Annex H |
|--------|---------------|--------------|
| Average thrust | 850–1050 N | ~850 N avg over burn |
| Total impulse | 2800–3200 N·s | ~2900 N·s nominal |
| Low thrust phase | 3.0–3.4 s burn | **First 2.0 s** explicit low phase |

---

## Related Documents

- [G — Mass and CG](G-mass-and-center-of-gravity.md)  
- [05 — Key Design Trades](../docs/05-key-design-trades.md)  
- [07 — Limitations and Risks](../docs/07-limitations-and-risks.md)
