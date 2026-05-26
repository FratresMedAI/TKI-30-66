#!/usr/bin/env python3
"""Print weighted CG from baseline_systems.json mass budgets (notional)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT / "data" / "baseline_systems.json"


def weighted_cg(components: list[dict]) -> tuple[float, float]:
    mass = sum(c["mass_kg"] for c in components)
    moment = sum(c["mass_kg"] * c["cg_mm"] for c in components)
    return mass, moment / mass if mass else 0.0


def main() -> int:
    data = json.loads(BASELINE.read_text(encoding="utf-8"))
    specs = data["locked_specs"]
    rocket = specs["rocket_mass_budget"]
    launcher = specs.get("launcher_mass_budget", {})

    rm, rcg = weighted_cg(rocket["components"])
    print("Rocket (from nose)")
    print(f"  mass_kg={rm:.3f}  cg_mm={rcg:.1f}  json_cg={rocket['cg_mm_from_nose']}")

    if launcher.get("components"):
        lm, lcg = weighted_cg(launcher["components"])
        ref = launcher.get("cg_reference", "pistol_grip")
        print(f"Launcher empty ({ref})")
        print(f"  mass_kg={lm:.3f}  cg_mm={lcg:.1f}")

    loaded = specs.get("system_mass_budget", {})
    if loaded:
        print("System CG notes:", loaded.get("notes", "(see Annex G)"))

    cg_drift = abs(rcg - rocket["cg_mm_from_nose"])
    mass_delta = rm - rocket["total_nominal_kg"]
    print(f"  component_sum_kg={rm:.3f}  delta_vs_nominal={mass_delta:+.3f} kg")
    if cg_drift > 5.0:
        print(f"WARN: CG drift {cg_drift:.1f} mm vs JSON nominal", file=sys.stderr)
        return 1
    if rm > rocket["cap_kg"]:
        print(f"WARN: component sum exceeds cap {rocket['cap_kg']} kg", file=sys.stderr)
        return 1
    print("OK: CG and cap checks passed (nominal total uses consolidated rollup).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
