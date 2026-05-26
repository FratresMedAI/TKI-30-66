# RADR Scripts

**Notional engineering tools only — not live-fire or certified ballistics.**

## `radr_performance_model.py` (primary, v2)

Traceable **2-D point-mass** model:

- **60 mm** frontal area \(A = \pi (d/2)^2 \approx 0.00283\ \mathrm{m}^2\)
- **Effective drag areas** \(C_d A\) in **m²** (boost vs coast), tied to geometry and locked to **330–350 m/s @ 1000 m**
- Thrust table → **3000 N·s** nominal impulse; **rocket-equation** check (\(I/m\) vs burnout \(v\))
- Range table **200–1200 m** with TOF, Mach, dynamic pressure \(q\)
- **Warhead** cube mass (300 × 7 mm @ 7800 kg/m³)
- **Evasion geometry** (lateral drift vs drone speed, 1000 vs 1200 m TOF delta)
- Optional **`crosswind_mps`** — notional lateral drift (not 6-DOF)
- Loft / mass / impulse / coast-drag sensitivity

### Run

```bash
python scripts/radr_performance_model.py --verify
python scripts/radr_performance_model.py --print
python scripts/radr_performance_model.py --json-out data/performance_model_output.json
```

### Locked nominal outputs (regenerate to refresh)

| Range | TOF (s) | v (m/s) |
|-------|---------|---------|
| 200 m | ~1.57 | ~253 (boost) |
| 1000 m | ~4.12 | ~335 |
| 1200 m | ~4.72 | ~332 |

| Drag | Value (m²) |
|------|------------|
| Boost \(C_d A\) | **0.0161** (\(C_{d,\mathrm{eq}} \approx 5.7\) × \(A_\mathrm{front}\)) |
| Coast \(C_d A\) | **0.000217** (\(C_{d,\mathrm{eq}} \approx 0.08\) × \(A_\mathrm{front}\)) |

**Interpretation:** Equivalent drag areas include fins, trim, and deploy transients — not bare skin friction on the 60 mm disk alone.

## `radr_trajectory.py` (legacy CLI)

Wraps `radr_performance_model.py` for CI and older doc links (`--smoke`, `--json-out`).

## `guidance_evasion_sanity.py`

Coarse **moderate-maneuver** (20–30 m/s²) lateral correction vs `evasion_geometry` drift @ **1000 m**. Compares residual miss to **~10–12 ft** fragment footprint radius — **not** Pk or seeker simulation.

```bash
python scripts/guidance_evasion_sanity.py --verify
python scripts/guidance_evasion_sanity.py --json-out data/guidance_evasion_output.json
```

Requires `data/performance_model_output.json` (run performance model first).

## `wind_loft_dispersion.py`

Sweeps **loft 2–5°** and **crosswind 0–15 m/s** @ **1000 m** using `ModelConfig.crosswind_mps`. **Not** 6-DOF or validated wind tunnel data.

```bash
python scripts/wind_loft_dispersion.py --verify
python scripts/wind_loft_dispersion.py --json-out data/wind_loft_dispersion.json
```

## `pk_geometry_sandbox.py`

Notional **P_geometric = exp(-(residual/R)²)** with **R = 1.55 m** and placeholder **P_kill|hit** by threat class (hover / crossing / glide). Uses `guidance_evasion_output.json`.

```bash
python scripts/pk_geometry_sandbox.py --verify
python scripts/pk_geometry_sandbox.py --json-out data/pk_geometry_sandbox.json
```

## `monte_carlo_envelope.py` / `run_light_dashboard.py`

Monte Carlo dispersion; dashboard regenerates JSON + PNGs including `guidance_evasion_sanity.png`.

## `mass_cg_calc.py`

Weighted CG from `baseline_systems.json` components; validates cube fragment mass vs warhead section.

```bash
python scripts/mass_cg_calc.py
```

## `make_system_triptych.py`

Landscape **Round | Launcher | Container** (horizontal L-R) for LinkedIn/pitch. Uses authoritative PNGs only (no AI regen).

```bash
python scripts/make_system_triptych.py
# -> visuals/output/radr-system-triptych-landscape.png
```

## Visual scripts

| Script | Purpose |
|--------|---------|
| `overlay_shoulder_bar.py` | Composite shoulder bar onto launcher art |
| `touchup_shoulder_bar.py` | Sleeve/bar touch-up on authoritative PNGs |

## CI

`.github/workflows/ci.yml` runs:

- `python scripts/radr_performance_model.py --verify`
- `python scripts/radr_trajectory.py --smoke`
- `python scripts/mass_cg_calc.py`
- `python scripts/guidance_evasion_sanity.py --verify`
- `python scripts/wind_loft_dispersion.py --verify`
- `python scripts/pk_geometry_sandbox.py --verify`

Wind and Pk JSON are **CLI-only** (not added to `run_light_dashboard.py`) to keep dashboard runtime short.
