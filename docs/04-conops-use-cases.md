# 04 — CONOPS / Use Cases

**Document ID:** TKI-30-66 / DOC-04  
**Version:** 0.2.0  
**Status:** Conceptual

---

## Overview

Six representative concepts of operation for TKI-30-66 employment by squad and SOF elements.

Baseline team: **2 personnel** — Gunner (launcher with integrated IR tracker) + Ammo Bearer (spare rounds, local security).

**No separate laser designator operator.**

---

## Use Case 1: Hasty Ambush Response

### Situation

A dismounted patrol is establishing or executing a hasty ambush when an enemy ISR quadcopter appears at low altitude (~100–200 m).

### Threat

Group 1 UAS, hovering or slow orbit, daylight or night (thermal signature from motors).

### Team Setup

- Gunner: launcher loaded, IR tracker active
- Ammo bearer: 2 spare rounds, provides rear/side security
- Backblast arc cleared behind gunner

### Engagement Sequence

1. Visual/acoustic detection; ROE confirm hostile
2. Gunner acquires UAS in launcher IR tracker
3. System confirms LOBL; gunner fires
4. Round homing autonomous; BDA visual
5. Reload if follow-on UAS

### Success Criteria

- UAS neutralized within ~30–60 s of detection
- ≤ 2 rounds expended

### Limitations

- Cold or low-thermal UAS may delay or prevent IR lock
- Multiple simultaneous UAS exceed single-team capacity

---

## Use Case 2: Static Position / LP-OP Defense

### Situation

A squad occupies an LP/OP for 2–6 hours. Enemy FPV or ISR drones probe the position.

### Threat

Group 1–2 UAS, loitering at 150–400 m.

### Team Setup

- Launcher pre-positioned with cleared rear arc
- Gunner rotates through LP scan; ammo bearer maintains security
- 4 rounds staged

### Engagement Sequence

1. Acoustic or visual cue
2. Gunner acquires in IR tracker when UAS enters envelope
3. LOBL confirm; fire
4. On miss, re-acquire and reload via flip breech

### Success Criteria

- OP not confirmed by enemy ISR over multi-hour period

### Limitations

- Gunner occupied during acquisition and lock; not scanning other sectors
- Loitering munitions in terminal dive reduce engagement window

---

## Use Case 3: Convoy Escort (Dismount Team)

### Situation

Convoy halted; dismount team provides security. Chase drone approaches at low altitude.

### Threat

Group 1 FPV, 30–60 km/h, 100–300 m range.

### Team Setup

- TKI element dismounts with launcher and 2 rounds
- Backblast oriented away from convoy

### Engagement Sequence

1. Visual acquire
2. Gunner tracks in IR sight; LOBL on crossing target
3. Fire; immediate remount after BDA

### Success Criteria

- UAS defeated before FPV attack range
- Dismount time ≤ 60 s

### Limitations

- Crossing geometry reduces Pk vs. hover
- Backblast must not endanger convoy

---

## Use Case 4: SOF Raid Exfiltration

### Situation

SOF element on foot exfil; enemy ISR drone detects movement.

### Threat

Group 1–2 UAS, 150–500 m.

### Team Setup

- TKI organic to team (launcher + 3 rounds)
- IR tracker provides low EM signature vs. active jamming

### Engagement Sequence

1. Halt at covered position
2. Gunner acquires UAS thermal signature in IR tracker
3. LOBL; fire from defilade
4. Resume exfil

### Success Criteria

- UAS defeated; exfil delay ≤ 2 min
- No large EW signature from team

### Limitations

- Night IR lock depends on UAS thermal contrast
- Exfil may already be compromised by prior detection

---

## Use Case 5: Forward Assembly Area Point Defense

### Situation

Company FAA; battalion SHORAD elsewhere. Platoon-level organic UAS defense required.

### Threat

Intermittent Group 1–2 UAS, 200–600 m.

### Team Setup

- One TKI team per platoon sector
- 4–6 rounds per team

### Engagement Sequence

1. External cue or visual acquire
2. Gunner IR lock and fire
3. Report to platoon HQ

### Success Criteria

- FAA operations continue without UAS-triggered indirect fire

### Limitations

- Not a substitute for dedicated FAA air defense plan

---

## Use Case 6: Urban Fringe / Compound Perimeter

### Situation

Squad defends compound; commercial drones conduct ISR overhead.

### Threat

Group 1 UAS, slow hover, 50–200 m.

### Team Setup

- Gunner on wall/rooftop; cleared backblast into courtyard or open ground
- Kinetic rod selected (minimal fragmentation)

### Engagement Sequence

1. ROE confirm
2. IR lock on motor/battery thermal signature
3. Fire; assess collateral from rod impact point

### Success Criteria

- UAS defeated with acceptable collateral

### Limitations

- Backblast critical in enclosed terrain
- Low-thermal plastic drones may resist IR lock

---

## Cross-Cutting Employment Notes

| Topic | Guidance |
|-------|----------|
| IR lock discipline | Confirm LOBL before every shot; cold targets may not lock |
| Ammunition discipline | Guided rounds are expensive; prioritize high-confidence shots |
| Swarm response | Engage highest threat; small arms/EW cover others |
| Obscuration | Smoke/fog degrades IR; escalate to EW or hold fire unless radar round available |

---

## Related Documents

| Document | Purpose |
|----------|---------|
| [06 — System Description](06-system-description.md) | Hardware and employment |
| [07 — Limitations and Risks](07-limitations-and-risks.md) | Capability ceiling |

---

[← Design Constraints](03-design-constraints.md) | [Next: Key Design Trades →](05-key-design-trades.md)
