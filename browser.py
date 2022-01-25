import os
import sys
import requests
from colorama import Fore
from bs4 import BeautifulSoup as bs


arg = sys.argv[1]
if os.access(arg, os.F_OK):
    pass
else:
    os.makedirs(arg, exist_ok=True)
while True:
    in_url = input("> ")
    if in_url == "exit":
        print("Error")
        break
    if "https://" not in in_url:
        url = "https://" + in_url
    else:
        url = in_url
        in_url.replace('https://', '', 1)
    try:
        r = requests.get(url)
    except OSError:
        print("Incorrect URL")
    else:
        if r:
            soup = bs(r.content, 'html.parser')
            tags = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'ol', 'a'])
            for clean_text in tags:
                # marking the links
                if clean_text.name == 'a':
                    print(Fore.BLUE + clean_text.text + Fore.RESET) 
                else:
                    print(clean_text.text)
            file_name = in_url.rsplit(".", 1)
            with open(f'{arg}/{file_name[0]}', "at", encoding='utf-8') as f:
                f.write(soup.get_text())
            print(soup.get_text())
        else:
            print(f"Error 404: {url} is not found :(")
