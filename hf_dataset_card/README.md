---
pretty_name: "ReadyHAR: Ready-to-Use HAR Datasets"
license: other
task_categories:
- time-series-classification
tags:
- preprocessed
- ready-to-use
- human-activity-recognition
- har
- wearable-sensors
- smartphone-sensing
- imu
- accelerometer
- gyroscope
- timeseries
- benchmark
- tabular
---

# ReadyHAR: Ready-to-Use HAR Datasets

This dataset repository provides **ready-to-use, preprocessed Human Activity Recognition (HAR) datasets**. The released files are already cleaned, windowed, split, and stored as NumPy arrays, so users can download them and run model comparisons directly.

The goal is to make HAR model comparison easier by releasing a consistent set of preprocessed windows, split files, labels, and metadata. The collection covers smartphone-based sensing, wearable IMU sensing, daily activities, fall-related motions, and multimodal wearable settings under different sensor layouts and label granularities.

## Current Dataset Folders

The browsable download layout is:

```text
datasets/
  uci/
  unimib/
  pamap2/
  wisdm/
  oppo/
  WSBHA/
archives/
  processed_har_npy_partial_2026-05-14.zip
metadata/
  partial_upload_2026-05-14_manifest.csv
```

The `datasets/` folders are intended for direct per-dataset downloads. The `archives/` zip is a convenient one-file mirror of the current uploaded batch.

## Quick Download

```python
from huggingface_hub import hf_hub_download, snapshot_download
import numpy as np

x_train_path = hf_hub_download(
    repo_id="shenjianmozhu/preprocessed-har-datasets",
    repo_type="dataset",
    filename="datasets/uci/x_train.npy",
)
y_train_path = hf_hub_download(
    repo_id="shenjianmozhu/preprocessed-har-datasets",
    repo_type="dataset",
    filename="datasets/uci/y_train.npy",
)

X_train = np.load(x_train_path)
y_train = np.load(y_train_path)
print(X_train.shape, y_train.shape)
```

To download everything:

```python
local_dir = snapshot_download(
    repo_id="shenjianmozhu/preprocessed-har-datasets",
    repo_type="dataset",
    local_dir="preprocessed-har-datasets",
)
```

## Dataset Notes

| Folder | Main files | Notes |
| --- | --- | --- |
| `datasets/uci` | `x_train.npy`, `y_train.npy`, `x_test.npy`, `y_test.npy` | UCI-HAR-style train/test arrays. |
| `datasets/unimib` | `training_data.npy`, `training_labels.npy`, `testing_data.npy`, `testing_labels.npy` | UniMiB-style preprocessed arrays. |
| `datasets/pamap2` | `train_X_new.npy`, `train_y_new.npy`, `total_pamap2_valtestx.npy`, `total_pamap2_valtesty.npy` | Train plus validation/test batch. |
| `datasets/wisdm` | `x_train.npy`, `y_train.npy`, `x_test.npy`, `y_test.npy` | WISDM-style preprocessed arrays. |
| `datasets/oppo` | `data_train_one.npy`, `label_train_onehot.npy`, `data_test_one.npy`, `label_test_onehot.npy` | OPPORTUNITY-style arrays with one-hot labels. |
| `datasets/WSBHA` | `training_data.npy`, `training_labels.npy`, `testing_data.npy`, `testing_labels.npy` | Current uploaded WSBHA folder, preserved as provided. |

File-level shapes and dtypes are listed in `metadata/partial_upload_2026-05-14_manifest.csv`.

## Google Drive Mirror

A Google Drive mirror is available for users who prefer browser-based downloads:

https://drive.google.com/drive/folders/1Qe8AQ8S2V4_uBIvC3Pv4WRmv-EPWERjG?usp=drive_link

Hugging Face remains the canonical dataset host for versioned files and programmatic downloads.

## Citation

There is no standalone dataset paper or DOI for this collection yet. Please do not cite an unpublished data-release entry.

If you use these processed files, cite the original dataset paper for each subset you use and cite the relevant Qi Teng HAR papers listed in the GitHub citation file:

https://github.com/tengqi159/ready-to-use-har-datasets/blob/main/docs/citation.md

## Licensing

This repository contains processed versions of public datasets. The original datasets retain their own licenses, citation requirements, and redistribution terms. The `license: other` metadata is intentional because the collection is license-mixed. Users must comply with the terms of each original dataset.

If any source dataset does not permit redistribution of derived/preprocessed files, the corresponding processed files should be removed from this Hugging Face repository and replaced by preprocessing scripts plus links to the original source.

## Responsible Use

The data are intended for research on HAR, time-series classification, wearable sensing, and benchmark reproducibility. Users should avoid using the data for identity inference, health-status inference, or surveillance applications beyond the scope of the original datasets and consent protocols.
