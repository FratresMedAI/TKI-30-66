# Annex D — Projectile Stabilization

**Document ID:** TKI-30-66 / ANX-D  
**Version:** 0.3.0  
**Status:** Conceptual — engineering notional

System context: [06 — System Description](../docs/06-system-description.md)

---

## Design Overview

The baseline combines rifled-barrel initial spin with spring-loaded, locking deployable fins. This provides stable flight for the guided terminal phase after LOBL launch.

Guidance corrections from the mini IR seeker act on deployable fins via the autopilot. Corrections should not demand high authority before fin lock (~15–30 m downrange).

---

## Rifled Barrel

| Parameter | Value | Notes |
|-----------|-------|-------|
| Caliber | 50 mm | Nominal bore |
| Barrel length | ~350–450 mm | ~7–9 calibers |
| Twist rate | 1:120 mm (notional) | Subject to stability analysis |
| Spin rate at muzzle | ~800–1200 RPM | Depends on muzzle velocity |

---

## Deployable Fin Assembly

| Parameter | Value |
|-----------|-------|
| Fin count | 4 (baseline) |
| Deployment style | Umbrella / pop-out with mechanical lock |
| Spring redundancy | **Dual springs per fin** |
| Fin span (deployed) | ~80–100 mm |
| Deployment distance | 15–30 m downrange |
| Control authority | Fin deflection for terminal homing post-lock |

### Deployment Sequence

1. Launch impulse; sabot discard 5–15 m
2. Setback triggers fin deployment 10–20 m
3. Mechanical lock engages 15–30 m
4. Seeker homing corrections authorized ≥ 30 m

---

## Interaction with IR Seeker

The mini IR seeker in the round nose must maintain track through fin deployment shock. Seeker window protection and soft-mount isolation are design requirements.

Roll rate from rifling decays after fin deploy; seeker roll compensation in autopilot firmware may be required for quad-cell seekers.

---

## Failure Modes

| Failure | Effect | Mitigation |
|---------|--------|------------|
| Fin fails to deploy | Yaw divergence; miss | Dual springs per fin; 100% production check |
| One fin hangs up | Spiral trajectory | Tolerance control |
| Seeker shock damage | Loss of track | Isolation mount; window protection |

---

## Test Plan (Proposed)

| Test | Purpose | Phase |
|------|---------|-------|
| Fin deployment bench | Lock and timing | Phase 1 |
| Seeker live-fire shock | Track through launch | Phase 2 |
| Guided flight vs. UAS target | End-to-end Pk | Phase 3 |

---

## Related Documents

- [06 — System Description](../docs/06-system-description.md)
- [Annex C — Trades Matrix](C-trades-matrix.md)
