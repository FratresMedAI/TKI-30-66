#!/usr/bin/env python3
"""
Coarse seeker / guidance sanity vs target lateral evasion.

Uses evasion_geometry from performance_model_output.json. Compares
uncorrected lateral drift (v_target * TOF) to a bang-bang upper bound
using moderate-maneuver lateral acceleration over the full TOF @ 1000 m.

NOT a Pk model, 6-DOF, or seeker simulation.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DEFAULT_PERF = DATA / "performance_model_output.json"
DEFAULT_OUT = DATA / "guidance_evasion_output.json"

# Locked moderate-maneuver band (m/s^2 equivalent lateral)
A_LAT_MIN_MPS2 = 20.0
A_LAT_MAX_MPS2 = 30.0

# Warhead footprint: 10-12 ft diameter at ~20 ft standoff -> radius ~1.5-1.85 m
FOOTPRINT_RADIUS_M = 1.55  # mid of ~3.0-3.7 m diameter
FOOTPRINT_DIAMETER_FT = (10.0, 12.0)
DETONATION_STANDOFF_FT = 20.0


def load_performance(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def run_sanity(perf: dict) -> dict:
    tof_1000 = float(perf["ranges"]["1000"]["tof_s"])
    t_go_s = tof_1000  # full-TOF correction budget (documented choice)

    rows = []
    for ev in perf["evasion_geometry"]:
        v = float(ev["drone_speed_mps"])
        lateral_uncorrected = float(ev["lateral_m_during_1000m_tof"])
        extra_1200 = float(ev["extra_lateral_m_1000_to_1200m"])

        def residual(a_lat: float) -> float:
            correction = 0.5 * a_lat * t_go_s * t_go_s
            return max(0.0, lateral_uncorrected - correction)

        res_min = residual(A_LAT_MIN_MPS2)
        res_max = residual(A_LAT_MAX_MPS2)

        def engageable(residual_m: float) -> bool:
            return residual_m <= FOOTPRINT_RADIUS_M

        rows.append(
            {
                "drone_speed_mps": v,
                "lateral_uncorrected_m": lateral_uncorrected,
                "extra_lateral_1000_to_1200m": extra_1200,
                "t_go_s": round(t_go_s, 3),
                "lateral_accel_band_mps2": [A_LAT_MIN_MPS2, A_LAT_MAX_MPS2],
                "residual_lateral_m_at_20mps2": round(res_min, 1),
                "residual_lateral_m_at_30mps2": round(res_max, 1),
                "footprint_radius_m": FOOTPRINT_RADIUS_M,
                "engageable_at_20mps2": engageable(res_min),
                "engageable_at_30mps2": engageable(res_max),
            }
        )

    return {
        "model": "guidance_evasion_sanity_v1",
        "disclaimer": "Geometric sanity only. Not Pk, not seeker loop, not Monte Carlo.",
        "assumptions": {
            "t_go_s": t_go_s,
            "t_go_note": "Full TOF @ 1000 m used as correction horizon (conservative vs last-1.5s only).",
            "lateral_accel_mps2": {"min": A_LAT_MIN_MPS2, "max": A_LAT_MAX_MPS2},
            "correction_model": "residual = max(0, lateral_uncorrected - 0.5 * a_lat * t_go^2)",
            "footprint_radius_m": FOOTPRINT_RADIUS_M,
            "footprint_diameter_ft": list(FOOTPRINT_DIAMETER_FT),
            "detonation_standoff_ft": DETONATION_STANDOFF_FT,
            "target_range_m": 1000.0,
        },
        "rows": rows,
    }


def verify(report: dict) -> bool:
    rows = report["rows"]
    ok = True
    print("Guidance evasion sanity @ 1000 m")
    print(f"  t_go={report['assumptions']['t_go_s']:.2f}s  a_lat={A_LAT_MIN_MPS2}-{A_LAT_MAX_MPS2} m/s^2  R_foot={FOOTPRINT_RADIUS_M} m")
    print(f"  {'v_tgt':>6} {'lat':>7} {'res@20':>8} {'res@30':>8} {'ok@30':>6}")
    for r in rows:
        flag = "Y" if r["engageable_at_30mps2"] else "N"
        print(
            f"  {r['drone_speed_mps']:6.0f} {r['lateral_uncorrected_m']:7.1f} "
            f"{r['residual_lateral_m_at_20mps2']:8.1f} {r['residual_lateral_m_at_30mps2']:8.1f} {flag:>6}"
        )
        if r["drone_speed_mps"] <= 25 and not r["engageable_at_30mps2"]:
            ok = False
    # Expect moderate band to cover at least up to ~25 m/s crossing targets at 1000 m
    fast = next((r for r in rows if r["drone_speed_mps"] == 40), None)
    if fast and fast["engageable_at_30mps2"]:
        print("  note: 40 m/s still inside footprint at 30 m/s^2 — review assumptions")
    return ok


def main() -> int:
    p = argparse.ArgumentParser(description="Guidance vs evasion geometric sanity check")
    p.add_argument("--perf", type=Path, default=DEFAULT_PERF)
    p.add_argument("--json-out", type=Path, default=None)
    p.add_argument("--verify", action="store_true")
    args = p.parse_args()

    if not args.perf.is_file():
        print(f"Missing {args.perf}", file=sys.stderr)
        return 1

    report = run_sanity(load_performance(args.perf))
    out_path = args.json_out or DEFAULT_OUT

    if args.verify:
        ok = verify(report)
    else:
        ok = True

    if args.json_out is not None or not args.verify:
        out_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(f"Wrote {out_path}")

    if args.verify:
        return 0 if ok else 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
