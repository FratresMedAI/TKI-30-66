#!/usr/bin/env python3
"""
Wind + loft dispersion sweep on the RADR point-mass model.

Adds optional crosswind via ModelConfig.crosswind_mps (lateral advection with
notional coupling — NOT 6-DOF). Sweeps loft 2–5° and crosswind 0–15 m/s.

NOT LIVE-FIRE DATA.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DEFAULT_OUT = DATA / "wind_loft_dispersion.json"

sys.path.insert(0, str(ROOT / "scripts"))
from radr_performance_model import ModelConfig, simulate, V_BAND_1000  # noqa: E402

LOFT_DEG = (2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0)
CROSSWIND_MPS = (0.0, 3.0, 6.0, 9.0, 12.0, 15.0)
TARGET_M = 1000.0
NOMINAL_MASS_KG = 3.1


def run_sweep() -> dict:
    rows = []
    for loft in LOFT_DEG:
        for wind in CROSSWIND_MPS:
            cfg = ModelConfig(
                mass_kg=NOMINAL_MASS_KG,
                loft_deg=loft,
                crosswind_mps=wind,
            )
            summary = simulate(cfg, [TARGET_M])
            pt = summary.ranges[str(int(TARGET_M))]
            reached = summary.max_downrange_m >= TARGET_M - 5.0
            in_band = V_BAND_1000[0] <= pt.v_mps <= V_BAND_1000[1]
            rows.append(
                {
                    "loft_deg": loft,
                    "crosswind_mps": wind,
                    "range_m": TARGET_M,
                    "reached_1000m": reached,
                    "tof_s": round(pt.tof_s, 3),
                    "v_mps": round(pt.v_mps, 2),
                    "lateral_m_at_1000m": round(pt.lateral_m, 2),
                    "in_velocity_band": in_band,
                }
            )

    worst_lateral = max(r["lateral_m_at_1000m"] for r in rows if r["reached_1000m"])
    nominal = next(
        r for r in rows if r["loft_deg"] == 3.5 and r["crosswind_mps"] == 0.0
    )
    wind15_nom = next(
        r for r in rows if r["loft_deg"] == 3.5 and r["crosswind_mps"] == 15.0
    )

    return {
        "model": "wind_loft_dispersion_v1",
        "disclaimer": "2-D point mass with notional crosswind coupling. Not 6-DOF or live fire.",
        "assumptions": {
            "mass_kg": NOMINAL_MASS_KG,
            "loft_sweep_deg": list(LOFT_DEG),
            "crosswind_sweep_mps": list(CROSSWIND_MPS),
            "crosswind_model": "vz tracks constant crosswind with 0.25/s coupling (see radr_performance_model.simulate)",
            "target_range_m": TARGET_M,
            "velocity_band_1000m": list(V_BAND_1000),
        },
        "summary": {
            "nominal_loft_3p5_v_mps": nominal["v_mps"],
            "nominal_loft_3p5_lateral_m": nominal["lateral_m_at_1000m"],
            "max_lateral_when_reached_m": round(worst_lateral, 2),
            "loft_3p5_crosswind_15m": wind15_nom,
        },
        "rows": rows,
    }


def verify(report: dict) -> bool:
    rows = report["rows"]
    ok = True
    print("Wind + loft dispersion @ 1000 m")
    # 2° loft must fail to reach (documented in performance JSON)
    low = next(r for r in rows if r["loft_deg"] == 2.0 and r["crosswind_mps"] == 0.0)
    if low["reached_1000m"]:
        print("  FAIL: 2° loft should not reach 1000 m in model")
        ok = False
    else:
        print("  OK: 2° loft does not reach 1000 m")

    nom15 = report["summary"]["loft_3p5_crosswind_15m"]
    if not nom15["reached_1000m"]:
        print("  FAIL: 3.5° + 15 m/s crosswind should still reach 1000 m downrange")
        ok = False
    else:
        lat = nom15["lateral_m_at_1000m"]
        print(f"  OK: 3.5° + 15 m/s reaches 1000 m, lateral={lat:.1f} m")
        if lat < 1.0:
            print("  WARN: lateral drift very small — check crosswind coupling")

    if nom15["lateral_m_at_1000m"] > 80.0:
        print("  FAIL: lateral drift unreasonably large at 15 m/s")
        ok = False

    # 5° loft at 0 wind should reach and stay near band
    hi = next(r for r in rows if r["loft_deg"] == 5.0 and r["crosswind_mps"] == 0.0)
    if not hi["reached_1000m"]:
        print("  FAIL: 5° loft should reach 1000 m")
        ok = False
    return ok


def main() -> int:
    p = argparse.ArgumentParser(description="Wind and loft dispersion sweep")
    p.add_argument("--json-out", type=Path, default=None)
    p.add_argument("--verify", action="store_true")
    args = p.parse_args()

    report = run_sweep()
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
