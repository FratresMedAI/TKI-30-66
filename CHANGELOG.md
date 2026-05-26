# Changelog

## v1.8.0 — 2026-05-25

### Agent 1 — Performance and modeling

- Added [`scripts/radr_trajectory.py`](scripts/radr_trajectory.py) (stdlib point-mass 2-D model) with `--smoke` and JSON export.
- Expanded [Annex I](annexes/I-performance-modeling.md): script traceability, 1200 m stretch table, acceleration profile, open questions.
- Synced `performance_model` in `data/baseline_systems.json` with script outputs; added `model_script` field.
- CI: trajectory smoke test in `.github/workflows/ci.yml`.
- [`scripts/README.md`](scripts/README.md) documents assumptions and drag calibration.

### Agent 2 — Mass, CG, and sizing

- [Annex G](annexes/G-mass-and-center-of-gravity.md) v1.8.0: launcher split (shoulder bar, retention stop), ±15% sensitivity, system CG stowed/deployed/loaded.
- `rocket_mass_budget` / `launcher_mass_budget` / `system_mass_budget` in baseline JSON.
- [`scripts/mass_cg_calc.py`](scripts/mass_cg_calc.py) rolls up component CG from JSON.

### Agent 3 — Mechanical (breech + retention)

- [Annex F](annexes/F-employment-and-breech.md) v1.8.0: gunner one-page summary, retention side view, breech/retention timeline, force table.
- [DOC-06](docs/06-system-description.md): links to authoritative annex sections; retention reset on breech open.

### Agent 4 — Motor and warhead

- [Annex H](annexes/H-motor-progressive-burn.md): grain geometry approach, manufacturing margin notes.
- [Annex J](annexes/J-warhead-dispersal.md): burster axial placement, ms-scale timing chain, **275-cube @ 1200 m trade-study (not locked)**.

### Locked specs unchanged

- **300 × 7 mm** @ **1000 m**; **330–350 m/s**; motor impulse **2950–3050 N·s**; launcher/round mass caps.
