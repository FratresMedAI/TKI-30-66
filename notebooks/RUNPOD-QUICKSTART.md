# RunPod — max CPU (your 4090 pod)

| Resource | Your pod | Used by RADR |
|----------|----------|--------------|
| GPU | RTX 4090 ×1 | **Not used** for ballistics (Jupyter only) |
| vCPU | **32** | **Monte Carlo** — use `--workers 32` |
| RAM | 125 GB | Plenty |
| Disk | 20 GB | Repo + pip fits easily |

## One-command max CPU (recommended)

Terminal on the pod:

```bash
git clone https://github.com/FratresMedAI/RADR-mk.60.git
cd RADR-mk.60
chmod +x scripts/runpod_max_cpu.sh
./scripts/runpod_max_cpu.sh
```

Defaults: **25,000** Monte Carlo samples · **32** workers · 4 PNGs in `notebooks/output/`.

### Tune without editing files

```bash
N_MC=50000 WORKERS=32 ./scripts/runpod_max_cpu.sh
```

## Why `OMP_NUM_THREADS=1`

Each worker is a separate process. If NumPy also spawns 32 threads *per* worker, you oversubscribe and slow down. The script sets **1 thread per process × 32 processes = 32 cores**.

## Manual steps (Jupyter pod)

```bash
export OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
git clone https://github.com/FratresMedAI/RADR-mk.60.git
cd RADR-mk.60
pip install -r requirements-modeling.txt
python scripts/run_light_dashboard.py --runpod-max
```

Or Monte Carlo only:

```bash
python scripts/monte_carlo_envelope.py --runpod-max --json-out data/monte_carlo_25000.json
```

## Jupyter notebook

Open `notebooks/RADR_Performance_Dashboard.ipynb` and set:

```python
N_MC = 25000
WORKERS = 32  # add parallel cell — or use runpod_max_cpu.sh instead (faster)
```

For max CPU, **prefer `runpod_max_cpu.sh`** over the notebook loop (parallel map).

## 20 GB disk tips

- `pip install -r requirements-modeling.txt` only (~numpy, matplotlib, jupyter if needed).
- Skip Conda mega-stacks.
- Download `notebooks/output/*.png` to your PC when done.

## Wow checklist

- [ ] `./scripts/runpod_max_cpu.sh` completes  
- [ ] `monte_carlo_25000.json` — **fraction_in_330_350_band** high  
- [ ] Four PNGs in `notebooks/output/`  
- [ ] Optional: zip and download folder before stopping pod  
