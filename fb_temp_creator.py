import time
import random
import string
import threading
import requests
import csv
import os
import uuid
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

NUM_ACCOUNTS = 5
THREADS = 2
BATCH_DELAY = 20
OTP_POLL = 4
OTP_ROUNDS = 30
CSV_FILE = "created_fb_accounts.csv"
PROFILE_PICS = "profile_pics"
PROXY_FILE = "proxies.txt"
UA_FILE = "useragents.txt"
MIN_PROFILE_PICS = 10  # Minimum images to download if not present

SELECTOR_MAP = {
    "firstname": ['input[name="firstname"]', 'input[aria-label="First name"]'],
    "lastname": ['input[name="lastname"]', 'input[aria-label="Surname"]'],
    "email": ['input[name="reg_email__"]', 'input[aria-label="Mobile number or email address"]'],
    "password": ['input[name="reg_passwd__"]', 'input[type="password"]'],
    "birthday_day": ['select[name="birthday_day"]'],
    "birthday_month": ['select[name="birthday_month"]'],
    "birthday_year": ['select[name="birthday_year"]'],
    "gender_male": ['input[name="sex"][value="2"]', 'input[aria-label="Male"]'],
    "submit": ['button[name="websubmit"]', 'button[type="submit"]'],
    "otp_field": ['input[name="code"]', 'input[aria-label="Confirmation code"]'],
    "profile_photo_edit": ['div[aria-label="Edit profile photo"]', 'div[aria-label="Update profile picture"]'],
    "profile_photo_file_input": ['input[type="file"]'],
    "profile_photo_save": ['div[aria-label="Save"]', 'div[aria-label="Apply"]'],
}

console = Console()
LOCK = threading.Lock()
CREATED = []
BLACKLISTED = set()

def log(msg, color="cyan"):
    console.print(f"[{color}]{msg}[/{color}]")

def ensure_folder_and_files():
    if not os.path.exists(PROFILE_PICS):
        os.makedirs(PROFILE_PICS)
    for file in [PROXY_FILE, UA_FILE]:
        if not os.path.exists(file):
            with open(file, "w") as f:
                f.write("")

def auto_download_images():
    images = [f for f in os.listdir(PROFILE_PICS) if f.lower().endswith((".jpg",".png",".jpeg",".jfif"))]
    needed = MIN_PROFILE_PICS - len(images)
    if needed <= 0:
        return
    log(f"Downloading {needed} profile images...", "yellow")
    for i in range(needed):
        try:
            resp = requests.get("https://randomuser.me/api/", timeout=10)
            resp.raise_for_status()
            imgurl = resp.json()["results"][0]["picture"]["large"]
            imgdata = requests.get(imgurl, timeout=10).content
            ext = imgurl.split('.')[-1].split('?')[0]
            fname = f"profile_{int(time.time())}_{uuid.uuid4().hex[:6]}.{ext}"
            with open(os.path.join(PROFILE_PICS, fname), "wb") as f:
                f.write(imgdata)
            time.sleep(1)
        except Exception as e:
            log(f"Image download failed: {e}", "red")
    log("Profile images download complete.", "green")

def load_list(filename, fallback=None):
    try:
        if os.path.exists(filename):
            with open(filename, "r") as f:
                return [x.strip() for x in f if x.strip()]
    except Exception as e:
        log(f"Failed to load {filename}: {e}", "red")
    return fallback or []

def get_proxies():
    proxies = load_list(PROXY_FILE)
    if not proxies:
        try:
            res = requests.get("https://www.proxy-list.download/api/v1/get?type=https", timeout=10)
            proxies = [p for p in res.text.strip().splitlines() if p]
            with open(PROXY_FILE, "w") as f:
                for p in proxies:
                    f.write(p + "\n")
        except Exception as e:
            log(f"Proxy fetch fail: {e}", "red")
            proxies = []
    return proxies

def is_proxy_ok(proxy):
    if proxy in BLACKLISTED:
        return False
    try:
        r = requests.get("https://www.facebook.com/", proxies={"http": f"http://{proxy}", "https": f"http://{proxy}"}, timeout=8)
        return r.status_code == 200
    except Exception:
        with LOCK:
            BLACKLISTED.add(proxy)
        return False

def get_user_agents():
    fallback = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15",
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
    ]
    uas = load_list(UA_FILE, fallback)
    if not os.path.exists(UA_FILE) or os.stat(UA_FILE).st_size == 0:
        with open(UA_FILE, "w") as f:
            for ua in uas:
                f.write(ua + "\n")
    return uas

def gen_name():
    first = ["Ali", "Ahmed", "Usman", "Hamza", "Fahad", "Maaz", "Imran", "Zohaib"]
    last = ["Khan", "Malik", "Butt", "Chaudhary", "Nazeer", "Sheikh"]
    return f"{random.choice(first)} {random.choice(last)}"

def gen_pass():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

def temp_mail():
    login = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = random.choice(["1secmail.com", "1secmail.org", "1secmail.net"])
    return login, domain, f"{login}@{domain}"

def poll_otp(login, domain):
    url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}"
    for _ in range(OTP_ROUNDS):
        time.sleep(OTP_POLL)
        try:
            res = requests.get(url, timeout=10)
            messages = res.json()
            if messages:
                msg_id = messages[0].get('id')
                if not msg_id:
                    continue
                msg_url = f"https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={msg_id}"
                msg_res = requests.get(msg_url, timeout=10)
                body = msg_res.json().get('body', '')
                otp = ''.join(filter(str.isdigit, body))
                if len(otp) >= 5:
                    return otp[:6]
        except Exception:
            continue
    return None

def save_csv(accounts):
    if not accounts:
        return
    file_exists = os.path.exists(CSV_FILE)
    try:
        with LOCK:
            with open(CSV_FILE, "a", newline='', encoding='utf-8') as f:
                w = csv.DictWriter(f, fieldnames=['email', 'password', 'name', 'proxy', 'user_agent'])
                if not file_exists:
                    w.writeheader()
                for a in accounts:
                    w.writerow(a)
            accounts.clear()
    except Exception as e:
        log(f"CSV Save Error: {e}", "red")

def get_profile_pic():
    try:
        pics = [os.path.join(PROFILE_PICS, f) for f in os.listdir(PROFILE_PICS) if f.lower().endswith((".jpg",".png",".jpeg",".jfif"))]
        if pics:
            return random.choice(pics)
    except Exception:
        pass
    return None

def s_fill(page, sel, val):
    for s in sel:
        try:
            if page.query_selector(s):
                page.fill(s, val, timeout=3000)
                return True
        except Exception:
            continue
    return False

def s_click(page, sel):
    for s in sel:
        try:
            if page.query_selector(s):
                page.click(s, timeout=3000)
                return True
        except Exception:
            continue
    return False

def s_select(page, sel, val):
    for s in sel:
        try:
            if page.query_selector(s):
                page.select_option(s, val)
                return True
        except Exception:
            continue
    return False

def create_account(idx, proxy, ua, progress=None, task=None):
    name = gen_name()
    password = gen_pass()
    login, domain, email = temp_mail()
    status = f"{idx}. {email}"
    try:
        with sync_playwright() as p:
            browser_args = {"headless": True}
            if proxy:
                browser_args["proxy"] = {"server": f"http://{proxy}"}
            browser = p.chromium.launch(**browser_args)
            context = browser.new_context(user_agent=ua)
            page = context.new_page()
            page.goto("https://www.facebook.com/reg", timeout=20000)
            time.sleep(2)
            if not (s_fill(page, SELECTOR_MAP["firstname"], name.split()[0]) and
                    s_fill(page, SELECTOR_MAP["lastname"], name.split()[1]) and
                    s_fill(page, SELECTOR_MAP["email"], email) and
                    s_fill(page, SELECTOR_MAP["password"], password)):
                with LOCK:
                    BLACKLISTED.add(proxy)
                raise Exception("Form fields fill fail")
            s_select(page, SELECTOR_MAP["birthday_day"], str(random.randint(2,28)))
            s_select(page, SELECTOR_MAP["birthday_month"], str(random.randint(1,12)))
            s_select(page, SELECTOR_MAP["birthday_year"], str(random.randint(1990,2001)))
            s_click(page, SELECTOR_MAP["gender_male"])
            time.sleep(1)
            if not s_click(page, SELECTOR_MAP["submit"]):
                raise Exception("Submit fail")
            if progress:
                progress.update(task, description=f"[yellow]{status} OTP wait")
            time.sleep(8)
            otp = poll_otp(login, domain)
            if otp:
                s_fill(page, SELECTOR_MAP["otp_field"], otp)
                s_click(page, SELECTOR_MAP["submit"])
                time.sleep(4)
            else:
                with LOCK:
                    BLACKLISTED.add(proxy)
                raise Exception("OTP fail")
            pic = get_profile_pic()
            if pic:
                try:
                    page.goto("https://www.facebook.com/me")
                    time.sleep(3)
                    s_click(page, SELECTOR_MAP["profile_photo_edit"])
                    time.sleep(1)
                    el = None
                    for s in SELECTOR_MAP["profile_photo_file_input"]:
                        try:
                            el = page.query_selector(s)
                            if el:
                                break
                        except Exception:
                            continue
                    if el:
                        el.set_input_files(pic)
                        time.sleep(3)
                        s_click(page, SELECTOR_MAP["profile_photo_save"])
                except Exception as e:
                    log(f"Profile picture update error: {e}", "yellow")
            with LOCK:
                CREATED.append({"email": email, "password": password, "name": name, "proxy": proxy, "user_agent": ua})
            if progress:
                progress.update(task, description=f"[green]{status} OK")
            context.close()
            browser.close()
        if progress:
            progress.update(task, advance=1)
    except Exception as e:
        with LOCK:
            if proxy:
                BLACKLISTED.add(proxy)
        if progress:
            progress.update(task, description=f"[red]{status} Fail: {e}")
        time.sleep(2)
        if progress:
            progress.update(task, advance=1)

def main():
    ensure_folder_and_files()
    auto_download_images()
    proxies_raw = get_proxies()
    proxies = [p for p in proxies_raw if is_proxy_ok(p)]
    uas = get_user_agents()
    log(f"[FB Creator] Proxies: {len(proxies)} | UserAgents: {len(uas)} | ProfilePics: {len(os.listdir(PROFILE_PICS)) if os.path.exists(PROFILE_PICS) else 0}", "green")
    total = NUM_ACCOUNTS
    done = 0
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        "[progress.percentage]{task.percentage:>3.0f}%",
        TimeElapsedColumn(),
        console=console
    ) as progress:
        while done < total:
            with LOCK:
                available_proxies = [p for p in proxies if p not in BLACKLISTED]
            if not available_proxies and proxies:
                log("Sab proxies blacklist ho chuki hain. Script ruk rahi hai.", "red")
                break
            batch = min(THREADS, total - done)
            threads = []
            tsk = progress.add_task(f"[cyan]Batch {done+1}-{done+batch}", total=batch)
            for i in range(batch):
                with LOCK:
                    proxy = random.choice(available_proxies) if available_proxies else None
                ua = random.choice(uas)
                t = threading.Thread(target=create_account, args=(done + i + 1, proxy, ua, progress, tsk))
                t.start()
                threads.append(t)
                time.sleep(random.uniform(1, 2))
            for t in threads:
                t.join()
            done += batch
            progress.remove_task(tsk)
            with LOCK:
                save_csv(CREATED)
            if done < total:
                log(f"Batch done. Sleeping {BATCH_DELAY}s...", "yellow")
                time.sleep(BATCH_DELAY)
    log(f"Done! Accounts created: {done} | Blacklisted Proxies: {len(BLACKLISTED)}", "magenta")
    log(f"Saved to {CSV_FILE}", "cyan")

if __name__ == "__main__":
    main()
