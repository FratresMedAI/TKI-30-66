# Annex J — Warhead and Pyrotechnic Dispersal

**Document ID:** RADR / ANX-J  
**Version:** 1.7.0  
**Status:** Conceptual — high-level mechanism only (no energetics or live-fire data)

Traceability: [06 — System Description](../docs/06-system-description.md) · [03 — Design Constraints](../docs/03-design-constraints.md)

---

## Warhead Summary (Locked)

| Element | Spec |
|---------|------|
| Kill mechanism | **300 × 7 mm** dense alloy **rough-edged** cubes |
| Dispersal | **Pyrotechnic dispersal charge** (burster) — **not** a shaped charge penetrator |
| Pattern | **Forward-biased cone**, **~10–12 ft** wide at **~20 ft** standoff |
| Fuze | **Radar or mm-wave proximity** (primary) + **timed backup** |
| Role of burster | **Disperser only** — opens pack and biases cube velocity forward |

---

## Round Layout (Aft → Forward)

```mermaid
flowchart LR
  Motor[Motor_Aft] --> Body[BodyTube]
  Body --> Pack[CubePack_300x7mm]
  Pack --> Burster[PyrotechnicDispersalCharge]
  Burster --> Bulkhead[ForwardBulkhead]
  Bulkhead --> Seeker[IRSeeker_100mm]
```

| Zone | Contents |
|------|----------|
| **Aft** | Motor, nozzle, fin roots |
| **Mid** | Cube pack in lightweight containment (fragmentation matrix) |
| **Forward of pack** | **Pyrotechnic dispersal charge** in annular / puck geometry |
| **Nose** | Seeker dome + fuze electronics forward of burster cavity |

The cube pack sits **aft of the burster** so gas pressure drives fragments **forward** through the open nose path and body liner, not back into the motor.

---

## Pyrotechnic Dispersal (Conceptual)

### Charge placement

- **Location:** Immediately **forward of the cube pack**, **aft of the seeker interface bulkhead**.  
- **Form:** Low-metal or inert-augmented **dispersal puck** (not HEAT liner).  
- **Initiation:** Fuze fires detonator → burster deflagrates/brisks rapidly (~milliseconds).  

### Forward-biased cone mechanism

| Mechanism | Effect |
|-----------|--------|
| **Forward cavity / petal liner** | Directs primary gas and cube impulse **toward the nose** |
| **Partial confinement** | Body wall contains lateral expansion; **nose aperture** is the preferential exit |
| **Pack stacking** | Cubes loaded in columns biased slightly forward — natural ejection bias |
| **Standoff ~20 ft** | Proximity fuze triggers before impact — cone has room to open |

**Resulting pattern (notional):** Full cone half-angle ~**15–25°** at **~20 ft**, footprint **~10–12 ft** diameter — wide enough for Group 1–2 UAS but not a spherical omnidirectional frag field.

### What the burster does *not* do

- Does **not** penetrate armor or structure (no rod).  
- Does **not** replace cube kinetic energy — cubes carry terminal kill.  
- Does **not** rely on blast overpressure alone against hardened targets.

---

## Fuze Chain

```mermaid
sequenceDiagram
  participant S as SeekerGuidance
  participant F as Fuze
  participant B as Burster
  participant C as CubePack

  S->>F: Close on target
  F->>F: Proximity at ~20ft
  alt Proximity fail
    F->>F: Timed backup
  end
  F->>B: Fire burster
  B->>C: Dispersal impulse
  C->>C: Forward cone flight
```

| Step | Event |
|------|--------|
| 1 | IR seeker delivers impact point; fuze arms on launch |
| 2 | **Radar or mm-wave proximity** senses target envelope at **~20 ft (6 m)** |
| 3 | Burster initiates; cubes exit forward |
| 4 | If proximity fails, **timed backup** fires at predicted intercept time |

---

## KISS Boundaries

- One primary proximity path per round (radar **or** mm-wave — engineering down-select).  
- No command link, no midcourse retarget of burster.  
- No launcher video of cube pattern — gunner uses holo + tone only pre-launch.

---

## Related Documents

- [06 — Fuze and Kill Chain](../docs/06-system-description.md#fuze-and-kill-chain)  
- [G — Mass/CG](G-mass-and-center-of-gravity.md) (warhead mass split)
