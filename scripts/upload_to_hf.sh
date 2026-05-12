#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 ORG_OR_USER/DATASET_NAME [LOCAL_RELEASE_DIR]" >&2
  exit 2
fi

REPO_ID="$1"
LOCAL_DIR="${2:-hf_release}"

HF_BIN="${HF_BIN:-hf}"
if ! command -v "$HF_BIN" >/dev/null 2>&1 && [[ -x "$HOME/Library/Python/3.9/bin/hf" ]]; then
  HF_BIN="$HOME/Library/Python/3.9/bin/hf"
fi

if ! command -v "$HF_BIN" >/dev/null 2>&1; then
  echo "The 'hf' CLI is not installed." >&2
  echo "Install it with: curl -LsSf https://hf.co/cli/install.sh | bash -s" >&2
  exit 127
fi

"$HF_BIN" auth whoami >/dev/null
"$HF_BIN" repos create "$REPO_ID" --type dataset --exist-ok

"$HF_BIN" upload-large-folder "$REPO_ID" "$LOCAL_DIR" \
  --type dataset \
  --exclude ".DS_Store" \
  --exclude "__MACOSX/*"

echo "Uploaded dataset files to https://huggingface.co/datasets/$REPO_ID"
