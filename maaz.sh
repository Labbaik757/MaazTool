#!/data/data/com.termux/files/usr/bin/bash

# Color Codes
green="\e[92m"
red="\e[91m"
blue="\e[94m"
reset="\e[0m"

clear
echo -e "${blue}🔧 Maaz Tool Installer Starting...${reset}"

# Step 1: Install Python silently
echo -e "${green}📦 Installing Python (if not installed)...${reset}"
apt-get -qq update > /dev/null 2>&1
apt-get -qq install python -y > /dev/null 2>&1

# Step 2: Create virtualenv if not exists
if [ ! -d "$HOME/maaz_venv" ]; then
    echo -e "${green}🧪 Creating virtual environment...${reset}"
    python3 -m venv $HOME/maaz_venv
fi

# Step 3: Activate virtual environment
source $HOME/maaz_venv/bin/activate

# Step 4: Upgrade pip silently
echo -e "${green}🔄 Upgrading pip inside virtualenv...${reset}"
python3 -m pip install --upgrade pip --quiet
echo -e "${green}✅ pip upgraded inside virtualenv: ~/maaz_venv${reset}"

# Step 5: Install required Python modules
echo -e "${green}📦 Installing required Python modules...${reset}"
pip install requests rich mechanize futures --quiet
echo -e "${green}✅ All required modules installed.${reset}"

# Step 6: Run Maaz Tool
echo -e "${blue}🚀 Running Maaz Tool...${reset}"
python3 maaz_tool.py

# Step 7: Handle error if tool fails
if [ $? -ne 0 ]; then
    echo -e "${red}❌ Error: Something went wrong while running Maaz Tool.${reset}"
    echo -e "${red}🔍 Tip: Check maaz_tool.py for syntax errors or missing code.${reset}"
    exit 1
fi
