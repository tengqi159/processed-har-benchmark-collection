# HAR 处理后数据集公开发布策略

结论先说：建议采用 **GitHub 做门面和说明，Hugging Face Dataset 做主数据仓库，Zenodo 做正式版本 DOI，Google Drive/机构网盘只做可选镜像**。公开名称统一用 **Ready-to-Use Preprocessed HAR Datasets**，让别人一眼知道这是已经预处理好的 HAR 数据，可以直接下载训练。

## 为什么不把数据本体放 GitHub

GitHub 普通仓库适合代码和文档，不适合承载大规模数据文件。当前官方说明中，GitHub 对普通仓库大文件有明显限制：超过 50 MiB 会警告，超过 100 MiB 会被阻止；Git LFS 虽然能存大文件，但免费/不同计划有单文件限制，而且 Git LFS 不能用于 GitHub Pages。GitHub Release 可以放一些归档包，但它更像版本附件，不如 Hugging Face Dataset 适合数据发现、下载、版本和 Python 生态加载。

所以 GitHub 仓库里只放：

- README 首页
- 数据介绍和下载链接
- 数据格式说明
- 预处理/转换脚本
- manifest/checksum
- citation 和 license 说明
- 小样例，不放完整数据

## 为什么主站放 Hugging Face Dataset

Hugging Face Dataset repo 更适合这个 HAR 场景：

- 可以直接作为公开数据主页，README 会渲染成 dataset card。
- 支持数据集标签、任务标签、论文链接和下载统计。
- 支持 `datasets.load_dataset(...)`、`huggingface_hub.snapshot_download(...)` 等标准接口。
- 对大数据集有官方推荐结构，例如 Parquet/WebDataset、控制单仓库文件数、控制单文件大小等。
- 同行复现实验时下载路径更干净，不需要从 Google Drive 手动点链接。

当前上传的 `.npy` 数据建议采用最直观的下载结构：

- 主下载结构：`datasets/{dataset}/*.npy`
- 一键下载压缩包：`archives/processed_har_npy_partial_2026-05-14.zip`
- 元信息：`metadata/datasets.yaml` 和 `metadata/manifest.csv`

## Zenodo 是否需要

需要，尤其是论文投稿和同行引用。Hugging Face 适合分发和使用，Zenodo 适合“一个不可变版本”的正式归档和 DOI。建议等数据、README、manifest 都定稿后，在 Zenodo 发布 `v1.0.0`，然后把 DOI 写回 GitHub README、HF dataset card 和论文的 Data Availability 段落。

## Google Drive 是否需要

可选，不建议作为主站。Google Drive 的优点是上传简单、国内外很多人会用；缺点是版本、引用、下载统计、程序化加载、长期维护都不如 HF/Zenodo。它更适合：

- 审稿阶段临时匿名共享
- 国内下载速度不好时的镜像
- 给合作者传输大文件

如果用 Google Drive，README 里应明确写成 `Optional mirror`，而不是主下载入口。

## 推荐公开架构

```text
GitHub repo
  README.md                         # 项目门面和下载入口
  docs/data_format.md               # 数据字段和文件布局
  docs/license_and_redistribution_checklist.md
  metadata/datasets.yaml            # 八个数据集的公开元信息
  scripts/convert_npz_to_parquet.py # 转换脚本
  scripts/build_manifest.py         # checksum/manifest 脚本

Hugging Face Dataset repo
  README.md                         # dataset card
  datasets/*/*.npy                  # 可直接训练的 NumPy 数据
  archives/*.zip                    # 一键下载压缩包
  metadata/*.yaml/csv               # 元信息与校验

Zenodo
  v1.0.0 frozen archive             # DOI，论文引用

Google Drive / institutional mirror
  optional zip mirror               # 只作备用
```

## 上传前必须检查的风险

1. 原始数据集是否允许二次分发或派生数据分发。
2. 处理后的数据是否包含 subject id、个人属性、时间戳等敏感字段。
3. 论文中报告的样本数、通道数、窗口长度、split 比例是否与发布文件一致。
4. 每个 split 是否可重复生成，是否记录随机种子或 subject split 规则。
5. 是否给出原始数据集引用，而不是只引用自己的处理包。
6. 是否写清楚这是 processed benchmark collection，不要暗示自己采集了这些原始数据。

## 论文里可以放的 Data Availability 文案

```latex
\paragraph{Data availability.}
To facilitate reproducible comparison, we release the preprocessed benchmark windows, split files, and metadata used in our experiments at \url{https://huggingface.co/datasets/shenjianmozhu/preprocessed-har-datasets}. The accompanying documentation and preprocessing utilities are available at \url{https://github.com/tengqi159/preprocessed-har-datasets}. All datasets are derived from public HAR benchmarks, and users should also cite and comply with the terms of the original dataset sources.
```

如果审稿阶段暂时不能完全公开，可以改成：

```latex
\paragraph{Data availability.}
The preprocessed benchmark windows, split files, and metadata will be released upon publication. During review, an anonymized access link can be provided for reproducibility checking where permitted by the original dataset licenses.
```
