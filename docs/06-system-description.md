# 06 — System Description

**Document ID:** RADR / DOC-06  
**Version:** 1.7.0  
**Status:** Conceptual

Engineering detail: [Annex F](../annexes/F-employment-and-breech.md) · [Annex G](../annexes/G-mass-and-center-of-gravity.md) · [Annex H](../annexes/H-motor-progressive-burn.md) · [Annex I](../annexes/I-performance-modeling.md) · [Annex J](../annexes/J-warhead-dispersal.md)

---

## System Overview

**RADR** comprises:

1. **Launcher** — 40 in reusable recoilless tube (≤ 5.5 kg empty), modernized M1 Bazooka ergonomics, Gustav flip breech, dual-trigger grips, **rocket retention stop**, no shoulder stock, slightly rear-biased CoG.  
2. **Rocket** — 60 mm × 18 in round (≤ 3.5 kg) in **ravioli-can style protective tube**: IR seeker, **moderate-maneuver** canards, mildly progressive motor, **pyrotechnic-dispersed** dense alloy cube flak warhead.

```mermaid
flowchart LR
  subgraph L [Launcher]
    B[GustavBreech_Lock]
    T[DualTrigger_Tone]
    R[RetentionStop]
  end
  subgraph R [Rocket]
    S[IRSeeker_100mm]
    C[NoseCanards]
    M[ProgressiveMotor]
    W[CubeCone_300x7mm]
    F[SpringFins_x4]
  end
  G[Gunner] --> L
  L --> R
  R --> UAS[PrimaryThreats_UAS]
```

---

## Diagrams

Mechanical and employment detail: [Annex F — Breech](../annexes/F-employment-and-breech.md#breech-mechanism) · [Retention stop](../annexes/F-employment-and-breech.md#rocket-retention-stop) · [Gunner sequence](../annexes/F-employment-and-breech.md#loading-and-firing--gunners-sequence)

### Physical Assembly (Conceptual)

At **LOCKED_SEATED**, the protective tube is fully inside the 60 mm smoothbore; the flip breech block is deadbolt-locked against the tube rim; the retention stop finger bears on the tube aft shoulder until the gunner arms the seeker and receives lock tone. Exhaust vents rearward through the recoilless path (10 yd danger zone).

```mermaid
flowchart TB
  subgraph Launcher [Launcher_40in]
    Bore[Smoothbore_60mm]
    BreechBlock[FlipBreech_Closed]
    Vent[RecoillessVent_Rear]
  end
  subgraph Tube [RavioliCan_Tube]
    CapOff[CapRemoved]
    subgraph Rocket [Rocket_18in]
      Seeker[Seeker_100mm]
      WH[Warhead_Cubes]
      Motor[Motor_297mm]
      Fins[SpringFins_Lock]
    end
  end
  BreechBlock --> Bore
  Bore --> Tube
  Rocket --> Bore
  Vent --> VentNote[10yd_DangerZone]
```

- **Ravioli-can style protective tube** is the factory shipping and launch container (soldier removes pull-off cap before load).  
- **Rocket** rides inside the tube; tube rim mates **breech sealing face** and **rim contacts**.  
- On fire, motor exhaust vents **rear** through launcher — not a closed-bore cannon.

### Employment Sequence (States)

Time-ordered interaction between gunner, breech, retention stop, seeker, and fire logic. The retention stop stays engaged until lock tone; the rear trigger is inert until then. Full step-by-step narrative: [Annex F § Gunner’s Sequence](../annexes/F-employment-and-breech.md#loading-and-firing--gunners-sequence).

```mermaid
sequenceDiagram
  participant G as Gunner
  participant B as Breech
  participant RS as RetentionStop
  participant S as Seeker
  participant FL as FireLogic

  G->>B: Open breech CLEAR
  RS->>RS: Engaged
  G->>G: Pop cap PREP
  G->>B: Load tube LOAD
  B->>FL: Close deadbolt SEAT
  RS->>RS: Engaged
  G->>S: Front trigger ARM
  S->>G: Lock tone
  S->>RS: Disengage
  G->>FL: Rear trigger FIRE
  G->>B: Open breech POST
  B-->>G: Empty tube drops
  RS->>RS: Engaged
```

### Safety Interlock Flow

Logical gates for carry-safe operation. All three conditions (closed locked breech, front held, lock tone) are required before the retention stop retracts and the rear trigger enables. Diagram matches [Annex F § Safety Interlock Flow](../annexes/F-employment-and-breech.md#safety-interlock-flow).

```mermaid
flowchart TD
  Start[BreechOpen_or_Unseated] --> Engaged[RetentionStop_Engaged]
  Engaged --> Closed{BreechClosed_and_DeadboltLocked}
  Closed -->|No| Engaged
  Closed -->|Yes| Seated{TubeSeated_OK}
  Seated -->|No| Engaged
  Seated -->|Yes| Front{FrontTriggerHeld}
  Front -->|No| Engaged
  Front -->|Yes| Tone{LockToneActive}
  Tone -->|No| Engaged
  Tone -->|Yes| Ready[Stop_Disengaged_RearEnabled]
  Ready --> Fire[RearTrigger_Launch]
  FrontRelease[FrontReleased] --> Engaged
```

### Post-Fire Tube Ejection

After motor burnout and safe interval, the gunner clears the rear arc, unlocks the breech, and the spent protective tube drops for the next reload cycle.

```mermaid
flowchart LR
  Fired[MotorBurns_RocketLeaves] --> Vent[Backblast_10yd]
  Vent --> Open[GunnerOpensBreech]
  Open --> Drop[SpentTube_DropsOut]
  Drop --> Reload[Next_RavioliCan]
```

---

## Primary Threats (Design Basis)

| Category | Representative behavior |
|----------|------------------------|
| FPV kamikaze | High closure, terminal dive |
| Small–medium quadcopters | Hover, orbit, light attack |
| Loitering munitions | Commit from standoff |
| GPS-denied / terrain-matching gliders | Low signature glide |
| Group 1–2 swarm / interdiction | Brief exposure, multiple tracks |

---

## Launcher

![RADR launcher concept — locked silhouette](../visuals/launcher/output/radr-bazooka-goodmk60.png)

| Parameter | Spec |
|-----------|------|
| Length | 40 in (1016 mm) |
| Mass (empty) | ≤ 5.5 kg (nominal **4.95 kg** — [Annex G](../annexes/G-mass-and-center-of-gravity.md)) |
| Bore | 60 mm smoothbore (baseline) |
| Layout | Modernized **M1 Bazooka** — long slim tube; **no shoulder stock** |
| Grips | Forward vertical foregrip (between muzzle and sight) with **pistol-style seeker trigger**; rear pistol grip with fire trigger |
| Padding | Rear section only (pistol grip → breech) |
| Sight | Integrated holo **1.5×–4×** + fold-out **~4 in** viewer |
| Zoom control | **+ / −** on **aft face** of foregrip (buttons face rear) |
| Launcher power | Grip battery — holo, display, fire-control |
| Finish | Matte tactical camo (non-reflective) |
| Round | Ravioli-can style tube; soldier removes **manual pull-off cap** before load |
| Seating | Pressure sensor + electrical contacts |
| Triggers | **Front:** same curved pistol trigger as rear, **slightly smaller** — seeker + **audible lock tone** · **Rear:** fire (front held) |
| **Retention stop** | Mechanical bore stop — see below |
| CoG | Slightly **rear-biased** (~248 mm rocket CG — Annex G) |
| Backblast | ≤ **10 yards (30 ft)** rear |
| Tracker | None |

### Forward device — muzzle brake / blast deflector

The fitting at the **muzzle** (M1 Bazooka–heritage silhouette) is a **combined muzzle brake and blast deflector**, not a decorative cap.

| Function | Description |
|----------|-------------|
| **Recoilless vent management** | A fraction of launch gas exits **rearward** through the breech vent path; the forward device captures and redirects **residual forward blast** away from the gunner’s support hand |
| **Impulse reduction** | Baffle surfaces reduce **peak overpressure** at the muzzle plane during firing |
| **Hand clearance** | Deflector geometry keeps the **forward foregrip** outside the primary blast cone |
| **Mass** | **~0.20 kg** (budgeted within main tube forward section — [Annex G](../annexes/G-mass-and-center-of-gravity.md)) |

Visual intent: [visuals/README.md](../visuals/README.md). Concept art (Goodmk60) — forward hardware to be read as this device in future renders.

### Rocket Retention Stop

A **spring-biased radial bore finger** in the lower bore wall bears on the protective tube **aft shoulder** and blocks **forward slide** toward the muzzle during sling carry. The breech sealing face holds the tube rearward; the finger is the anti-creep element. The stop **disengages** only when: breech **deadbolt-locked**, gunner holds **front trigger**, and seeker outputs **steady lock tone** — then a **release cam** retracts the finger **~2–4 mm** flush to the bore. Releasing the front trigger **re-engages** immediately. The **rear trigger never** drives the stop.

| State | Retention stop |
|-------|----------------|
| Breech open / not seated | **Engaged** |
| Breech closed, front trigger not held | **Engaged** |
| Breech closed, front held, no ready tone | **Engaged** |
| Breech closed, front held, **ready tone** | **Disengaged** |
| Front trigger released | **Re-engages** immediately |

Full mechanism and causality table: [Annex F § Rocket Retention Stop](../annexes/F-employment-and-breech.md#rocket-retention-stop).

### Breech (Summary)

**Gustav-style flip block** on a rear hinge (~90° open). Pull the **spring-return bolt handle** **15–25 mm** aft — **unlock cam** lifts the **deadbolt**; swing open on detent; insert tube; close; **release** handle so the return spring drives the deadbolt into the receiver notch with an audible **snap**. That snap is the positive lock (bolt-action feel). `SEATED` confirm via pressure + rim contacts gates seeker and retention logic.

Full mechanical detail (bolt kinematics, lock elements, user feel): [Annex F § Breech Mechanism](../annexes/F-employment-and-breech.md#breech-mechanism).

### Integrated Sight, Fold-Out Viewer, and Controls

| Element | Baseline |
|---------|----------|
| **Optics module** | Low-profile **variable holo/optics pod** (**1.5×–4×**) **integrated** on the tube — not a rail-mounted aftermarket sight |
| **Fold-out viewer** | **~4 in (102 mm) wide** panel on a side hinge; **stowed:** folds **flush** against the tube — **bottom edge aligned with bottom of holo pod** (no step, no overhang) |
| **Display** | Panel shows the holo/optics picture + reticle when **deployed** (~barrel-height swing out) |
| **Zoom** | **+** and **−** on the **aft-facing (rear) face** of the forward foregrip — buttons face rear; right-handed gunner uses **left index** on front trigger, **left thumb** on zoom — steps through **1.5× → 4×** (default **1.5×** on power-up) |
| **Battery** | Rechargeable cell in the **pistol grip** powers holo, display, zoom logic, triggers, and tone |
| **Round seeker** | **100 mm IR F&F** on the rocket; powered via **rim contacts** when seated — **seeker lock** at endgame, not the launcher camera |

#### Stowed vs. deployed

| State | Configuration |
|-------|----------------|
| **Carry / sling** | Viewer **folded flush** — panel face against tube; **lower edge coplanar with holo housing lower edge** |
| **Engage** | Flip viewer out on hinge; bottom was flush with holo baseline — panel swings out to viewing angle |
| **Fire** | Hold front trigger for seeker tone while keeping threat in view on panel; rear trigger when tone steady |

#### Why fold-out + foregrip zoom (not 40×, not rail scope)

- **4 in panel** gives a **stable view** at arm’s length — easier than squinting through a tiny optic at 1000 m.  
- **1.5×–4×** stays inside **rough-aim + seeker FOV** discipline (~2–4° notional seeker cone).  
- **Foregrip + / −** on the **aft face** keeps zoom on the **support-hand thumb** while the **index finger** stays on the seeker trigger — no grip shift on the firing hand.  
- **Not** the rocket IR feed on the screen pre-lock — launcher optics only. **Lock tone** = round seeker; avoids wiring/video from disposable round.

#### Human eye vs. mag (unchanged rationale)

At **1000 m**, a **~0.4 m** drone is ~**1.4 arcmin** at 1× — edge of vision. **4×** on the panel ≈ **5.5 arcmin** — enough to **center the reticle** before seeker search. Rotor detail still comes from **IR seeker**, not the holo.

**KISS boundary:** No 40× optical stack; no seeker video on launcher display until a future variant. Panel + holo + grip battery stay one integrated launcher subsystem.

---

## Rocket

| Parameter | Spec |
|-----------|------|
| Caliber / length | 60 mm × 18 in (457 mm) max |
| Mass | ≤ 3.5 kg (nominal **3.1 kg** — Annex G) |
| Seeker | 100 mm IR fire-and-forget |
| Canards | Small movable surfaces **near nose**; **moderate-maneuver** trim |
| Fins | 4 swept **spring-loaded** at **base**; deploy on exit; **mechanical lock** once deployed |
| Motor | Solid rocket; **Evolution Space** propellant; **mildly progressive** grain — [Annex H](../annexes/H-motor-progressive-burn.md) |
| Warhead | 300 × 7 mm **dense alloy** rough-edged cubes |
| Dispersal | **Pyrotechnic dispersal charge** — forward-biased cone **~10–12 ft** wide @ **~20 ft** |
| Fuze | **Radar or millimeter-wave proximity** (primary) + **timed backup** |

### Mass (Summary)

| Component | kg (nominal) |
|-----------|--------------|
| Seeker + avionics | 0.65 |
| Warhead | 1.05 |
| Motor + propellant | 1.20 |
| Structure, fins, canards | 0.20 |
| **Total** | **3.10** |

Component-level mass budget, axial distribution, and CG sensitivity: [Annex G](../annexes/G-mass-and-center-of-gravity.md).

---

## Motor (Summary — 1000 m Goal)

| Parameter | Locked baseline |
|-----------|-----------------|
| Total impulse | **2950–3050 N·s** (~3000 nominal) |
| Burn time | **~3.3 s** |
| Grain | **Mildly progressive** — lower thrust first **1–2 s**, then ramp |
| Initial thrust | **750–850 N** |
| Peak thrust | **1050–1150 N** |
| Est. velocity @ 1000 m | **330–350 m/s** |

| Time (s) | Thrust (N, notional) | Phase |
|----------|----------------------|--------|
| 0–2.0 | 780–820 avg | Low — recoil/backblast |
| 2.0–3.0 | 870 → 1120 ramp | Mildly progressive |
| 3.0–3.3 | ~1050 tail | Burnout |

Full table and rationale: [Annex H](../annexes/H-motor-progressive-burn.md). Performance model: [Annex I](../annexes/I-performance-modeling.md).

---

## Fuze and Kill Chain

**Primary (locked):** **Radar or millimeter-wave proximity** sensor at **~20 ft** standoff — engineering selects one baseline path (radar proximity or mm-wave proximity), not both on one round. Detects the target envelope and initiates the burster without requiring direct impact.

**Backup:** **Timed fuze** if the proximity channel fails — preserves forward-cone geometry.

**Why this choice:** Group 1–2 UAS present small radar/RF and physical cross-sections at **engagement range**; proximity at standoff matches the **forward kill cone** flak pattern and **KISS** fire-and-forget employment (no impact fuze, no command link).

1. Proximity (radar or mm-wave) initiates at **~20 ft** (primary).  
2. Timed backup if proximity does not fire.  
3. Burster opens cube pack into **forward cone** (~10–12 ft wide).  
4. Cubes strike rotors, battery, sensors, and airframe.

Detail: [Annex H — Motor](../annexes/H-motor-progressive-burn.md) · [Annex I — Performance](../annexes/I-performance-modeling.md) · [Annex J — Warhead](../annexes/J-warhead-dispersal.md) · [Annex F — Employment](../annexes/F-employment-and-breech.md)

---

## Operational Flow (Summary)

| Step | Action |
|------|--------|
| 1 | Open breech |
| 2 | Pop cap off tube |
| 3 | Load tube |
| 4 | Close breech — deadbolt locks, **SEATED** |
| 5 | Hold front trigger → **lock tone** (retention stop **releases**) |
| 6 | Pull rear trigger (front held) → fire |
| 7 | Open breech → empty tube drops out |

**Authoritative detail** (interlocks, abort rules, timing): [Annex F](../annexes/F-employment-and-breech.md).

---

## Employment

**Team:** Gunner + ammo bearer. **Single carry:** ≤ 9.0 kg (nominal **8.05 kg** loaded — Annex G).

---

[← Key Design Trades](05-key-design-trades.md) | [Next: Limitations →](07-limitations-and-risks.md)
