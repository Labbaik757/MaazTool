import time, random, string, threading, requests, csv, os
from PIL import Image, ImageDraw
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

NUM_ACCOUNTS = 2
THREADS = 2
BATCH_DELAY = 10
OTP_POLL = 4
OTP_ROUNDS = 30
CSV_FILE = "created_fb_accounts.csv"
PROFILE_PICS = "profile_pics"
UA_FILE = "useragents.txt"
MIN_PROFILE_PICS = 10

console = Console()
LOCK = threading.Lock()
CREATED = []

FALLBACK_UAS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
]

def log(msg, color="cyan"):
    console.print(f"[{color}]{msg}[/{color}]")

def ensure_folder_and_files():
    if not os.path.exists(PROFILE_PICS): os.makedirs(PROFILE_PICS)
    if not os.path.exists(UA_FILE): open(UA_FILE, "a").close()

def dummy_image(path, text="IMG"):
    img = Image.new("RGB", (128,128), random.choice([(80,150,200),(200,180,80),(150,80,180)]))
    d = ImageDraw.Draw(img)
    d.text((40,50), text, fill=(255,255,255))
    img.save(path)

def auto_download_images():
    images = [f for f in os.listdir(PROFILE_PICS) if f.lower().endswith((".jpg",".png",".jpeg",".jfif"))]
    missing = MIN_PROFILE_PICS - len(images)
    if missing <= 0: return
    log(f"Downloading {missing} profile images...", "yellow")
    sources = [
        "https://randomuser.me/api/",
        "https://api.dicebear.com/7.x/adventurer/png?seed={rnd}",
        "https://loremflickr.com/128/128/face?lock={rnd}",
        "https://avatars.dicebear.com/api/personas/{rnd}.png"
    ]
    for i in range(missing):
        success = False
        for src in sources:
            try:
                url = src.format(rnd=random.randint(1000,9999))
                if "randomuser" in url:
                    resp = requests.get(url, timeout=10)
                    imgurl = resp.json()["results"][0]["picture"]["large"]
                else:
                    imgurl = url
                imgdata = requests.get(imgurl, timeout=10).content
                ext = imgurl.split('.')[-1][:4]
                fname = f"profile_{int(time.time())}_{i}.{ext}"
                with open(os.path.join(PROFILE_PICS, fname), "wb") as f:
                    f.write(imgdata)
                success = True
                break
            except Exception as e:
                continue
        if not success:
            fname = f"profile_{int(time.time())}_{i}.png"
            dummy_image(os.path.join(PROFILE_PICS, fname))
    log("Profile images download complete.", "green")

def get_user_agents():
    try:
        with open(UA_FILE, "r") as f:
            uas = [x.strip() for x in f if x.strip()]
    except Exception: uas = []
    if not uas:
        uas = FALLBACK_UAS
        with open(UA_FILE, "w") as f:
            for ua in uas: f.write(ua + "\n")
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
            res = requests.get(url)
            messages = res.json()
            if messages:
                msg_id = messages[0]['id']
                msg_url = f"https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={msg_id}"
                otp = ''.join(filter(str.isdigit, requests.get(msg_url).json().get('body', '')))
                if len(otp) >= 5: return otp[:6]
        except: continue
    return None

def save_csv(accounts):
    file_exists = os.path.exists(CSV_FILE)
    with open(CSV_FILE, "a", newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=['email', 'password', 'name', 'user_agent'])
        if not file_exists: w.writeheader()
        for a in accounts: w.writerow(a)

def get_profile_pic():
    pics = [os.path.join(PROFILE_PICS, f) for f in os.listdir(PROFILE_PICS) if f.lower().endswith((".jpg",".png",".jpeg",".jfif"))]
    if pics: return random.choice(pics)
    return None

def s_fill(page, sel, val): return any([page.fill(s, val, timeout=3000) or True for s in sel if page.query_selector(s)])
def s_click(page, sel): return any([page.click(s, timeout=3000) or True for s in sel if page.query_selector(s)])
def s_select(page, sel, val): return any([page.select_option(s, val) or True for s in sel if page.query_selector(s)])

def create_account(idx, ua, progress=None, task=None):
    name = gen_name()
    password = gen_pass()
    login, domain, email = temp_mail()
    status = f"{idx}. {email}"
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(user_agent=ua)
            page = context.new_page()
            page.goto("https://www.facebook.com/reg", timeout=20000)
            time.sleep(2)
            if not (s_fill(page, [
                'input[name="firstname"]', 'input[aria-label="First name"]'
            ], name.split()[0]) and
            s_fill(page, [
                'input[name="lastname"]', 'input[aria-label="Surname"]'
            ], name.split()[1]) and
            s_fill(page, [
                'input[name="reg_email__"]', 'input[aria-label="Mobile number or email address"]'
            ], email) and
            s_fill(page, [
                'input[name="reg_passwd__"]', 'input[type="password"]'
            ], password)):
                raise Exception("Form fields fail")
            s_select(page, ['select[name="birthday_day"]'], str(random.randint(2,28)))
            s_select(page, ['select[name="birthday_month"]'], str(random.randint(1,12)))
            s_select(page, ['select[name="birthday_year"]'], str(random.randint(1990,2001)))
            s_click(page, ['input[name="sex"][value="2"]', 'input[aria-label="Male"]'])
            time.sleep(1)
            if not s_click(page, ['button[name="websubmit"]', 'button[type="submit"]']): raise Exception("Submit fail")
            if progress: progress.update(task, description=f"[yellow]{status} OTP wait")
            time.sleep(8)
            otp = poll_otp(login, domain)
            if otp:
                s_fill(page, ['input[name="code"]', 'input[aria-label="Confirmation code"]'], otp)
                s_click(page, ['button[name="websubmit"]', 'button[type="submit"]'])
                time.sleep(4)
            else:
                raise Exception("OTP fail")
            pic = get_profile_pic()
            if pic:
                try:
                    page.goto("https://www.facebook.com/me")
                    time.sleep(3)
                    s_click(page, [
                        'div[aria-label="Edit profile photo"]', 
                        'div[aria-label="Update profile picture"]'
                    ])
                    time.sleep(1)
                    el = next((page.query_selector(s) for s in [
                        'input[type="file"]'
                    ] if page.query_selector(s)), None)
                    if el: el.set_input_files(pic)
                    time.sleep(3)
                    s_click(page, [
                        'div[aria-label="Save"]', 
                        'div[aria-label="Apply"]'
                    ])
                except: pass
            with LOCK:
                CREATED.append({"email": email, "password": password, "name": name, "user_agent": ua})
            if progress: progress.update(task, description=f"[green]{status} OK")
        if progress: progress.update(task, advance=1)
    except Exception as e:
        if progress: progress.update(task, description=f"[red]{status} Fail: {e}")
        time.sleep(2)
        if progress: progress.update(task, advance=1)

def main():
    ensure_folder_and_files()
    auto_download_images()
    uas = get_user_agents()
    log(f"[FB Creator] UserAgents: {len(uas)} | ProfilePics: {len(os.listdir(PROFILE_PICS)) if os.path.exists(PROFILE_PICS) else 0}", "green")
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
            batch = min(THREADS, total-done)
            threads = []
            tsk = progress.add_task(f"[cyan]Batch {done+1}-{done+batch}", total=batch)
            for i in range(batch):
                ua = random.choice(uas)
                t = threading.Thread(target=create_account, args=(done+i+1, ua, progress, tsk))
                t.start()
                threads.append(t)
                time.sleep(random.uniform(1,2))
            for t in threads: t.join()
            done += batch
            progress.remove_task(tsk)
            save_csv(CREATED)
            if done < total:
                log(f"Batch done. Sleeping {BATCH_DELAY}s...", "yellow")
                time.sleep(BATCH_DELAY)
    log(f"Done! Accounts created: {len(CREATED)}", "magenta")
    log(f"Saved to {CSV_FILE}", "cyan")

if __name__ == "__main__":
    main()
