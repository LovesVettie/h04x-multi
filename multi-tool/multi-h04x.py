import concurrent.futures, time, random, os
import colorama
from colorama import Fore
import time
import sys
import os 


def menu():
	global onstart
	print(f"""{Fore.MAGENTA}

                                                    
     HH   HH  00000      44   XX    XX 
     HH   HH 00   00    444    XX  XX  
     HHHHHHH 00   00  44  4     XXXX   
     HH   HH 00   00 44444444  XX  XX  
     HH   HH  00000     444   XX    XX 
                                                                  
                                                       

                      

{Fore.WHITE}[0] {Fore.MAGENTA}Cikis 		{Fore.WHITE}[5] {Fore.MAGENTA}IP Sorgu
{Fore.WHITE}[1] {Fore.MAGENTA}Webhook spam	{Fore.WHITE}[6] {Fore.MAGENTA}QR Code Oluşturucu
{Fore.WHITE}[2] {Fore.MAGENTA}Port Scanner	{Fore.WHITE}[7] {Fore.MAGENTA}Server Copy
{Fore.WHITE}[3] {Fore.MAGENTA}DDoS Tool  		{Fore.WHITE}[8] {Fore.MAGENTA}ID To Token
{Fore.WHITE}[4] {Fore.MAGENTA}URL TO IP   							
{Fore.MAGENTA}
""")

	command = input("	root/kali$")
	if command == "0":
		print("			root/kali$ Çıkmak İstediğine Eminmisin?")
		command = input("			> Evet İse Y / Hayır İse N >root/kali$")
		time.sleep(1)
	if command == "1":
		print("			root/kali$ Webhook spammer Başlatılıyor..")
		time.sleep(3)
		os.system('spammer.py')
	if command == "2":
		print("			root/kali$ Port Scanner Başlatılıyor..")
		os.system("portscan.py")
		onstart()
	if command == "4":
		print("			root/kali$ URL TO IP Başlatılıyor..")
		os.system("urlip.py")
		time.sleep(5)
		onstart()
	if command == "7":
		print("			root/kali$ Server Cloner Başlatılıyor..")
		os.system("servercloner.py")
		onstart()
	if command == "3":
		print("			root/kali$ DDoS Tool Başlatılıyor..")
		os.system("DDoS.py")
		onstart()
	if command == "5":
		print("			root/kali$ IP Sorgu Başlatılıyor.. ")
		os.system("ipsorgu.py")
		time.sleep(10)
	if command == "9":
		print("			root/kali$ Id To Token Başlatılıyor...")
		os.system("idtotoken.py")
		time.sleep(10)
		onstart()
	if command == "6":
		print("			root/kali$ QR Code Oluşturucu Başlatılıyor..")
		os.system("QRgen.py")
		onstart()
		time.sleep(1)
		time.sleep(2)
		onstart()
	if command == "y":
		time.sleep(1)
		print("			root/kali$ Görüşmek Üzere!")
		time.sleep(1)
		sys.exit(0)
	if command == "n":
		time.sleep(1)
		print("			root/kali$ Restart Atılıyor")
		time.sleep(1)
		onstart()




def onstart():
    cmd = 'mode 100,27' 
    os.system(cmd)
    os.system("cls && title H04X Multi Tool pack")
    menu()

onstart()
