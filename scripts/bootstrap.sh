#!/usr/bin/env bash
set -euo pipefail
python hdc/hdc.py status
python hdc/hdc.py next
printf '\nRead HDC_MASTER_PROMPT.md before implementation.\n'
