# Annex I — Performance Modeling (Notional)

**Document ID:** RADR / ANX-I  
**Version:** 1.9.0  
**Status:** Conceptual — traceable point-mass model v2 (`radr_performance_model.py`)

*All results are engineering estimates from a simplified point-mass model. Not live-fire data.*

Traceability: [H — Motor](H-motor-progressive-burn.md) · [G — Mass/CG](G-mass-and-center-of-gravity.md) · [06 — System Description](../docs/06-system-description.md) · [`scripts/radr_performance_model.py`](../scripts/radr_performance_model.py) · [`data/performance_model_output.json`](../data/performance_model_output.json)

---

## Model Scope

| Assumption | Value |
|------------|--------|
| Degrees of freedom | **2-D** point mass (loft ~3.5°, flat ground, sea level) |
| Launch mass \(m_0\) | **3.10 kg** nominal (3.50 kg cap) |
| Burn time \(t_b\) | **3.3 s** |
| Total impulse \(I\) | **3000 N·s** nominal (**2950–3050** band) |
| Thrust profile | Mildly progressive — [Annex H table](H-motor-progressive-burn.md#thrust-time-profile-notional--matches-locked-bands) |
| Drag | Quadratic, \(F_d = \tfrac{1}{2}\rho\, C_d A\, v^2\) |
| Frontal area \(A\) | \(\pi (0.03)^2 \approx \mathbf{0.00283\ \mathrm{m}^2}\) (60 mm body) |
| **Boost** \(C_d A\) | **0.0161 m²** (\(C_{d,\mathrm{eq}} \approx 5.7\)) |
| **Coast** \(C_d A\) | **0.000217 m²** (\(C_{d,\mathrm{eq}} \approx 0.08\)) |
| Air density \(\rho\) | **1.225 kg/m³** (sea level) |
| Launch elevation | **3.5°** loft nominal (2–5° field variation — see loft sweep in JSON) |

---

## Runnable Model (v1.9)

```bash
python scripts/radr_performance_model.py --verify
python scripts/radr_performance_model.py --json-out data/performance_model_output.json
python scripts/mass_cg_calc.py
```

See [`scripts/README.md`](../scripts/README.md). CI runs **verify**, trajectory `--smoke`, and mass/CG checks.

**Nominal output** (`performance_model_output.json` — regenerate after changes):

| Range (m) | TOF (s) | v (m/s) | Mach | q (kPa) | Phase |
|-----------|---------|---------|------|---------|-------|
| 200 | 1.57 | 253 | 0.74 | 39 | boost |
| 500 | 2.62 | 314 | 0.92 | 60 | boost |
| 800 | 3.52 | 338 | 0.99 | 70 | coast |
| **1000** | **4.12** | **334.7** | 0.98 | 69 | coast |
| **1200** | **4.72** | **331.9** | 0.98 | 68 | coast |

Burnout: **338.8 m/s** @ **726 m** downrange · **3000 N·s** impulse · **35%** of ideal \(I/m\) after boost drag (rocket-equation fraction).

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
| **1200** | **~4.72** | **~332** (max envelope) |
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

## Range envelope (locked framing)

| Band | Range | Script (nominal) | Role |
|------|-------|------------------|------|
| **Minimum** | **200 m** | ~253 m/s, ~1.6 s TOF; **boost** | Do not engage closer |
| **Sweet spot** | **1000 m** | **~335 m/s**, ~4.1 s TOF | **330–350 m/s** anchor |
| **Maximum** | **1200 m** | ~332 m/s, ~4.7 s TOF | Envelope limit |

**800–1200 m** = primary employment band. **275-cube** lighter pack **archived** — see [Annex J](J-warhead-dispersal.md#trade-study-275-cube-pack-1200-m-stretch--not-locked).

---

## Drag (traceable basis)

| Quantity | Value | Meaning |
|----------|-------|---------|
| \(A_\mathrm{front}\) | **0.00283 m²** | 60 mm circular reference |
| \(C_d A_\mathrm{boost}\) | **0.0161 m²** | Motor phase + deploy + trim (effective) |
| \(C_d A_\mathrm{coast}\) | **0.000217 m²** | Post-burnout bleed (fins trimmed / low base) |
| \(C_{d,\mathrm{eq}}\) | boost **5.7** · coast **0.08** | \(C_d A / A_\mathrm{front}\) — not skin-friction alone |

At **334.7 m/s** @ 1000 m: **Mach ~0.98**, **q ~69 kPa** (sea level) — subsonic/transonic band; no shock model.

**Protective tube** separates at launch; in-flight mass = **3.1 kg** rocket only.

---

## Warhead fragment mass (calculated)

\[
m_\mathrm{cube} = N \cdot s^3 \cdot \rho,\quad N=300,\ s=7\ \mathrm{mm},\ \rho=7800\ \mathrm{kg/m^3}
\]

| Item | Mass |
|------|------|
| **Cubes only** | **0.803 kg** |
| **Warhead section (Annex G)** | **1.05 kg** total |
| **Burster + casing + liner** | **~0.25 kg** allowance |

Verified: `python scripts/mass_cg_calc.py`

---

## Evasion geometry (@ 1000 m vs 1200 m)

Extra TOF **1000 → 1200 m:** **~0.60 s**. Lateral displacement \(\approx v_\mathrm{target} \cdot \Delta t\):

| Drone speed (m/s) | Lateral during 4.12 s @ 1000 m | Extra lateral (+200 m band) |
|-------------------|--------------------------------|-----------------------------|
| 15 | 62 m | 9 m |
| 25 | 103 m | 15 m |
| 40 | 165 m | 24 m |

Supports **1000 m sweet spot** vs marginal gain at 1200 m — see JSON `evasion_geometry`.

---

## Sensitivity @ 1000 m (script v2)

From `performance_model_output.json` → `sensitivity_1000m`:

| Case | Δv (m/s) | Δ TOF (s) |
|------|----------|-----------|
| Mass +5% | **−1.0** | +0.03 |
| Mass −5% | **+0.9** | −0.04 |
| Impulse −3% | **−5.6** | +0.05 |
| Impulse +3% | **+5.5** | −0.06 |
| Coast \(C_d A\) +10% | **−0.4** | ~0 |
| Coast \(C_d A\) −10% | **+0.4** | ~0 |
| Mass **3.35 kg** (cap edge) | **−3.4** | +0.08 |
| Mass **2.95 kg** | **+2.8** | −0.07 |

**Interpretation:** **Impulse** and **mass at cap** move the band; **coast drag** is second-order once calibrated. Fin/boost drag uncertainty should be bounded in live-fire or 6-DOF before production.

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
- Fin-deploy transient not time-resolved; boost/coast use effective \(C_d A\) fit.  
- 275-cube variant archived — see [Annex J](J-warhead-dispersal.md).

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
