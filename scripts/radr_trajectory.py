#!/usr/bin/env python3
"""
RADR notional point-mass trajectory (stdlib only).

2-D boost + coast with quadratic drag. Baseline CdA (0.35 m²) uses separate
boost/coast multipliers calibrated to locked 330–350 m/s @ 1000 m — see scripts/README.md.

NOT LIVE-FIRE DATA.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path

G = 9.80665
RHO = 1.225
BURN_END_S = 3.3
# Calibrated notional multipliers on baseline cd_a_m2 (0.35 m² reference).
CDA_BOOST_MULT = 0.046
CDA_COAST_MULT = 0.00062
NOMINAL_IMPULSE_NS = 3000.0

THRUST_TABLE = [
    (0.0, 0.0),
    (0.5, 780.0),
    (1.0, 800.0),
    (1.5, 820.0),
    (2.0, 870.0),
    (2.5, 1000.0),
    (3.0, 1120.0),
    (3.3, 1050.0),
]


@dataclass
class Config:
    mass_kg: float = 3.1
    cd_a_m2: float = 0.35
    loft_deg: float = 3.5
    thrust_scale: float = 1.0
    dt_s: float = 0.002


@dataclass
class Result:
    burnout_t_s: float
    burnout_v_mps: float
    burnout_x_m: float
    range_m: float
    tof_s: float
    v_at_range_mps: float


def thrust_at(t: float, scale: float) -> float:
    if t < 0 or t > BURN_END_S:
        return 0.0
    for i in range(len(THRUST_TABLE) - 1):
        t0, f0 = THRUST_TABLE[i]
        t1, f1 = THRUST_TABLE[i + 1]
        if t0 <= t <= t1:
            u = (t - t0) / (t1 - t0) if t1 > t0 else 0.0
            return (f0 + u * (f1 - f0)) * scale
    return 0.0


def impulse_table(scale: float = 1.0) -> float:
    impulse = 0.0
    for i in range(len(THRUST_TABLE) - 1):
        t0, f0 = THRUST_TABLE[i]
        t1, f1 = THRUST_TABLE[i + 1]
        impulse += 0.5 * (f0 + f1) * scale * (t1 - t0)
    return impulse


def default_thrust_scale() -> float:
    return NOMINAL_IMPULSE_NS / impulse_table(1.0)


def drag_accel(vx: float, vy: float, cda: float, mass: float) -> tuple[float, float]:
    v = math.hypot(vx, vy)
    if v < 1e-6:
        return 0.0, 0.0
    fd = 0.5 * RHO * cda * v * v
    return -fd * vx / (mass * v), -fd * vy / (mass * v)


def integrate_flight(cfg: Config) -> tuple[float, float, list[dict], list[tuple[float, float, float]]]:
    scale = cfg.thrust_scale * default_thrust_scale()
    theta = math.radians(cfg.loft_deg)
    cda_boost = cfg.cd_a_m2 * CDA_BOOST_MULT
    cda_coast = cfg.cd_a_m2 * CDA_COAST_MULT

    x = y = vx = vy = t = 0.0
    profile: list[dict] = []
    history: list[tuple[float, float, float]] = []
    next_p = 0.0
    v_bo = x_bo = 0.0
    burned_out = False

    while t < BURN_END_S + 15.0 and y >= -1.0:
        v = math.hypot(vx, vy)
        phase = "boost" if t <= BURN_END_S + 1e-9 else "coast"
        if t >= next_p:
            profile.append(
                {"t_s": round(t, 2), "x_m": round(x, 1), "v_mps": round(v, 1), "phase": phase}
            )
            next_p += 0.5

        cda = cda_boost if phase == "boost" else cda_coast
        ax = ay = 0.0
        if phase == "boost":
            f = thrust_at(t, scale)
            ax = f * math.cos(theta) / cfg.mass_kg
            ay = f * math.sin(theta) / cfg.mass_kg
        dax, day = drag_accel(vx, vy, cda, cfg.mass_kg)
        ax += dax
        ay += day
        ay -= G

        vx += ax * cfg.dt_s
        vy += ay * cfg.dt_s
        x += vx * cfg.dt_s
        y += vy * cfg.dt_s
        t += cfg.dt_s
        history.append((x, t, v))

        if not burned_out and t >= BURN_END_S:
            burned_out = True
            v_bo = v
            x_bo = x

        if v < 50.0 and phase == "coast":
            break

    if not burned_out:
        v_bo = math.hypot(vx, vy)
        x_bo = x
    return v_bo, x_bo, profile, history


def interp_history(history: list[tuple[float, float, float]], target_x: float) -> tuple[float, float]:
    for i in range(1, len(history)):
        x0, t0, v0 = history[i - 1]
        x1, t1, v1 = history[i]
        if x0 < target_x <= x1:
            u = (target_x - x0) / (x1 - x0)
            return t0 + u * (t1 - t0), v0 + u * (v1 - v0)
    return history[-1][1], history[-1][2]


def simulate(cfg: Config, targets: list[float]) -> tuple[float, float, list[dict], dict[float, Result]]:
    v_bo, x_bo, profile, history = integrate_flight(cfg)
    hits: dict[float, Result] = {}
    for r in sorted(targets):
        tof, v_r = interp_history(history, r)
        hits[r] = Result(
            burnout_t_s=BURN_END_S,
            burnout_v_mps=v_bo,
            burnout_x_m=x_bo,
            range_m=r,
            tof_s=tof,
            v_at_range_mps=v_r,
        )
        profile.append(
            {"t_s": round(tof, 2), "x_m": r, "v_mps": round(v_r, 1), "phase": f"mark_{int(r)}m"}
        )
    return v_bo, x_bo, profile, hits


def run_sensitivity() -> list[dict]:
    cases = [
        ("nominal", Config()),
        ("mass_plus_5pct", Config(mass_kg=3.1 * 1.05)),
        ("mass_minus_5pct", Config(mass_kg=3.1 * 0.95)),
        ("impulse_minus_3pct", Config(thrust_scale=0.97)),
        ("impulse_plus_3pct", Config(thrust_scale=1.03)),
        ("cd_a_plus_10pct", Config(cd_a_m2=0.35 * 1.10)),
        ("cd_a_minus_10pct", Config(cd_a_m2=0.35 * 0.90)),
    ]
    _, _, _, nom = simulate(Config(), [1000.0])
    v_nom = nom[1000.0].v_at_range_mps
    rows = []
    for name, cfg in cases:
        _, _, _, h = simulate(cfg, [1000.0])
        v = h[1000.0].v_at_range_mps
        rows.append(
            {
                "case": name,
                "v_1000_mps": round(v, 1),
                "delta_v_vs_nominal_mps": round(v - v_nom, 1),
                "tof_1000_s": round(h[1000.0].tof_s, 2),
            }
        )
    return rows


def smoke_test() -> None:
    _, _, _, hits = simulate(Config(), [1000.0, 1200.0])
    v1 = hits[1000.0].v_at_range_mps
    if not (325 <= v1 <= 355):
        raise SystemExit(f"smoke fail: v@1000m={v1:.1f}")
    print(
        f"smoke ok: v@1000m={v1:.1f} m/s TOF={hits[1000.0].tof_s:.2f}s, "
        f"v@1200m={hits[1200.0].v_at_range_mps:.1f} m/s"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()
    if args.smoke:
        smoke_test()
        return 0

    cfg = Config()
    targets = [500.0, 750.0, 1000.0, 1200.0]
    v_bo, x_bo, profile, hits = simulate(cfg, targets)
    print("RADR trajectory — NOTIONAL")
    print(
        f"  impulse={impulse_table(default_thrust_scale()):.0f} N·s  "
        f"v_bo={v_bo:.1f} m/s  x_bo={x_bo:.0f} m"
    )
    for r in targets:
        h = hits[r]
        print(f"  {int(r):4d} m: TOF={h.tof_s:.2f} s  v={h.v_at_range_mps:.1f} m/s")
    if args.json_out:
        args.json_out.write_text(
            json.dumps(
                {
                    "impulse_ns": round(impulse_table(default_thrust_scale()), 1),
                    "burnout_v_mps": round(v_bo, 1),
                    "burnout_x_m": round(x_bo, 1),
                    "ranges": {
                        str(int(r)): {
                            "tof_s": round(hits[r].tof_s, 2),
                            "v_mps": round(hits[r].v_at_range_mps, 1),
                        }
                        for r in targets
                    },
                    "sensitivity_1000m": run_sensitivity(),
                    "acceleration_profile": profile,
                },
                indent=2,
            ),
            encoding="utf-8",
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
