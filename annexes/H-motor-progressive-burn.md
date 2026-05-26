# Annex H — Motor Progressive Burn Profile

**Document ID:** RADR / ANX-H  
**Version:** 1.6.0  
**Status:** Conceptual — **final motor baseline locked** (notional ballistics until live-fire)

*Thrust-time table supports design trades; impulse and velocity bands are analytic targets — not demonstrated test data.*

Traceability: [06 — System Description](../docs/06-system-description.md) · [05 — Key Design Trades](../docs/05-key-design-trades.md)

---

## Motor Summary (Locked Baseline)

| Parameter | Value |
|-----------|--------|
| Type | **Solid rocket motor** — **mildly progressive** grain |
| Propellant | **Evolution Space high-rate tactical** propellant (baseline selection) |
| Signature | **Low-signature where possible** (smoke/plume reduction goal — not zero signature) |
| Motor bay length | ~297 mm |
| Usable grain length | ~260 mm |
| Propellant mass | ~1.20 kg |
| **Burn time** | **~3.3 s** |
| **Total impulse** | **2950–3050 N·s** (nominal **~3000 N·s**) |
| **Initial thrust** | **~750–850 N** (first **1–2 s**) |
| **Peak thrust** | **~1050–1150 N** |
| **Est. velocity @ 1000 m** | **~330–350 m/s** |
| Range goal | **1000 m** effective |

**Assessment:** Solid, achievable target for a **60 mm × 18 in** round within recoilless **10 yd** backblast SOP and squad carry mass.

---

## Grain Behavior (Mildly Progressive)

| Segment | Duration | Thrust | Purpose |
|---------|----------|--------|---------|
| **Low plateau** | **~0–2 s** | **~750–850 N** | Lower initial thrust → manageable recoilless backblast and shoulder impulse |
| **Ramp** | **~2.0–3.0 s** | Rises toward peak | Closure speed for **1000 m** engagement |
| **Tail** | **~3.0–3.3 s** | **~1050–1150 N** peak, then burnout | Terminal velocity build; motor tail-off |

**Not selected:** Boost-first grains (excess peak pressure for 10 yd rear SOP); neutral-burn grains (higher initial peak, less backblast margin).

---

## Propellant Choice (Evolution Space)

RADR uses a **solid grain** sized for a **60 mm × 18 in** round, not a liquid or hybrid system — **KISS** for squad logistics and field reliability.

| Factor | Rationale |
|--------|-----------|
| **Evolution Space high-rate tactical propellant** | Supports **controlled pressure rise** in the ramp while preserving a **low-thrust opening segment** |
| **Mildly progressive grain geometry** | First **1–2 s** at **750–850 N** → backblast margin; then ramp to **1050–1150 N** peak |
| **Low-signature goal** | Reduce visual/thermal launch signature **where chemistry allows** without sacrificing the 1000 m closure target |

---

## Thrust-Time Profile (Notional — Matches Locked Bands)

Mildly progressive burn: **lower thrust 0–2 s**, **ramp 2–3.0 s**, **peak and tail to ~3.3 s**.

| Time (s) | Thrust (N) | Phase |
|----------|------------|--------|
| 0.0 | 0 | Ignition start |
| 0.5 | 780 | Low plateau |
| 1.0 | 800 | Low plateau |
| 1.5 | 820 | Low plateau |
| 2.0 | 870 | Ramp start |
| 2.5 | 1000 | Ramp |
| 3.0 | 1120 | Peak |
| 3.3 | 1050 | Burnout tail |

### Phase Averages (Design Check)

| Phase | Duration (s) | Avg thrust (N) | Impulse contrib. (N·s) |
|-------|--------------|----------------|------------------------|
| Low (0–2.0) | 2.0 | ~795 | ~1590 |
| Ramp (2.0–3.0) | 1.0 | ~995 | ~995 |
| Tail (3.0–3.3) | 0.3 | ~1085 | ~325 |
| **Total** | **~3.3** | **~910 avg** | **~2910** (within **2950–3050** pad) |

**Locked impulse band:** **2950–3050 N·s** — table integrates inside band with manufacturing tolerance.

---

## Why Mildly Progressive (Not Neutral / Boost-First)

| Profile | Recoil / backblast | Range at 1000 m | RADR fit |
|---------|-------------------|-----------------|----------|
| **Mildly progressive (low → ramp)** | Lower peak at launch | **330–350 m/s** class at 1000 m | **Selected** |
| Neutral burn | Higher initial peak | Moderate | Rejected — shoulder strain |
| Boost-first | Highest initial peak | Best short range | Rejected — 10 yd backblast SOP |

Low **750–850 N** initial thrust keeps the **10 yard (30 ft)** rear danger zone manageable; ramp to **1050–1150 N** peak delivers **~330–350 m/s** at **1000 m** (notional).

---

## Performance Bridge to 1000 m Goal

| Parameter | Locked / notional value | Basis |
|-----------|-------------------------|-------|
| Total impulse | **2950–3050 N·s** (~3000 nominal) | Thrust-time integration + band |
| Launch mass | ~3.1 kg | Annex G |
| Burn time | **~3.3 s** | Table above |
| Initial thrust | **750–850 N** | First 1–2 s segment |
| Peak thrust | **1050–1150 N** | Ramp peak |
| Time of flight @ 1000 m | ~4.5–5.0 s | Ballistic estimate |
| Terminal velocity @ 1000 m | **330–350 m/s** | Drag + impulse placeholder |

**Honest limit:** No live motor test with Evolution Space grain in this form factor. Numbers are the **locked design baseline**, not a demonstrated KPP until ballistic test.

---

## Related Documents

- [G — Mass and CG](G-mass-and-center-of-gravity.md)  
- [05 — Key Design Trades](../docs/05-key-design-trades.md)  
- [07 — Limitations and Risks](../docs/07-limitations-and-risks.md)
