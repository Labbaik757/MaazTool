#!/bin/bash

# Define colors
G='\033[1;32m'
R='\033[1;31m'
N='\033[0m'

clear

echo -e "${G}"
echo "╔════════════════════════════════════════════╗"
echo "║        🔥 Starting Maaz FB Cloner Tool 🔥       ║"
echo "╚════════════════════════════════════════════╝"
sleep 1

# 📁 Create folders
folders=("results" "logs" "dump")
for folder in "${folders[@]}"; do
    if [ ! -d "$folder" ]; then
        mkdir "$folder"
        echo -e "📁 Creating missing folder: ${folder}"
        sleep 0.3
    fi
done

# 📄 Create files
files=("ok.txt" "cp.txt" "approved_keys.txt")
for file in "${files[@]}"; do
    if [ ! -f "$file" ]; then
        touch "$file"
        echo -e "📄 Creating empty file: ${file}"
        sleep 0.3
    fi
done

# 🔧 Install Required Python Modules
echo -e "${G}🔧 Installing required Python modules...${N}"
pkgs=("requests" "rich" "bs4" "mechanize" "futures")
for pkg in "${pkgs[@]}"; do
    pip install $pkg > /dev/null 2>&1
done
sleep 1

# 🌐 WhatsApp Group Number (change link if needed)
xdg-open "https://wa.me/923079741690" > /dev/null 2>&1 &
sleep 2

# ▶️ Launch the actual Python tool
echo -e "${G}▶️ Loading Maaz Tool...${N}"
sleep 1
python3 maaz_tool.py
