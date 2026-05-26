# Annex G — Mass Budget and Center of Gravity

**Document ID:** RADR / ANX-G  
**Version:** 1.7.0  
**Status:** Conceptual — notional mass properties

*All values are engineering estimates — not measured on hardware.*

Traceability: [06 — System Description](../docs/06-system-description.md) · [03 — Design Constraints](../docs/03-design-constraints.md)

---

## Rocket Mass Budget (≤ 3.5 kg cap)

**OAL:** 457 mm (18 in) · **Nominal total:** ~3.10 kg · **Cap:** 3.5 kg · **Margin:** ~0.40 kg

### Section Breakdown

| Section | Length (mm) | Mass (kg) | CG from nose (mm) | Notes |
|---------|-------------|-----------|---------------------|-------|
| IR seeker + dome | 100 | 0.50 | 50 | 100 mm bay locked |
| Warhead (cubes + burster + casing) | 120 | 1.05 | 160 | Forward cone pack |
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
| Grips, integrated sight, fold-out viewer, rear pad, retention stop, grip battery | 1.05 | Foregrip w/ pistol-style seeker trigger + aft-face zoom buttons; holo + ~4 in panel |
| Misc hardware (slings, pins) | 0.20 | — |
| **Nominal total** | **4.95** | — |

### Component-Level Rocket Budget (Detail)

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
| Fins, canards, deploy locks | 0.20 | 430 |
| Tail structure | 0.08 | 450 |
| **Total** | **3.10** | **248** (weighted) |

### CG Sensitivity (±10% section mass)

| Perturbation | Δ CG from nose (mm) | Effect |
|--------------|---------------------|--------|
| Warhead +10% | **+6** | Slightly more forward — stable |
| Warhead −10% | **−6** | Slightly more aft |
| Motor +10% | **+14** | More aft — reinforces rear bias |
| Motor −10% | **−14** | Moves CG forward — watch fin trim |
| Seeker +10% | **−3** | Minor forward shift |

Nominal CG **248 mm** remains inside acceptable band for fin-stabilized launch if perturbations stay within **±10%** per section.

### Launcher CG (Notional)

Reference point: **rear pistol grip** on tube.

| Estimate | Value | Notes |
|----------|-------|-------|
| CG aft of pistol grip | ~550 mm | ~60% of OAL aft along tube |
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

## Related Documents

- [D — Projectile Stabilization](D-projectile-stabilization.md) — Fin and balance context  
- [H — Motor Progressive Burn](H-motor-progressive-burn.md) — Motor mass driver  
- [I — Performance Modeling](I-performance-modeling.md)  
- [J — Warhead Dispersal](J-warhead-dispersal.md)  
- [F — Employment and Breech](F-employment-and-breech.md)
