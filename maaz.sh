#!/bin/bash

clear echo -e "\e[92m" figlet -f slant "MAAZ TOOL" echo -e "\e[93mOne-Command Installer by MaazTool Devs" echo -e "\e[90m======================================"

echo -e "\e[94m[+] Redirecting to WhatsApp support group..." xdg-open "https://wa.me/923079741690" > /dev/null 2>&1 sleep 2

echo -e "\e[92m[+] Updating Termux packages..." pkg update -y && pkg upgrade -y

echo -e "\e[92m[+] Installing Python and dependencies..." pkg install python -y pip install requests pip install futures

echo -e "\e[92m[+] Running MaazTool now..." python maaz_tool.py

