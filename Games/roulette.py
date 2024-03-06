#================= Imports =================#
from framework import bcolors, clear, read, write,end_print
from random import randint
import time
import os

#================= Default Variables =================#
rolls = randint(20,35) # Number of visual rolls
money = float(read())

#================= Function =================#
def print_numbers(): # Prints the number in/and their color
    if number == 35:
        print(f"{bcolors.GREEN_B}{number}{bcolors.ENDC} || Green")
    elif number % 2 == 0:
        print(f"{bcolors.RED_B}{number}{bcolors.ENDC} || Red")
    else:
        print(f"{bcolors.BLACK_B}{number}{bcolors.ENDC} || Black")

def end(money, bet, bet_location): # Same a print_numbers() func but with cash out
    if number == 0:
        print(f"{bcolors.GREEN_B}{number}{bcolors.ENDC} || Green")
        end_print("green")

        if bet_location == "green":
            money += bet*35
        elif bet_location == "0":
            money += bet*70
        else:
            money -= bet

    elif number % 2 == 0:
        print(f"{bcolors.RED_B}{number}{bcolors.ENDC} || Red")
        end_print("red")
        
        if bet_location == "red":
            money += bet*1.5
        else :
            money -= bet

    else:
        print(f"{bcolors.BLACK_B}{number}{bcolors.ENDC} || Black")
        end_print("black")
        
        if bet_location == "black":
            money += bet*1.5
        else:
            money -= bet
    
    if bet_location == str(number):
        money += bet*35

    # Print cashout and balance
    old_money = float(read())
    cashout = money - old_money
    if cashout > 0:
        print(f"\n\n{bcolors.GREEN_B}+{cashout}{bcolors.ENDC}")
    else:
        print(f"\n\n{bcolors.RED_B}{cashout}{bcolors.ENDC}")

    print(f"Your balance : {bcolors.WHITE_B}{money}{bcolors.ENDC}")
    write(money)

clear()
print("Roulette by 0range_ ©\n\n")

# Get the bet
bet = float(input(f"Place your {bcolors.GREEN_B}bet{bcolors.ENDC} ({bcolors.WHITE_U}<{money}{bcolors.ENDC}) : "))
if bet > money:
    print(f"{bcolors.WARNING}You're poor.{bcolors.ENDC}")
    exit()

# Get the bet_location
print(f"{bcolors.WHITE_B}Where{bcolors.ENDC} do you place your bet :")
print(f"{bcolors.OKBLUE}[Color]{bcolors.ENDC} Black({bcolors.BLACK_B}x1.5{bcolors.ENDC}),Red({bcolors.RED_B}x1.5{bcolors.ENDC}),Green({bcolors.GREEN_B}x3{bcolors.ENDC})")
print(f"{bcolors.OKBLUE}[Number]{bcolors.ENDC} 1-36({bcolors.RED_B}x3{bcolors.BLACK_B}5{bcolors.ENDC}), 0({bcolors.GREEN_B}x70{bcolors.ENDC})")
bet_location = input(f"{bcolors.WHITE_U}Input{bcolors.ENDC} - ").lower()

# This is cosmetic
time.sleep(0.25)
print(f"\n{bcolors.OKCYAN}Rolling...{bcolors.ENDC}\n")
time.sleep(0.15)

for i in range(rolls):
    time.sleep(0.1)
    number = randint(0,36)
    if i == rolls - 1: # Detects if its the last roll
        time.sleep(0.4) # Delays the last roll
        end(money, bet, bet_location)
    else: # Any other roll
        print_numbers()


print(f"\n\nRoulette by 0range_ ©\n")