import requests
import os
import sys
import time
import colorama
from colorama import init, Fore, Style, Back
import threading

os.system("title H04X WebHook Spammer Loading...")
print(f"""
{Fore.MAGENTA}

██╗░░██╗░█████╗░░░██╗██╗██╗░░██╗      ██╗░░██╗  
██║░░██║██╔══██╗░██╔╝██║╚██╗██╔╝      ╚██╗██╔╝  
███████║██║░░██║██╔╝░██║░╚███╔╝░      ░╚███╔╝░  
██╔══██║██║░░██║███████║░██╔██╗░      ░██╔██╗░  
██║░░██║╚█████╔╝╚════██║██╔╝╚██╗      ██╔╝╚██╗  
╚═╝░░╚═╝░╚════╝░░░░░░╚═╝╚═╝░░╚═╝      ╚═╝░░╚═╝  

░██████╗██╗░░██╗███████╗░██╗░░░░░░░██╗░██████╗███████╗
██╔════╝██║░░██║██╔════╝░██║░░██╗░░██║██╔════╝██╔════╝
╚█████╗░███████║█████╗░░░╚██╗████╗██╔╝╚█████╗░█████╗░░
░╚═══██╗██╔══██║██╔══╝░░░░████╔═████║░░╚═══██╗██╔══╝░░
██████╔╝██║░░██║███████╗░░╚██╔╝░╚██╔╝░██████╔╝███████╗
╚═════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═════╝░╚══════╝
                                                 Loading...
								[Coded BY h04x#1773], [Designed BY shewse#1000]
							       [ Contact: h04x#1773 or shewse#1000 ]
""")

message = input("H04X Webhook spammer| Spam Atılacak Mesaj -----> ")
webhookurl = input("H04X Webhook spammer| Webhook URL -----> ")

def spam(message, webhookurl):
    while True:
        try:
            r = requests.post(webhookurl, json={"content": message})
            s = [200, 201, 204]
            if r.status_code in s:
                print(Fore.GREEN + "Mesaj Gönderildi")
            elif r.status_code == 429:
                b = r.json
                print(Fore.RED + f"Zaman Aşımına Uğradı, {b['retry_after']} Saniye Sonra Tekrar Dene")

        except:
            print(Fore.RED + "Kötü Webhook > " +webhookurl)
            time.sleep(5)
            exit()

def spamming():
    for i in range(2):
        threading.Thread(target=spam, args=(message, webhookurl)).start()
spammed = 100

while spammed == 100:
    spam(message, webhookurl)