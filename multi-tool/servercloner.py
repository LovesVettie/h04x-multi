mytitle = "Server Cloner BY H04X"
from os import system
system("title "+mytitle)
import psutil
from pypresence import Presence
import time
import sys
client_id = 'Hesap ID'
import discord
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
from cloner import Clone
import requests

client = discord.Client(intents=discord.Intents.default())
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
print(f"""{Fore.GREEN}

██████╗░░█████╗░  ░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗  ██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗
██║░░██║██║░░╚═╝  ██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██████╔╝
██║░░██║██║░░██╗  ██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██╔══██╗
██████╔╝╚█████╔╝  ╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██║░░██║
╚═════╝░░╚════╝░  ░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
             [Author h04x#1773 & shewse#1000], Contact [h04x#1773,shewse#1000]
                                                                      
{Style.RESET_ALL}
{Fore.YELLOW}> Developed BY h04x#1773{Style.RESET_ALL}
{Fore.YELLOW}> Discord https://discord.gg/PQknMWQyBv{Style.RESET_ALL}
{Fore.GREEN}> Program Sorunsuz Çalışıyor...{Style.RESET_ALL}
        """)


token = input(f'h04x|DC Cloner| Token -->')
guild_s = input('h04x|DC Cloner|Kopyalanacak Sunucu ID -->') #Coded BY H04X
guild = input('h04x|DC Cloner|Yapıştırılacak Sunucu ID -->') #Coded BY H04X
input_guild_id = guild_s  #Kopyaladığın Sunucu
output_guild_id = guild  #Yapıştırdığın Sunucu
token = token  #Hesabının Tokeni

print("  ")
print("  ")

@client.event
async def on_ready():
    extrem_map = {}
    print(f"Giriş Yapılan Hesap: {client.user}")
    print("Sunucu Kopyalanıyor")
    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)
    print(f"""{Fore.GREEN}



████████████████████████████████████████████████████████████
█▄─█─▄█─▄▄─█▄─▄▄─█▄─█─▄██▀▄─██▄─▄████▀▄─██▄─▀█▄─▄█▄─▄▄▀█▄─▄█
██─▄▀██─██─██─▄▄▄██▄─▄███─▀─███─██▀██─▀─███─█▄▀─███─██─██─██
▀▄▄▀▄▄▀▄▄▄▄▀▄▄▄▀▀▀▀▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▀▀▄▄▄▀                   


    {Style.RESET_ALL}""")
    await asyncio.sleep(5)
    client.close()


client.run(token, bot=False) #Coded BY H04X
