#!/data/data/com.termux/files/usr/bin/bash
set -eo pipefail

# 1. Prepare logging directory
LOGDIR="$HOME/.maaz_logs"
mkdir -p "$LOGDIR"
PIP_LOG="$LOGDIR/pip_upgrade.log"
ERR_LOG="$LOGDIR/maaz_error.log"

# 2. Update/upgrade Termux packages safely
echo "➤ Updating Termux packages…"
pkg update -y && pkg upgrade -y

# 3. Ensure python-pip (Termux-compatible) is installed
if ! pkg list-installed | grep -q '^python-pip'; then
  echo "➤ Installing python-pip package…"
  pkg install -y python-pip
fi

# 4. Try upgrading pip globally, log errors
echo "➤ Attempting global pip upgrade…"
python3 -m pip install --upgrade pip >"$PIP_LOG" 2>&1 || true

# 5. If forbidden, create & use a venv for pip upgrade
if grep -q "Installing pip is forbidden" "$PIP_LOG"; then
  echo "⚠️  Global pip upgrade blocked. Creating virtualenv…"
  python3 -m venv "$HOME/maaz_venv"
  source "$HOME/maaz_venv/bin/activate"
  pip install --upgrade pip
  deactivate
  echo "✅ pip upgraded inside virtualenv: ~/maaz_venv"
else
  echo "✅ Global pip upgrade successful or not needed."
fi

# 6. Auto-fix MaazTool mismatched brackets
MAAZ_FILE="$HOME/MaazTool/maaz_tool.py"
if [ ! -f "$MAAZ_FILE" ]; then
  echo "❌ Cannot find MaazTool script at $MAAZ_FILE"
  exit 1
fi

echo "➤ Attempting to run MaazTool and auto-fix SyntaxErrors…"
MAX_TRIES=5
try=1

while [ $try -le $MAX_TRIES ]; do
  # run MaazTool, capture stderr only
  python3 "$MAAZ_FILE" 2>"$ERR_LOG" 1>/dev/null || true

  if ! grep -q "SyntaxError" "$ERR_LOG"; then
    echo "✅ MaazTool ran successfully on try #$try."
    rm -f "$ERR_LOG"
    exit 0
  fi

  echo "⚠️  SyntaxError detected (attempt $try/$MAX_TRIES). Parsing error…"

  # extract all line numbers with mismatched-bracket errors
  lines=$(grep -oP "line \K[0-9]+" "$ERR_LOG" | sort -n | uniq)
  for ln in $lines; do
    echo "    ‣ Fixing bracket mismatch at line $ln"
    # replace any standalone ']' closing a dict with '}', and ')' with '}'
    sed -i "${ln}s/]/}/g; ${ln}s/)/}/g" "$MAAZ_FILE"
  done

  try=$((try+1))
done

echo "❌ Still errors after $MAX_TRIES attempts. Inspect log at $ERR_LOG and file $MAAZ_FILE manually."
exit 1
