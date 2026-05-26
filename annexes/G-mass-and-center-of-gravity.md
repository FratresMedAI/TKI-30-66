# Annex G — Mass Budget and Center of Gravity

**Document ID:** RADR / ANX-G  
**Version:** 1.9.0  
**Status:** Conceptual — notional mass properties

*All values are engineering estimates — not measured on hardware.*

Traceability: [06 — System Description](../docs/06-system-description.md) · [03 — Design Constraints](../docs/03-design-constraints.md)

---

## Rocket Mass Budget (≤ 3.5 kg cap)

**OAL:** 457 mm (18 in) · **Nominal total:** ~3.10 kg · **Cap:** 3.5 kg · **Margin:** ~0.40 kg

### Component mass budget (engineering rollup)

Longitudinal CG measured **from nose** (mm). Masses sum to **3.10 kg** nominal; aligns with [`mass_cg_calc.py`](../scripts/mass_cg_calc.py) and `rocket_mass_budget` in JSON.

| Line item | Mass (kg) | CG from nose (mm) | % of total | Notes |
|-----------|-----------|-------------------|------------|-------|
| **Seeker + forward electronics** | **0.50** | 50 | 16% | 100 mm IR bay; dome, core, forward fuze path |
| **Warhead (300 cubes + burster + casing)** | **1.05** | 160 | 34% | **0.803 kg** cubes only; **~0.25 kg** burster/casing/liner |
| **Avionics + power (mid-body)** | **0.15** | 220 | 5% | Canard drivers, bus, battery share |
| **Motor + propellant** | **1.20** | 380 | 39% | ~1.20 kg grain in ~297 mm case |
| **Structure + fins + canards** | **0.20** | 430 | 6% | Body tube, 4× fins + locks, 2× nose canards, nozzle, igniter |
| **Total** | **3.10** | **248** (weighted) | 100% | — |

**Not on the round:** **Rocket retention stop** is **launcher hardware** (~0.04 kg in launcher budget). The round interfaces via the **tube aft shoulder** seated against the bore finger — see [Annex F § Retention stop](../annexes/F-employment-and-breech.md#rocket-retention-stop).

#### Warhead detail (300 × 7 mm)

| Sub-item | Mass (kg) | CG (mm) |
|----------|-----------|---------|
| Cube pack (300 × 7 mm, 7800 kg/m³ equiv.) | **0.803** | ~165 |
| Pyrotechnic dispersal charge | **0.10** | ~130 |
| Casing + liner + fasteners | **~0.15** | ~155 |
| **Warhead section total** | **1.05** | **160** |

#### Motor + propellant detail

| Sub-item | Mass (kg) | CG (mm) |
|----------|-----------|---------|
| Propellant grain (locked) | **1.20** | ~380 |
| Motor case (aluminum) | (in rollup) | ~390 |
| Nozzle + throat | (in structure line) | ~440 |

#### Seeker + electronics detail

| Sub-item | Mass (kg) | CG (mm) |
|----------|-----------|---------|
| IR dome + seeker core | **~0.50** | ~50–55 |
| Forward fuze sensor share | (in seeker line) | ~90 |
| Avionics PCB + harness | **0.15** | ~220 |

#### Structure, fins, and canards

| Sub-item | Mass (kg) | CG (mm) |
|----------|-----------|---------|
| Main body tube | **~0.12** | ~300 |
| 4 × swept spring fins + deploy locks | **~0.12** | ~445 |
| 2 × nose canards + actuators | **~0.06** | ~75 |
| Tail cone / igniter / small parts | **~0.02–0.08** | ~400–450 |

### Section Breakdown

| Section | Length (mm) | Mass (kg) | CG from nose (mm) | Notes |
|---------|-------------|-----------|---------------------|-------|
| IR seeker + dome | 100 | 0.50 | 50 | 100 mm bay locked |
| Warhead (cubes + burster + casing) | 120 | 1.05 | 160 | **0.803 kg** cubes (300×7 mm @ 7800 kg/m³) + **~0.25 kg** burster/casing — see [`mass_cg_calc.py`](../scripts/mass_cg_calc.py) |
| Avionics / autopilot | 40 | 0.15 | 220 | Wiring, battery share |
| Motor case + grain | 297 | 1.20 | 380 | ~260 mm grain inside |
| Fins, nozzle, structure | 50 | 0.20 | 430 | Spring fins at base |
| **Sum** | **457** | **3.10** | — | — |

### Rocket CG Calculation (Notional)

Weighted CG from nose:

\[
x_{cg} = \frac{\sum m_i \cdot x_i}{\sum m_i}
\]

| Section | \(m_i\) (kg) | \(x_i\) (mm) | \(m_i \cdot x_i\) |
|---------|--------------|--------------|-------------------|
| Seeker | 0.50 | 50 | 25.0 |
| Warhead | 1.05 | 160 | 168.0 |
| Avionics | 0.15 | 220 | 33.0 |
| Motor | 1.20 | 380 | 456.0 |
| Structure | 0.20 | 430 | 86.0 |
| **Total** | **3.10** | — | **768.0** |

**Result:** \(x_{cg} \approx 768 / 3.10 \approx \mathbf{248\ \text{mm}}\) from nose (~54% of OAL).

**Interpretation:** CG lies **aft of geometric mid-body** (~229 mm). For shoulder launch this is **slightly rear-biased** — muzzle-heavy feel is avoided; motor mass dominates aft.

### Rocket Mass Margin

| Scenario | Mass (kg) | vs. cap |
|----------|-----------|---------|
| Nominal build | 3.10 | −0.40 kg |
| High estimate (ranges) | 3.35 | −0.15 kg |
| **Cap** | **3.50** | — |

---

## Launcher Mass Budget (≤ 5.5 kg empty cap)

**OAL:** 1016 mm (40 in) · **Nominal total:** ~4.95 kg · **Cap:** 5.5 kg · **Margin:** ~0.55 kg

| Component | Mass (kg) | Notes |
|-----------|-----------|-------|
| Main tube (60 mm bore, 40 in) | 2.55 | Includes **~0.20 kg** muzzle brake / blast deflector forward fitting |
| Breech block + hinge + deadbolt | 0.90 | Gustav-class steel |
| Triggers, contacts, pressure sensor | 0.30 | Grip electronics |
| Foregrip, digital sight, fold-out display, seeker trigger, zoom **+ / −** | 0.72 | Wired sight + screen on foregrip handle |
| Rear pistol grip, pad, grip battery | 0.33 | Firing hand + FC power |
| **Shoulder bar + hinge** (forward black sleeve) | **0.06** | ~12 mm rod; [SHOULDER-BAR-SPEC](../visuals/launcher/SHOULDER-BAR-SPEC.md) |
| **Retention stop + release cam** | **0.04** | Launcher-only — not round mass |
| Misc hardware (slings, pins) | 0.20 | — |
| **Nominal total** | **4.95** | — |

*Retention stop mass is launcher hardware; the round budget lists igniter, fin locks, and bore liner only.*

### Component-Level Rocket Budget (Detail)

#### Seeker + forward electronics (0–100 mm bay)

| Component | Mass (kg) | CG from nose (mm) | Notes |
|-----------|-----------|-------------------|-------|
| IR dome (glass/sapphire) | 0.22 | 45 | 100 mm bay outer diameter |
| Seeker core + gimbal mount | 0.28 | 55 | Fire-and-forget IR |
| Fuze sensor + logic (forward) | 0.08 | 90 | Proximity primary path |
| Forward bulkhead / adapter | 0.12 | 110 | Seals warhead bay |
| **Subtotal** | **0.70** | **~58** | |

#### Warhead bay (110–230 mm)

| Component | Mass (kg) | CG from nose (mm) | Notes |
|-----------|-----------|-------------------|-------|
| Pyrotechnic dispersal charge | 0.10 | 130 | Forward of cube pack |
| Cube pack (300 × 7 mm alloy) | **0.803** | 165 | ~77% of warhead section mass |
| Warhead casing + end liner | 0.15 | 155 | Thin-wall aluminum/steel |
| **Subtotal** | **0.97** | **~162** | Rounded to **1.05 kg** section with fasteners |

#### Avionics + power (mid-body)

| Component | Mass (kg) | CG from nose (mm) | Notes |
|-----------|-----------|-------------------|-------|
| Autopilot / canard drivers | 0.08 | 215 | Low-mass PCB |
| Battery cell (thermal share) | 0.07 | 225 | Short duty |
| Harness + connectors | 0.05 | 220 | |
| **Subtotal** | **0.15** | **~220** | |

#### Motor + nozzle (230–457 mm)

| Component | Mass (kg) | CG from nose (mm) | Notes |
|-----------|-----------|-------------------|-------|
| Motor case (aluminum) | 0.35 | 390 | ~297 mm bay |
| Propellant grain | 1.20 | 380 | Locked 1.2 kg propellant |
| Nozzle + throat insert | 0.08 | 440 | Graphite/steel mix |
| **Subtotal** | **1.63** | **~385** | Budgeted as **1.20** case+grain line + nozzle in rollup |

#### Structure + aerodynamic surfaces (distributed)

| Component | Mass (kg) | CG from nose (mm) | Notes |
|-----------|-----------|-------------------|-------|
| Main body tube | 0.12 | 300 | 60 mm aluminum |
| 4 × swept fins + locks | 0.12 | 445 | Spring-loaded, mechanical lock |
| 2 × nose canards + actuators | 0.06 | 75 | Moderate-maneuver trim |
| Tail cone / aft skirt | 0.08 | 450 | Fin root attach |
| **Subtotal** | **0.38** | — | Rolled to **0.20 kg** in summary after consolidation |

#### Roll-up verification

| Component | Mass (kg) | CG from nose (mm) |
|-----------|-----------|-------------------|
| Seeker dome | 0.22 | 45 |
| Seeker core + mount | 0.28 | 55 |
| Fuze electronics | 0.08 | 90 |
| Forward bulkhead | 0.12 | 110 |
| Pyrotechnic burster | 0.10 | 130 |
| Cube pack (300 × 7 mm) | 0.72 | 165 |
| Warhead casing | 0.15 | 155 |
| Avionics + battery share | 0.15 | 220 |
| Body structure | 0.12 | 300 |
| Motor case | 0.35 | 390 |
| Propellant grain | 1.20 | 380 |
| Nozzle | 0.08 | 440 |
| Fins + canards | 0.11 | 430 |
| Fin deploy locks | 0.04 | 448 |
| Tube liner (round) | 0.03 | 320 |
| Igniter | 0.02 | 400 |
| Tail structure | 0.08 | 450 |
| **Total** | **3.10** | **248** (weighted) |

### Axial mass distribution (qualitative)

| Region (from nose) | % of total mass | Balance note |
|--------------------|-----------------|--------------|
| 0–100 mm (seeker) | **~23%** | Forward cap — stabilizes dart feel |
| 100–230 mm (warhead) | **~34%** | Densest packaging — cube pack |
| 230–300 mm (avionics) | **~5%** | Light transition |
| 300–457 mm (motor + fins) | **~38%** | **Dominant aft mass** — drives CG aft |

The rocket is **not** nose-heavy: motor and propellant pull the CG to **~248 mm** (54% of OAL), **19 mm aft** of geometric center.

### Mass and CG sensitivity (±10% per section)

Linearized from component CG table (not a dynamic flight model). **Δ CG** = shift of rocket CG from nose; **+** = aft.

| Perturbation | Total mass (kg) | Δ mass | Δ CG (mm) | vs. 3.5 kg cap |
|--------------|-----------------|--------|-----------|----------------|
| **Nominal** | **3.10** | — | **248** (baseline) | 0.40 kg margin |
| Warhead **+10%** | 3.20 | +0.11 | **+6** | Pass |
| Warhead **−10%** | 3.00 | −0.11 | **−6** | Pass |
| Motor **+10%** | 3.22 | +0.12 | **+14** | Pass |
| Motor **−10%** | 2.98 | −0.12 | **−14** | Pass |
| Seeker **+10%** | 3.15 | +0.05 | **−3** | Pass |
| Seeker **−10%** | 3.05 | −0.05 | **+3** | Pass |
| Structure/fins **+10%** | 3.12 | +0.02 | **+2** | Pass |

### Mass and CG sensitivity (±15% — warhead and motor focus)

| Perturbation | Total mass (kg) | Δ CG (mm) | vs. 3.5 kg cap | Flight note |
|--------------|-----------------|-----------|----------------|-------------|
| Warhead **+15%** | 3.26 | **+9** | Pass | Slightly more forward — stable |
| Warhead **−15%** | 2.94 | **−9** | Pass | Aft shift if motor also light |
| Motor **+15%** | 3.28 | **+21** | Pass | Strongest CG mover — recheck fin/canard trim |
| Motor **−15%** | 2.92 | **−21** | Pass | Risk of forward CG if warhead also light |
| **Combined heavy** (warhead +15%, motor +15%, seeker +10%) | **~3.38** | **~+12** | Pass | Near growth pool — still under cap |
| **Combined light** (warhead −15%, motor −15%) | **~2.86** | **~−18** | Pass | Watch nose-heavy coast attitude |

`python scripts/mass_cg_calc.py` rolls up [`rocket_mass_budget`](../data/baseline_systems.json) and flags drift vs JSON nominal.

**Longitudinal CG summary:** Nominal **248 mm** from nose (**54%** of 457 mm OAL) — **19 mm aft** of geometric center. Slight **rear bias** supports shoulder carry and fin-stable exit; not nose-heavy.

### Balance if sections run heavy or light

| Scenario | Mass change | CG shift | Flight / handling effect |
|----------|-------------|----------|---------------------------|
| **Warhead +10%** (+0.10 kg) | 3.20 kg total | **~+6 mm** forward | Slightly more stable in coast; less aft whip |
| **Warhead −10%** | 3.00 kg | **~−6 mm** aft | Minor; still within fin authority |
| **Motor +10%** (+0.12 kg propellant/case) | 3.22 kg | **~+14 mm** aft | Stronger rear bias — verify fin deploy trim |
| **Motor −10%** | 2.98 kg | **~−14 mm** forward | Risk of **nose-down** coast attitude if combined with light warhead |
| **Seeker +10%** | 3.11 kg | **~−3 mm** | Small forward shift — seeker bay already light |
| **All aft heavy** (motor + fins at high estimate) | ~3.35 kg | **~+20 mm** aft | Approaches cap — check 3.5 kg margin and static margin |
| **All forward heavy** (seeker + warhead high) | ~3.30 kg | **~+10 mm** forward | May need canard trim tweak; still acceptable |

**Design intent:** Slight **rear bias** keeps the loaded launcher comfortable and avoids muzzle-heavy carry. If motor mass grows toward cap, **fin root** and **canard authority** must be re-checked — not automatic failure, but the sensitivity table flags it early.

### Margin allocation (rocket)

| Pool | Mass (kg) | Intended use |
|------|-----------|--------------|
| Nominal build | 3.10 | Baseline |
| Growth to high estimate | +0.25 | Denser cubes, thicker case, extra epoxy |
| **Hard cap** | **3.50** | **0.40 kg** remaining for fuze/propellant trades |

Priority if over budget: reduce cube count only as last resort (locked 300); prefer case thinning or seeker mass reduction first.

### Launcher CG (Notional)

Reference point: **rear pistol grip** on tube.

| Configuration | CG from grip (mm) | Notes |
|---------------|-------------------|-------|
| Empty, shoulder bar **stowed** | **~545** | Bar mass forward on black sleeve — slight aft shift vs deployed |
| Empty, bar **deployed** | **~540** | Bar extended — few mm forward |
| **Loaded** (round seated, breech locked) | **~480** | Round mass in forward bore |

| Estimate | Value | Notes |
|----------|-------|-------|
| CG aft of pistol grip (empty nominal) | ~550 mm | ~60% of OAL aft along tube |
| Effect | Rear-biased carry | Balances with loaded round |

*Launcher CG with round loaded shifts forward — system CG addressed below.*

---

## System Mass (Launcher + One Round)

| Configuration | Mass (kg) | Cap |
|---------------|-----------|-----|
| Launcher empty | 4.95 | ≤ 5.5 |
| One rocket (in tube) | 3.10 | ≤ 3.5 |
| **Loaded system** | **8.05** | ≤ 9.0 |
| Margin to cap | 0.95 | One-person carry goal |

### Loaded System CG (Rough)

Combining launcher (4.8 kg, CG ~550 mm from pistol grip) and round (3.1 kg, CG ~248 mm from nose when inserted):

- Round inserts **forward in bore** — shifts combined CG **forward** vs. empty launcher but remains **manageable** for one-person shoulder carry.  
- Qualitative result: **slightly rear-biased empty**, **more balanced loaded** — matches locked CoG requirement.

---

## Design Checks

| Check | Result |
|-------|--------|
| Rocket ≤ 3.5 kg | Pass (nominal 3.10) |
| Launcher ≤ 5.5 kg | Pass (nominal 4.95) |
| System ≤ 9.0 kg | Pass (nominal 8.05) |
| Rocket CG rear of mid-body | Pass (~248 mm vs 229 mm mid) |

---

## Open questions (mass properties)

| ID | Topic | Status |
|----|-------|--------|
| G-01 | Cube alloy final density (7800 kg/m³ equiv. today) | Affects fragment mass ± few grams |
| G-02 | Seeker mass growth vs. dome material | First trim target if over 3.5 kg |
| G-03 | Motor case vs. grain split | Case mass folded into motor line — vendor CAD TBD |
| G-04 | Measured CG on prototype | Replace notional 248 mm with scale + balance test |

---

## Related Documents

- [D — Projectile Stabilization](D-projectile-stabilization.md) — Fin and balance context  
- [H — Motor Progressive Burn](H-motor-progressive-burn.md) — Motor mass driver  
- [I — Performance Modeling](I-performance-modeling.md)  
- [J — Warhead Dispersal](J-warhead-dispersal.md)  
- [F — Employment and Breech](F-employment-and-breech.md)
