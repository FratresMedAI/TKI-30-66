#!/usr/bin/env python3
"""Mass/CG and warhead cube checks against baseline_systems.json."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT / "data" / "baseline_systems.json"

# Match radr_performance_model.py
CUBE_COUNT = 300
CUBE_MM = 7.0
CUBE_DENSITY_KG_M3 = 7800.0


def weighted_cg(components: list[dict]) -> tuple[float, float]:
    mass = sum(c["mass_kg"] for c in components)
    moment = sum(c["mass_kg"] * c["cg_mm"] for c in components)
    return mass, moment / mass if mass else 0.0


def cube_fragment_mass_kg() -> float:
    side_m = CUBE_MM / 1000.0
    return CUBE_COUNT * (side_m**3) * CUBE_DENSITY_KG_M3


def main() -> int:
    data = json.loads(BASELINE.read_text(encoding="utf-8"))
    specs = data["locked_specs"]
    rocket = specs["rocket_mass_budget"]
    launcher = specs.get("launcher_mass_budget", {})

    rm, rcg = weighted_cg(rocket["components"])
    print("Rocket (from nose)")
    print(f"  mass_kg={rm:.3f}  cg_mm={rcg:.1f}  json_cg={rocket['cg_mm_from_nose']}")

    frag = cube_fragment_mass_kg()
    wh = next(c for c in rocket["components"] if c["id"] == "warhead_section")
    print("Warhead cubes (steel-class 7 mm)")
    print(f"  fragment_mass_kg={frag:.3f}  warhead_section_kg={wh['mass_kg']}")
    print(f"  burster+casing_allowance_kg={wh['mass_kg'] - frag:.3f}")

    if launcher.get("components"):
        lm, lcg = weighted_cg(launcher["components"])
        ref = launcher.get("cg_reference", "pistol_grip")
        print(f"Launcher empty ({ref})")
        print(f"  mass_kg={lm:.3f}  cg_mm={lcg:.1f}")

    cg_drift = abs(rcg - rocket["cg_mm_from_nose"])
    mass_delta = rm - rocket["total_nominal_kg"]
    print(f"  component_sum_kg={rm:.3f}  delta_vs_nominal={mass_delta:+.3f} kg")

    err = 0
    if cg_drift > 5.0:
        print(f"WARN: CG drift {cg_drift:.1f} mm vs JSON nominal", file=sys.stderr)
        err = 1
    if rm > rocket["cap_kg"]:
        print(f"WARN: component sum exceeds cap {rocket['cap_kg']} kg", file=sys.stderr)
        err = 1
    if frag > wh["mass_kg"]:
        print("WARN: cube fragments alone exceed warhead section mass", file=sys.stderr)
        err = 1
    if err == 0:
        print("OK: CG, cap, and cube mass checks passed.")
    return err


if __name__ == "__main__":
    sys.exit(main())
