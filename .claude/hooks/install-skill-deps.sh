#!/bin/bash
# Installs Python libraries that skills need (charts, spreadsheets, PDF reports).
# Cloud sessions start from a fresh machine, so this runs on every session start.
# Runs in the background so it never delays the session.

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

(pip install -q reportlab openpyxl xlsxwriter pandas numpy matplotlib seaborn plotly \
  > /tmp/skill-deps.log 2>&1 &)

exit 0
