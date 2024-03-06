
# 0range_'s Casino

Welcome to my casino ! This is a compilation of well-known casino games such as Blackjack, Roulette and coinflip *(for now, more coming soon)*

## Money

The code containes a text file called `bank.txt` which, as it may sound, countains your money. You can touch it if you want to but that's like cheating.

## Blackjack

Blackjack is a well-know game in the world of casino. The rules are simple :

- You draw 2 cards, the game will show you your total "score" or the total of the values of your cards.
    - Color or symbol has no impact on the score
    - Every number card is worth it's number (Ex: 5 is worth 5)
    - The letter cards (J,Q,K,A) are worth respectivily, 10,10,10 and 1 or 11, the game chooses the Aces' values for you depending on your total
- The dealer draws as many cards as he need to hit a cap of 17, card values explained before apply. One exception : the Aces.
    - The dealer's first ace always counts as 11, the other ones always count as 1 (this may be unaccurate but who cares)
- You can then choose to Hit, type `hit`, (draw a new card), which will add the card's value to the total or Stand, type `stand`, which will compare your total to the dealer's and cash you out. The game will recommend what action you should choose (but you don't have to follow it)
- Your goal is to hit a total of 21 (Blackjack) but not go above that (Busted)
- If your total is higher then the dealer's, you win
- If your total is equal to the dealer's, you draw
- If you bust, you lose
- If you and the dealer bust, you draw

### Bets

- Winning rewards you with 2 times your bet
- Losing removes your bet from the bank
- Drawing has no impact on the money in your bank
- Blackjacking rewards you with 21 times your bet

## Roulette

Roulette is one of those classic games we see in movies and everyone knows what the rules are, as they are very simple :

- Bet an amount on a color or number
- Wait for the wheel to stop
- If the wheel stops on where you bet, you win.
- Cash out (the game does it for you)

### Bets

- Betting on a color (Red or Black) and winning rewards you with 1.5 times your bet
- Betting on green and winning rewards you 35 times your bet
- Betting on a number (1-36) and winning rewards you with 35 times your bet
- Betting on 0 and winning rewards you with 70 times your bet

# Projects for the Future

- Poker
- Card race
- Dice
- Coinflip
- Slots
- User suggestions
