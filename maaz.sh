#!/data/data/com.termux/files/usr/bin/bash

# Colors
green="\e[92m"
red="\e[91m"
blue="\e[94m"
reset="\e[0m"

clear
echo -e "${blue}🔧 Maaz Tool Installer Starting...${reset}"

# Step 1: Install Python if not present
echo -e "${green}📦 Checking Python...${reset}"
apt-get -qq update > /dev/null 2>&1
apt-get -qq install python -y > /dev/null 2>&1

# Step 2: Create virtualenv (if not exists)
if [ ! -d "$HOME/maaz_venv" ]; then
    echo -e "${green}🧪 Creating virtual environment...${reset}"
    python3 -m venv $HOME/maaz_venv
fi

# Step 3: Activate virtualenv
source $HOME/maaz_venv/bin/activate

# Step 4: Upgrade pip
echo -e "${green}🔄 Upgrading pip...${reset}"
python3 -m pip install --upgrade pip --quiet

# Step 5: Install required modules
echo -e "${green}📦 Installing required Python modules...${reset}"
pip install --quiet requests rich mechanize futures

# Step 6: Ensure working folders exist
REQUIRED_DIRS=("results" "logs" "dump")
for dir in "${REQUIRED_DIRS[@]}"; do
    if [ ! -d "$dir" ]; then
        echo -e "${green}📁 Creating missing folder: $dir${reset}"
        mkdir -p "$dir"
    fi
done

# Step 7: Create default files if missing
REQUIRED_FILES=("combo.txt" "ok.txt" "cp.txt" "approved_keys.txt")
for file in "${REQUIRED_FILES[@]}"; do
    if [ ! -f "$file" ]; then
        echo -e "${green}📄 Creating empty file: $file${reset}"
        touch "$file"
    fi
done

# Step 8: Check main tool file
if [ ! -f "maaz_tool.py" ]; then
    echo -e "${red}❌ maaz_tool.py not found!${reset}"
    echo -e "${blue}📥 Creating placeholder maaz_tool.py...${reset}"
    cat > maaz_tool.py <<EOF
# Placeholder file created by installer
print("⚠️ maaz_tool.py is missing actual tool code.")
EOF
fi

# Step 9: Make tool executable (optional)
chmod +x maaz_tool.py

# Step 10: Run tool
echo -e "${blue}🚀 Running Maaz Tool...${reset}"
python3 maaz_tool.py

# Step 11: Auto error fix if tool crashes
if [ $? -ne 0 ]; then
    echo -e "${red}❌ Tool crashed. Attempting auto-fix...${reset}"
    
    # Reinstall modules
    pip install --force-reinstall requests rich mechanize futures --quiet
    
    # Retry tool
    echo -e "${blue}🔄 Retrying...${reset}"
    python3 maaz_tool.py
    
    # Final check
    if [ $? -ne 0 ]; then
        echo -e "${red}⚠️ Auto-fix failed. Please check tool code manually.${reset}"
        exit 1
    fi
fi
