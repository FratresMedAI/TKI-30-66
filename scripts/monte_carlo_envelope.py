#!/usr/bin/env python3
"""
Lightweight Monte Carlo on radr_performance_model (CPU).

Default n=200 for laptop-friendly runs; use n=5000+ on RunPod.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from radr_performance_model import (  # noqa: E402
    CDA_COAST_M2,
    ModelConfig,
    simulate,
)

DEFAULT_RANGES = [1000.0]


def run_mc(
    n: int,
    seed: int,
    target_m: float = 1000.0,
) -> dict:
    rng = np.random.default_rng(seed)
    v_samples = np.empty(n)
    tof_samples = np.empty(n)

    for i in range(n):
        mass = rng.uniform(2.95, 3.35)
        impulse_scale = rng.uniform(2950 / 3000, 3050 / 3000)
        loft = rng.uniform(2.5, 5.0)
        cda_coast = CDA_COAST_M2 * rng.uniform(0.9, 1.1)
        cfg = ModelConfig(
            mass_kg=mass,
            loft_deg=loft,
            thrust_scale=impulse_scale,
            cda_coast_m2=cda_coast,
        )
        pt = simulate(cfg, [target_m]).ranges[str(int(target_m))]
        v_samples[i] = pt.v_mps
        tof_samples[i] = pt.tof_s

    in_band = (v_samples >= 330) & (v_samples <= 350)
    return {
        "n": n,
        "seed": seed,
        "target_m": target_m,
        "v_mps": {
            "p5": float(np.percentile(v_samples, 5)),
            "p50": float(np.percentile(v_samples, 50)),
            "p95": float(np.percentile(v_samples, 95)),
            "mean": float(np.mean(v_samples)),
            "std": float(np.std(v_samples)),
        },
        "tof_s": {
            "p5": float(np.percentile(tof_samples, 5)),
            "p50": float(np.percentile(tof_samples, 50)),
            "p95": float(np.percentile(tof_samples, 95)),
        },
        "fraction_in_330_350_band": float(np.mean(in_band)),
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("-n", type=int, default=200, help="samples (use 5000+ on RunPod)")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--json-out", type=Path)
    p.add_argument("--range-m", type=float, default=1000.0)
    args = p.parse_args()

    if args.n > 800 and args.n <= 2000:
        print(f"Running n={args.n} — moderate CPU load.", file=sys.stderr)
    elif args.n > 2000:
        print(f"Running n={args.n} — prefer RunPod for large n.", file=sys.stderr)

    report = run_mc(args.n, args.seed, args.range_m)
    print(json.dumps(report, indent=2))
    if args.json_out:
        args.json_out.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(f"Wrote {args.json_out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
