# Google Drive Mirror

Google Drive is an optional browser-download mirror for users who do not want to use the Hugging Face Hub tooling.

Public mirror folder:

https://drive.google.com/drive/folders/1Qe8AQ8S2V4_uBIvC3Pv4WRmv-EPWERjG?usp=drive_link

Hugging Face remains the primary public dataset repository because it supports versioned data repositories, programmatic downloads, dataset metadata, and download statistics.

Recommended Drive structure:

```text
Ready-to-Use Preprocessed HAR Datasets/
  processed_har_npy_partial_2026-05-14.zip
  partial_upload_2026-05-14_manifest.csv
  README.txt
```

Public sharing status: enabled by the maintainer.

When adding new data, keep the Drive folder names aligned with the Hugging Face `datasets/<dataset>/` layout so users can move between the two download routes without guessing.
