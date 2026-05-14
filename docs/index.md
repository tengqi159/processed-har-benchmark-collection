# Ready-to-Use Preprocessed HAR Datasets

This page is a lightweight GitHub Pages landing page for ready-to-use, preprocessed Human Activity Recognition (HAR) datasets.

## Download

- Primary dataset host: `https://huggingface.co/datasets/shenjianmozhu/preprocessed-har-datasets`
- Documentation and scripts: `https://github.com/tengqi159/preprocessed-har-datasets`
- Google Drive mirror: pending public share link
- Versioned DOI archive: pending Zenodo release

## Benchmarks

The planned collection contains processed windows for UCI-HAR, UniMiB-SHAR, USC-HAD, FLAAP, HAPT, mHealth, DSADS, and PAMAP2. The current partial data upload contains browsable NumPy folders under `datasets/` for `uci`, `unimib`, `pamap2`, `wisdm`, `oppo`, and `WSBHA`.

## Quick Start

```python
from huggingface_hub import hf_hub_download

path = hf_hub_download(
    repo_id="shenjianmozhu/preprocessed-har-datasets",
    repo_type="dataset",
    filename="datasets/uci/x_train.npy",
)
print(path)
```

## Citation

Please cite this processed data release, the original dataset papers, and relevant HAR method papers listed in `docs/citation.md`.
