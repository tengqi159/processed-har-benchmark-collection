# Processed HAR Benchmark Collection

This page is a lightweight GitHub Pages landing page for the processed HAR benchmark release.

## Download

- Primary dataset host: `https://huggingface.co/datasets/tengqi159/processed-har-benchmark-collection`
- Documentation and scripts: `https://github.com/tengqi159/processed-har-benchmark-collection`
- Versioned DOI archive: pending Zenodo release

## Benchmarks

The collection contains processed windows for UCI-HAR, UniMiB-SHAR, USC-HAD, FLAAP, HAPT, mHealth, DSADS, and PAMAP2. These benchmarks cover smartphone sensing, wearable IMU sensing, daily activities, postural transitions, fall-related motions, and sports-style activities.

## Quick Start

```python
from datasets import load_dataset

ds = load_dataset("tengqi159/processed-har-benchmark-collection", "uci_har")
print(ds)
```

## Citation

Please cite both this processed release and the original dataset papers.
