# 05 — Key Design Trades

**Document ID:** RADR / DOC-05  
**Version:** 1.6.0  
**Status:** Conceptual

---

## Locked Trades

| Trade | Selection | Rationale |
|-------|-----------|-----------|
| Echelon | **Squad / SOF terminal layer** | Not divisional air defense |
| Threat focus | **Group 1–2 UAS** (see DOC-02) | FPV, quads, loiter, glide, swarm |
| Primary virtue | **Speed-to-target** | Beats evasion timeline |
| Guidance | **Moderate-maneuver nose canards** | Pairs with rough aim + IR lock; not high OBA |
| Off-boresight | **Rejected** | Complexity vs. mission |
| Warhead | **Dense alloy cubes + pyrotechnic dispersal** | Forward cone at ~20 ft |
| Fuze | **Radar or mm-wave proximity + timed backup** | Standoff kill at ~20 ft without impact fuze |
| Motor | **Evolution Space propellant; mildly progressive grain** | **2950–3050 N·s**, low initial thrust, **330–350 m/s** @ 1000 m |
| Caliber | **60 mm** | Payload + motor + seeker balance |
| Launcher | **40 in M1 Bazooka layout + Gustav breech** | Familiar silhouette; reload; 10 yd backblast |
| Round | **Ravioli-can style tube + pull cap** | Rugged field handling |
| Fins | **Spring deploy + mechanical lock** | Stable boost phase |
| Controls | **Dual-trigger + tone** | Safe seeker/arm sequence |
| Carry safety | **Rocket retention stop** | Mechanical anti-slide when slung; releases only when armed |

---

## Speed vs. Agility

RADR deliberately **does not** pursue high off-boresight or aggressive intercept maneuvers. Closure speed and a reliable terminal cone are the kill chain.

---

## Motor: Mildly Progressive Burn (Locked)

| Phase | Thrust (locked band) | Purpose |
|-------|----------------------|---------|
| 0–2.0 s | **750–850 N** | Recoil and 10 yd backblast control |
| 2.0–3.0 s | Ramp to **1050–1150 N** peak | Range closure |
| ~3.3 s total | Burnout tail | End of motor impulse |

| Parameter | Value |
|-----------|--------|
| Total impulse | **2950–3050 N·s** (~3000 nominal) |
| Burn time | **~3.3 s** |
| Est. velocity @ 1000 m | **330–350 m/s** |

See [Annex H](../annexes/H-motor-progressive-burn.md).

---

## Threat-Driven Design Choices

| Threat | Design response |
|--------|-----------------|
| FPV kamikaze | Fast motor ramp; short time-to-intercept |
| Quadcopters | IR lock on hover/orbit; forward cone at ~20 ft |
| Loitering munitions | 1000 m envelope; single-shot F&F |
| Glide / low signature | Passive IR seeker; speed over snap-shot OBA |
| Swarm leakthrough | Quick tube-out reload; 2-man sustainment |

---

## Removed from Program

| Concept | Status |
|---------|--------|
| Laser beam-riding | Removed |
| Launcher-tracked guidance | Removed |
| Kinetic penetrator rod | Removed |
| High off-boresight autopilot | Rejected |
| FMCW radar seeker | Not baseline |

---

[← CONOPS](04-conops-use-cases.md) | [Next: System Description →](06-system-description.md)
