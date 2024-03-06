from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR
from colorama import Fore, Style
import time
import os

class bcolors: # Terminal Colors
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLACK = '\033[30m'
    BLACK_B = '\033[30;1m'
    RED_B = '\033[31;1m'
    GREEN_B = '\033[32;1m'
    PINK = '\033[35m'
    PINK_B = '\033[35;1m'
    WHITE_B = '\033[37;1m'
    WHITE_U = '\033[37;4m'
    TURQUOISE = '\033[36m'
    TURQUOISE_B = '\033[36;1m'
    ORANGE = '\e[38;5;214m'

def clear(): # clears the terminal
    os.system("clear")

def read(): # Stores bank.txt content to value
    f = open("bank.txt", "r")
    score = f.read()
    return score

def write(new_score): # Overwrites bank.txt with a new score
    os.chmod("bank.txt", S_IWUSR|S_IREAD)
    f = open("bank.txt", "w")
    f.write(str(new_score))
    os.chmod("bank.txt", S_IREAD|S_IRGRP|S_IROTH)

def end_print(parameter): # Progressively prints the end text
    match parameter:
        case "win":
            time.sleep(0.25)
            print(f"{bcolors.GREEN_B}.------..------..------.{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.GREEN_B}|W.--. ||I.--. ||N.--. |{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.GREEN_B}| :/\: || (\/) || :(): |{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.GREEN_B}| :\/: || :\/: || ()() |{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.GREEN_B}| '--'W|| '--'I|| '--'N|{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.GREEN_B}`------'`------'`------'{bcolors.ENDC}")

        case "lose":
            time.sleep(0.25)
            print(f"{bcolors.RED_B}.------..------..------..------.{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.RED_B}|L.--. ||O.--. ||S.--. ||E.--. |{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.RED_B}| :/\: || :/\: || :/\: || (\/) |{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.RED_B}| (__) || :\/: || :\/: || :\/: |{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.RED_B}| '--'L|| '--'O|| '--'S|| '--'E|{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.RED_B}`------'`------'`------'`------'{bcolors.ENDC}")

        case "draw":
            time.sleep(0.25)
            print(f"{bcolors.TURQUOISE_B}.------..------..------..------.{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.TURQUOISE_B}|D.--. ||R.--. ||A.--. ||W.--. |{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.TURQUOISE_B}| :/\: || :(): || (\/) || :/\: |{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.TURQUOISE_B}| (__) || ()() || :\/: || :\/: |{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.TURQUOISE_B}| '--'D|| '--'R|| '--'A|| '--'W|{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.TURQUOISE_B}`------'`------'`------'`------'{bcolors.ENDC}")

        case "jackpot":
            time.sleep(0.25)
            print(f"{bcolors.PINK_B}.------..------..------..------..------..------..------.{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.PINK_B}|J.--. ||A.--. ||C.--. ||K.--. ||P.--. ||O.--. ||T.--. |{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.PINK_B}| :(): || (\/) || :/\: || :/\: || :/\: || :/\: || :/\: |{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.PINK_B}| ()() || :\/: || :\/: || :\/: || (__) || :\/: || (__) |{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.PINK_B}| '--'J|| '--'A|| '--'C|| '--'K|| '--'P|| '--'O|| '--'T|{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.PINK_B}`------'`------'`------'`------'`------'`------'`------'{bcolors.ENDC}")

        case "red":
            time.sleep(0.25)
            print(f"{bcolors.RED_B}.------..------..------.{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.RED_B}|R.--. ||E.--. ||D.--. |{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.RED_B}| :(): || (\/) || :/\: |{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.RED_B}| ()() || :\/: || (__) |{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.RED_B}| '--'R|| '--'E|| '--'D|{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.RED_B}`------'`------'`------'{bcolors.ENDC}")

        case "black":
            time.sleep(0.25)
            print(f"{bcolors.BLACK_B}.------..------..------..------..------.{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.BLACK_B}|B.--. ||L.--. ||A.--. ||C.--. ||K.--. |{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.BLACK_B}| :(): || :/\: || (\/) || :/\: || :/\: |{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.BLACK_B}| ()() || (__) || :\/: || :\/: || :\/: |{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.BLACK_B}| '--'B|| '--'L|| '--'A|| '--'C|| '--'K|{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.BLACK_B}`------'`------'`------'`------'`------'{bcolors.ENDC}")

        case "green":
            time.sleep(0.25)
            print(f"{bcolors.GREEN_B}.------..------..------..------..------.{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.GREEN_B}|G.--. ||R.--. ||E.--. ||E.--. ||N.--. |{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.GREEN_B}| :/\: || :(): || (\/) || (\/) || :(): |{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.GREEN_B}| :\/: || ()() || :\/: || :\/: || ()() |{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.GREEN_B}| '--'G|| '--'R|| '--'E|| '--'E|| '--'N|{bcolors.ENDC}")
            time.sleep(0.25)
            print(f"{bcolors.GREEN_B}`------'`------'`------'`------'`------'{bcolors.ENDC}")

        case _ :
            print(f"{bcolors.WARNING}Type correctly{bcolors.ENDC}")