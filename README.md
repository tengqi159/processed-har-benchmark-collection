# Ready-to-Use Preprocessed HAR Datasets

This repository is the public landing page for **ready-to-use, preprocessed Human Activity Recognition (HAR) datasets**. The data files are already cleaned, windowed, split, and stored as model-ready NumPy arrays, so users can download a dataset folder and run HAR model comparisons directly.

GitHub keeps the release documentation, citation metadata, file layout, and reproducibility notes. Large dataset files are hosted on Hugging Face and mirrored on Google Drive.

## Download

| Route | Use it for | Link |
| --- | --- | --- |
| Hugging Face Dataset | Primary host, versioned files, scriptable downloads | https://huggingface.co/datasets/shenjianmozhu/preprocessed-har-datasets |
| Google Drive Mirror | Browser-based backup download | https://drive.google.com/drive/folders/1Qe8AQ8S2V4_uBIvC3Pv4WRmv-EPWERjG?usp=drive_link |
| GitHub | Documentation, citation, metadata, release notes | https://github.com/tengqi159/preprocessed-har-datasets |
| Latest GitHub Release | Version snapshot of this documentation package | https://github.com/tengqi159/preprocessed-har-datasets/releases/latest |

An archival DOI can be added after the full public release is frozen on Zenodo.

## Current Upload

The current public batch is organized under `datasets/<dataset>/` so each dataset can be downloaded independently.

| Folder | Main files | Notes |
| --- | --- | --- |
| `datasets/uci` | `x_train.npy`, `y_train.npy`, `x_test.npy`, `y_test.npy` | UCI-HAR-style train/test arrays. |
| `datasets/unimib` | `training_data.npy`, `training_labels.npy`, `testing_data.npy`, `testing_labels.npy` | UniMiB-style preprocessed arrays. |
| `datasets/pamap2` | `train_X_new.npy`, `train_y_new.npy`, `total_pamap2_valtestx.npy`, `total_pamap2_valtesty.npy` | Train plus validation/test batch. |
| `datasets/wisdm` | `x_train.npy`, `y_train.npy`, `x_test.npy`, `y_test.npy` | WISDM-style preprocessed arrays. |
| `datasets/oppo` | `data_train_one.npy`, `label_train_onehot.npy`, `data_test_one.npy`, `label_test_onehot.npy` | OPPORTUNITY-style arrays with one-hot labels. |
| `datasets/WSBHA` | `training_data.npy`, `training_labels.npy`, `testing_data.npy`, `testing_labels.npy` | Preserved with the uploaded folder name. |

File-level shapes, dtypes, and checksums are recorded in the manifest when available.

## Paper-Aligned Benchmark Set

The broader benchmark documentation tracks eight widely used public HAR datasets. Some of these are planned or metadata-only until redistribution terms and processed files are finalized.

| Dataset | Samples | Classes | Channels | Timesteps | Sampling Rate | Window Overlap | Split |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| UCI-HAR | 10,299 | 6 | 9 | 128 | 50 Hz | 50% | 70%/30% |
| UniMiB-SHAR | 11,771 | 17 | 3 | 151 | 50 Hz | 50% | 70%/30% |
| USC-HAD | 9,873 | 12 | 6 | 512 | 100 Hz | 50% | 70%/30% |
| FLAAP | 13,123 | 10 | 6 | 100 | 100 Hz | 0% | 80%/20% |
| HAPT | 10,908 | 12 | 6 | 128 | 50 Hz | 50% | 70%/30% |
| mHealth | 4,818 | 12 | 12 | 128 | 50 Hz | 50% | 80%/20% |
| DSADS | 9,113 | 19 | 45 | 125 | 25 Hz | 0% | 75%/25% |
| PAMAP2 | 7,616 | 12 | 40 | 171 | 100 Hz | 78% | 80%/20% |

## Quick Start

Use Hugging Face for programmatic downloads. To download one file:

```python
from huggingface_hub import hf_hub_download

x_train = hf_hub_download(
    repo_id="shenjianmozhu/preprocessed-har-datasets",
    repo_type="dataset",
    filename="datasets/uci/x_train.npy",
)
```

To download the full Hugging Face snapshot:

```python
from huggingface_hub import snapshot_download

local_dir = snapshot_download(
    repo_id="shenjianmozhu/preprocessed-har-datasets",
    repo_type="dataset",
    local_dir="preprocessed-har-datasets",
)
print(local_dir)
```

Google Drive can be used as a one-click mirror when users prefer browser downloads.

## Repository Layout

The Hugging Face Dataset repository uses a direct, dataset-first layout:

```text
README.md
datasets/
  uci/
    x_train.npy
    y_train.npy
    x_test.npy
    y_test.npy
  unimib/
    training_data.npy
    training_labels.npy
    testing_data.npy
    testing_labels.npy
  pamap2/
    train_X_new.npy
    train_y_new.npy
    total_pamap2_valtestx.npy
    total_pamap2_valtesty.npy
  wisdm/
    x_train.npy
    y_train.npy
    x_test.npy
    y_test.npy
  oppo/
    data_train_one.npy
    label_train_onehot.npy
    data_test_one.npy
    label_test_onehot.npy
  WSBHA/
    training_data.npy
    training_labels.npy
    testing_data.npy
    testing_labels.npy
archives/
  processed_har_npy_partial_2026-05-14.zip
metadata/
  partial_upload_2026-05-14_manifest.csv
  datasets.yaml
```

See [docs/data_format.md](docs/data_format.md) for the full format contract.
For the step-by-step publication workflow, see [docs/release_checklist_zh.md](docs/release_checklist_zh.md).

## GitHub Scope

Do not commit large data files to this repository. GitHub should only host:

- documentation
- metadata
- preprocessing and conversion scripts
- checksums or manifests
- small examples, if needed

The actual dataset files belong in the Hugging Face Dataset repo and the Google Drive mirror. A frozen archival copy can later be attached to a Zenodo record.

## Licensing and Redistribution

This collection is derived from public datasets created by their original authors. The original datasets retain their own licenses, citation requirements, and redistribution terms. Before uploading processed files, verify that each source permits redistribution of derived/preprocessed data. If a dataset does not clearly permit redistribution, publish only the preprocessing code, metadata, and instructions for users to obtain the raw data from the original source.

See [docs/license_and_redistribution_checklist.md](docs/license_and_redistribution_checklist.md).

## Citation

If you use this processed collection, cite this data release, the original dataset papers for the subsets you use, and relevant HAR method papers from the maintainer's publication line.

```bibtex
@misc{teng_preprocessed_har_datasets_2026,
  title        = {Ready-to-Use Preprocessed HAR Datasets},
  author       = {Teng, Qi and collaborators},
  year         = {2026},
  howpublished = {\url{https://huggingface.co/datasets/shenjianmozhu/preprocessed-har-datasets}},
  note         = {Preprocessed fixed-window NumPy arrays for HAR benchmarking}
}
```

Original dataset citations are listed in [metadata/datasets.yaml](metadata/datasets.yaml). Selected related HAR papers, including recent and earlier Qi Teng HAR work, are listed in [docs/citation.md](docs/citation.md).

## Maintainers

- Qi Teng and collaborators. Please use GitHub issues for release questions.
