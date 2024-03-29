#================= Imports =================#
from framework import bcolors, clear, read, write, end_print
from random import randint
import time
import os

#================= Default Variables =================#
money = float(read())

#================= Functions =================#
def transform_hand(given_hand):
    for index, card in enumerate(given_hand):
        i = randint(1,3)
        if card == "1": # Chooses the aces value acording to total
            if total <= 10:
                given_hand[index] = "A (11)"
                total += 10
            else:
                given_hand[index] = "A (1)"
        elif card == "10": # Randomizes each card with value 10 to J,Q,K
            if i == 1:
                given_hand[index] = "J"
            elif i == 2:
                given_hand[index] = "Q"
            else:
                given_hand[index] = "K"

def end(money, bet):
    print(f"Your total was {bcolors.RED_B}{total}{bcolors.ENDC}\nThe dealer's total was {bcolors.GREEN_B}{dealer_total}{bcolors.ENDC}\n")
    if total > 21: # Bust condition
        if dealer_total > 21:
            end_print("draw")
        else:
            end_print("lose")
            money -= bet
    elif total < 21: # Win/Lose conditions
        if dealer_total > 21:
            end_print("win")
            money += bet*2
        elif dealer_total > total or dealer_total == 21:
            end_print("lose")
            money -= bet
        else:
            end_print("win")
            money += bet*2
    else:
        end_print("jackpot")
        money += bet*21

# Print cashout and balance and overwrite bank.txt file
    old_money = float(read())
    cashout = money - old_money
    if cashout > 0:
        print(f"\n\n{bcolors.GREEN_B}+{cashout}{bcolors.ENDC}")
    else:
        print(f"\n\n{bcolors.RED_B}{cashout}{bcolors.ENDC}")
    print(f"Your balance : {bcolors.WHITE_B}{money}{bcolors.ENDC}")
    write(money)

# Initialize cards, hand and total
card1 = str(randint(1,10))
card2 = str(randint(1,10))
hand = [card1, card2]
hand = hand

total = int(card1) + int(card2)

# Initialize dealer first card and total
i_dealer = randint(1,3) # same as i in transform_hand but for the dealer
dealer_cards = 2
dealer_card1 = str(randint(2,11))

dealer_total = randint(1,10) + int(dealer_card1)

while dealer_total <= 16: # Following the rule that the dealer must hit until his total is 16 or more
    dealer_total += randint(1,10)
    dealer_cards += 1

match dealer_card1: # Only do this once because we only see the dealer's first card
    case "10":
        if i_dealer == 1:
            dealer_card1 = "J"
        elif i_dealer == 2:
            dealer_card1 = "Q"
        elif i_dealer == 3:
            dealer_card1 = "K"
    case "11": # Dealer's first ace is always counts as 11
        dealer_card1 = "A (11)"

# Modify cards in the hand list
transform_hand(hand)

#== Start ==#
clear()
print(f"Blackjack by 0range_ ©\n\n")

# Get bet
bet = float(input(f"Place your {bcolors.GREEN_B}bet{bcolors.ENDC} ({bcolors.WHITE_U}<{money}{bcolors.ENDC}) : "))
if bet > money:
    print(f"{bcolors.WARNING}You're poor.{bcolors.ENDC}")
    exit()
clear()
time.sleep(0.1)

# Start the first round
print(f"Dealer : {bcolors.GREEN_B}{dealer_card1}{bcolors.ENDC} " + "| ? "*(dealer_cards-1))
print(f"Your hand : {bcolors.RED_B}{hand[0]}{bcolors.ENDC} | {bcolors.RED_B}{hand[1]}{bcolors.ENDC}")

# Print player plus recommendation (you can comment this out)
if total <= 16:
    print(f"Total : {bcolors.RED_B}{total}{bcolors.ENDC} {bcolors.BLACK}(Hit){bcolors.ENDC}\n")
else :
    print(f"Total : {bcolors.RED_B}{total}{bcolors.ENDC} {bcolors.BLACK}(Stand){bcolors.ENDC}\n")

# If you comment out recommendation, uncomment this vv
# print(f"Total : {bcolors.RED_B}{total}{bcolors.ENDC}\n")

user_input = input(f"{bcolors.OKBLUE}[Stand]{bcolors.ENDC} to stand\n{bcolors.OKBLUE}[Hit]{bcolors.ENDC} to hit\n{bcolors.WHITE_U}Input{bcolors.ENDC} - ").lower()

match user_input:
    case "stand": # Ends the game
        clear()
        print(f"\n{bcolors.TURQUOISE}You stood.{bcolors.ENDC}\n")
        end(money, bet)

    case "hit": # Round 1 --> round 2
        clear()
        print(f"\n{bcolors.TURQUOISE}You hit.{bcolors.ENDC}\n")

        # Adds a new card to the hand and total, transform the hand
        card3 = randint(1,10)
        total += card3
        hand.append(card3)
        transform_hand(hand)

        # Print hands
        print(f"Dealer : {bcolors.GREEN_B}{dealer_card1}{bcolors.ENDC} " + "| ? "*(dealer_cards-1))
        print(f"Your hand : {bcolors.RED_B}{hand[0]}{bcolors.ENDC} | {bcolors.RED_B}{hand[1]}{bcolors.ENDC} | {bcolors.RED_B}{hand[2]}{bcolors.ENDC}")
        
        # Print player plus recommendation (you can comment this out)
        if total <= 16:
            print(f"Total : {bcolors.RED_B}{total}{bcolors.ENDC} {bcolors.BLACK}(Hit){bcolors.ENDC}\n")
        else :
            print(f"Total : {bcolors.RED_B}{total}{bcolors.ENDC} {bcolors.BLACK}(Stand){bcolors.ENDC}\n")

        # If you comment out recommendation, uncomment this vv
        # print(f"Total : {bcolors.RED_B}{total}{bcolors.ENDC}\n")
        
        user_input = input(f"{bcolors.OKBLUE}[Stand]{bcolors.ENDC} to stand\n{bcolors.OKBLUE}[Hit]{bcolors.ENDC} to hit\n{bcolors.WHITE_U}Input{bcolors.ENDC} - ").lower()

        match user_input:
            case "stand": # Ends the game
                clear()
                print(f"{bcolors.TURQUOISE}You stood.{bcolors.ENDC}\n")
                end(money, bet)

            case "hit": # Round 2 --> round 3 (no more then this is needed)
                clear()
                print(f"{bcolors.TURQUOISE}You hit.{bcolors.ENDC}\n")

                # Add new card to total and hand, transform it
                card4 = randint(1,10)
                total += card4
                hand.append(card4)
                transform_hand(hand)

                # Print hands
                print(f"Dealer : {bcolors.GREEN_B}{dealer_card1}{bcolors.ENDC} " + "| ? "*(dealer_cards-1))
                print(f"Your hand : {bcolors.RED_B}{hand[0]}{bcolors.ENDC} | {bcolors.RED_B}{hand[1]}{bcolors.ENDC} | {bcolors.RED_B}{hand[2]}{bcolors.ENDC} | {bcolors.RED_B}{hand[3]}{bcolors.ENDC}")
                
                # Print player plus recommendation (you can comment this out)
                if total <= 16:
                    print(f"Total : {bcolors.RED_B}{total}{bcolors.ENDC} {bcolors.BLACK}(Hit){bcolors.ENDC}\n")
                else :
                    print(f"Total : {bcolors.RED_B}{total}{bcolors.ENDC} {bcolors.BLACK}(Stand){bcolors.ENDC}\n")

                # If you comment out recommendation, uncomment this vv
                # print(f"Total : {bcolors.RED_B}{total}{bcolors.ENDC}\n")

                end(money, bet) # Ends here because low probability of you needing to hit one more time

            case _ :
                print(f"\n{bcolors.WARNING}Type correctly dude.{bcolors.ENDC}")

    case _ :
        print(f"\n{bcolors.WARNING}Type correctly dude.{bcolors.ENDC}")

print(f"\nBlackjack by 0range_ ©\n")