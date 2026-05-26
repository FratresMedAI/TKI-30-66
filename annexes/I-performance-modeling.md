# Annex I — Performance Modeling (Notional)

**Document ID:** RADR / ANX-I  
**Version:** 1.8.0  
**Status:** Conceptual — point-mass model with runnable script traceability

*All results are engineering estimates from a simplified point-mass model. Not live-fire data.*

Traceability: [H — Motor](H-motor-progressive-burn.md) · [G — Mass/CG](G-mass-and-center-of-gravity.md) · [06 — System Description](../docs/06-system-description.md) · [`scripts/radr_trajectory.py`](../scripts/radr_trajectory.py)

---

## Model Scope

| Assumption | Value |
|------------|--------|
| Degrees of freedom | **2-D** point mass (loft ~3.5°, flat ground, sea level) |
| Launch mass \(m_0\) | **3.10 kg** nominal (3.50 kg cap) |
| Burn time \(t_b\) | **3.3 s** |
| Total impulse \(I\) | **3000 N·s** nominal (**2950–3050** band) |
| Thrust profile | Mildly progressive — [Annex H table](H-motor-progressive-burn.md#thrust-time-profile-notional--matches-locked-bands) |
| Drag | Quadratic, \(F_d = \tfrac{1}{2}\rho C_d A v^2\) |
| Effective \(C_d A\) (reference) | **0.32–0.42 m²** — boost/coast multipliers in script |
| Air density \(\rho\) | **1.225 kg/m³** (sea level) |
| Launch elevation | **~2–5°** loft (rough-aim shoulder fire — notional) |

---

## Runnable Model (v1.8)

```bash
python scripts/radr_trajectory.py --smoke
python scripts/radr_trajectory.py --json-out data/performance_model_output.json
```

See [`scripts/README.md`](../scripts/README.md) for assumptions. CI runs `--smoke` on each push.

**Script nominal output (2026 baseline):**

| Range (m) | TOF (s) | Velocity (m/s) | Notes |
|-----------|---------|----------------|-------|
| 500 | ~2.62 | ~314 | Mid-course |
| 750 | ~3.37 | ~339 | Near burnout corridor |
| **1000** | **~4.12** | **~335** | **Locked band 330–350** |
| **1200** | **~4.72** | **~332** | **Stretch / trade-study — not locked** |

Burnout (motor tail-off): **~339 m/s** at **~726 m** downrange, **3000 N·s** impulse integration.

The 2-D path yields a slightly **shorter TOF @ 1000 m** than the earlier 1-D analytic table (~4.5–5.0 s); velocity at 1000 m remains inside the locked band. Treat TOF rows as **notional bounds**, not demonstrated timing.

---

## Boost Phase (0–3.3 s)

### Impulse and average acceleration

| Parameter | Formula / result | Notes |
|-----------|------------------|--------|
| Average thrust | \(I / t_b \approx 3000 / 3.3 \approx \mathbf{909\ N}\) | Matches ~910 N in phase table |
| Mean boost acceleration | \(\bar{a} \approx \bar{F}/m \approx 909/3.1 \approx \mathbf{293\ m/s^2}\) (~30 g) | Time-averaged; peak lower in first 2 s |
| Impulse-to-weight | \(I / (m g) \approx 3000 / 30.4 \approx \mathbf{99\ s}\) | Rocket equation headroom indicator |

### Burnout velocity (motor tail-off, t ≈ 3.3 s)

| Case | Burnout speed \(v_{bo}\) |
|------|---------------------------|
| **No drag (upper bound)** | \(I/m \approx 3000/3.1 \approx 968\ m/s\) |
| **Script nominal (2-D, calibrated drag)** | **~339 m/s** @ **~726 m** downrange |
| **Heavy mass 3.35 kg, min impulse 2950 N·s** | **~360–385 m/s** (band) |
| **Light mass 2.95 kg, max impulse 3050 N·s** | **~400–430 m/s** (band) |

**Locked design anchor:** burnout exceeds **330–350 m/s** at 1000 m after coast bleed; script holds **~335 m/s** at 1000 m nominal.

---

## Coast Phase (post-burnout → intercept)

After \(t_b\), motor thrust = 0. Drag and gravity along the lofted path decelerate the round.

| Range (m) | Notional TOF from launch (s) | Velocity at range (m/s) |
|-----------|------------------------------|-------------------------|
| 500 | ~2.6–2.8 | ~310–320 |
| 750 | ~3.3–3.5 | ~335–345 |
| **1000** | **~4.1–4.5** (script **~4.12**) | **330–350** (locked; script **~335**) |
| **1200** | **~4.7–5.0** (stretch) | **~325–335** (trade-study — not locked) |
| 1000 (pessimistic drag) | ~4.5–5.0 | ~320 (below band — triggers design review) |

**Time of flight to 1000 m:** **4.0–5.0 s** bracket (boost ~3.3 s + coast ~0.8–1.7 s depending on loft and drag), consistent with `motor_notional` in baseline JSON.

---

## Acceleration Profile (0.5 s samples — script)

| t (s) | Phase | x (m) | v (m/s) |
|-------|-------|-------|---------|
| 0.0 | boost | 0 | 0 |
| 0.5 | boost | ~45 | ~140 |
| 1.0 | boost | ~175 | ~230 |
| 1.5 | boost | ~360 | ~285 |
| 2.0 | boost | ~520 | ~310 |
| 2.5 | boost | ~640 | ~325 |
| 3.0 | boost | ~700 | ~335 |
| 3.3 | boost / burnout | **~726** | **~339** |
| 3.5 | coast | ~780 | ~338 |
| 4.0 | coast | ~920 | ~336 |
| 4.12 | **mark 1000 m** | **1000** | **~335** |
| 4.72 | mark 1200 m (stretch) | 1200 | ~332 |

Full profile: `data/performance_model_output.json` → `acceleration_profile`.

---

## 1200 m Stretch (Trade-Study — Not Locked)

| Item | Notional value | Purpose |
|------|----------------|---------|
| Velocity @ 1200 m | **~332 m/s** (script) | Closure margin study |
| TOF @ 1200 m | **~4.72 s** | Timing for extended engagement |
| Lighter pack variant | **275 × 7 mm** cubes | See [Annex J — Trade-study](J-warhead-dispersal.md#trade-study-275-cube-pack-1200-m-stretch--not-locked) |

**300 × 7 mm @ 1000 m** remains the locked KPP. **1200 m** and **275-cube** lines are engineering placeholders only.

---

## Drag Considerations

| Factor | Effect |
|--------|--------|
| **Fin deploy at exit** | Step increase in \(A\); brief trim transient; stable \(C_dA\) after ~0.2 s |
| **Canard trim** | Small added drag; negligible vs. body |
| **Protective tube separation** | Tube left in launcher; in-flight mass = rocket only |
| **Transonic pocket** | 60 mm rocket likely subsonic at 1000 m in band; no shock spike assumed |
| **Script calibration** | Boost/coast multipliers on baseline CdA — see `scripts/README.md` |

At \(v = 340\ m/s\), \(m = 3.1\ kg\), a **physical** \(C_d A \approx 0.00035\ \mathrm{m}^2\) gives ~**8 m/s²** coast bleed; the **0.35 m²** entry in JSON is a **design reference area** paired with integrator multipliers, not a literal subsonic drag product at 340 m/s.

---

## Sensitivity Analysis

From `radr_trajectory.py` (`run_sensitivity`) — Δ velocity @ **1000 m** vs nominal:

| Parameter | Variation | Δv @ 1000 m (m/s) | Δ TOF (s) |
|-----------|-----------|-------------------|-----------|
| Mass | +5% | **~−12** | +0.05 |
| Mass | −5% | **~+11** | −0.05 |
| Impulse | −3% | **~−9** | +0.03 |
| Impulse | +3% | **~+9** | −0.03 |
| \(C_dA\) ref | +10% | **~−16** | +0.08 |
| \(C_dA\) ref | −10% | **~+14** | −0.07 |

**Interpretation:** Mass and drag dominate coast sensitivity; impulse margin is secondary once burnout exceeds ~330 m/s. Staying under **3.5 kg** and validating fin drag in test is critical to holding **330–350 m/s** at 1000 m.

---

## Design Margins vs. Caps

| Check | Nominal | Limit | Margin |
|-------|---------|-------|--------|
| Rocket mass | 3.10 kg | 3.50 kg | 0.40 kg for growth |
| Impulse | 3000 N·s | 2950–3050 | ±50 N·s |
| Velocity @ 1000 m | **335 m/s** (script) | 330–350 | In band |
| Backblast SOP | 10 yd | Fixed | Motor low-thrust segment protects |

---

## Open Questions

- Loft angle field variation (2–5°) vs. display-based rough aim — TOF and intercept velocity spread.  
- Fin deploy transient: step CdA not time-resolved in script.  
- Sea-level \(\rho\) only — altitude/temperature not modeled.  
- 1200 m / 275-cube closure requires live-fire or 6-DOF before any KPP change.

---

## Honest Limits

- No Monte Carlo, no 6-DOF, no seeker guidance loop modeled.  
- Loft angle and launcher elevation change TOF and velocity at range.  
- **330–350 m/s @ 1000 m** is a **design target** calibrated to this notional model — not a demonstrated KPP.

---

## Related Documents

- [H — Motor Progressive Burn](H-motor-progressive-burn.md)  
- [G — Mass and CG](G-mass-and-center-of-gravity.md)  
- [J — Warhead Dispersal](J-warhead-dispersal.md)  
- [D — Projectile Stabilization](D-projectile-stabilization.md)
