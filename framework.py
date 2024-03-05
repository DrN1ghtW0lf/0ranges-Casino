from colorama import Fore, Style
import os

class bcolors:
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
    WHITE_B = '\033[37;1m'
    WHITE_U = '\033[37;4m'
    TURQUOISE = '\033[36m'
    ORANGE = '\e[38;5;214m'

def clear():
    os.system("clear")

def write(new_score):
    f = open("bank.txt", "w")
    f.write(str(new_score))

def read():
    f = open("bank.txt", "r")
    score = f.read()
    return score