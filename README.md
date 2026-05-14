# ReadyHAR: Ready-to-Use HAR Datasets

ReadyHAR provides preprocessed Human Activity Recognition (HAR) datasets for direct benchmarking. The files are already cleaned, windowed, split, and saved as NumPy arrays, so users can start from train/test tensors instead of repeating raw sensor preprocessing.

## Download

- Primary data host: https://huggingface.co/datasets/shenjianmozhu/preprocessed-har-datasets
- Google Drive mirror: https://drive.google.com/drive/folders/1Qe8AQ8S2V4_uBIvC3Pv4WRmv-EPWERjG?usp=drive_link
- GitHub documentation: https://github.com/tengqi159/ready-to-use-har-datasets
- Latest GitHub release: https://github.com/tengqi159/ready-to-use-har-datasets/releases/latest

## Current Dataset Folders

The current public upload is organized as independent folders under `datasets/`.

| Folder | Main files |
| --- | --- |
| `datasets/uci` | `x_train.npy`, `y_train.npy`, `x_test.npy`, `y_test.npy` |
| `datasets/unimib` | `training_data.npy`, `training_labels.npy`, `testing_data.npy`, `testing_labels.npy` |
| `datasets/pamap2` | `train_X_new.npy`, `train_y_new.npy`, `total_pamap2_valtestx.npy`, `total_pamap2_valtesty.npy` |
| `datasets/wisdm` | `x_train.npy`, `y_train.npy`, `x_test.npy`, `y_test.npy` |
| `datasets/oppo` | `data_train_one.npy`, `label_train_onehot.npy`, `data_test_one.npy`, `label_test_onehot.npy` |
| `datasets/WSBHA` | `training_data.npy`, `training_labels.npy`, `testing_data.npy`, `testing_labels.npy` |

The paper-aligned benchmark metadata also tracks UCI-HAR, UniMiB-SHAR, USC-HAD, FLAAP, HAPT, mHealth, DSADS, and PAMAP2. See [metadata/datasets.yaml](metadata/datasets.yaml) for details.

## Quick Load

```python
from huggingface_hub import hf_hub_download
import numpy as np

x_train_path = hf_hub_download(
    repo_id="shenjianmozhu/preprocessed-har-datasets",
    repo_type="dataset",
    filename="datasets/uci/x_train.npy",
)

x_train = np.load(x_train_path)
print(x_train.shape)
```

## Citation

There is no standalone dataset paper or DOI for this collection yet. Please do not cite an unpublished data-release entry.

If you use these processed files, cite:

1. the original public dataset paper for each subset you use;
2. the relevant Qi Teng HAR papers listed in [docs/citation.md](docs/citation.md);
3. this GitHub/Hugging Face URL only as a repository link in your data-availability statement.

For a short default HAR citation set, start with:

- Teng et al., *Innovative Dual-Decoupling CNN With Layer-Wise Temporal-Spatial Attention for Sensor-Based Human Activity Recognition*, IEEE JBHI, 2025.
- Teng et al., *Large Receptive Field Attention: An Innovation in Decomposing Large-Kernel Convolution for Sensor-Based Activity Recognition*, IEEE Sensors Journal, 2024.
- Teng et al., *RepHAR: Decoupling Networks With Accuracy-Speed Tradeoff for Sensor-Based Human Activity Recognition*, IEEE TIM, 2023.

## Licensing

These files are derived from public HAR datasets. Each original dataset keeps its own license, citation requirements, and redistribution terms. If a source dataset does not allow redistribution of processed files, publish only the preprocessing script and source-data instructions for that subset.
