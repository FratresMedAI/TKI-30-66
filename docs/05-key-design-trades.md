# 05 — Key Design Trades

**Document ID:** RADR / DOC-05  
**Version:** 0.8.0  
**Status:** Conceptual

---

## Locked Trades

| Trade | Selection | Rationale |
|-------|-----------|-----------|
| Echelon | **Squad / SOF terminal layer** | Not divisional air defense |
| Threat focus | **Group 1–2 UAS** (see DOC-02) | FPV, quads, loiter, glide, swarm |
| Primary virtue | **Speed-to-target** | Beats evasion timeline |
| Guidance | **Low-maneuver nose canards** | Pairs with rough aim + IR lock |
| Off-boresight | **Rejected** | Complexity vs. mission |
| Warhead | **Dense alloy cube forward cone** | Fragile UAS structures |
| Fuze | **Proximity + timed backup** | Reliable ~20 ft actuation |
| Motor | **Progressive burn** | Recoil/backblast then range |
| Caliber | **60 mm** | Payload + motor + seeker balance |
| Launcher | **36 in reusable Gustav breech** | Reload + 10 yd backblast clearance |
| Round | **Ravioli-can + pull cap** | Rugged field handling |
| Controls | **Dual-trigger + tone** | Safe seeker/arm sequence |

---

## Speed vs. Agility

RADR deliberately **does not** pursue high off-boresight or aggressive intercept maneuvers. Closure speed and a reliable terminal cone are the kill chain.

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
