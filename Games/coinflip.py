#================= Imports =================#
from framework import bcolors, clear, read, write,end_print
from random import randint
import time
import os

#================= Default Variables =================#
money = float(read())
rolls = randint(1,10)

# Start
clear()
print("Coinflip by 0range_ ©\n\n")

bet = float(input(f"Place your {bcolors.GREEN_B}bet{bcolors.ENDC} ({bcolors.WHITE_U}<{money}{bcolors.ENDC}) : "))
if bet > money:
    print(f"{bcolors.WARNING}You're poor.{bcolors.ENDC}")
    exit()

print(f"{bcolors.WHITE_B}Where{bcolors.ENDC} do you place your bet :")
print(f"{bcolors.OKBLUE}[Heads]{bcolors.ENDC} Heads")
print(f"{bcolors.OKBLUE}[Tails]{bcolors.ENDC} Tails")
bet_location = input(f"{bcolors.WHITE_U}Input{bcolors.ENDC} - ").lower()

time.sleep(0.25)
print(f"\n{bcolors.OKCYAN}Rolling...{bcolors.ENDC}\n")
time.sleep(0.15)

for i in range(rolls):
    time.sleep(0.1)
    coin_side = randint(1,2)
    if i == rolls - 1:
        time.sleep(0.15)
        if coin_side == 1:
            coin_side = "heads\n"
        else:
            coin_side = "tails\n"

        if bet_location == coin_side:
            money += bet*2
            end_print("win")
        else:
            money -= bet
            end_print("lose")
    else:
        if coin_side == 1:
            coin_side = "heads"
            print(f"{bcolors.BLACK_B}Heads{bcolors.ENDC}")
        else:
            coin_side = "tails"
            print(f"{bcolors.WHITE_B}Tails{bcolors.ENDC}")

old_money = float(read())
cashout = money - old_money
if cashout > 0:
    print(f"\n\n{bcolors.GREEN_B}+{cashout}{bcolors.ENDC}")
else:
    print(f"\n\n{bcolors.RED_B}{cashout}{bcolors.ENDC}")
print(money)
write(money)