#!/data/data/com.termux/files/usr/bin/bash

# 1. Update Termux packages
pkg update -y && pkg upgrade -y

# 2. Ensure Termux's python-pip is installed (avoids forbidden pip install)
if ! pkg list-installed | grep -q '^python-pip'; then
  pkg install -y python-pip
fi

# 3. Attempt global pip upgrade (will log forbidden error)
python3 -m pip install --upgrade pip 2>/tmp/pip_upgrade.log

# 4. On forbidden-pip error, create & use a virtual environment to upgrade pip
if grep -q "Installing pip is forbidden" /tmp/pip_upgrade.log; then
  echo "Global pip upgrade failed. Creating virtual environment..."
  python3 -m venv ~/maaz_venv
  source ~/maaz_venv/bin/activate
  pip install --upgrade pip
  deactivate
fi

# 5. Auto-fix mismatched braces in maaz_tool.py
MAAZ_FILE="$HOME/MaazTool/maaz_tool.py"
if [ -f "$MAAZ_FILE" ]; then
  # Replace any standalone ']' line with '}' to correct stray bracket
  sed -i 's/^[[:space:]]*]\s*$/}/' "$MAAZ_FILE"
  echo "Applied brace-fix patch to $MAAZ_FILE"
fi

# 6. Run MaazTool and capture any syntax errors
ERROR_LOG=$(python3 "$MAAZ_FILE" 2>&1 >/dev/null)

# 7. If errors remain, notify user
if echo "$ERROR_LOG" | grep -q "SyntaxError"; then
  echo "❌ Still errors detected in MaazTool."
  echo "Please inspect $MAAZ_FILE manually or contact support."
else
  echo "✅ MaazTool ran successfully."
fi
