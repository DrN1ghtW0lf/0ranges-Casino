#================= Imports =================#
from Games.framework import bcolors, clear
import time
import os

clear()
print("Roulette by 0range_ ©\n\n")

input = str(input(f"Which game do you want to play ?\n{bcolors.OKBLUE}[Blackjack]{bcolors.ENDC} Blackjack\n{bcolors.OKBLUE}[Roulette]{bcolors.ENDC} Roulette\n{bcolors.WHITE_U}Input{bcolors.ENDC} - ")).lower()
match input:
    case "blackjack":
        time.sleep(0.25)
        os.system("python3 Games/blackjack.py")
    case "roulette":
        time.sleep(0.25)
        os.system("python3 Games/roulette.py")