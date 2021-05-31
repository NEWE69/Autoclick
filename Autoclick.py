"""
Created by NEWE
Telegram : https://t.me/MondialMarketplace0
31/05/2021
"""

import keyboard
import mouse
import time
import ctypes
from colorama import init, Fore


def autoclicker(k, c):
    while True:
        keyboard.wait(k)
        mouse.click('left')
        time.sleep(c)


init(convert=True)
ctypes.windll.kernel32.SetConsoleTitleW("Autoclick By NEWE")
text = """

 ▄▄▄       █    ██ ▄▄▄█████▓ ▒█████   ▄████▄   ██▓     ██▓ ▄████▄   ██ ▄█▀
▒████▄     ██  ▓██▒▓  ██▒ ▓▒▒██▒  ██▒▒██▀ ▀█  ▓██▒    ▓██▒▒██▀ ▀█   ██▄█▒ 
▒██  ▀█▄  ▓██  ▒██░▒ ▓██░ ▒░▒██░  ██▒▒▓█    ▄ ▒██░    ▒██▒▒▓█    ▄ ▓███▄░ 
░██▄▄▄▄██ ▓▓█  ░██░░ ▓██▓ ░ ▒██   ██░▒▓▓▄ ▄██▒▒██░    ░██░▒▓▓▄ ▄██▒▓██ █▄ 
 ▓█   ▓██▒▒▒█████▓   ▒██▒ ░ ░ ████▓▒░▒ ▓███▀ ░░██████▒░██░▒ ▓███▀ ░▒██▒ █▄
 ▒▒   ▓▒█░░▒▓▒ ▒ ▒   ▒ ░░   ░ ▒░▒░▒░ ░ ░▒ ▒  ░░ ▒░▓  ░░▓  ░ ░▒ ▒  ░▒ ▒▒ ▓▒
  ▒   ▒▒ ░░░▒░ ░ ░     ░      ░ ▒ ▒░   ░  ▒   ░ ░ ▒  ░ ▒ ░  ░  ▒   ░ ░▒ ▒░
  ░   ▒    ░░░ ░ ░   ░      ░ ░ ░ ▒  ░          ░ ░    ▒ ░░        ░ ░░ ░ 
      ░  ░   ░                  ░ ░  ░ ░          ░  ░ ░  ░ ░      ░  ░   
                                     ░                    ░               By NEWE


"""
print(Fore.RED + text + Fore.WHITE)

key = input("Setup autoclick key :")

clicktemp = float(input("Time between clicks (0 to 0.5), 0 = fast / 0.5 = very low :"))

print("autoclick launched, (tip, don't keep pressing the key to avoid having a fixed cps)")

autoclicker(key, clicktemp)
