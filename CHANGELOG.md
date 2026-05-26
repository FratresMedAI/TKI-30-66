# Changelog

## v1.8.3 — Partner validation & analytic gaps (2026-05-24)

- **Live-fire / partner path:** [DOC-11](docs/11-live-fire-and-partner-validation.md) Phase 2 gates (2A–2D), instrumentation, collaboration hooks; [`data/live_fire_results.template.json`](data/live_fire_results.template.json) (`status: pending` — no fabricated test data).
- **Mechanical:** [Annex F](annexes/F-employment-and-breech.md) v1.10 — solenoid + release cam baseline (M-01 closed), prototype tolerance stack; [DOC-06](docs/06-system-description.md) retention baseline locked.
- **Wind / loft:** `crosswind_mps` on performance model; [`scripts/wind_loft_dispersion.py`](scripts/wind_loft_dispersion.py), `data/wind_loft_dispersion.json`, CI verify.
- **Notional Pk:** [`scripts/pk_geometry_sandbox.py`](scripts/pk_geometry_sandbox.py), `data/pk_geometry_sandbox.json`; [Annex I](annexes/I-performance-modeling.md) wind/Pk sections + traceability; **6-DOF explicitly deferred** (I-07).
- CI: DOC-11 required; template JSON validation; wind + Pk script checks.

## v1.8.2 — Phase 0 closure pack (2026-05-25)

- **Round authoritative art:** `radr-round-authoritative.png` (v1 stowed fins); [ROUND-SPEC](visuals/rocket/ROUND-SPEC.md), README gallery, `baseline_systems.json` `rocket_round`.
- **Validated vs notional:** [Annex I § traceability](annexes/I-performance-modeling.md#validated-vs-notional-traceability) + README summary; MC / guidance limits updated.
- **Guidance sanity:** [`scripts/guidance_evasion_sanity.py`](scripts/guidance_evasion_sanity.py) (20–30 m/s²), `data/guidance_evasion_output.json`, dashboard PNG, CI.
- **Motor vendor path:** Annex H grain sketch + vendor packet; [DOC-09](docs/09-motor-vendor-brief.md).
- **Phase 1 gates:** [DOC-10](docs/10-phase-1-prototype-gates.md) — 1A breech/retention, 1B tube/continuity, 1C fire-control UX.

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

## v1.8.1 — Digital sight (2026-05-25)

- Replaced holographic **1.5×–4×** optic with **digital camera-style sight**, **smooth 1×–20×** zoom.
- **+ / −** on foregrip wired to sight + fold-out display; **RPG-style shouldering** (no cheek weld).
- Updated README, DOC-01/02/03/05/06, Annex F/G/I/J, `baseline_systems.json`, pitch deck draft.

## Container art + two-end closure (2026-05-25)

- Locked [`visuals/rocket/output/radr-container-authoritative.png`](visuals/rocket/output/radr-container-authoritative.png) — **pop top** (PULL) + **breech screw cap** (hand-unscrew).
- Side view: **left = top**, **right = breech**. Prep sequence in Annex F, JSON `round_packaging`, README gallery.

## Jupyter dashboard + RunPod guide (2026-05-25)

- [`notebooks/RADR_Performance_Dashboard.ipynb`](notebooks/RADR_Performance_Dashboard.ipynb) — range, sensitivity, evasion, Monte Carlo (`N_MC` 200 laptop / 5000+ pod).
- [`scripts/monte_carlo_envelope.py`](scripts/monte_carlo_envelope.py), [`requirements-modeling.txt`](requirements-modeling.txt), [`notebooks/RUNPOD-QUICKSTART.md`](notebooks/RUNPOD-QUICKSTART.md).

## Performance model v2 — traceable ballistics (2026-05-25)

- New [`scripts/radr_performance_model.py`](scripts/radr_performance_model.py): explicit \(C_d A\) in m², rocket-equation checks, range 200–1200 m, cube mass, evasion table, sensitivity.
- Regenerated [`data/performance_model_output.json`](data/performance_model_output.json); CI verify + `mass_cg_calc.py` warhead check.
- [Annex I](annexes/I-performance-modeling.md) v1.9 aligned to v2 outputs.

## Range envelope: 200 m min, 800–1200 m band, 1000 m sweet spot (2026-05-25)

- **200 m** minimum (not 150 m) — seeker/fuze margin; **800–1200 m** primary; **1000 m** sweet spot; **1200 m** max. JSON + DOC-01/02, Annex A/B/I/H.

## Tank-shell CAD spec + load sequence (2026-05-25)

- Official [`CONTAINER-SPEC.md`](visuals/rocket/CONTAINER-SPEC.md): tube stays in launcher; rocket clearance; foil continuity; under **10 s** trained load.
- Load order: **pop top → slide tube in → unscrew bottom in bore → close → rocket ready → arm/fire**.
- Render unchanged. Annex F, DOC-01–06, JSON `round_packaging` + `rocket_tube_interface`.

## Rocket CAD spec + render attempts (2026-05-25)

- [`ROUND-SPEC.md`](visuals/rocket/ROUND-SPEC.md): full rocket CAD; reconciled to **300 cubes**, **2950–3050 N·s**, **330–350 m/s** (`radr_trajectory.py` smoke **334.7**).
- Review renders: `radr-round-v1-stowed-fins.png`, `radr-round-v2-fins-deploy.png`. Digital sight stays on **launcher**, not round.
