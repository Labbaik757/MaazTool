#!/data/data/com.termux/files/usr/bin/bash

# Colors
green="\e[92m"
red="\e[91m"
blue="\e[94m"
reset="\e[0m"

clear
echo -e "${blue}🔧 Maaz Tool Installer Starting...${reset}"

# Step 1: Install Python if needed
echo -e "${green}📦 Installing Python...${reset}"
apt-get -qq update > /dev/null 2>&1
apt-get -qq install python -y > /dev/null 2>&1

# Step 2: Create virtualenv
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
echo -e "${green}📦 Installing required modules...${reset}"
pip install requests rich mechanize futures --quiet

# Step 6: Create passlist.txt (Pakistani style)
if [ ! -f "passlist.txt" ]; then
    echo -e "${green}📂 Creating passlist.txt...${reset}"
    cat > passlist.txt <<EOF
123456
123456789
786786
pakistan
khan123
iloveyou
bismillah
first123
name123
ali786
pak786
EOF
fi

# Step 7: Create worldlist.txt (Top global)
if [ ! -f "worldlist.txt" ]; then
    echo -e "${green}🌍 Creating worldlist.txt...${reset}"
    cat > worldlist.txt <<EOF
123456
password
123456789
12345678
qwerty
abc123
letmein
princess
dragon
football
baseball
welcome
admin
sunshine
monkey
iloveyou
password1
000000
111111
EOF
fi

# Step 8: Create fb_leaked.txt (Facebook leaked passwords)
if [ ! -f "fb_leaked.txt" ]; then
    echo -e "${green}🔐 Creating fb_leaked.txt...${reset}"
    cat > fb_leaked.txt <<EOF
123456
password
123456789
qwerty
abc123
111111
iloveyou
password1
123123
letmein
monkey
dragon
sunshine
princess
welcome
football
EOF
fi

# Step 9: Download rockyou.txt if missing
if [ ! -f "rockyou.txt" ]; then
    echo -e "${green}💾 Downloading rockyou.txt (15M+ passwords)...${reset}"
    wget -q --show-progress https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt -O rockyou.txt
    if [ -f "rockyou.txt" ]; then
        echo -e "${green}✅ rockyou.txt downloaded successfully.${reset}"
    else
        echo -e "${red}❌ Failed to download rockyou.txt${reset}"
    fi
else
    echo -e "${blue}📂 rockyou.txt already exists. Skipping download.${reset}"
fi

# Step 10: Run Maaz Tool
echo -e "${blue}🚀 Running Maaz Tool...${reset}"
python3 maaz_tool.py

# Step 11: Error handling
if [ $? -ne 0 ]; then
    echo -e "${red}❌ Error running maaz_tool.py. Check for bugs or missing files.${reset}"
    exit 1
fi
