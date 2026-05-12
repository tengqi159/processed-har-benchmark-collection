# Data Format

This document defines the public format for the processed HAR benchmark release.

## Repository Layout

```text
data/{dataset_slug}/{split}.parquet
arrays/{dataset_slug}.npz
metadata/datasets.yaml
metadata/manifest.csv
```

Use the following dataset slugs:

- `uci_har`
- `unimib_shar`
- `usc_had`
- `flaap`
- `hapt`
- `mhealth`
- `dsads`
- `pamap2`

## Parquet Schema

Each row is one preprocessed window.

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | yes | Stable id, e.g. `uci_har_train_000001` |
| `dataset` | string | yes | Dataset slug |
| `split` | string | yes | `train`, `validation`, or `test` |
| `signal` | list<float32> | yes | Flattened sensor window |
| `channels` | int32 | yes | Number of channels |
| `timesteps` | int32 | yes | Window length |
| `layout` | string | yes | `channels_first` or `timesteps_first` |
| `label` | int32 | yes | Integer class id |
| `label_name` | string | recommended | Human-readable activity name |
| `subject` | string | optional | Subject id if release is permitted |
| `source_window_id` | string | optional | Id from the internal preprocessing pipeline |

## Array Layout

Use `channels_first` by default:

```text
signal.reshape(channels, timesteps)
```

If your current processed files are `timesteps_first`, either convert them before release or set `layout = "timesteps_first"` consistently:

```text
signal.reshape(timesteps, channels)
```

Do not mix layouts within one subset.

## NPZ Schema

Each `arrays/{dataset_slug}.npz` file should contain:

```text
X_train
y_train
X_test
y_test
label_names        # optional
subject_train      # optional
subject_test       # optional
```

If a validation split exists, add:

```text
X_val
y_val
subject_val        # optional
```

## Manifest

`metadata/manifest.csv` should include one row per released file:

```text
path,bytes,sha256,created_at_utc,notes
```

The manifest should be regenerated after every data change.

