# RunPod + Jupyter — RADR mk.60

Your **4090** pod is fine for **preloaded Jupyter** even though RADR ballistics are **CPU math**. Use the GPU pod as a fast remote workstation, not because the rocket model needs CUDA.

## 1. Start pod → open Jupyter

Use the template that includes **Jupyter Lab**. Open the web URL RunPod gives you.

## 2. Terminal in Jupyter (or SSH)

```bash
git clone https://github.com/FratresMedAI/RADR-mk.60.git
cd RADR-mk.60
pip install -r requirements-modeling.txt
python scripts/radr_performance_model.py --verify
python scripts/radr_performance_model.py --json-out data/performance_model_output.json
python scripts/mass_cg_calc.py
jupyter lab notebooks/ --ip=0.0.0.0 --port=8888 --no-browser
```

(If Jupyter is already running on the pod, skip the last line and open `notebooks/RADR_Performance_Dashboard.ipynb` from the file browser.)

## 3. In the notebook

1. Set **`N_MC = 5000`** (or higher) in the Monte Carlo cell.  
2. **Kernel → Restart & Run All**.  
3. **File → Export** plots or save notebook as PDF for pitch deck.

## 4. Do not expect GPU speedup

`radr_performance_model.py` and the notebook use **NumPy on CPU**. That is correct. Optional later: JAX/CuPy for huge MC — not required for v1 wow.

## 5. Wow checklist for meetings

- [ ] `performance_model_output.json` regenerated on pod  
- [ ] Dashboard notebook all cells green  
- [ ] Three exports: `range_envelope.png`, `sensitivity_1000m.png`, `monte_carlo_v1000.png`  
- [ ] Annex I numbers match notebook title card  
