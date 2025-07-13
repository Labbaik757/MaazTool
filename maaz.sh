#!/bin/bash

clear echo -e "\e[92m" figlet -f slant "MAAZ TOOL" echo -e "\e[93mOne-Command Installer by MaazTool Devs" echo -e "\e[90m======================================"

echo -e "\e[94m[+] Redirecting to WhatsApp support group..." xdg-open "https://wa.me/923079741690" > /dev/null 2>&1 sleep 2

echo -e "\e[92m[+] Updating Termux packages..." pkg update -y && pkg upgrade -y

echo -e "\e[92m[+] Installing Python and dependencies..." pkg install python -y pip install requests pip install futures

echo -e "\e[92m[+] Cloning tool from GitHub..." git clone https://github.com/Labbaik757/MaazTool.git

cd MaazTool

chmod +x * echo -e "\e[93m[✓] Installation complete. Starting tool..."

python maaz_tool.py

