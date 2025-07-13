#!/bin/bash

clear
echo -e "\e[92m"
figlet -f slant "MAAZ TOOL"
echo -e "\e[93mOne-Command Installer by MaazTool Devs"
echo -e "\e[90m======================================"

# ✅ Redirect to WhatsApp
echo -e "\e[94m[+] Redirecting to WhatsApp support group..."
xdg-open "https://wa.me/923079741690" > /dev/null 2>&1
sleep 2

# ✅ Update and Install Basic Packages
echo -e "\e[92m[+] Updating Termux packages..."
pkg update -y && pkg upgrade -y

echo -e "\e[92m[+] Installing Python and required libraries..."
pkg install python -y
pip install --upgrade pip
pip install requests futures rich || pip install --break-system-packages requests futures rich

# ✅ Error Auto-Fix System
fix_errors() {
    echo -e "\e[91m[!] Detected crash. Attempting auto-fix...\e[0m"

    # 🛠 Auto-fix line breaks in imports (common paste error)
    sed -i 's/import os import/import os\nimport/' maaz_tool.py
    sed -i 's/ import /\nimport /g' maaz_tool.py

    # 🛠 Add missing color variables if broken
    if ! grep -q "R = '\x1b" maaz_tool.py; then
        echo -e "\n# Color Fix" >> maaz_tool.py
        echo "R = '\x1b[38;5;196m'" >> maaz_tool.py
        echo "G = '\x1b[38;5;46m'" >> maaz_tool.py
        echo "Y = '\x1b[38;5;226m'" >> maaz_tool.py
        echo "B = '\x1b[38;5;44m'" >> maaz_tool.py
        echo "P = '\x1b[38;5;201m'" >> maaz_tool.py
        echo "W = '\x1b[0;97m'" >> maaz_tool.py
        echo "N = '\x1b[0m'" >> maaz_tool.py
    fi
}

# ✅ Try to run your main script
echo -e "\e[92m[+] Starting MaazTool..."
python maaz_tool.py || {
    fix_errors
    echo -e "\e[93m[!] Retrying MaazTool after auto-fix...\e[0m"
    python maaz_tool.py || echo -e "\e[91m[✘] Still errors. Please contact support.\e[0m"
}
