import os
import time
import random
import string
import json
import threading
import requests
from rich import print
from playwright.sync_api import sync_playwright

# Global Variables
CREATED = 0
LOCK = threading.Lock()

# Get random proxy
def get_proxy():
    try:
        res = requests.get("https://www.proxy-list.download/api/v1/get?type=https").text
        proxies = res.strip().split("\r\n")
        return random.choice(proxies)
    except:
        return None

# Generate random user info
def generate_name():
    fname = random.choice(["Ali", "Ahmed", "Usman", "Hamza", "Fahad", "Maaz"])
    lname = random.choice(["Khan", "Malik", "Butt", "Chaudhary", "Nazeer"])
    return f"{fname} {lname}"

def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

# Create TempMail (1secmail)
def create_temp_mail():
    login = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = random.choice(["1secmail.com", "1secmail.org", "1secmail.net"])
    return login, domain, f"{login}@{domain}"

# Check OTP from inbox
def fetch_otp(login, domain):
    url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}"
    for _ in range(20):
        time.sleep(5)
        try:
            res = requests.get(url).json()
            if res:
                msg_id = res[0]['id']
                msg_url = f"https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={msg_id}"
                msg = requests.get(msg_url).json()
                body = msg['body']
                otp = ''.join(filter(str.isdigit, body))
                if len(otp) >= 5:
                    return otp[:6]
        except:
            continue
    return None

# Account Creator Logic
def create_account(thread_id):
    global CREATED

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        # Set proxy if available
        proxy = get_proxy()
        if proxy:
            context = browser.new_context(proxy={"server": f"http://{proxy}"})

        page = context.new_page()

        # Generate details
        full_name = generate_name()
        password = generate_password()
        login, domain, email = create_temp_mail()

        try:
            print(f"[yellow]({thread_id}) Creating account for: [bold]{email}[/bold][/yellow]")
            page.goto("https://www.facebook.com/reg", timeout=60000)
            time.sleep(3)

            # Fill details
            page.fill('input[name=firstname]', full_name.split()[0])
            page.fill('input[name=lastname]', full_name.split()[1])
            page.fill('input[name=reg_email__]', email)
            page.fill('input[name=reg_passwd__]', password)

            time.sleep(2)
            page.keyboard.press("Tab")  # Let FB detect email

            # Random birthdate
            page.select_option('select[name=birthday_day]', str(random.randint(1, 28)))
            page.select_option('select[name=birthday_month]', str(random.randint(1, 12)))
            page.select_option('select[name=birthday_year]', str(random.randint(1988, 2003)))
            page.click('input[value="2"]')  # Male

            # Submit
            page.click('button[name=websubmit]')
            time.sleep(10)

            # OTP stage
            otp = fetch_otp(login, domain)
            if otp:
                print(f"[green]({thread_id}) OTP received: {otp}[/green]")
                page.fill('input[name=code]', otp)
                page.click('button[name=confirm]')
                time.sleep(10)

                with LOCK:
                    CREATED += 1
                    with open("maaz_auto.txt", "a") as f:
                        f.write(f"{email}|{password}\n")
                    print(f"[bold green]({thread_id}) ✅ Account Created: {email}[/bold green]")
            else:
                print(f"[red]({thread_id}) ❌ OTP Not received, skipping...[/red]")

        except Exception as e:
            print(f"[red]({thread_id}) Error: {e}[/red]")
        finally:
            context.close()
            browser.close()

# Dashboard UI
def dashboard():
    os.system("clear")
    print("[bold cyan]\n   MAAZ AUTO FB CREATOR TOOL v2.3[/bold cyan]")
    print("[white]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/white]")
    print("[yellow]• Proxy Enabled     :[/yellow] ✅")
    print("[yellow]• OTP via TempMail :[/yellow] ✅")
    print("[yellow]• Headful Browser  :[/yellow] ✅")
    print("[yellow]• Multithreaded    :[/yellow] ✅")
    print("[white]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/white]\n")

    try:
        threads = int(input("[bold green]Enter number of accounts to create:[/bold green] "))
    except:
        threads = 1

    thread_list = []
    for i in range(threads):
        t = threading.Thread(target=create_account, args=(i+1,))
        t.start()
        thread_list.append(t)
        time.sleep(1)

    for t in thread_list:
        t.join()

    print(f"\n[bold cyan]✨ Done. Total Accounts Created: {CREATED}[/bold cyan]")

if __name__ == "__main__":
    dashboard()
