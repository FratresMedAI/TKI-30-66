# RADR Jupyter (RunPod / local)

**Start here on RunPod:** [`RUNPOD-QUICKSTART.md`](RUNPOD-QUICKSTART.md)

| Notebook | Purpose |
|----------|---------|
| [`RADR_Performance_Dashboard.ipynb`](RADR_Performance_Dashboard.ipynb) | Trajectory, sensitivity, Monte Carlo envelope, pitch charts |

**Laptop:** run `N_MC = 200` in the notebook. **4090 pod:** safe to raise to `2000–10000` (still CPU-bound math; GPU not required).

```bash
cd TKI-30-66
pip install -r requirements-modeling.txt
python scripts/radr_performance_model.py --json-out data/performance_model_output.json
jupyter lab notebooks/
```
