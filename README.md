# Processed HAR Benchmark Collection

This repository is the public documentation and release companion for a collection of preprocessed Human Activity Recognition (HAR) benchmark datasets. The actual data files should be hosted in a Hugging Face Dataset repository, while this GitHub repository keeps the documentation, citation metadata, preprocessing notes, and download instructions lightweight and stable.

## Release Links

- Hugging Face Dataset: to be published as `processed-har-benchmark-collection`
- GitHub documentation: this repository
- Archival DOI: pending Zenodo release
- Optional mirror: not configured

## What Is Included

The release provides fixed-window, model-ready versions of eight public HAR benchmarks. Each subset is distributed with consistent train/test split files, labels, and metadata so that researchers can compare HAR models under the same preprocessing and split protocol.

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

Use Hugging Face for the data files:

```python
from datasets import load_dataset

uci = load_dataset("shenjianmozhu/processed-har-benchmark-collection", "uci_har")
print(uci["train"][0].keys())
```

For deep-learning pipelines that prefer array files, download the release snapshot:

```python
from huggingface_hub import snapshot_download

local_dir = snapshot_download(
    repo_id="shenjianmozhu/processed-har-benchmark-collection",
    repo_type="dataset",
    local_dir="har-benchmark-processed",
)
print(local_dir)
```

## Data Layout

The Hugging Face Dataset repository should use this structure:

```text
README.md
data/
  uci_har/
    train.parquet
    test.parquet
  unimib_shar/
    train.parquet
    test.parquet
  usc_had/
    train.parquet
    test.parquet
  flaap/
    train.parquet
    test.parquet
  hapt/
    train.parquet
    test.parquet
  mhealth/
    train.parquet
    test.parquet
  dsads/
    train.parquet
    test.parquet
  pamap2/
    train.parquet
    test.parquet
arrays/
  uci_har.npz
  unimib_shar.npz
  usc_had.npz
  flaap.npz
  hapt.npz
  mhealth.npz
  dsads.npz
  pamap2.npz
metadata/
  datasets.yaml
  manifest.csv
```

Each Parquet row represents one preprocessed window. The recommended fields are:

- `id`: stable window id
- `dataset`: dataset slug
- `split`: `train`, `validation`, or `test`
- `signal`: flattened sensor window values
- `channels`: number of sensor channels
- `timesteps`: window length
- `layout`: array interpretation, e.g. `channels_first`
- `label`: integer class id
- `label_name`: class name when available
- `subject`: subject id when redistribution terms permit release

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

If you use this processed collection, cite both this release and the original dataset papers:

```bibtex
@misc{har_processed_benchmark_collection_2026,
  title        = {Processed HAR Benchmark Collection},
  author       = {Qi Teng and collaborators},
  year         = {2026},
  howpublished = {\url{https://huggingface.co/datasets/shenjianmozhu/processed-har-benchmark-collection}},
  note         = {Version v0.1.0}
}
```

Original dataset citations are listed in [metadata/datasets.yaml](metadata/datasets.yaml).

## Maintainers

- Qi Teng and collaborators. Please use GitHub issues for release questions.
