# RADR Scripts

**Notional engineering tools only — not live-fire or certified ballistics.**

## `radr_trajectory.py`

Point-mass **2-D** trajectory: progressive thrust from [Annex H](../annexes/H-motor-progressive-burn.md), quadratic drag, sea-level air density, ~3.5° loft.

### Run

```bash
python scripts/radr_trajectory.py
python scripts/radr_trajectory.py --smoke
python scripts/radr_trajectory.py --json-out data/performance_model_output.json
```

### Assumptions

| Input | Nominal | Source |
|-------|---------|--------|
| Mass | 3.1 kg | `baseline_systems.json` |
| CdA reference | 0.35 m² | Baseline JSON (design bookkeeping area) |
| Boost / coast drag | Multipliers on reference | Calibrated to **330–350 m/s @ 1000 m** |
| Impulse | 3000 N·s | Thrust table scaled to locked band |
| Burn | 3.3 s | Motor baseline |

The integrator uses **separate boost and coast drag multipliers** on the baseline CdA so the locked velocity band is met in 2-D; this is not a literal \(C_d A = 0.35\ \mathrm{m}^2\) ballistic coefficient at 340 m/s.

### Outputs

- Burnout speed and downrange at motor tail-off  
- TOF and speed at **500 / 750 / 1000 / 1200 m**  
- Optional JSON: ranges, sensitivity flags, 0.5 s acceleration profile samples  

**1200 m** row is a **stretch trade-study** coordinate — not a locked KPP.

### Sensitivity CLI

Perturbations are implemented in code (`run_sensitivity`): ±5% mass, ±3% impulse, ±10% CdA reference. Re-run with `--json-out` after changing `Config` in the script for ad-hoc cases.

## Visual / overlay scripts

| Script | Purpose |
|--------|---------|
| `overlay_shoulder_bar.py` | Composite shoulder bar onto launcher art |
| `touchup_shoulder_bar.py` | Sleeve/bar touch-up on authoritative PNGs |

## CI

`.github/workflows/ci.yml` runs `python scripts/radr_trajectory.py --smoke` on each push/PR.
