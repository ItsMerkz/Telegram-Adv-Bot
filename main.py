import time
import weakref
from pkg_resources import EggMetadata
from scipy.fft import fftfreq
from telethon import TelegramClient, sync
import json 
import datetime
import os 
import colorama 
from colorama import Fore, init
from torch import fbgemm_linear_fp16_weight_fp32_activation

init()

config = json.load(open("config.json", encoding="utf-8"))
api_id = config["api_id"] 
api_hash = config["api_hash"] 
interval = int(config["interval"])
msg = config["message"]
groups = config["groups"]

os.system("cls")

print(f""" {Fore.BLUE}
  ______         __                   _______               __     
 /      \       /  |                 /       \             /  |    
/$$$$$$  |  ____$$ | __     __       $$$$$$$  |  ______   _$$ |_   
$$ |__$$ | /    $$ |/  \   /  |      $$ |__$$ | /      \ / $$   |  
$$    $$ |/$$$$$$$ |$$  \ /$$/       $$    $$< /$$$$$$  |$$$$$$/   
$$$$$$$$ |$$ |  $$ | $$  /$$/        $$$$$$$  |$$ |  $$ |  $$ | __ 
$$ |  $$ |$$ \__$$ |  $$ $$/         $$ |__$$ |$$ \__$$ |  $$ |/  |
$$ |  $$ |$$    $$ |   $$$/          $$    $$/ $$    $$/   $$  $$/ 
$$/   $$/  $$$$$$$/     $/           $$$$$$$/   $$$$$$/     $$$$/  
{Fore.RESET}""")

sentmsgs = 0 
print(msg)

client = TelegramClient('AdvBot', api_id, api_hash).start()
def main(): 
  global sentmsgs 
  for group in groups:
    client. send_message(entity=group, message=msg)
    now = datetime.datetime.now()
    print(f"{Fore.RED}{now} | Message Sent{Fore.RESET}") 
    sentmsgs += 1
    os.system(f"title Sent - {sentmsgs}")
  time.sleep(interval)

while True:
  main()
