# RADR Jupyter (RunPod / local)

**Start here on RunPod:** [`RUNPOD-QUICKSTART.md`](RUNPOD-QUICKSTART.md)

| Notebook | Purpose |
|----------|---------|
| [`RADR_Performance_Dashboard.ipynb`](RADR_Performance_Dashboard.ipynb) | Trajectory, sensitivity, Monte Carlo envelope, pitch charts |

**Laptop:** `python scripts/run_light_dashboard.py` (n=200). **RunPod 32 vCPU:** `./scripts/runpod_max_cpu.sh` (n=25000, workers=32).

```bash
cd TKI-30-66
pip install -r requirements-modeling.txt
python scripts/radr_performance_model.py --json-out data/performance_model_output.json
jupyter lab notebooks/
```
