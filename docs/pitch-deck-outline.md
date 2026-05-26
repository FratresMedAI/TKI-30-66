# RADR — Pitch Deck Outline (8–10 Slides)

**Audience:** Squad/SOF stakeholders, engineering partners, **defense primes**, concept sponsors  
**Version:** 1.8.0 · Expand each slide to 1–2 minutes spoken

---

## Slide 1 — Title

- **RADR** — Recoilless Anti-Drone Rocket  
- **Mid-range drone destroyer** for squad and SOF  
- Phase 0 conceptual · 60 mm · 1000 m goal  
- Visual: [Goodmk60](../visuals/launcher/output/radr-bazooka-goodmk60.png) side profile  

---

## Slide 2 — The gap

- FPV, quads, loiter, glide UAS in **150–1000 m**  
- MG runs out of effective range; SAM not always there  
- Need: **fast, simple, reloadable**, one-person carry  

---

## Slide 3 — System overview

- **Reusable launcher** (40 in, ≤ 5.5 kg) + **sealed round** in ravioli-can tube (≤ 3.5 kg)  
- **IR fire-and-forget** + moderate canards  
- **Cube flak** — not a rod, not beam-riding  
- Diagram: launcher + round block diagram (from DOC-06 mermaid)  

---

## Slide 4 — How the gunner fights (sequence)

1. Open breech → cap off → load → close  
2. Front trigger → tone → retention stop out  
3. Rear trigger → fire → clear 10 yd → reload  

- Emphasize **bolt-action breech certainty** and **retention stop** for slung carry  

---

## Slide 5 — Kill mechanism

- **Pyrotechnic dispersal** → **300 × 7 mm** rough alloy cubes  
- **Forward kill cone** ~10–12 ft @ ~20 ft  
- Proximity fuze (radar or mm-wave) + timed backup  
- Ref: [Annex J](../annexes/J-warhead-dispersal.md)  

---

## Slide 6 — Motor and range (notional)

- Mildly progressive: **750–850 N** → **1050–1150 N** peak  
- **2950–3050 N·s**, **~3.3 s** burn  
- **~330–350 m/s** at **1000 m**; TOF **~4.5–5 s**  
- Speed-first — not high off-boresight  
- Ref: [Annex H](../annexes/H-motor-progressive-burn.md) · [Annex I](../annexes/I-performance-modeling.md)  

---

## Slide 7 — Safety and interlocks

- Retention stop · deadbolt breech · dual trigger · lock tone  
- Backblast **10 yd** discipline  
- Mermaid: interlock flow (Annex F)  

---

## Slide 8 — Mass and ergonomics

- System **8.05 kg** nominal loaded · one-person reload  
- Rear-biased CG · holo + fold-out viewer · foregrip zoom  
- Forward **muzzle brake / blast deflector**  
- Ref: [Annex G](../annexes/G-mass-and-center-of-gravity.md)  

---

## Slide 9 — Roadmap and open questions

- Live-fire Pk @ 1000 m  
- Fuze down-select (radar vs mm-wave)  
- Retention stop mechanism detail (function locked)  
- Propellant/backblast validation in 10 yd zone  

---

## Slide 10 — IP & prime partnership

- **Open concept:** MIT on repo (transparency, capture, community review)  
- **Prime path:** [LICENSE-COMMERCIAL](../LICENSE-COMMERCIAL.md) — evaluation → development → production under **PCA**  
- **Background IP** (concept) · **Foreground IP** (joint prototype) — defined up front  
- Guide: [Licensing & partnership](licensing-and-partnership.md)  
- CTA: [Partnership inquiry](https://github.com/FratresMedAI/RADR-mk.60/issues/new?template=partnership_inquiry.yml)  

---

## Slide 11 — Ask / close

- Feedback on **mid-range** role vs. layered stack (DOC-08)  
- Partners for propellant, fuze, seeker trades · **prime integrators welcome**  
- Repo: https://github.com/FratresMedAI/RADR-mk.60  
- **Not** fielded · **not** procurement-ready  

---

## Appendix slides (optional)

- Comparison table vs. Gustaf / Stinger (Annex A)  
- CONOPS use cases (DOC-04)  
- Full locked spec table (README)  
