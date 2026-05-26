#!/usr/bin/env python3
"""Laptop-light dashboard: regenerate JSON, MC n=200, export PNGs (no Jupyter UI)."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
DATA = ROOT / "data"
OUT = ROOT / "notebooks" / "output"
N_MC = 200

sys.path.insert(0, str(SCRIPTS))
from monte_carlo_envelope import run_mc  # noqa: E402
from radr_performance_model import CDA_COAST_M2, ModelConfig, simulate  # noqa: E402


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    py = sys.executable

    print("1/4 Performance model verify + JSON...")
    subprocess.run([py, str(SCRIPTS / "radr_performance_model.py"), "--verify"], cwd=ROOT, check=True)
    subprocess.run(
        [py, str(SCRIPTS / "radr_performance_model.py"), "--json-out", str(DATA / "performance_model_output.json")],
        cwd=ROOT,
        check=True,
    )

    report = json.loads((DATA / "performance_model_output.json").read_text(encoding="utf-8"))

    print("2/4 Range envelope plot...")
    ranges = report["ranges"]
    keys = sorted(ranges.keys(), key=int)
    xm = [int(k) for k in keys]
    vel = [ranges[k]["v_mps"] for k in keys]
    tof = [ranges[k]["tof_s"] for k in keys]

    fig, ax1 = plt.subplots(figsize=(9, 4.5))
    ax1.plot(xm, vel, "o-", color="#2d5a27", lw=2, markersize=8)
    ax1.axhspan(330, 350, color="#c4e7c4", alpha=0.5)
    ax1.axvline(1000, color="#8b0000", ls="--", alpha=0.7)
    ax1.axvline(200, color="#555", ls=":", alpha=0.7)
    ax1.axvline(1200, color="#555", ls="-.", alpha=0.7)
    ax1.set_xlabel("Downrange (m)")
    ax1.set_ylabel("Velocity (m/s)")
    ax1.set_title("RADR mk.60 — Velocity along trajectory (nominal)")
    ax1.grid(True, alpha=0.3)
    ax2 = ax1.twinx()
    ax2.plot(xm, tof, "s--", color="#1a4d7a", alpha=0.8)
    ax2.set_ylabel("Time of flight (s)")
    fig.tight_layout()
    p1 = OUT / "range_envelope.png"
    fig.savefig(p1, dpi=150)
    plt.close(fig)

    print("3/4 Sensitivity + evasion plots...")
    sens = report["sensitivity_1000m"]
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.barh([r["case"] for r in sens], [r["delta_v_mps"] for r in sens], color=["#2d5a27" if r["delta_v_mps"] >= 0 else "#8b4513" for r in sens])
    ax.axvline(0, color="black", lw=0.8)
    ax.set_xlabel("Delta v @ 1000 m (m/s)")
    ax.set_title("Sensitivity — velocity at sweet spot")
    ax.grid(True, axis="x", alpha=0.3)
    fig.tight_layout()
    p2 = OUT / "sensitivity_1000m.png"
    fig.savefig(p2, dpi=150)
    plt.close(fig)

    ev = report["evasion_geometry"]
    speeds = [r["drone_speed_mps"] for r in ev]
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(speeds, [r["extra_lateral_m_1000_to_1200m"] for r in ev], "o-", label="Extra 1000→1200 m")
    ax.plot(speeds, [r["lateral_m_during_1000m_tof"] for r in ev], "s--", alpha=0.6, label="Full 1000 m TOF")
    ax.set_xlabel("Target speed (m/s)")
    ax.set_ylabel("Lateral displacement (m)")
    ax.set_title("Maneuver margin — extra 200 m downrange")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    p3 = OUT / "evasion_geometry.png"
    fig.savefig(p3, dpi=150)
    plt.close(fig)

    print(f"4/4 Monte Carlo n={N_MC}...")
    mc = run_mc(N_MC, seed=42, target_m=1000.0)
    (DATA / "monte_carlo_200.json").write_text(json.dumps(mc, indent=2), encoding="utf-8")

    rng = np.random.default_rng(42)
    v_samples = []
    for _ in range(N_MC):
        cfg = ModelConfig(
            mass_kg=rng.uniform(2.95, 3.35),
            loft_deg=rng.uniform(2.5, 5.0),
            thrust_scale=rng.uniform(2950 / 3000, 3050 / 3000),
            cda_coast_m2=CDA_COAST_M2 * rng.uniform(0.9, 1.1),
        )
        v_samples.append(simulate(cfg, [1000.0]).ranges["1000"].v_mps)
    v_samples = np.array(v_samples)

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.hist(v_samples, bins=40, color="#2d5a27", edgecolor="white", alpha=0.85)
    ax.axvline(330, color="red", ls="--")
    ax.axvline(350, color="red", ls="--")
    ax.axvline(mc["v_mps"]["p50"], color="navy", lw=2, label=f"p50={mc['v_mps']['p50']:.1f}")
    ax.set_xlabel("v @ 1000 m (m/s)")
    ax.set_title(f"Monte Carlo (n={N_MC})")
    ax.legend()
    fig.tight_layout()
    p4 = OUT / "monte_carlo_v1000.png"
    fig.savefig(p4, dpi=150)
    plt.close(fig)

    print("\nDone.")
    print(f"  v@1000 nominal: {ranges['1000']['v_mps']} m/s  TOF: {ranges['1000']['tof_s']} s")
    print(f"  MC p50: {mc['v_mps']['p50']:.1f} m/s  in-band: {mc['fraction_in_330_350_band']*100:.1f}%")
    print(f"  PNGs: {p1}\n        {p2}\n        {p3}\n        {p4}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
