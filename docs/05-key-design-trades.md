# 05 — Key Design Trades

**Document ID:** TKI-30-66 / DOC-05  
**Version:** 0.3.0  
**Status:** Conceptual

Trade matrix: [Annex C — Trades Matrix](../annexes/C-trades-matrix.md)

---

## 0. Reliability as Primary Design Driver

When trades conflict, **reliability wins** over unit cost, peak range, and feature count.

| Reliability Rule | Implementation |
|------------------|----------------|
| Test before fire | Mandatory pre-fire BIT at breech contact; no-fire on fail |
| Minimize round electronics | Quad-cell IR only — no imaging FPA, no radar on baseline |
| Reuse smart hardware | Tracker + BIT logic in launcher (field-replaceable module) |
| Mechanical over pyrotechnic | Spring fin deploy; mechanical breech interlock |
| Redundancy on critical mechanics | Dual springs per fin |
| Conservative propulsion | ~650 m/s muzzle velocity class — lower shock, higher seeker survival |
| Single guidance SKU | One round type; reject dual-mode seekers |
| Factory round QA | 100% BIT at production; lot sampling for live function |

---

## 1. Caliber: Size vs. Payload / Guidance

### Options

| Caliber | Launcher Mass | Round Mass | KE at 600 m/s | Backblast |
|---------|---------------|------------|---------------|-----------|
| 40 mm | ~6.0 kg | ~1.8 kg | Low | Low |
| **50 mm ★** | **~8.0 kg** | **~2.5 kg** | **Moderate** | **Low–moderate** |
| 58–66 mm | ~9.5 kg | ~3.5 kg | High | Moderate |

### Analysis

Smaller caliber reduces carry burden but limits seeker aperture, propellant volume, and terminal kinetic energy. At 40 mm, defeating Group 2 UAS (9–25 kg) at 600 m becomes marginal. At 58–66 mm, the system approaches Carl Gustaf mass without proportional guidance benefit.

### Recommendation

**50 mm nominal** within a 40–66 mm design envelope.

---

## 2. Backblast Mitigation vs. Performance

### Options

| Approach | Backblast Reduction | Velocity Impact | Complexity |
|----------|--------------------|-----------------|------------|
| Countermass (recoilless) | High | Moderate loss | Low |
| Soft launch (eject then ignite) | High | Low loss | Moderate |
| **Hybrid ★** | **High** | **Moderate loss** | **Moderate** |
| Conventional (minimal mitigation) | None | Maximum | Lowest |

### Recommendation

**Hybrid backblast mitigation** selected for Phase 1 study.

---

## 3. Reusable Launcher vs. Disposable Tube

### Recommendation

**Reusable flip-breech launcher** with integrated IR tracker (reusable guidance asset).

---

## 4. Guidance Architecture (Critical Trade)

**Constraint:** No laser beam-riding.

### Options

| Architecture | Reliability | Round Cost | Notes |
|--------------|-------------|------------|-------|
| **Launcher IR + quad-cell round IR (LOBL) ★** | **High** | Moderate | BIT before fire; proven architecture |
| Imaging IR FPA on round | Moderate | High | FPA damage, calibration drift |
| FMCW radar on round | Moderate | High | RF failure modes; active signature |
| Command guidance only (datalink) | Low–moderate | Low round | Link break = miss; EW vulnerable |
| Round-only seeker (no launcher tracker) | Moderate | Higher | Harder LOBL; more operator error |

### Analysis

**Javelin model + reliability hardening:** Reusable tracker runs BIT on every round before fire. Quad-cell seeker on round is the **simplest IR homing head** — four detector elements, no microbolometer array, no moving parts. Failed rounds never leave the tube.

**Rejected for reliability:** Imaging FPAs (fragile), radar seekers (complex RF chain), dual-mode guidance (twice the failure paths).

### Recommendation

**Launcher IR tracker + rugged quad-cell IR seeker on round (LOBL) + mandatory pre-fire BIT.**

Radar and imaging seekers **deprioritized** unless reliability case approved in Phase 2 review.

---

## 5. Kinetic Rod vs. Flechette Pack vs. HE

### Recommendation

**Unitary kinetic rod baseline.** Flechette variant reserved for Phase 2 if swarm MOE is mandated.

---

## 6. Rifling vs. Fin-Only Stabilization

### Recommendation

**Rifled barrel + spring-loaded locking deployable fins.**

---

## 7. Single Operator vs. Two-Man Team

### Options

| Configuration | Pros | Cons |
|---------------|------|------|
| **Gunner + ammo bearer ★** | **Sustained fire; security** | **2 personnel** |
| Solo gunner (3 rounds on launcher pouch) | Fewer personnel | Slow reload; no security |

### Recommendation

**Two-man team:** gunner + ammo bearer. No separate designator required with integrated launcher tracker.

---

## Trade Decision Summary

| Trade | Baseline Selection | Status |
|-------|-------------------|--------|
| **Design priority** | **Reliability first** | Set |
| Caliber | 50 mm | Set |
| Backblast | Hybrid mitigation | Open (Phase 1 test) |
| Launcher | Reusable breech + IR tracker + BIT | Set |
| Guidance | Launcher IR + quad-cell round IR (LOBL) | Set |
| Pre-fire BIT | Mandatory | Set |
| Propulsion | Moderate velocity (~650 m/s) | Set |
| Payload | Unitary rod | Set |
| Stabilization | Rifling + dual-spring deployable fins | Set |
| Team | Gunner + ammo bearer | Set |
| Radar / imaging seeker | **Rejected baseline** | Deprioritized |
| Flechette variant | **Rejected baseline** | SKU complexity |

---

## Related Documents

| Document | Purpose |
|----------|---------|
| [Annex C — Trades Matrix](../annexes/C-trades-matrix.md) | Full matrix |
| [06 — System Description](06-system-description.md) | Integrated system view |

---

[← CONOPS / Use Cases](04-conops-use-cases.md) | [Next: System Description →](06-system-description.md)
