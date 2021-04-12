import random
diceval = random.randint(1,6)
diceeng = ["One" , "Two" , "Three", "Four" , "Five" , "Six"]
value = diceeng[diceval - 1]
print("Value is" , value)
notebooks = ["" , "" , "", "" , "" , "" , "" , "" , "" , ""]
notebookindex = int(input("Enter the notebook ypu wish to use from 0 to 9 and -1 to exit: "))
while notebookindex != -1:
    notebooks[notebookindex] = input("Enter thy notes: ")#
    printchoice = int(input("Enter 0 to print all notes or 1 to continue editing;"))
    if printchoice == 0:
        for a in range(0,10):
            print(a, "notebooks values is", notebooks[a])
    notebookindex = int(input("Enter the notebook you wish to use from 0 to 9 and -1 to exit: "))
print("Currency Conversion Problem")
nameofcurrency = ["US Dollar","Euro","Australian Dollar","Canadian Dollar","Chinese Yuan","Japanese Yen","Swiss Franc"]
valuetopound = [1.384 , 1.167 , 1.802 , 1.749 , 9.029 , 150.591 , 1.294]
print("What currency do you want to convert to?")
for i in range(0,len(nameofcurrency)):
    print(i , nameofcurrency[i])
choice = int(input("Enter the selection: "))
if choice >= 0 and choice < len(valuetopound):
    amount = int(input("Enter the amount: "))
    conversion_rate = valuetopound[choice]
    converted = amount * conversion_rate
    print("The converted value is" , converted)
else:
    print("Invalid Choice.")
board1 = [[False] * 8] * 8
board2 = [[False] * 8] * 8
playerOnePlaced = 0
print("This is player One.")
while playerOnePlaced < 10:
    x = int(input("Enter a value between 0 and 7 for the x coordinate: "))
    y = int(input("Enter a value between 0 and 7 for the y coordinate: "))
    if x < 0 or x > 7:
        print("Not valid x coordinate.")
        continue
    if y < 0 or y > 7:
        print("Not a valid y coordinate.")
        continue
    if not board1[x][y]:
        board1[x][y] = True
        playerOnePlaced = playerOnePlaced + 1
    else:
        print("You've already placed something there")
playerTwoPlaced = 0
print("This is player Two.")
while playerTwoPlaced < 10:
    x = int(input("Enter a value between 0 and 7 for the x coordinate: "))
    y = int(input("Enter a value between 0 and 7 for the y coordinate: "))
    if x < 0 or x > 7:
        print("Not valid x coordinate.")
        continue
    if y < 0 or y > 7:
        print("Not a valid y coordinate.")
        continue
    if not board2[x][y]:
        board2[x][y] = True
        playerTwoPlaced = playerTwoPlaced + 1
    else:
        print("You've already placed something there")
score1 = 0
score2 = 0
while score1 != 10 and score2 != 10:
    print("Guess the coordinate for a potential tank Player 1. The missionaries are after you.")
    x = int(input("Enter a value between 0 and 7 for the x coordinate: "))
    y = int(input("Enter a value between 0 and 7 for the y coordinate: "))
    if x < 0 or x > 7:
        print("Not valid x coordinate.")
    elif y < 0 or y > 7:
        print("Not a valid y coordinate.")
    else:
        if board2[x][y]:
            score1 = score1 + 1
            board2[x][y] = False
            print("You have hit player Twos tank.")
            if score1 == 10:
                break
    print("Guess the coordinate for a potential tank Player 2. The missionaries are after you.")
    x = int(input("Enter a value between 0 and 7 for the x coordinate: "))
    y = int(input("Enter a value between 0 and 7 for the y coordinate: "))
    if x < 0 or x > 7:
        print("Not valid x coordinate.")
    elif y < 0 or y > 7:
        print("Not a valid y coordinate.")
    else:
        if board1[x][y]:
            score2 = score2 + 1
            board1[x][y] = False
            print("You have hit player One tank.")
if score1 == 10:
    print("Player 1 won!")
else:
    print("Player Two won. ")
