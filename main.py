import os
try:
  import requests
  import colorama
  from colorama import Fore
except ImportError:
  os.system('pip install requests colorama')
  exit()

colorama.init()

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

clear()
print(Fore.RED + "Webhook Spammer made by [encq]")

webhook = input(Fore.RED + "Webhook >> " + Fore.WHITE)

while True:
  res = requests.post(webhook, json={"content":"@everyone nigger gets fucked? 😂😂 discord.gg/kiyubot https://github.com/dedsociety"})
  print(Fore.RED + "sent " + str(res.status_code))
