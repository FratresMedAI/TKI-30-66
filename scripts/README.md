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

## `mass_cg_calc.py`

Weighted CG from `baseline_systems.json` components; validates cube fragment mass vs warhead section.

```bash
python scripts/mass_cg_calc.py
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
