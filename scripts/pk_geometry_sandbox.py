#!/usr/bin/env python3
"""
Notional geometric Pk sandbox — complements guidance_evasion_sanity.py.

P_geometric = exp(-(residual/R)^2) inside footprint radius R.
P_kill|hit are user-locked notional lethality factors (NOT live-fire).

NOT certified lethality or arena test data.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DEFAULT_GUIDANCE = DATA / "guidance_evasion_output.json"
DEFAULT_OUT = DATA / "pk_geometry_sandbox.json"

FOOTPRINT_RADIUS_M = 1.55
A_LAT_MPS2 = 30.0  # upper moderate-maneuver bound from guidance script

# Notional P_kill | hit by threat class (README engagement classes)
P_KILL_HIT = {
    "hover": 0.70,
    "crossing": 0.40,
    "glide": 0.35,
}

# Representative target speeds (m/s) for each class
THREAT_SPEED_MPS = {
    "hover": 10.0,
    "crossing": 25.0,
    "glide": 40.0,
}


def p_geometric(residual_m: float, radius_m: float) -> float:
    if residual_m <= 0.0:
        return 1.0
    x = residual_m / radius_m
    return math.exp(-(x * x))


def load_guidance(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def residual_at_accel(guidance: dict, drone_speed_mps: float, a_lat: float) -> float:
    row = next(
        (r for r in guidance["rows"] if r["drone_speed_mps"] == drone_speed_mps),
        None,
    )
    if row is None:
        # interpolate nearest by speed
        rows = sorted(guidance["rows"], key=lambda r: r["drone_speed_mps"])
        if drone_speed_mps <= rows[0]["drone_speed_mps"]:
            row = rows[0]
        elif drone_speed_mps >= rows[-1]["drone_speed_mps"]:
            row = rows[-1]
        else:
            for i in range(len(rows) - 1):
                if rows[i]["drone_speed_mps"] <= drone_speed_mps <= rows[i + 1]["drone_speed_mps"]:
                    u = (drone_speed_mps - rows[i]["drone_speed_mps"]) / (
                        rows[i + 1]["drone_speed_mps"] - rows[i]["drone_speed_mps"]
                    )
                    lat = rows[i]["lateral_uncorrected_m"] + u * (
                        rows[i + 1]["lateral_uncorrected_m"] - rows[i]["lateral_uncorrected_m"]
                    )
                    t_go = rows[i]["t_go_s"]
                    correction = 0.5 * a_lat * t_go * t_go
                    return max(0.0, lat - correction)
            row = rows[-1]

    t_go = float(row["t_go_s"])
    lat = float(row["lateral_uncorrected_m"])
    correction = 0.5 * a_lat * t_go * t_go
    return max(0.0, lat - correction)


def run_sandbox(guidance: dict) -> dict:
    threats = []
    for threat_id, speed in THREAT_SPEED_MPS.items():
        residual = residual_at_accel(guidance, speed, A_LAT_MPS2)
        p_geo = p_geometric(residual, FOOTPRINT_RADIUS_M)
        p_leth = P_KILL_HIT[threat_id]
        p_notional = p_geo * p_leth
        threats.append(
            {
                "threat_class": threat_id,
                "representative_speed_mps": speed,
                "residual_lateral_m": round(residual, 2),
                "footprint_radius_m": FOOTPRINT_RADIUS_M,
                "p_geometric": round(p_geo, 4),
                "p_kill_given_hit_notional": p_leth,
                "p_notional_combined": round(p_notional, 4),
                "inside_footprint_step": residual <= FOOTPRINT_RADIUS_M,
            }
        )

    return {
        "model": "pk_geometry_sandbox_v1",
        "disclaimer": "Geometric Pk only. P_kill|hit are notional design placeholders — not arena or live-fire.",
        "assumptions": {
            "footprint_radius_m": FOOTPRINT_RADIUS_M,
            "p_geometric_formula": "exp(-(residual/R)^2)",
            "lateral_accel_mps2": A_LAT_MPS2,
            "guidance_source": "data/guidance_evasion_output.json",
            "p_kill_given_hit": P_KILL_HIT,
            "threat_speed_map_mps": THREAT_SPEED_MPS,
        },
        "threats": threats,
    }


def verify(report: dict) -> bool:
    ok = True
    print("Notional Pk (geometric) @ 1000 m, a_lat=30 m/s^2")
    print(f"  {'class':>10} {'v':>4} {'res':>7} {'P_geo':>7} {'P_k|h':>6} {'P_*':>7}")
    for t in report["threats"]:
        print(
            f"  {t['threat_class']:>10} {t['representative_speed_mps']:4.0f} "
            f"{t['residual_lateral_m']:7.2f} {t['p_geometric']:7.4f} "
            f"{t['p_kill_given_hit_notional']:6.2f} {t['p_notional_combined']:7.4f}"
        )
        if t["threat_class"] == "hover" and t["p_geometric"] < 0.99:
            print("  FAIL: hover should be inside footprint at 30 m/s^2")
            ok = False
        if t["threat_class"] == "crossing" and t["p_geometric"] < 0.99:
            print("  FAIL: crossing @ 25 m/s should be inside footprint at 30 m/s^2")
            ok = False
    glide = next(t for t in report["threats"] if t["threat_class"] == "glide")
    if glide["p_geometric"] > 0.99 and glide["residual_lateral_m"] > 0.5:
        print("  note: glide has residual but high P_geo — check formula")
    return ok


def main() -> int:
    p = argparse.ArgumentParser(description="Notional geometric Pk sandbox")
    p.add_argument("--guidance", type=Path, default=DEFAULT_GUIDANCE)
    p.add_argument("--json-out", type=Path, default=None)
    p.add_argument("--verify", action="store_true")
    args = p.parse_args()

    if not args.guidance.is_file():
        print(f"Missing {args.guidance}", file=sys.stderr)
        return 1

    report = run_sandbox(load_guidance(args.guidance))
    out_path = args.json_out or DEFAULT_OUT

    if args.verify:
        ok = verify(report)
    else:
        ok = True

    if args.json_out is not None or not args.verify:
        out_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(f"Wrote {out_path}")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
