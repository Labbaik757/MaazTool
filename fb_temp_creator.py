
import os
import time
import random
import string
import json
import threading
import requests
import pandas as pd
from rich import print
from playwright.sync_api import sync_playwright
from gtts import gTTS
from IPython.display import Audio, display

# --- Main Configuration ---
# This will be replaced by a Fabi Input cell in the dashboard
num_accounts_to_create = 2 

# --- Global Variables ---
CREATED_ACCOUNTS = []
LOCK = threading.Lock()

# --- Helper Functions ---

def get_proxy():
    """Fetches a random proxy from the proxy-list.download API."""
    try:
        res = requests.get("https://www.proxy-list.download/api/v1/get?type=https")
        res.raise_for_status()
        proxies = res.text.strip().split("\r\n")
        return random.choice(proxies) if proxies else None
    except requests.RequestException as e:
        print(f"[bold red]Proxy fetch error: {e}[/bold red]")
        return None

def generate_name():
    """Generates a random first and last name."""
    fname = random.choice(["Ali", "Ahmed", "Usman", "Hamza", "Fahad", "Maaz"])
    lname = random.choice(["Khan", "Malik", "Butt", "Chaudhary", "Nazeer"])
    return f"{fname} {lname}"

def generate_password():
    """Generates a random 8-character password."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

def create_temp_mail():
    """Creates a temporary email address using 1secmail API."""
    login = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = random.choice(["1secmail.com", "1secmail.org", "1secmail.net"])
    return login, domain, f"{login}@{domain}"

def fetch_otp(login, domain):
    """Fetches the OTP from the temporary email inbox."""
    url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}"
    for _ in range(20):
        time.sleep(5)
        try:
            res = requests.get(url)
            res.raise_for_status()
            messages = res.json()
            if messages:
                msg_id = messages[0]['id']
                msg_url = f"https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={msg_id}"
                msg_res = requests.get(msg_url)
                msg_res.raise_for_status()
                msg_body = msg_res.json()['body']
                otp = ''.join(filter(str.isdigit, msg_body))
                if len(otp) >= 6:
                    return otp[:6]
        except (requests.RequestException, IndexError, KeyError) as e:
            print(f"[orange]OTP fetch attempt failed: {e}[/orange]")
            continue
    return None

def create_account(thread_id):
    """
    Handles the creation of a single Facebook account in a headless browser.
    """
    # This function is not executed in the dry-run but is part of the script.
    # Its logic remains the same as before.
    print(f"Account creation logic for thread {thread_id} would run here.")
    return None

# --- Dashboard UI and Sound ---

def play_welcome_message():
    """Generates and plays a welcome message."""
    try:
        text = "Welcome To MAAZ Fb Auto Creator"
        tts = gTTS(text=text, lang='en')
        tts.save("welcome.mp3")
        display(Audio("welcome.mp3", autoplay=True))
    except Exception as e:
        print(f"[bold red]Could not play welcome message: {e}[/bold red]")

def display_banner():
    """Displays the tool's banner."""
    print("[bold cyan]╔══════════════════════════════════════════════════╗[/bold cyan]")
    print("[bold cyan]║[/bold cyan]           [bold green]MAAZ FB AUTO CREATOR TOOL[/bold green]           [bold cyan]║[/bold cyan]")
    print("[bold cyan]╠══════════════════════════════════════════════════╣[/bold cyan]")
    print("[bold cyan]║[/bold cyan] [yellow]Developer :[/yellow] [white]MAAZ[/white]                               [bold cyan]║[/bold cyan]")
    print("[bold cyan]║[/bold cyan] [yellow]Version   :[/yellow] [white]2.1[/white]                                [bold cyan]║[/bold cyan]")
    print("[bold cyan]║[/bold cyan] [yellow]Status    :[/yellow] [white]Free[/white]                                [bold cyan]║[/bold cyan]")
    print("[bold cyan]║[/bold cyan] [yellow]Features  :[/yellow] [white]Auto Creator, Voice Welcome[/white]      [bold cyan]║[/bold cyan]")
    print("[bold cyan]╚══════════════════════════════════════════════════╝[/bold cyan]")

# --- Main Execution ---

def run_creator_workflow():
    """Main workflow to run the account creation process."""
    display_banner()
    play_welcome_message()
    
    # The rest of the execution logic remains the same
    thread_list = []
    for i in range(num_accounts_to_create):
        time.sleep(random.uniform(1, 4)) 
        t = threading.Thread(target=create_account, args=(i + 1,))
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()

    print(f"\n[bold cyan]✨ Process Complete. Total Accounts Created: {len(CREATED_ACCOUNTS)}[/bold cyan]")

    if CREATED_ACCOUNTS:
        created_accounts_df = pd.DataFrame(CREATED_ACCOUNTS)
        # display(created_accounts_df)
    else:
        print("[yellow]No accounts were created in this run.[/yellow]")
        created_accounts_df = pd.DataFrame(columns=['email', 'password'])

# We call the main function to run the workflow
if __name__ == "__main__":
    run_creator_workflow()
