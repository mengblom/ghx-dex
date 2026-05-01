#!/usr/bin/env bash
# Helper script to run GHX to Dex migration
# Usage:
#   ./migrate-ghx.sh          # Dry run (preview)
#   ./migrate-ghx.sh --apply  # Execute migration
#   ./migrate-ghx.sh --rollback  # Undo migration

set -euo pipefail

# Navigate to vault root
cd "$(dirname "$0")"

# Activate venv
if [ ! -d ".venv" ]; then
    echo "Error: Python venv not found. Run: python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt"
    exit 1
fi

source .venv/bin/activate

# Set VAULT_PATH
export VAULT_PATH="$(pwd)"

# Run migration
python core/migrations/migrate_ghx_to_dex.py "$@"
