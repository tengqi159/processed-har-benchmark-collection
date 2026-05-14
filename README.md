# Ready-to-Use Preprocessed HAR Datasets

This repository is the public documentation and release companion for a set of **ready-to-use, preprocessed Human Activity Recognition (HAR) datasets**. The goal is simple: researchers should be able to download fixed-window train/test arrays and run HAR models directly, without repeating raw-data cleaning, windowing, splitting, or label formatting.

The large data files are hosted on Hugging Face Dataset and mirrored on Google Drive when available. GitHub stays lightweight and keeps the landing page, citation metadata, file layout, and reproducibility notes.

## Release Links

- Hugging Face Dataset: https://huggingface.co/datasets/shenjianmozhu/preprocessed-har-datasets
- GitHub documentation: https://github.com/tengqi159/preprocessed-har-datasets
- GitHub latest release: https://github.com/tengqi159/preprocessed-har-datasets/releases/latest
- Google Drive mirror: pending public share link
- Archival DOI: pending Zenodo release

## What Is Included

The planned release covers fixed-window, model-ready versions of eight public HAR benchmarks. The current partial upload contains NumPy arrays for `WSBHA`, `unimib`, `pamap2`, `wisdm`, `oppo`, and `uci`; additional subsets can be added under the same `datasets/<dataset>/` layout.

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

## Recommended Access

Use Hugging Face for the primary data files. To download one file:

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

## Data Layout

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

## What Is Not Included in GitHub

Do not commit large data files to this repository. GitHub should only host:

- documentation
- metadata
- preprocessing and conversion scripts
- checksums or manifests
- small examples, if needed

The actual dataset files belong in the Hugging Face Dataset repo and, for archival citation, a Zenodo record.

## Licensing and Redistribution

This collection is derived from public datasets created by their original authors. The original datasets retain their own licenses, citation requirements, and redistribution terms. Before uploading processed files, verify that each source permits redistribution of derived/preprocessed data. If a dataset does not clearly permit redistribution, publish only the preprocessing code, metadata, and instructions for users to obtain the raw data from the original source.

See [docs/license_and_redistribution_checklist.md](docs/license_and_redistribution_checklist.md).

## Citation

If you use this processed collection, cite both this data release and the original dataset papers:

```bibtex
@misc{teng_preprocessed_har_datasets_2026,
  title        = {Ready-to-Use Preprocessed HAR Datasets},
  author       = {Teng, Qi and collaborators},
  year         = {2026},
  howpublished = {\url{https://huggingface.co/datasets/shenjianmozhu/preprocessed-har-datasets}},
  note         = {Preprocessed fixed-window NumPy arrays for HAR benchmarking}
}
```

Original dataset citations are listed in [metadata/datasets.yaml](metadata/datasets.yaml). Related HAR method papers from the maintainer's publication line are listed in [docs/citation.md](docs/citation.md).

## Maintainers

- Qi Teng and collaborators. Please use GitHub issues for release questions.
