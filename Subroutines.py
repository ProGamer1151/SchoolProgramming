import random
#Write a program that asks the user for a price of an item.  Include a function that returns the VAT for the item.  This should be output in the main program.
price = float(input("Enter the price: "))
def tax(value):
    return value * 0.2
print("The price is" , price ,"and the VAT is" , tax(price))
# darts
score = 501
score2 = 501
print("New Game! Players starting with" , score)
while score != 0:
    dart1 = int(input("Enter the first dart: "))
    darts1 = int(input("Second Person , Enter the first dart: "))
    dart2 = int(input("Enter the second dart: "))
    darts2 = int(input("Second Person , Enter the second dart: "))
    dart3 = int(input("Enter the third dart: "))
    darts3 = int(input("Second Person , Enter the third dart: "))
    darttot = dart1 + dart2 + dart3
    dartstot = darts1 + darts2 + darts3
    if score - darttot > 1:
        score = score - darttot
        print("Score is",score)
    elif score - darttot == 0:
        score = score - darttot
        print("Player one wins the Game")
    if score2 - dartstot > 1:
        score2 = score2 - dartstot
        print("Score is",score2)
    elif score2 - dartstot == 0:
        score2 = score2 - dartstot
        print("Player two wins the Game")#
print("Snake eyes")
player0 = 0
player1 = 0
nonBanked0 = 0
nonBanked1 = 0
Player0Turn = True
while player0 < 100 and player1 < 100:
    playerDice0 = int(random.randint(1, 6))
    playerDice1 = int(random.randint(1, 6))
    if Player0Turn == True:
        print("Player 0 turn.")
    else:
        print("Player 1's turn.")
    if playerDice0 == 1 and playerDice1 == 0:
        if Player0Turn:
            player0 = 0
            nonBanked0 = 0
            Player0Turn = False
            continue
        else:
            player1 = 0
            nonBanked1 = 0
            Player0Turn = True
            continue
    elif playerDice0 == 1 or playerDice1 == 0:
        if Player0Turn:
            nonBanked0 = 0
            Player0Turn = False
            continue
        else:
            nonBanked1 = 0
            Player0Turn = True
            continue
    else:
        diceTotal = playerDice1 + playerDice0

        if Player0Turn:
            nonBanked0 += diceTotal
            print("Your not banked total is:", nonBanked0)
        else:
            nonBanked1 += diceTotal
            print("Your not banked total is: ", nonBanked1)
        choice = int(input("Please enter 0 to bank the points or anything else to gamble again."))
        if choice == 0:
            if Player0Turn:
                player0 += nonBanked0
                nonBanked0 = 0
                Player0Turn = False
                print("Banked total is:", player0)
            else:
                player1 += nonBanked1
                nonBanked1 = 0
                Player0Turn = True
                print("Banked total is:", player1)
if player0 >= 100:
    print("Player 0 won. Well Done.")
else:
    print('Player 1 won the game.')