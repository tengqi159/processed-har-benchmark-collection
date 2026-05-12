# 发布执行清单

下面这套顺序适合正式公开前执行。

## 1. 替换占位符

在整个目录中搜索：

```bash
rg "TODO_|TODO_VERIFY" .
```

正式发布后至少替换：

- `shenjianmozhu/processed-har-benchmark-collection` 中的 `shenjianmozhu`
- Zenodo DOI，目前写为 pending
- 可选镜像链接，目前写为 not configured
- `v0.1.0`，正式数据齐全后建议升级为 `v1.0.0`

## 2. 检查原始数据集再分发权限

逐项完成：

```text
docs/license_and_redistribution_checklist.md
metadata/datasets.yaml
```

如果某个数据集不确定能否再分发，不要上传它的 processed files。保留 metadata 和 preprocessing instruction 即可。

## 3. 准备本地 processed array 目录

建议整理成：

```text
processed_arrays/
  uci_har/
    X_train.npy
    y_train.npy
    X_test.npy
    y_test.npy
    label_names.txt
  hapt/
    X_train.npy
    y_train.npy
    X_test.npy
    y_test.npy
```

每个 `X_*.npy` 应为三维数组。默认发布脚本假设 `channels_first`，即：

```text
[num_windows, channels, timesteps]
```

如果当前数据是 `[num_windows, timesteps, channels]`，运行转换脚本时加：

```bash
--layout timesteps_first
```

## 4. 转换成 HF release 目录

```bash
cd /path/to/har-benchmark-release
python -m pip install -r requirements.txt
python scripts/convert_npz_to_parquet.py /path/to/processed_arrays hf_release --layout channels_first
cp hf_dataset_card/README.md hf_release/README.md
mkdir -p hf_release/metadata
cp metadata/datasets.yaml hf_release/metadata/datasets.yaml
python scripts/build_manifest.py hf_release
```

## 5. 上传 Hugging Face Dataset

如果没有安装 `hf` CLI：

```bash
curl -LsSf https://hf.co/cli/install.sh | bash -s
hf auth login
```

然后上传：

```bash
scripts/upload_to_hf.sh shenjianmozhu/processed-har-benchmark-collection hf_release
```

## 6. 建 GitHub 仓库

GitHub 仓库只放当前目录里的文档、脚本和元信息，不放 `hf_release/`、`data/`、`arrays/`。

```bash
git init
git add .
git commit -m "Initial processed HAR benchmark release docs"
gh repo create processed-har-benchmark-collection --public --source=. --remote=origin --push
```

## 7. Zenodo DOI

等 GitHub 和 Hugging Face 都稳定后：

1. 打 GitHub release，例如 `v1.0.0`。
2. 在 Zenodo 新建 dataset/software record，上传同一版本归档或启用 GitHub integration。
3. 拿到 DOI 后，回填到 GitHub README、HF dataset card、`CITATION.cff` 和论文 Data Availability。

## 8. 最后公开前检查

- 下载命令可以跑通。
- 每个数据集样本数与论文表格一致。
- 每个 split 的标签分布合理。
- manifest 中每个文件有 sha256。
- README 没有内部路径、服务器路径、学生名字缩写等不该公开的信息。
- license 文案没有承诺超出原始数据集许可的东西。
