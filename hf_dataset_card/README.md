---
pretty_name: Processed HAR Benchmark Collection
license: other
task_categories:
- time-series-classification
tags:
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
configs:
- config_name: uci_har
  data_files:
  - split: train
    path: data/uci_har/train.parquet
  - split: test
    path: data/uci_har/test.parquet
- config_name: unimib_shar
  data_files:
  - split: train
    path: data/unimib_shar/train.parquet
  - split: test
    path: data/unimib_shar/test.parquet
- config_name: usc_had
  data_files:
  - split: train
    path: data/usc_had/train.parquet
  - split: test
    path: data/usc_had/test.parquet
- config_name: flaap
  data_files:
  - split: train
    path: data/flaap/train.parquet
  - split: test
    path: data/flaap/test.parquet
- config_name: hapt
  data_files:
  - split: train
    path: data/hapt/train.parquet
  - split: test
    path: data/hapt/test.parquet
- config_name: mhealth
  data_files:
  - split: train
    path: data/mhealth/train.parquet
  - split: test
    path: data/mhealth/test.parquet
- config_name: dsads
  data_files:
  - split: train
    path: data/dsads/train.parquet
  - split: test
    path: data/dsads/test.parquet
- config_name: pamap2
  data_files:
  - split: train
    path: data/pamap2/train.parquet
  - split: test
    path: data/pamap2/test.parquet
---

# Processed HAR Benchmark Collection

This dataset repository provides model-ready, fixed-window versions of eight public Human Activity Recognition (HAR) benchmarks: UCI-HAR, UniMiB-SHAR, USC-HAD, FLAAP, HAPT, mHealth, DSADS, and PAMAP2.

The goal is to make HAR model comparison easier by releasing a consistent set of preprocessed windows, split files, labels, and metadata. The collection covers smartphone-based sensing, wearable IMU sensing, daily activities, postural transitions, fall-related motions, and sports-style activities under different sensor layouts and label granularities.

## Dataset Subsets

| Config | Dataset | Sensing Setting | Classes | Channels | Timesteps | Sampling Rate |
| --- | --- | --- | ---: | ---: | ---: | --- |
| `uci_har` | UCI-HAR | Waist-mounted smartphone accelerometer and gyroscope | 6 | 9 | 128 | 50 Hz |
| `unimib_shar` | UniMiB-SHAR | Trouser-pocket smartphone accelerometer | 17 | 3 | 151 | 50 Hz |
| `usc_had` | USC-HAD | MotionNode at the front right hip | 12 | 6 | 512 | 100 Hz |
| `flaap` | FLAAP | Waist-mounted smartphone accelerometer and gyroscope | 10 | 6 | 100 | 100 Hz |
| `hapt` | HAPT | Waist-mounted smartphone accelerometer and gyroscope | 12 | 6 | 128 | 50 Hz |
| `mhealth` | mHealth | Body-worn sensors on chest, right wrist, and left ankle | 12 | 12 | 128 | 50 Hz |
| `dsads` | DSADS | Five wearable inertial units on torso, arms, and legs | 19 | 45 | 125 | 25 Hz |
| `pamap2` | PAMAP2 | IMUs on hand, chest, and ankle plus heart-rate sensing | 12 | 40 | 171 | 100 Hz |

## Usage

```python
from datasets import load_dataset

ds = load_dataset("tengqi159/processed-har-benchmark-collection", "uci_har")
train = ds["train"]
example = train[0]

signal = example["signal"]
channels = example["channels"]
timesteps = example["timesteps"]
label = example["label"]
```

The `signal` field stores a flattened window. Reshape it according to `layout`:

```python
import numpy as np

def restore_window(row):
    x = np.asarray(row["signal"], dtype="float32")
    if row["layout"] == "channels_first":
        return x.reshape(row["channels"], row["timesteps"])
    if row["layout"] == "timesteps_first":
        return x.reshape(row["timesteps"], row["channels"])
    raise ValueError(f"Unknown layout: {row['layout']}")
```

If you prefer NumPy archives:

```python
from huggingface_hub import hf_hub_download
import numpy as np

path = hf_hub_download(
    repo_id="tengqi159/processed-har-benchmark-collection",
    repo_type="dataset",
    filename="arrays/uci_har.npz",
)
arr = np.load(path)
print(arr.files)
```

## Data Fields

- `id`: stable sample identifier
- `dataset`: subset slug
- `split`: split name
- `signal`: flattened sensor window
- `channels`: number of sensor channels
- `timesteps`: number of time steps
- `layout`: `channels_first` or `timesteps_first`
- `label`: integer label
- `label_name`: human-readable label, when available
- `subject`: subject identifier, when redistribution terms permit release

## Licensing

This repository contains processed versions of public datasets. The original datasets retain their own licenses, citation requirements, and redistribution terms. The `license: other` metadata is intentional because the collection is license-mixed. Users must comply with the terms of each original dataset.

If any source dataset does not permit redistribution of derived/preprocessed files, the corresponding processed files should be removed from this Hugging Face repository and replaced by preprocessing scripts plus links to the original source.

## Citation

Please cite this processed collection and the original datasets used in your work.

```bibtex
@misc{har_processed_benchmark_collection_2026,
  title        = {Processed HAR Benchmark Collection},
  author       = {Qi Teng and collaborators},
  year         = {2026},
  howpublished = {\url{https://huggingface.co/datasets/tengqi159/processed-har-benchmark-collection}},
  note         = {Version v0.1.0}
}
```

Original dataset citation keys: `anguita2013public`, `micucci2017unimib`, `zhang2012usc`, `kumar2022flaap`, `reyes2016transition`, `banos2014mhealth`, `altun2010comparative`, and `reiss2012creating`.

## Responsible Use

The data are intended for research on HAR, time-series classification, wearable sensing, and benchmark reproducibility. Users should avoid using the data for identity inference, health-status inference, or surveillance applications beyond the scope of the original datasets and consent protocols.
