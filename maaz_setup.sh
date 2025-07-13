#!/bin/bash

clear
echo -e "\e[1;96m"
echo '███╗   ███╗ █████╗  █████╗ ███████╗'
echo '████╗ ████║██╔══██╗██╔══██╗╚══███╔╝'
echo '██╔████╔██║███████║███████║  ███╔╝ '
echo '██║╚██╔╝██║██╔══██║██╔══██║ ███╔╝  '
echo '██║ ╚═╝ ██║██║  ██║██║  ██║███████╗'
echo '╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝'
echo -e "\e[1;92m⚡ MAAZ FACEBOOK CLONER TOOL ⚡\e[0m"
echo
sleep 2

echo -e "\e[1;93m🔧 Updating packages...\e[0m"
pkg update -y &> /dev/null || apt update -y &> /dev/null
pkg install python -y &> /dev/null || apt install python3 -y &> /dev/null

echo -e "\e[1;93m📦 Installing Python modules...\e[0m"
pip install rich requests --quiet

if [ ! -f "maaz_tool.py" ]; then
    echo -e "\e[1;91m❌ maaz_tool.py not found in this folder.\e[0m"
    echo -e "\e[1;94mPlace your tool script here and run again.\e[0m"
    exit 1
fi

echo -e "\e[1;93m🔗 Creating command: \e[1;92mmaaz\e[0m"
cp maaz_tool.py $PREFIX/bin/maaz
chmod +x $PREFIX/bin/maaz

echo -e "\n\e[1;96m📲 Join WhatsApp Group:"
echo -e "\e[1;92mhttps://chat.whatsapp.com/CFGuz089SUe5npFZDS8iTh\e[0m"
sleep 3

echo -e "\n\e[1;92m🚀 Starting MAAZ TOOL...\e[0m"
sleep 1
python maaz_tool.py
