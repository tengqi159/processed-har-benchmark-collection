# Data Format

This document defines the public format for the ready-to-use preprocessed HAR dataset release.

## Repository Layout

```text
datasets/{dataset_slug}/*.npy
archives/*.zip
metadata/datasets.yaml
metadata/manifest.csv
```

The current partial release uses these folder slugs:

- `uci`
- `unimib`
- `pamap2`
- `wisdm`
- `oppo`
- `WSBHA`

The planned full release can add more folders such as `usc_had`, `flaap`, `hapt`, `mhealth`, and `dsads`.

## NumPy Array Convention

Each sample array is already windowed and split. Most feature tensors follow:

```text
num_windows x timesteps x channels
```

The exact shape and dtype of every uploaded file are listed in:

```text
metadata/partial_upload_2026-05-14_manifest.csv
```

For example:

```python
from huggingface_hub import hf_hub_download
import numpy as np

x_path = hf_hub_download(
    repo_id="shenjianmozhu/preprocessed-har-datasets",
    repo_type="dataset",
    filename="datasets/uci/x_train.npy",
)
X = np.load(x_path)
print(X.shape)
```

## Recommended Standard Names

When adding new processed datasets, prefer one of these patterns:

- `x_train.npy`, `y_train.npy`, `x_test.npy`, `y_test.npy`
- `training_data.npy`, `training_labels.npy`, `testing_data.npy`, `testing_labels.npy`

If a dataset has validation files, use explicit names such as `x_val.npy` and `y_val.npy`.

## Manifest

`metadata/*manifest.csv` should include one row per released file:

```text
relative_path,dataset_dir,file_name,shape,dtype,size_bytes
```

The manifest should be regenerated after every data change.
