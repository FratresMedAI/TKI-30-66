# Annex I — Performance Modeling (Notional)

**Document ID:** RADR / ANX-I  
**Version:** 1.12.0  
**Status:** Conceptual — traceable point-mass model v2 + wind/loft sweep + geometric Pk sandbox

*All results are engineering estimates from a simplified point-mass model. Not live-fire data.*

Traceability: [H — Motor](H-motor-progressive-burn.md) · [G — Mass/CG](G-mass-and-center-of-gravity.md) · [06 — System Description](../docs/06-system-description.md) · [`scripts/radr_performance_model.py`](../scripts/radr_performance_model.py) · [`data/performance_model_output.json`](../data/performance_model_output.json)

---

## Model Scope

| Assumption | Value |
|------------|--------|
| Degrees of freedom | **2-D** point mass (loft ~3.5°, flat ground, sea level); optional **crosswind** lateral channel (not 6-DOF) |
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

## Key performance estimates (nominal — script v2)

Single reference for briefings. Regenerate from `performance_model_output.json` after any model change.

### Primary intercept points

| Metric | **@ 1000 m** (sweet spot) | **@ 1200 m** (max envelope) | **Burnout** (motor tail-off) |
|--------|---------------------------|-----------------------------|------------------------------|
| **Downrange** | 1000 m | 1200 m | **~726 m** |
| **Time of flight** | **4.12 s** | **4.72 s** | **~3.3 s** (thrust ends) |
| **Velocity** | **334.7 m/s** | **331.9 m/s** | **338.8 m/s** |
| **Mach** (sea level) | **0.98** | **0.98** | **~1.00** at burnout |
| **Dynamic pressure \(q\)** | **~69 kPa** | **~68 kPa** | peak boost **~70 kPa** @ 800 m |
| **Flight phase** | Coast | Coast | End of boost |

**Locked band @ 1000 m:** **330–350 m/s**. Nominal sits **~5 m/s below** band midpoint — intentional calibration anchor, not live-fire proof.

**1000 → 1200 m:** Extra **~0.60 s** TOF, velocity drops **~2.8 m/s** — marginal closure gain vs longer target motion (see evasion table).

### Burnout and coast handoff

| Parameter | Value | Notes |
|-----------|-------|-------|
| Burnout speed \(v_{bo}\) | **338.8 m/s** | Last motor sample before coast drag model |
| Burnout range \(x_{bo}\) | **725.9 m** | ~73% of 1000 m downrange under boost+early coast |
| Coast segment @ 1000 m | **~0.82 s** | TOF 4.12 − 3.3 s boost |
| Velocity bleed 1000 m | **~4 m/s** | 338.8 → 334.7 (low coast \(C_d A\)) |

### Along-track snapshot (selected ranges)

| Range (m) | TOF (s) | v (m/s) | Phase |
|-----------|---------|---------|-------|
| 200 | 1.57 | 253.1 | Boost |
| 500 | 2.62 | 314.1 | Boost |
| 800 | 3.52 | 337.7 | Coast (just post-burnout) |
| **1000** | **4.12** | **334.7** | Coast |
| **1200** | **4.72** | **331.9** | Coast |

---

## Assumptions and engineering margins

| Category | Assumption | Margin / limit | If violated |
|----------|------------|----------------|-------------|
| Atmosphere | Sea level, **ρ = 1.225 kg/m³** | No altitude model | High DA reduces \(q\) and Mach — velocity band shifts |
| Terrain | Flat earth, **3.5°** loft | **2–5°** field sweep in JSON | Low loft (2°) fails to reach 1000 m in model |
| Mass | **3.10 kg** launch | **3.50 kg** cap (+12.9%) | At cap: **−3.4 m/s** @ 1000 m (script) |
| Impulse | **3000 N·s** | **2950–3050 N·s** (±1.7%) | −3% impulse: **−5.6 m/s** @ 1000 m |
| Drag | Effective **\(C_d A\)** boost/coast fit | Coast ±10% → **±0.4 m/s** | Fin-deploy transient not time-resolved |
| Tube | Separates at launch | In-flight mass = rocket only | Tube drag not in flight model |
| Guidance | Not modeled | See guidance sanity script | MC is ballistic dispersion only |

**Statistical margin (Monte Carlo n = 25 000 @ 1000 m):** **p5–p95** velocity **331.1–337.4 m/s**; **99.76%** of draws in **330–350 m/s** band (`monte_carlo_25000.json`).

---

## Validated vs notional traceability

One-page matrix for PM, legal, and engineering reviewers. **Locked** = requirements baseline. **Modeled + CI** = reproducible script checks. **Statistical (MC)** = dispersion around the model. **Notional** = design intent without test proof. **Archived** = explicit non-baseline trade study.

| Item | Status | Evidence | Disclaimer |
|------|--------|----------|------------|
| **300 × 7 mm** warhead, forward cone @ ~20 ft | **Locked requirement** | README, Annex J, `baseline_systems.json` | Lethality vs threat class not live-fire proven |
| Range envelope **200 m min · 800–1200 m · 1000 m sweet** | **Locked requirement** | DOC-02, Annex I, JSON ranges | Employment doctrine, not ballistic test |
| Tank-shell load sequence (pop top → bore screw → rocket ready) | **Locked requirement** | Annex F, CONTAINER-SPEC | Prototype mechanical proof TBD ([Phase 1 gates](../docs/10-phase-1-prototype-gates.md)) |
| Launcher / container / round **authoritative art** | **Locked requirement** | `visuals/*/output/*-authoritative.png` | Concept art only — not as-built |
| **v @ 1000 m = 334.7 m/s**, TOF **~4.12 s**, burnout **~339 m/s @ ~726 m** | **Modeled + CI** | `radr_performance_model.py --verify`, `radr_trajectory.py --smoke` | 2-D point mass; effective \(C_d A\) fit — not live fire |
| Effective **\(C_d A\)** boost/coast, impulse **3000 N·s** integration | **Modeled + CI** | `performance_model_output.json`, CI verify | Calibrated to velocity band, not wind tunnel |
| **300-cube** fragment mass **~0.803 kg** | **Modeled + CI** | `mass_cg_calc.py` | Geometry sanity; alloy final TBD |
| Monte Carlo **n=25 000** @ 1000 m: **99.76%** in **330–350 m/s** band | **Statistical (MC)** | `data/monte_carlo_25000.json`, `monte_carlo_envelope.py` | Parameter dispersion only — no guidance/wind |
| Evasion lateral vs drone speed + canard sanity | **Modeled + CI** | `guidance_evasion_sanity.py`, JSON `evasion_geometry` | Coarse bang-bang bound; not full engagement sim |
| Wind + loft dispersion @ 1000 m | **Modeled + CI** | `wind_loft_dispersion.py`, [`data/wind_loft_dispersion.json`](../data/wind_loft_dispersion.json) | Notional crosswind coupling; not validated in tunnel |
| Notional **P\_k** (geometric × lethality placeholder) | **Modeled + CI** | `pk_geometry_sandbox.py`, [`data/pk_geometry_sandbox.json`](../data/pk_geometry_sandbox.json) | **P\_kill\|hit** are design placeholders — not arena test |
| Live-fire velocity, impulse, warhead arena | **Pending partner test** | [DOC-11](../docs/11-live-fire-and-partner-validation.md), [`live_fire_results.template.json`](../data/live_fire_results.template.json) | Template `status: pending` — no fabricated shots |
| Motor thrust table, Evolution Space propellant, grain geometry | **Notional / untested** | Annex H, DOC-11 gate **2A** | Vendor static fire / backblast TBD |
| IR seeker track, proximity fuze timing (full loop) | **Notional / untested** | Annex J, DOC-06, DOC-11 gate **2D** | No seeker HIL data in repo |
| **275-cube @ 1200 m** lighter pack | **Archived trade-study** | Annex J § trade-study | **Not** product baseline |

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

## Acceleration profile (script — along-track)

Net acceleration along the lofted path from `acceleration_profile` in JSON (includes thrust, drag, and gravity along path). **Not** constant — peaks early boost, tapers as drag rises.

| t (s) | Phase | x (m) | v (m/s) | a (m/s²) | Comment |
|-------|-------|-------|---------|----------|---------|
| 0.0 | boost | 0.0 | 0.0 | 9.8 | Ignition / start |
| 0.5 | boost | 11.3 | 67.0 | **260.7** | High apparent accel — low speed, full thrust |
| 1.0 | boost | 74.7 | 179.2 | 179.9 | Drag rising with \(v^2\) |
| 1.5 | boost | 183.1 | 246.9 | 95.3 | Mildly progressive thrust ramp |
| 2.0 | boost | 316.3 | 282.7 | 52.6 | Approaching peak thrust segment |
| 2.5 | boost | 464.8 | 308.5 | 50.1 | Still boosting |
| 3.0 | boost | 625.0 | 332.1 | 44.2 | Near burnout |
| **3.3** | **burnout** | **~726** | **338.8** | — | Motor tail-off (motor block in JSON) |
| 3.5 | coast | 793.5 | 337.8 | 11.1 | Thrust = 0; drag + gravity |
| 4.0 | coast | 961.7 | 335.3 | 11.0 | Approaching 1000 m mark |
| **4.12** | coast | **1000** | **334.7** | ~11 | **Sweet spot** |
| **4.72** | coast | **1200** | **331.9** | ~11 | **Max envelope** |

**Readout:** Peak **~260 m/s²** (~27 g) at 0.5 s is a model artifact of low initial speed + full thrust — use for qualitative load order, not structural sign-off without transient FEA.

Full time series: `data/performance_model_output.json` → `acceleration_profile`.

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

**Guidance sanity (not P\_k):** [`scripts/guidance_evasion_sanity.py`](../scripts/guidance_evasion_sanity.py) compares uncorrected lateral drift to a **20–30 m/s²** moderate-maneuver correction over full TOF @ 1000 m vs a **~3.0–3.7 m** fragment footprint (10–12 ft). Output: `data/guidance_evasion_output.json`. Trajectory Monte Carlo does **not** model the seeker loop.

---

## Sensitivity @ 1000 m (mass, impulse, drag — script v2)

From `performance_model_output.json` → `sensitivity_1000m`. All cases use nominal loft **3.5°** unless noted.

| Case | v @ 1000 m (m/s) | Δv vs nominal | Δ TOF (s) | In 330–350 band? |
|------|------------------|---------------|-----------|------------------|
| **Nominal** | **334.7** | 0 | 4.12 | Yes |
| Mass +5% (3.26 kg) | 333.7 | −1.0 | +0.03 | Yes |
| Mass −5% (2.95 kg) | 335.6 | +0.9 | −0.04 | Yes |
| Impulse −3% (2910 N·s) | 329.1 | **−5.6** | +0.05 | **Marginal** (below 330) |
| Impulse +3% (3090 N·s) | 340.2 | +5.5 | −0.06 | Yes |
| Coast \(C_d A\) +10% | 334.3 | −0.4 | ~0 | Yes |
| Coast \(C_d A\) −10% | 335.1 | +0.4 | ~0 | Yes |
| Mass **3.35 kg** (cap edge) | 333.0 | **−1.7** | +0.05 | Yes |
| Mass **2.95 kg** (light) | 335.6 | +0.9 | −0.04 | Yes |

### Combined perturbation (engineering judgment — not separate script runs)

| Combined case | Expected trend @ 1000 m | Action if prototyping |
|---------------|-------------------------|------------------------|
| Heavy mass **+** low impulse | Largest downward velocity shift; highest risk of sub-330 | Prioritize motor I verification |
| Light mass **+** high impulse | Upper band edge (~340 m/s); watch transonic \(q\) | Confirm structure/heating margin |
| Heavy mass **+** high coast drag | Moderate downward; TOF slightly long | Bound fin-deploy Cd step |

**Interpretation:** **Impulse** is the dominant lever on the locked velocity band; **mass at cap** is second. **Coast drag** is third once boost/coast \(C_d A\) are calibrated. Fin-deploy transient and wind are **not** in this table — bound in live-fire or 6-DOF before production sign-off.

---

## Wind and aim-error dispersion

Notional **crosswind** (0–15 m/s) and **loft** (2–5°) sweep at **1000 m** from [`wind_loft_dispersion.py`](../scripts/wind_loft_dispersion.py). Regenerate: `python scripts/wind_loft_dispersion.py --json-out data/wind_loft_dispersion.json`.

| Loft (°) | Crosswind (m/s) | Reaches 1000 m? | v @ 1000 m (m/s) | Lateral @ 1000 m (m) |
|----------|-----------------|-----------------|------------------|----------------------|
| 3.5 | 0 | Yes | **334.7** | **0.0** |
| 3.5 | 15 | Yes | **334.7** | **~23** |
| 2.0 | 0 | **No** | — | — |
| 5.0 | 0 | Yes | ~336 | ~0 |

**Assumption:** Constant crosswind with first-order coupling to lateral velocity — **not** fin moments, gust spectrum, or altitude wind shear. Full **6-DOF** attitude integration is **out of scope** for stdlib Phase 0 (see **I-07**).

---

## Notional Pk (geometric only)

[`pk_geometry_sandbox.py`](../scripts/pk_geometry_sandbox.py) combines guidance residuals @ **30 m/s²** with footprint **R = 1.55 m**:

\[
P_{\mathrm{geometric}} = \exp\left(-\left(\frac{\mathrm{residual}}{R}\right)^2\right)
\]

| Threat class | Rep. speed (m/s) | Residual @ 30 m/s² (m) | P\_geo | P\_kill\|hit (notional) | P\_\* |
|--------------|------------------|------------------------|--------|-------------------------|-------|
| Hover | 10 | 0 | 1.00 | 0.70 | **0.70** |
| Crossing | 25 | 0 | 1.00 | 0.40 | **0.40** |
| Glide | 40 | 0 | 1.00 | 0.35 | **0.35** |

**Disclaimer:** P\_kill\|hit values are **locked placeholders** for briefing — **not** arena fragment velocity or live-fire. Replace after partner warhead test ([DOC-11](../docs/11-live-fire-and-partner-validation.md) gate **2C**).

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

| ID | Topic | Impact |
|----|-------|--------|
| I-01 | Loft **2–5°** field variation vs. display aim | TOF and v @ 1000 m spread — see `loft_sweep_1000m` in JSON |
| I-02 | Fin-deploy **CdA step** (0.25 s deploy) | Boost/coast use effective fit only |
| I-03 | Altitude / temperature | Sea-level \(\rho\) only |
| I-04 | Wind / crosswind | **Partial** — `crosswind_mps` + `wind_loft_dispersion.py`; not in MC |
| I-05 | Live-fire velocity confirmation | **Pending** — [DOC-11](../docs/11-live-fire-and-partner-validation.md); fill `live_fire_results.template.json` |
| I-06 | 275-cube @ 1200 m | **Archived** — [Annex J](J-warhead-dispersal.md) |
| I-07 | Full **6-DOF** (Euler/quaternion + fin moments) | **Deferred** — partner range test or external tool (OpenRocket / CFD); not stdlib Phase 0 |

---

## Honest Limits

- **2-D point mass** — optional notional crosswind channel only; **no 6-DOF**, fin-deploy transient, or altitude tables in the primary model.  
- **Monte Carlo** (`monte_carlo_25000.json`) varies mass/impulse/drag — not seeker noise, wind, or guidance.  
- **Guidance sanity** + **Pk sandbox** are geometric bounds — not seeker IR, fuze timing, or arena lethality.  
- **Live-fire** proof requires partner range — see DOC-11; repo holds template JSON only.  
- Loft angle and launcher elevation change TOF and velocity at range.  
- **330–350 m/s @ 1000 m** is a **design target** calibrated to this notional model — not a demonstrated KPP.

---

## Related Documents

- [H — Motor Progressive Burn](H-motor-progressive-burn.md)  
- [G — Mass and CG](G-mass-and-center-of-gravity.md)  
- [J — Warhead Dispersal](J-warhead-dispersal.md)  
- [D — Projectile Stabilization](D-projectile-stabilization.md)
