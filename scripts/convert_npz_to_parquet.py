#!/usr/bin/env python3
"""Convert processed HAR NumPy arrays into the public Parquet/NPZ layout.

Expected input layout:

input_root/
  uci_har/
    X_train.npy
    y_train.npy
    X_test.npy
    y_test.npy
    label_names.txt      # optional, one label per line
    subject_train.npy    # optional
    subject_test.npy     # optional

The script writes:

output_root/
  data/{dataset}/{split}.parquet
  arrays/{dataset}.npz
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict, Iterable, Optional

np = None
pd = None


def require_dependencies() -> None:
    global np, pd
    if np is not None and pd is not None:
        return
    try:
        import numpy as _np
        import pandas as _pd
        import pyarrow  # noqa: F401
    except ModuleNotFoundError as exc:
        raise SystemExit(
            "Missing release dependency. Install with: "
            "python -m pip install -r requirements.txt"
        ) from exc
    np = _np
    pd = _pd


SPLITS = ("train", "val", "test")


def read_label_names(dataset_dir: Path) -> Optional[Dict[int, str]]:
    path = dataset_dir / "label_names.txt"
    if not path.exists():
        return None
    labels = [line.strip() for line in path.read_text(encoding="utf-8").splitlines()]
    return {idx: name for idx, name in enumerate(labels) if name}


def split_name(name: str) -> str:
    return "validation" if name == "val" else name


def iter_rows(
    dataset: str,
    split: str,
    x: np.ndarray,
    y: np.ndarray,
    layout: str,
    label_names: Optional[Dict[int, str]],
    subjects: Optional[np.ndarray],
) -> Iterable[dict]:
    if x.shape[0] != y.shape[0]:
        raise ValueError(f"{dataset}/{split}: X and y have different lengths")

    if x.ndim != 3:
        raise ValueError(f"{dataset}/{split}: expected X with 3 dims, got {x.shape}")

    if layout == "channels_first":
        channels, timesteps = x.shape[1], x.shape[2]
    elif layout == "timesteps_first":
        timesteps, channels = x.shape[1], x.shape[2]
    else:
        raise ValueError(f"Unsupported layout: {layout}")

    for idx in range(x.shape[0]):
        label = int(y[idx])
        subject = "" if subjects is None else str(subjects[idx])
        yield {
            "id": f"{dataset}_{split_name(split)}_{idx:06d}",
            "dataset": dataset,
            "split": split_name(split),
            "signal": x[idx].astype("float32", copy=False).reshape(-1).tolist(),
            "channels": int(channels),
            "timesteps": int(timesteps),
            "layout": layout,
            "label": label,
            "label_name": "" if label_names is None else label_names.get(label, ""),
            "subject": subject,
            "source_window_id": "",
        }


def convert_dataset(dataset_dir: Path, output_root: Path, layout: str) -> None:
    dataset = dataset_dir.name
    label_names = read_label_names(dataset_dir)

    parquet_dir = output_root / "data" / dataset
    parquet_dir.mkdir(parents=True, exist_ok=True)
    array_dir = output_root / "arrays"
    array_dir.mkdir(parents=True, exist_ok=True)

    archive = {}
    for split in SPLITS:
        x_path = dataset_dir / f"X_{split}.npy"
        y_path = dataset_dir / f"y_{split}.npy"
        if not x_path.exists() and split == "val":
            continue
        if not x_path.exists() or not y_path.exists():
            raise FileNotFoundError(f"Missing files for {dataset}/{split}")

        x = np.load(x_path)
        y = np.load(y_path)
        subject_path = dataset_dir / f"subject_{split}.npy"
        subjects = np.load(subject_path) if subject_path.exists() else None

        public_split = split_name(split)
        df = pd.DataFrame(
            iter_rows(dataset, split, x, y, layout, label_names, subjects)
        )
        df.to_parquet(parquet_dir / f"{public_split}.parquet", index=False)

        archive[f"X_{split}"] = x
        archive[f"y_{split}"] = y
        if subjects is not None:
            archive[f"subject_{split}"] = subjects

    if label_names is not None:
        ordered = [label_names[idx] for idx in sorted(label_names)]
        archive["label_names"] = np.asarray(ordered)

    np.savez_compressed(array_dir / f"{dataset}.npz", **archive)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_root", type=Path)
    parser.add_argument("output_root", type=Path)
    parser.add_argument(
        "--layout",
        choices=["channels_first", "timesteps_first"],
        default="channels_first",
    )
    args = parser.parse_args()

    require_dependencies()

    for dataset_dir in sorted(args.input_root.iterdir()):
        if dataset_dir.is_dir():
            print(f"Converting {dataset_dir.name}")
            convert_dataset(dataset_dir, args.output_root, args.layout)


if __name__ == "__main__":
    main()
