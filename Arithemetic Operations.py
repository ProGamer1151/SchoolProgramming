import random
import time
import math
import calendar
print("Dice Problem")
dicesides = int(input("Enter dice sides:    "))
dicefig = random.randint(1, dicesides)
print("You rolled a", dicefig, "out of", dicesides)
time.sleep(2)
input1 = int(input("Number 1:    "))
input2 = int(input("Number 2:    "))
if input1 == 0 or input2 == 0:
    print("ERROR 404: object will not work.")
num = input1 % input2
if num == 0:
    print("They are divisible!")
else:
    print("They are not directly divisible. The remainder is" , num)
print("Cash machine problem")
balance = 231
withdr = int(input("Enter amount you wish to withdraw:   "))
if withdr > 0 and withdr <= 250 and withdr % 10 == 0 and withdr <= balance:
    twenties = math.floor(withdr / 20)
    tens = 0
    if withdr % 20 != 0:
        tens = 1
    balAft = balance - withdr
    print("Your balance is", str(balAft) + ".")
    print("You will have", twenties, "twenties and", tens, "tenners.")
    print("You have withdrawed", withdr)
else:
    print("Amount entered was not valid. Please enter an amount less then your balance, divisible by 10 and not 0 or else contact Support.")
print("Game dice problem")
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
dice3 = random.randint(1,6)
allT = dice1 == dice2 == dice3
print("The dice values are " + str(dice1) + "," + str(dice2) + "," + str(dice3)+".")
if allT:
    score = dice1 * 3
else:
    if dice1 == dice2:
        score = dice1 * 2
        score = score - dice3
    elif dice1 == dice3:
        score = dice1 * 2
        score = score - dice2
    elif dice2 == dice3:
        score = dice2 * 2
        score = score - dice1
    else:
        score = 0
print("Score is" , score)
print("Month problem")
year = int(input("Enter the year: "))
monthNum = int(input("Enter the number of the month - from 1 to 12: "))
monthNameFromNum = calendar.month_name[monthNum]
daysOfMonth = calendar.monthrange(year, monthNum)[1]
print("The year is", year)
print("The month is", monthNameFromNum)
print("This month has", str(daysOfMonth) +" days.")






