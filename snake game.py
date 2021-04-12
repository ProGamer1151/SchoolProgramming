import random
import time
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
        time.sleep(1)
    else:
        print("Player 1's turn.")
        time.sleep(1)
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
            time.sleep(1)
        else:
            nonBanked1 += diceTotal
            print("Your not banked total is: ", nonBanked1)
            time.sleep(1)
        choice = int(input("Please enter 0 to bank the points or anything else to gamble again."))
        if choice == 0:
            if Player0Turn:
                player0 += nonBanked0
                nonBanked0 = 0
                Player0Turn = False
                print("Banked total is:", player0)
                time.sleep(1)
            else:
                player1 += nonBanked1
                nonBanked1 = 0
                Player0Turn = True
                print("Banked total is:", player1)
                time.sleep(1)
if player0 >= 100:
    print("Player 0 won. Well Done.")
    time.sleep(20)
    exit
else:
    print('Player 1 won the game.')
    time.sleep(20)
    exit
