import os
import base64
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
init()

banner = (Fore.MAGENTA + """
 __     _____        ______   ______        ______   ______     __  __     ______     __   __    
/\ \   /\  __-.     /\__  _\ /\  __ \      /\__  _\ /\  __ \   /\ \/ /    /\  ___\   /\ "-.\ \   
\ \ \  \ \ \/\ \    \/_/\ \/ \ \ \/\ \     \/_/\ \/ \ \ \/\ \  \ \  _"-.  \ \  __\   \ \ \-.  \  
 \ \_\  \ \____-       \ \_\  \ \_____\       \ \_\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_\\"\_\ 
  \/_/   \/____/        \/_/   \/_____/        \/_/   \/_____/   \/_/\/_/   \/_____/   \/_/ \/_/ 
                                                                                                 
""" + Fore.LIGHTCYAN_EX)
print(banner)
print("Bir ID Gir")
userid = input("root/kali$ ")
encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
print(f'\nroot/kali$ {encodedStr}')
os.system('pause >nul')