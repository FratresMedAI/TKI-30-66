#!/usr/bin/env python3
"""
RADR trajectory CLI — delegates to radr_performance_model.py (v2).

Legacy entry point for CI and docs. NOT LIVE-FIRE DATA.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from radr_performance_model import (
    CDA_BOOST_M2,
    CDA_COAST_M2,
    ModelConfig,
    build_report,
    simulate,
    sensitivity_sweep,
    verify,
)


def smoke_test() -> None:
    verify()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()

    if args.smoke:
        smoke_test()
        return 0

    cfg = ModelConfig()
    summary = simulate(cfg, [500.0, 750.0, 1000.0, 1200.0])
    print("RADR trajectory (performance model v2) -- NOTIONAL")
    print(
        f"  impulse={summary.impulse_ns:.0f} N*s  v_bo={summary.burnout_v_mps:.1f} m/s  "
        f"x_bo={summary.burnout_x_m:.0f} m"
    )
    for r in [500.0, 750.0, 1000.0, 1200.0]:
        h = summary.ranges[str(int(r))]
        print(f"  {int(r):4d} m: TOF={h.tof_s:.2f} s  v={h.v_mps:.1f} m/s")

    if args.json_out:
        report = build_report()
        # Legacy keys for consumers
        legacy = {
            "impulse_ns": report["motor"]["impulse_ns"],
            "burnout_v_mps": report["motor"]["burnout_v_mps"],
            "burnout_x_m": report["motor"]["burnout_x_m"],
            "ranges": {
                k: {"tof_s": v["tof_s"], "v_mps": v["v_mps"]}
                for k, v in report["ranges"].items()
            },
            "sensitivity_1000m": report["sensitivity_1000m"],
            "acceleration_profile": report["acceleration_profile"],
            "performance_model_v2": report,
            "cda_boost_m2": CDA_BOOST_M2,
            "cda_coast_m2": CDA_COAST_M2,
        }
        args.json_out.write_text(json.dumps(legacy, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
