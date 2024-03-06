#================= Imports =================#
from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR
from Games.framework import bcolors, clear, write
import platform # Checks OS
import time
import os

clear()
print("0range_'s Casino ©\n\n")

# Choose which game
input = str(input(f"Which game do you want to play ?\n{bcolors.OKBLUE}[Blackjack]{bcolors.ENDC} Blackjack\n{bcolors.OKBLUE}[Roulette]{bcolors.ENDC} Roulette\n{bcolors.OKBLUE}[Coinflip]{bcolors.ENDC} Coinflip\n{bcolors.WHITE_U}Input{bcolors.ENDC} - ")).lower()
match input:
    case "blackjack":
        time.sleep(0.25)
        if platform.system() == "Darwin": # Check is os is mac
            os.system("python3 Games/blackjack.py")
        else:
            os.system("python Games/blackjack.py")

    case "roulette":
        time.sleep(0.25)
        if platform.system() == "Darwin":
            os.system("python3 Games/blackjack.py")
        else:
            os.system("python Games/blackjack.py")

    case "coinflip":
        time.sleep(0.25)
        if platform.system() == "Darwin":
            os.system("python3 Games/blackjack.py")
        else:
            os.system("python Games/blackjack.py")

    case _ :
        print(f"\n{bcolors.WARNING}Type correctly dude.{bcolors.ENDC}")

if not os.path.exists("bank.txt"): # Check if bank.txt exists
    write("1000.0")