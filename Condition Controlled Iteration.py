import random
import time
menu = 1 or 2 or 3
menu_sel = int(input("Please input 1 for the game, 2 for instruction and 3 to quit: "))
while menu_sel != 1 and menu_sel != 2:
    if menu_sel == 3:
        print("Exiting...")
        time.sleep(2)
        exit()
    menu_sel = int(input("That's wrong. Please input 1 for the game, 2 for instruction and 3 to quit: "))
else:
    print("Let's go.")


print("Compound Interest problem")
balance = float(input("Enter account balance: "))
percentage_intrest = float(input("Enter interest rate: "))
percentage_intrest_decimal = percentage_intrest / 100
desired_figure = float(input("How much money would you like: "))
year = 0
while balance < desired_figure:
    balance = balance * (1 + percentage_intrest_decimal)
    year = year + 1
    print("In the year", year,",you will have £" + str(balance))
print("Guessing game")
gen_num = random.randint(1,100)
print("Guess the number between 1 & 100")
guess = input("Enter your guess: ")
counter = 0
while int(guess) != gen_num:
    counter = 1 + counter
    print("That was your", counter , "attempt.")
    if int(guess) > gen_num:
        print("Too high")
    if int(guess) < gen_num:
        print("Too low.")
    guess = input("Enter your guess: ")
else:
    print("You're correct. ")
#This program checks the length of gamertags entered.
valid_gamertag = False
while valid_gamertag != True:
    print("Gamertags must be shorter than 15 charecters. ")
    gamertag = input("Enter gamertag: ")
    gamertag_len = len(gamertag)
    if gamertag_len > 15:
        print("Gamertag is too long")
    else:
        print("Gamertag accepted.")
        valid_gamertag = True
#Rock Paper Scissors
choices = ["Rock" , "Paper" , "Scissors"]
compScore = 0
humanScore = 0
while compScore < 10 and humanScore < 10:
    compSel = choices[random.randint(0, 2)]
    humanChoice = int(input("Enter a number from 0 for Rock, 1 is Paper and 2 being Scissors: "))
    while humanChoice > 2 or humanChoice < 0:
        humanChoice = int(input("That didn't work. Try again. Enter a number from 0 for Rock, 1 is Paper and 2 being Scissors: "))
    print("The computer selected", compSel)
    humanSel = choices[humanChoice]
    if compSel == humanSel:
        print("Tie.")
    elif compSel == "Rock" and humanSel == "Paper":
        print("Human wins. ")
        humanScore = humanScore + 1
    elif compSel == "Rock" and humanSel == "Scissors":
        print("Computer Wins.")
        compScore = compScore + 1
    elif compSel == "Paper" and humanSel == "Rock":
        print("Computer Wins.")
        compScore = compScore + 1
    elif compSel == "Paper" and humanSel == "Scissors":
        print("Human wins.")
        humanScore = humanScore + 1
    elif compSel == "Scissors" and humanSel == "Rock":
        print("Human Wins.")
        humanScore = humanScore + 1
    elif compSel == "Scissors" and humanSel == "Paper":
        print("Computer Wins.")
        compScore = compScore + 1
if compScore == 10:
    print("Computer Wins!")
elif humanScore == 10:
    print("Human wins.")
print("Computer scored", compScore)
print("Human scored", humanScore)
#happy numbers
numEnt = int(input("Enter a nummber: "))
while numEnt != 1 and numEnt != 4:
    sum = 0
    numStr = str(numEnt)
    for i in range(0, len(numStr)):
        digit = int(numStr[i]) - int('0')
        sum += digit ** 2
    numEnt = sum
if numEnt == 1:
    print("Happy Number.")
elif numEnt == 4:
    print("Sad Number.")
