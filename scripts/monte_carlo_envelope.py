#!/usr/bin/env python3
"""
Monte Carlo on radr_performance_model (CPU).

Use --workers to saturate RunPod vCPUs (set OMP_NUM_THREADS=1 per process).
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from radr_performance_model import CDA_COAST_M2, ModelConfig, simulate  # noqa: E402


def _mc_worker(args: tuple[int, int, float]) -> tuple[float, float]:
    i, seed, target_m = args
    rng = np.random.default_rng(seed + i)
    cfg = ModelConfig(
        mass_kg=float(rng.uniform(2.95, 3.35)),
        loft_deg=float(rng.uniform(2.5, 5.0)),
        thrust_scale=float(rng.uniform(2950 / 3000, 3050 / 3000)),
        cda_coast_m2=float(CDA_COAST_M2 * rng.uniform(0.9, 1.1)),
    )
    pt = simulate(cfg, [target_m]).ranges[str(int(target_m))]
    return pt.v_mps, pt.tof_s


def _summarize(
    n: int,
    seed: int,
    target_m: float,
    v_samples: np.ndarray,
    tof_samples: np.ndarray,
    workers: int,
    elapsed_s: float,
) -> dict:
    in_band = (v_samples >= 330) & (v_samples <= 350)
    return {
        "n": n,
        "seed": seed,
        "target_m": target_m,
        "workers": workers,
        "elapsed_s": round(elapsed_s, 2),
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


def run_mc(
    n: int,
    seed: int,
    target_m: float = 1000.0,
    workers: int = 1,
    return_samples: bool = False,
) -> dict | tuple[dict, np.ndarray]:
    workers = max(1, workers)
    t0 = time.perf_counter()

    if workers == 1:
        v_list: list[float] = []
        t_list: list[float] = []
        for i in range(n):
            v, t = _mc_worker((i, seed, target_m))
            v_list.append(v)
            t_list.append(t)
        v_samples = np.array(v_list)
        tof_samples = np.array(t_list)
    else:
        tasks = [(i, seed, target_m) for i in range(n)]
        chunk = max(1, n // (workers * 8))
        with ProcessPoolExecutor(max_workers=workers) as pool:
            results = list(pool.map(_mc_worker, tasks, chunksize=chunk))
        v_samples = np.array([r[0] for r in results])
        tof_samples = np.array([r[1] for r in results])

    elapsed = time.perf_counter() - t0
    report = _summarize(n, seed, target_m, v_samples, tof_samples, workers, elapsed)
    if return_samples:
        return report, v_samples
    return report


def default_workers() -> int:
    return min(32, os.cpu_count() or 4)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("-n", type=int, default=200, help="Monte Carlo samples")
    p.add_argument("--workers", type=int, default=0, help="0 = auto (min(32, cpu_count))")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--json-out", type=Path)
    p.add_argument("--range-m", type=float, default=1000.0)
    p.add_argument(
        "--runpod-max",
        action="store_true",
        help="Preset: n=25000, workers=32 (override with -n/--workers)",
    )
    args = p.parse_args()

    n = 25000 if args.runpod_max and args.n == 200 else args.n
    workers = 32 if args.runpod_max and args.workers == 0 else args.workers
    if workers <= 0:
        workers = default_workers()

    print(
        f"MC n={n} workers={workers} (set OMP_NUM_THREADS=1 on RunPod)",
        file=sys.stderr,
    )
    report = run_mc(n, args.seed, args.range_m, workers=workers)
    print(json.dumps(report, indent=2))
    if args.json_out:
        args.json_out.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(f"Wrote {args.json_out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
