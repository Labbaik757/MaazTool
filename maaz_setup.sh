#!/bin/bash

# ========================
# 📦 MAAZ TOOL INSTALLER
# ========================

clear
echo "🔧 Installing Maaz Tool requirements..."

# Check and install Python
if ! command -v python &> /dev/null; then
  echo "📥 Installing Python..."
  pkg install python -y || apt install python3 -y
fi

# Install pip & rich
echo "📥 Installing pip & rich..."
pip install --upgrade pip > /dev/null 2>&1
pip install rich requests --quiet

# Create alias (optional)
if [[ "$PREFIX" != "" ]]; then
  # We're in Termux
  echo "alias maaz='python maaz_tool.py'" >> ~/.bashrc
else
  echo "alias maaz='python3 maaz_tool.py'" >> ~/.bashrc
fi

# Make tool executable
chmod +x maaz_tool.py

# Start the tool
clear
echo "🚀 Launching Maaz Tool..."
python maaz_tool.py
