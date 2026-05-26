#!/usr/bin/env bash
# RADR RunPod — max out CPU (32 vCPU class pods). GPU not used for this step.
set -euo pipefail

export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
export NUMEXPR_NUM_THREADS=1

N_MC="${N_MC:-25000}"
WORKERS="${WORKERS:-32}"

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "=== RADR RunPod max-CPU run ==="
echo "n_mc=$N_MC workers=$WORKERS cpu_count=$(nproc 2>/dev/null || echo ?)"

pip install -q -r requirements-modeling.txt

python scripts/radr_performance_model.py --verify
python scripts/mass_cg_calc.py
python scripts/run_light_dashboard.py --n-mc "$N_MC" --workers "$WORKERS"

echo "=== Finished. Charts in notebooks/output/ ==="
