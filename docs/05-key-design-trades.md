# 05 — Key Design Trades

**Document ID:** TKI-30-66 / DOC-05  
**Version:** 0.4.0  
**Status:** Conceptual

Trade matrix: [Annex C — Trades Matrix](../annexes/C-trades-matrix.md)

---

## 0. KISS and Lightweight as Primary Drivers

When trades conflict, **simplicity and low mass** take priority over peak range, feature count, and lowest unit cost at any quality tier.

| Rule | Implementation |
|------|----------------|
| One rocket SKU | Ti BB flak + onboard IR only |
| No external designator | Gunner lock-and-fire |
| Minimum electronics | Seeker + fuze + autopilot on rocket |
| Lightweight structure | 18 in max OAL; mass goal ~2.3 kg |

---

## 1. Caliber: Size vs. Rocket Volume

| Caliber | Launcher Mass | Rocket Capacity | Backblast |
|---------|---------------|-----------------|-----------|
| 40 mm | Lightest | Smallest BB load | Lowest |
| **50 mm ★** | **~7 kg** | **Balanced** | **Low–moderate** |
| 58–66 mm | Heavier | More BBs | Moderate |

**Recommendation:** **50 mm nominal** within 40–66 mm envelope.

---

## 2. Rocket Length

| Option | Mass | BB payload | Pack fit |
|--------|------|------------|----------|
| ~305 mm (12 in) | Lightest | Smallest cloud | Best |
| **≤ 457 mm (18 in) ★** | **Moderate** | **More BBs** | **Acceptable** |
| > 457 mm | Heavy | Marginal gain | Poor |

**Recommendation:** **Up to 457 mm (18 in) maximum**, design toward minimum mass within envelope.

---

## 3. Payload Type (Critical)

| Payload | vs. Hover UAS | Collateral | Logistics |
|---------|---------------|------------|-----------|
| Unitary kinetic rod | High precision | Low (miss = rod impact) | Simple |
| Flechette pack | Moderate spread | Moderate | Moderate |
| HE-frag | High | High | Regulated |
| **Ti BB flak ★** | **Good cloud coverage** | **Moderate BB hazard** | **Simple; non-explosive** |

**Recommendation:** **Ti BB flak dispersal** — matches rocket-delivered flak concept; lighter than HE; broader defeat than single rod.

---

## 4. Guidance Architecture (Critical)

| Architecture | Employment | Cost | Notes |
|--------------|------------|------|-------|
| **Onboard IR fire-and-forget ★** | **Gunner lock-and-fire** | **~$200–400/rd** | **Baby MANPADS class** |
| Laser beam-riding | Designator required | Lower seeker | **Rejected** |
| Launcher-tracked guidance | 2-step cue | Launcher complexity | **Removed** |
| Unguided | Cheap | Low Pk | Insufficient |

**Recommendation:** **Onboard IR seeker, fire-and-forget**, drone-optimized (simplified vs. full Stinger).

---

## 5. Dispersal Mechanism (Open)

| Option | Pros | Cons |
|--------|------|------|
| Proximity IR fuze | Adapts to miss distance | CCM, fuze reliability |
| Timed fuze | Simple | Range/wind sensitivity |
| Seeker-gated | Uses track quality | Software complexity |

**Baseline:** Not locked — proximity IR fuze preferred in analysis; see open questions in README.

---

## 6. Backblast vs. Performance

**Recommendation:** **Hybrid backblast mitigation** with moderate muzzle velocity (~650 m/s class).

---

## 7. Launcher Life Cycle

**Recommendation:** **Reusable flip-breech launcher** — no disposable tube.

---

## Trade Decision Summary

| Trade | Baseline | Status |
|-------|----------|--------|
| Philosophy | KISS, lightweight, cheap per shot | Set |
| Caliber | 50 mm | Set |
| Rocket length | ≤ 457 mm (18 in max) | Set |
| Payload | Ti BB flak | Set |
| Guidance | Onboard IR F&F | Set |
| Beam-riding / launcher-tracked / BIT | Removed | — |
| Kinetic rod | Removed | — |
| Launcher | Reusable tube, simple sight | Set |
| Team | Gunner + ammo bearer | Set |

---

[← CONOPS / Use Cases](04-conops-use-cases.md) | [Next: System Description →](06-system-description.md)
