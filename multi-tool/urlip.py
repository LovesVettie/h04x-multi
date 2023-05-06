import socket

website = input("H04X/URL-TO-IP-Site Linki Gir: ")

full_web_url = f"www.{website}.com"

ip_add = socket.gethostbyname(full_web_url)

print("Bulunan IP Adresi:", ip_add)