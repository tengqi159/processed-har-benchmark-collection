# License and Redistribution Checklist

This release is derived from public HAR datasets. Before uploading processed files, confirm the redistribution terms for each original source.

Use this checklist conservatively. If redistribution is unclear, do not upload the processed data files for that source. Instead, publish preprocessing code and instructions that reproduce the processed windows from the original dataset.

| Dataset | Public Source | Processed Files Can Be Uploaded? | Notes |
| --- | --- | --- | --- |
| UCI-HAR | UCI Machine Learning Repository | verify_before_upload | Check UCI dataset page and citation/license terms. |
| UniMiB-SHAR | UniMiB / original paper | verify_before_upload | Verify whether derived window files can be redistributed. |
| USC-HAD | USC Sipi HAD page / original paper | verify_before_upload | Verify dataset terms and attribution requirements. |
| FLAAP | Procedia Computer Science open-access paper | verify_before_upload | Check dataset download terms in addition to paper license. |
| HAPT | UCI Machine Learning Repository | verify_before_upload | Check UCI dataset page and citation/license terms. |
| mHealth | UCI Machine Learning Repository | verify_before_upload | Check UCI dataset page and citation/license terms. |
| DSADS | UCI Machine Learning Repository | verify_before_upload | Check UCI dataset page and citation/license terms. |
| PAMAP2 | UCI Machine Learning Repository | verify_before_upload | Check UCI dataset page and citation/license terms. |

## Minimum Public Wording

Use this wording in the README and dataset card until every source is verified:

> This collection contains processed versions of public datasets. The original datasets retain their own licenses, citation requirements, and redistribution terms. Users must comply with the terms of each original source.

## Sensitive Fields

Before release, remove or justify:

- names, emails, or direct personal identifiers
- exact collection timestamps if not needed
- unnecessary demographic attributes
- device identifiers not present in the original public release
- internal file paths or lab machine names

Subject ids may be useful for reproducibility, but only keep them if the original dataset already releases them and redistribution is permitted.
