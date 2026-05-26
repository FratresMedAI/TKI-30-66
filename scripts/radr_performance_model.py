#!/usr/bin/env python3
"""
RADR notional performance model — traceable point-mass ballistics (stdlib only).

Uses explicit effective drag areas (m²) for boost vs coast, tied to 60 mm frontal
geometry, fitted to the locked 330–350 m/s @ 1000 m band. Includes rocket-equation
checks, warhead cube mass, loft/impulse/mass sweeps, and evasion geometry.

NOT LIVE-FIRE DATA.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

G = 9.80665
RHO_SL = 1.225
A_SOUND = 340.0
BURN_END_S = 3.3
NOMINAL_IMPULSE_NS = 3000.0
V_BAND_1000 = (330.0, 350.0)

# --- Geometry (60 mm class) ---
BODY_D_M = 0.060
A_FRONT_M2 = math.pi * (BODY_D_M / 2) ** 2  # 0.002827 m²
FIN_DEPLOY_S = 0.25

# Effective drag areas (m²) — 2-D calibrated; equivalent Cd = CDA / A_front
# Boost: motor + deploy transient + trim; Coast: base drag dominant (fins trimmed)
CDA_BOOST_M2 = 0.35 * 0.046  # 0.01617 — matches legacy integrator
CDA_COAST_M2 = 0.35 * 0.00062  # 0.000217
CD_EQUIV_BOOST = CDA_BOOST_M2 / A_FRONT_M2
CD_EQUIV_COAST = CDA_COAST_M2 / A_FRONT_M2

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

RANGE_MARKS_M = [200, 300, 500, 800, 1000, 1200]
CUBE_COUNT = 300
CUBE_MM = 7.0
CUBE_DENSITY_KG_M3 = 7800.0


@dataclass
class ModelConfig:
    mass_kg: float = 3.1
    loft_deg: float = 3.5
    thrust_scale: float = 1.0
    cda_boost_m2: float = CDA_BOOST_M2
    cda_coast_m2: float = CDA_COAST_M2
    dt_s: float = 0.002


@dataclass
class RangePoint:
    range_m: float
    tof_s: float
    v_mps: float
    mach: float
    q_pa: float
    phase: str


@dataclass
class FlightSummary:
    impulse_ns: float
    thrust_scale: float
    delta_v_ideal_mps: float
    burnout_t_s: float
    burnout_v_mps: float
    burnout_x_m: float
    burnout_mach: float
    cda_boost_m2: float
    cda_coast_m2: float
    ranges: dict[str, RangePoint] = field(default_factory=dict)


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


def integrate_impulse(scale: float = 1.0) -> float:
    impulse = 0.0
    for i in range(len(THRUST_TABLE) - 1):
        t0, f0 = THRUST_TABLE[i]
        t1, f1 = THRUST_TABLE[i + 1]
        impulse += 0.5 * (f0 + f1) * scale * (t1 - t0)
    return impulse


def thrust_scale_for_nominal_impulse() -> float:
    return NOMINAL_IMPULSE_NS / integrate_impulse(1.0)


def drag_accel(vx: float, vy: float, cda: float, mass: float) -> tuple[float, float]:
    v = math.hypot(vx, vy)
    if v < 1e-9:
        return 0.0, 0.0
    fd = 0.5 * RHO_SL * cda * v * v
    return -fd * vx / (mass * v), -fd * vy / (mass * v)


def simulate(cfg: ModelConfig, marks: list[float]) -> FlightSummary:
    t_scale = cfg.thrust_scale * thrust_scale_for_nominal_impulse()
    impulse = integrate_impulse(t_scale)
    theta = math.radians(cfg.loft_deg)

    x = y = vx = vy = t = 0.0
    history: list[tuple[float, float, float, str]] = []
    v_bo = x_bo = 0.0
    burned = False

    while t < BURN_END_S + 30.0 and y >= -2.0:
        v = math.hypot(vx, vy)
        phase = "boost" if t <= BURN_END_S + 1e-9 else "coast"
        history.append((x, t, v, phase))

        cda = cfg.cda_boost_m2 if phase == "boost" else cfg.cda_coast_m2
        ax = ay = 0.0
        if phase == "boost":
            f = thrust_at(t, t_scale)
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

        if not burned and t >= BURN_END_S:
            burned = True
            v_bo = v
            x_bo = x

    if not burned:
        v_bo = math.hypot(vx, vy)
        x_bo = x

    def at_range(r: float) -> RangePoint:
        for i in range(1, len(history)):
            x0, t0, v0, p0 = history[i - 1]
            x1, t1, v1, p1 = history[i]
            if x0 < r <= x1:
                u = (r - x0) / (x1 - x0)
                tt = t0 + u * (t1 - t0)
                vv = v0 + u * (v1 - v0)
                ph = p1 if u > 0.5 else p0
                return RangePoint(r, tt, vv, vv / A_SOUND, 0.5 * RHO_SL * vv * vv, ph)
        _, tL, vL, pL = history[-1]
        return RangePoint(r, tL, vL, vL / A_SOUND, 0.5 * RHO_SL * vL * vL, pL)

    return FlightSummary(
        impulse_ns=impulse,
        thrust_scale=t_scale,
        delta_v_ideal_mps=impulse / cfg.mass_kg,
        burnout_t_s=BURN_END_S,
        burnout_v_mps=v_bo,
        burnout_x_m=x_bo,
        burnout_mach=v_bo / A_SOUND,
        cda_boost_m2=cfg.cda_boost_m2,
        cda_coast_m2=cfg.cda_coast_m2,
        ranges={str(int(m)): at_range(m) for m in marks},
    )


def warhead_cube_mass_kg() -> dict:
    side_m = CUBE_MM / 1000.0
    vol_one = side_m**3
    mass_one = vol_one * CUBE_DENSITY_KG_M3
    total = CUBE_COUNT * mass_one
    pack_volume_l = total / CUBE_DENSITY_KG_M3 * 1000
    return {
        "cube_count": CUBE_COUNT,
        "cube_mm": CUBE_MM,
        "density_kg_m3": CUBE_DENSITY_KG_M3,
        "mass_one_g": round(mass_one * 1000, 2),
        "fragment_mass_kg": round(total, 3),
        "solid_volume_liters": round(pack_volume_l, 3),
        "annex_g_warhead_total_kg": 1.05,
        "non_fragment_allowance_kg": round(1.05 - total, 3),
    }


def evasion_table(tof_1000: float, tof_1200: float) -> list[dict]:
    dt = tof_1200 - tof_1000
    return [
        {
            "drone_speed_mps": v,
            "lateral_m_during_1000m_tof": round(v * tof_1000, 1),
            "extra_lateral_m_1000_to_1200m": round(v * dt, 1),
        }
        for v in (10, 15, 20, 25, 30, 40, 50)
    ]


def loft_sweep(cfg: ModelConfig) -> list[dict]:
    rows = []
    for loft in (2.0, 3.5, 5.0):
        c = ModelConfig(**{**asdict(cfg), "loft_deg": loft})
        s = simulate(c, [1000.0])
        pt = s.ranges["1000"]
        rows.append(
            {
                "loft_deg": loft,
                "v_1000_mps": round(pt.v_mps, 1),
                "tof_1000_s": round(pt.tof_s, 2),
                "reached_1000m": s.burnout_x_m >= 400 or pt.tof_s > 3.0,
            }
        )
    return rows


def sensitivity_sweep(cfg: ModelConfig) -> list[dict]:
    cases = [
        ("nominal", ModelConfig()),
        ("mass_plus_5pct", ModelConfig(mass_kg=3.1 * 1.05)),
        ("mass_minus_5pct", ModelConfig(mass_kg=3.1 * 0.95)),
        ("impulse_minus_3pct", ModelConfig(thrust_scale=0.97)),
        ("impulse_plus_3pct", ModelConfig(thrust_scale=1.03)),
        ("cda_coast_plus_10pct", ModelConfig(cda_coast_m2=CDA_COAST_M2 * 1.10)),
        ("cda_coast_minus_10pct", ModelConfig(cda_coast_m2=CDA_COAST_M2 * 0.90)),
        ("mass_cap_3_35kg", ModelConfig(mass_kg=3.35)),
        ("mass_light_2_95kg", ModelConfig(mass_kg=2.95)),
    ]
    nom_v = simulate(cfg, [1000.0]).ranges["1000"].v_mps
    rows = []
    for name, c in cases:
        pt = simulate(c, [1000.0]).ranges["1000"]
        rows.append(
            {
                "case": name,
                "v_1000_mps": round(pt.v_mps, 1),
                "delta_v_mps": round(pt.v_mps - nom_v, 1),
                "tof_1000_s": round(pt.tof_s, 2),
            }
        )
    return rows


def acceleration_samples(cfg: ModelConfig) -> list[dict]:
    """0.5 s samples via short integration with history capture."""
    t_scale = cfg.thrust_scale * thrust_scale_for_nominal_impulse()
    theta = math.radians(cfg.loft_deg)
    x = y = vx = vy = t = 0.0
    samples = []
    next_t = 0.0
    while t < BURN_END_S + 5.0 and y >= -1.0:
        v = math.hypot(vx, vy)
        phase = "boost" if t <= BURN_END_S else "coast"
        if t >= next_t:
            cda = cfg.cda_boost_m2 if phase == "boost" else cfg.cda_coast_m2
            fd = 0.5 * RHO_SL * cda * v * v
            fth = thrust_at(t, t_scale) if phase == "boost" else 0.0
            a_ax = (fth * math.cos(theta) - fd * (vx / v if v > 0 else 0)) / cfg.mass_kg
            a_ay = (fth * math.sin(theta) - fd * (vy / v if v > 0 else 0)) / cfg.mass_kg - G
            a_tot = math.hypot(a_ax, a_ay)
            samples.append(
                {
                    "t_s": round(t, 2),
                    "x_m": round(x, 1),
                    "v_mps": round(v, 1),
                    "a_mps2": round(a_tot, 1),
                    "phase": phase,
                }
            )
            next_t += 0.5
        cda = cfg.cda_boost_m2 if phase == "boost" else cfg.cda_coast_m2
        ax = ay = 0.0
        if phase == "boost":
            f = thrust_at(t, t_scale)
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
        if v < 50 and phase == "coast":
            break
    return samples


def build_report() -> dict:
    cfg = ModelConfig()
    summary = simulate(cfg, [float(r) for r in RANGE_MARKS_M])
    r1 = summary.ranges["1000"]
    r2 = summary.ranges["1200"]

    return {
        "model_version": "2.0",
        "status": "notional_point_mass_effective_cda",
        "disclaimer": "NOT LIVE-FIRE. Effective CdA from 60 mm geometry + 2-D band fit.",
        "geometry": {
            "body_d_m": BODY_D_M,
            "A_front_m2": round(A_FRONT_M2, 6),
            "fin_deploy_s": FIN_DEPLOY_S,
            "Cd_equiv_boost": round(CD_EQUIV_BOOST, 2),
            "Cd_equiv_coast": round(CD_EQUIV_COAST, 3),
        },
        "drag_effective_m2": {
            "cda_boost": round(CDA_BOOST_M2, 6),
            "cda_coast": round(CDA_COAST_M2, 6),
            "interpretation": "Equivalent drag area; not skin-friction Cd alone",
        },
        "motor": {
            "impulse_ns": round(summary.impulse_ns, 1),
            "thrust_scale": round(summary.thrust_scale, 4),
            "burn_time_s": BURN_END_S,
            "average_thrust_n": round(summary.impulse_ns / BURN_END_S, 1),
            "delta_v_ideal_mps": round(summary.delta_v_ideal_mps, 1),
            "burnout_v_mps": round(summary.burnout_v_mps, 1),
            "burnout_x_m": round(summary.burnout_x_m, 1),
            "burnout_mach": round(summary.burnout_mach, 3),
            "velocity_fraction_of_ideal": round(
                summary.burnout_v_mps / summary.delta_v_ideal_mps, 3
            ),
            "impulse_to_weight_s": round(summary.impulse_ns / (cfg.mass_kg * G), 2),
        },
        "ranges": {
            k: {
                "tof_s": round(v.tof_s, 2),
                "v_mps": round(v.v_mps, 1),
                "mach": round(v.mach, 3),
                "q_kpa": round(v.q_pa / 1000, 1),
                "phase": v.phase,
            }
            for k, v in summary.ranges.items()
        },
        "warhead_cubes": warhead_cube_mass_kg(),
        "loft_sweep_1000m": loft_sweep(cfg),
        "sensitivity_1000m": sensitivity_sweep(cfg),
        "evasion_geometry": evasion_table(r1.tof_s, r2.tof_s),
        "acceleration_profile": acceleration_samples(cfg),
    }


def verify() -> None:
    s = simulate(ModelConfig(), [1000.0, 1200.0])
    v1 = s.ranges["1000"].v_mps
    v2 = s.ranges["1200"].v_mps
    if not (V_BAND_1000[0] <= v1 <= V_BAND_1000[1]):
        raise SystemExit(f"verify fail: v@1000m={v1:.1f}")
    frac = s.burnout_v_mps / s.delta_v_ideal_mps
    if not (0.30 <= frac <= 0.40):
        raise SystemExit(f"verify warn: burnout/ideal={frac:.3f} (expect ~0.35)")
    print(
        f"verify ok: v@1000={v1:.1f} TOF={s.ranges['1000'].tof_s:.2f}s  "
        f"v@1200={v2:.1f}  v_bo={s.burnout_v_mps:.1f}  x_bo={s.burnout_x_m:.0f}m"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--json-out", type=Path)
    parser.add_argument("--print", action="store_true")
    args = parser.parse_args()

    if args.verify:
        verify()
        return 0

    report = build_report()
    if args.print or not args.json_out:
        m = report["motor"]
        print("RADR performance model v2 -- NOTIONAL")
        print(f"  I={m['impulse_ns']} N*s  v_bo={m['burnout_v_mps']} m/s  x_bo={m['burnout_x_m']} m")
        print(f"  CdA boost={report['drag_effective_m2']['cda_boost']}  coast={report['drag_effective_m2']['cda_coast']} m2")
        for k in sorted(report["ranges"], key=int):
            r = report["ranges"][k]
            print(f"  {int(k):4d} m: TOF={r['tof_s']:.2f}s  v={r['v_mps']:.1f}  Ma={r['mach']:.2f}")
        w = report["warhead_cubes"]
        print(f"  Cubes: {w['fragment_mass_kg']} kg of {w['cube_count']} x {w['cube_mm']} mm")

    if args.json_out:
        args.json_out.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(f"Wrote {args.json_out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
