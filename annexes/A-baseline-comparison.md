# Annex A — Baseline System Comparison

**Document ID:** TKI-30-66 / ANX-A  
**Version:** 0.2.0  
**Status:** Conceptual

Structured data: [`data/baseline_systems.json`](../data/baseline_systems.json)

---

## Summary Comparison Table

| System | Status | Launcher Mass | Round Mass | Caliber | Reusable | Guidance | Effective Range | Backblast | Cost / Shot | Squad Suitable |
|--------|--------|---------------|------------|---------|----------|----------|-----------------|-----------|-------------|----------------|
| **TKI-30-66 (Splash)** | Conceptual | ~8.0 kg | ~2.5 kg | 50 mm | Yes | Launcher IR + round IR (LOBL) | 150–600 m | Low–moderate | ~$300–450 | Yes (2-man) |
| FGM-148 Javelin | Fielded | ~6.4 kg (CLU) | ~11.8 kg | 127 mm | Yes | IR imaging LOBL | 500–4750 m | Moderate | ~$80,000 | Yes |
| M72 LAW | Fielded | ~3.2 kg | ~3.2 kg | 66 mm | No | Unguided | 50–350 m | Moderate | ~$500 | Yes |
| Carl Gustaf M4 | Fielded | ~6.6 kg | ~3.2 kg | 84 mm | Yes | Unguided | 100–1000 m | Significant | ~$3,000 | Yes |
| FIM-92 Stinger | Fielded | ~15.2 kg | ~10.1 kg | 70 mm | No | IR homing | 500–4800 m | Moderate | ~$120,000 | No |
| C-UAS Rifle (5.56) | Fielded | ~4.0 kg | ~12 g | 5.56 mm | Yes | Unguided | 50–400 m | Minimal | ~$1 | Yes |
| Smart Shooter SMASH | Commercial | ~0.5 kg add-on | ~12 g | 5.56 mm | Yes | Fire-control assist | 50–500 m | Minimal | ~$1 | Yes |
| Coyote Block 2 | Fielded | Vehicle system | ~5.9 kg | N/A | No | RF/radar | 500–5000 m | Minimal | ~$150,000 | No |

---

## Role Positioning

### vs. Javelin

Javelin is the **guidance architecture reference**: reusable launcher-mounted IR tracker cues missile seeker for LOBL. TKI-30-66 applies the same split (tracker in launcher, seeker on round) at much smaller scale, against UAS instead of armor, at ~1/200th the cost per shot.

### vs. Stinger

Stinger carries a full IR seeker but is heavier, more expensive, and optimized for larger aerial targets. TKI-30-66 uses a deliberately simpler, cheaper mini IR seeker sized for small thermal targets at shorter range.

### vs. Carl Gustaf

Gustaf provides form-factor reference but lacks guidance. TKI-30-66 adds ~1.5 kg for integrated tracker and guided rounds while remaining in the same employment class.

### vs. Small Arms C-UAS

TKI trades per-shot cost for guided single-shot effectiveness. No continuous fire or extreme marksmanship required once IR lock achieved.

---

## Key Takeaways

1. **Guidance gap filled differently:** Launcher-tracked LOBL + round mini IR — no laser designator, no beam-riding.
2. **Cost envelope:** ~$300–450/round — above passive concepts but far below missiles.
3. **Javelin analogy:** Reusable tracker amortizes; round carries expendable seeker.

---

## Related Documents

- [06 — System Description](../docs/06-system-description.md)
- [Annex B — KPP Targets](B-kpp-targets.md)
