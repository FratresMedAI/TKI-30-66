# Annex I — Performance Modeling (Notional)

**Document ID:** RADR / ANX-I  
**Version:** 1.7.0  
**Status:** Conceptual — analytic placeholders aligned to locked motor baseline

*All results are engineering estimates from a simplified point-mass model. Not live-fire data.*

Traceability: [H — Motor](H-motor-progressive-burn.md) · [G — Mass/CG](G-mass-and-center-of-gravity.md) · [06 — System Description](../docs/06-system-description.md)

---

## Model Scope

| Assumption | Value |
|------------|--------|
| Degrees of freedom | **1-D** along launch axis (no wind, flat ground reference) |
| Launch mass \(m_0\) | **3.10 kg** nominal (3.50 kg cap) |
| Burn time \(t_b\) | **3.3 s** |
| Total impulse \(I\) | **3000 N·s** nominal (**2950–3050** band) |
| Thrust profile | Mildly progressive — [Annex H table](H-motor-progressive-burn.md#thrust-time-profile-notional--matches-locked-bands) |
| Drag | Quadratic, \(F_d = \tfrac{1}{2}\rho C_d A v^2\) |
| Effective \(C_d A\) | **0.32–0.42 m²** (60 mm body + 4 deployed fins; notional) |
| Air density \(\rho\) | **1.225 kg/m³** (sea level) |
| Launch elevation | **~2–5°** loft (rough-aim shoulder fire — notional) |

---

## Boost Phase (0–3.3 s)

### Impulse and average acceleration

| Parameter | Formula / result | Notes |
|-----------|------------------|--------|
| Average thrust | \(I / t_b \approx 3000 / 3.3 \approx \mathbf{909\ N}\) | Matches ~910 N in phase table |
| Mean boost acceleration | \(\bar{a} \approx \bar{F}/m \approx 909/3.1 \approx \mathbf{293\ m/s^2}\) (~30 g) | Time-averaged; peak lower in first 2 s |
| Impulse-to-weight | \(I / (m g) \approx 3000 / 30.4 \approx \mathbf{99\ s}\) | Rocket equation headroom indicator |

### Burnout velocity (motor tail-off, t ≈ 3.3 s)

Integrated thrust minus drag over burn (notional, using Annex H thrust points):

| Case | Burnout speed \(v_{bo}\) |
|------|---------------------------|
| **No drag (upper bound)** | \(I/m \approx 3000/3.1 \approx 968\ m/s\) |
| **With drag, \(C_dA = 0.35\ m²\)** | **~385–410 m/s** |
| **Heavy mass 3.35 kg, min impulse 2950 N·s** | **~360–385 m/s** |
| **Light mass 2.95 kg, max impulse 3050 N·s** | **~400–430 m/s** |

**Locked design anchor:** burnout is **well above** the **330–350 m/s** band at 1000 m; coast phase drag bleeds energy before intercept.

---

## Coast Phase (post-burnout → intercept)

After \(t_b\), motor thrust = 0. Drag decelerates the round along the trajectory.

| Range (m) | Notional TOF from launch (s) | Velocity at range (m/s) |
|-----------|------------------------------|-------------------------|
| 500 | ~2.8 | ~370–390 |
| 750 | ~3.8 | ~350–365 |
| **1000** | **~4.5–5.0** | **330–350** (locked) |
| 1000 (pessimistic drag) | ~5.0 | ~320 (below band — triggers design review) |

**Time of flight to 1000 m:** **4.5–5.0 s** total (boost ~3.3 s + coast ~1.2–1.7 s), consistent with `motor_notional` in baseline JSON.

**Velocity at 1000 m:** **330–350 m/s** — matches locked motor outcome; closure time ~3 s of coast after burnout at nominal loft.

---

## Drag Considerations

| Factor | Effect |
|--------|--------|
| **Fin deploy at exit** | Step increase in \(A\); brief trim transient; stable \(C_dA\) after ~0.2 s |
| **Canard trim** | Small added drag; negligible vs. body |
| **Protective tube separation** | Instantaneous mass drop not modeled here (tube left in launcher); in-flight mass = rocket only |
| **Transonic pocket** | 60 mm rocket likely subsonic at 1000 m in band; no shock drag spike assumed |

Rough deceleration in coast at \(v = 340\ m/s\), \(C_dA = 0.35\), \(m = 3.1\ kg\):

\[
a_{drag} \approx \frac{0.5 \rho C_d A v^2}{m} \approx \frac{0.5 \times 1.225 \times 0.35 \times 340^2}{3.1} \approx 8.2\ m/s^2
\]

(~0.8 g bleed) — explains ~35–55 m/s loss from burnout to 1000 m over ~1.5 s coast.

---

## Sensitivity Analysis

| Parameter | Variation | Δ velocity @ 1000 m (m/s) | Δ TOF @ 1000 m (s) |
|-----------|-----------|---------------------------|---------------------|
| Mass | +5% (3.26 kg) | **−12 to −18** | +0.1–0.2 |
| Mass | −5% (2.95 kg) | **+10 to +15** | −0.1 |
| Impulse | −3% (2910 N·s) | **−8 to −12** | +0.05–0.1 |
| Impulse | +3% (3090 N·s) | **+8 to +12** | −0.05 |
| \(C_dA\) | +10% | **−15 to −22** | +0.15–0.25 |
| \(C_dA\) | −10% | **+12 to +18** | −0.1–0.15 |

**Interpretation:** Mass and drag dominate coast sensitivity; impulse margin is secondary once burnout exceeds ~360 m/s. Staying under **3.5 kg** and validating fin \(C_dA\) in test is critical to holding **330–350 m/s** at 1000 m.

---

## Design Margins vs. Caps

| Check | Nominal | Limit | Margin |
|-------|---------|-------|--------|
| Rocket mass | 3.10 kg | 3.50 kg | 0.40 kg for growth |
| Impulse | 3000 N·s | 2950–3050 | ±50 N·s |
| Velocity @ 1000 m | 340 m/s | 330–350 | ~±10 m/s band |
| Backblast SOP | 10 yd | Fixed | Motor low-thrust segment protects |

---

## Honest Limits

- No Monte Carlo, no 6-DOF, no seeker guidance loop modeled.  
- Loft angle and launcher elevation change TOF and velocity at range.  
- **330–350 m/s @ 1000 m** is a **design target** calibrated to this notional model — not a demonstrated KPP.

---

## Related Documents

- [H — Motor Progressive Burn](H-motor-progressive-burn.md)  
- [G — Mass and CG](G-mass-and-center-of-gravity.md)  
- [D — Projectile Stabilization](D-projectile-stabilization.md)
