# RADR mk.60 — Rocket round (CAD design spec)

**Status:** **Locked** — CAD spec and authoritative concept art (`radr-round-authoritative.png`, v1 stowed fins). Do not regenerate.

Parent: [`CONTAINER-SPEC.md`](CONTAINER-SPEC.md) (tank-shell tube, load sequence).

---

## Overall philosophy

- **Self-contained** 18 in (~457 mm), **≤ 3.5 kg** projectile inside the protective tube.
- After breech close + **rocket ready** (continuity), **launcher retention stop** holds the **tube** until front trigger + lock tone; rocket must **exit cleanly** with negligible tube drag.
- **KISS:** rugged sections, frangible forward paths for dispersal, **4 × swept spring fins** (locked; 3-fin remains a trade only).

**Not on the round:** **Digital sight 1×–20×** is **launcher hardware** (foregrip **+ / −**), not integrated in the seeker nose.

---

## Authoritative art (locked)

| Asset | File | Notes |
|-------|------|-------|
| **Authoritative round** | [`output/radr-round-authoritative.png`](output/radr-round-authoritative.png) | **Locked** — copy of v1 stowed fins; do not regenerate |
| **Source v1** | [`output/radr-round-v1-stowed-fins.png`](output/radr-round-v1-stowed-fins.png) | Same image as authoritative (archive filename) |

### Review only (not authoritative)

| Variant | File | Notes |
|---------|------|-------|
| **V2 — fins deploying** | [`output/radr-round-v2-fins-deploy.png`](output/radr-round-v2-fins-deploy.png) | Exit moment — reference only |

**View:** Horizontal **left = nose (seeker)**, **right = tail (nozzle)** — matches container convention (container **left = top**).

---

## Key dimensions (locked with repo)

| Parameter | Spec | Source |
|-----------|------|--------|
| **OAL** | **457 mm** (18 in max) | DOC-02, Annex G |
| **Body OD** | **60 mm** nominal | Caliber lock |
| **OD in tube** | Smaller than tube ID — annular clearance | CONTAINER-SPEC |
| **Mass** | **Nominal ~3.1 kg**, **≤ 3.5 kg** cap | Annex G, `baseline_systems.json` |
| **Seeker bay** | **100 mm** IR dome + moderate-maneuver **nose canards** | Locked |

---

## Packaging order (nose → tail)

| Section | Length (nominal) | Mass (nominal) | Notes |
|---------|------------------|----------------|-------|
| **Nose / seeker** | 100 mm | 0.50 kg | IR F&F seeker; **2 nose canards**; frangible forward path for cube egress |
| **Warhead** | ~120 mm | 1.05 kg | **300 × 7 mm** dense alloy rough cubes + pyrotechnic dispersal; proximity + timed backup |
| **Avionics** | ~40 mm | 0.15 kg | Fuze, bus, battery share |
| **Motor** | ~297 mm case / ~260 mm grain | 1.20 kg | Mildly progressive solid; see motor table below |
| **Tail** | ~50 mm | 0.20 kg | **4 swept** spring fins + nozzle + locks |

Layout traceability: [Annex J](../annexes/J-warhead-dispersal.md) (burster **forward of cube pack**).

---

## Motor & trajectory (repo math — use these numbers)

Values below match [`scripts/radr_trajectory.py`](../scripts/radr_trajectory.py), [Annex H](../annexes/H-motor-progressive-burn.md), and CI smoke (**334.7 m/s @ 1000 m**, TOF ~4.12 s @ 3.1 kg).

| Parameter | **Locked / modeled** | Draft CAD note (do not use) |
|-----------|----------------------|-----------------------------|
| **Total impulse** | **2950–3050 N·s** (nominal **3000**) | 3200–3300 N·s — **too high** for locked **330–350 m/s @ 1000 m** without retuning mass/drag |
| **Burn time** | **~3.3 s** | ✓ aligns |
| **Initial thrust** | **~750–850 N** (first ~1–2 s) | 750–900 N — acceptable near band |
| **Peak thrust** | **~1050–1150 N** | 1100–1300 N — **high** vs backblast / 10 yd SOP margin |
| **Velocity @ 1000 m** | **330–350 m/s** (smoke **334.7**) | Set by calibrated 2-D model, not higher impulse alone |

Thrust table integral (unscaled): **~2741 N·s**; script scales **× ~1.095** → **3000 N·s** nominal.

---

## Warhead (repo lock vs draft)

| Item | **Locked** | Draft CAD |
|------|------------|-----------|
| Cube count | **300 × 7 mm** | 275 @ 1200 m — **not worth it** (~+0.3 m/s @ 1200 m for −60 g; see [Annex J](../annexes/J-warhead-dispersal.md#trade-study-275-cube-pack-1200-m-stretch--not-locked)) |
| Pattern | Forward-biased cone **~10–12 ft** @ **~20 ft** | ✓ aligns |
| Cube mass (steel-equiv sanity) | **~0.81 kg** fragment mass alone | 275 → **~0.74 kg** (−70 g — minor) |

---

## Center of gravity (Annex G — trust over “forward of center” wording)

Weighted notional CG from nose:

\[
x_{cg} \approx 248\ \text{mm}\ (\sim 54\%\ \text{OAL})
\]

- **Aft of geometric mid-body** (~229 mm) because motor mass dominates the tail.
- **Ahead of the motor centroid** — sensible for **moderate nose canards** (trim authority without tail-heavy instability at launch).

Stowed in tube: CG unchanged; clearance ring does not shift CG requirement.

---

## Interfaces (launcher / tube)

| Interface | Spec |
|-----------|------|
| **Electrical** | Light **foil / pad** contacts — continuity with tube when seated → **rocket ready** |
| **Retention** | Stop bears on **tube aft shoulder**, not rocket OD |
| **Launch** | No bind; rocket **shoots out** when stop releases |
| **Survivability** | Launch accel + flight loads; fins deploy and **mechanically lock** after exit |

---

## Constraints (locked)

- Fit in tube with **clearance all sides**.
- Fins **stow flat** (V1 art) → deploy + lock (V2 art).
- Electrical path **reliable**, **negligible** launch resistance.
- **≤ 3.5 kg**; trained load cycle under **10 s** with tube (CONTAINER-SPEC).

---

## Math cross-check summary

| Check | Result |
|-------|--------|
| `radr_trajectory.py --smoke` | **PASS** — v@1000 m = **334.7 m/s** ∈ [330, 350] |
| Impulse nominal | **3000 N·s** (not 3200+) |
| Mass nominal | **3.1 kg** (within 3.3–3.5 kg goal band) |
| Cube count | **300** locked |

Authoritative art locked **2026-05-25** from v1 stowed fins. Regenerate only on explicit art revision; update ROUND-SPEC if replaced.
