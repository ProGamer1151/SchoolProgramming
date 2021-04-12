import time
print("Identifying if you are under age or over age!")
time.sleep(2)
age = int(input("How old are you:   "))
if age < 18:
    print("Your underage. ")
else:
    print("Go buy all the drinks you want.")
time.sleep(2)
print("Write a program that reads in the temperature of water in a container in Centigrade and displays a message stating whether the water is frozen (zero or below), boiling (100 or greater) or neither.")
temp = float(input("Enter the temperature of the water: "))
if temp < 0:
    print("The water is freeing")
elif temp > 100:
    print("Be careful, the water is at boiling point AND IS VERY HOT.")
else:
    print("The water is between 0 and 100 degrees centigrade.")
print("Vocational grade problem")
grade = float(input("Enter your score: "))
if grade < 40:
    print("You have failed! You are a disgrace to your parents.")
elif grade < 60:
    print("You have passed but clearly weren't gunning for the best.")
elif grade < 80:
    print("You have received merit but you do not have a distinction!")
elif grade > 100:
    print("LIAR! YOU ARE A NAUGHTY BOY")
else:
    print("You actually did good! Your parents should be proud of you.")
import time
dice = int(input("Enter a number between one and six:   "))
if dice is 1:
    print("000000000000")
    time.sleep(1)
    print("0          0")
    time.sleep(1)
    print("0          0")
    time.sleep(1)
    print("0    #     0")
    time.sleep(1)
    print("0          0")
    time.sleep(1)
    print("0          0")
    time.sleep(1)
    print("000000000000")
if dice is 2:
    print("000000000000")
    time.sleep(1)
    print("0          0")
    time.sleep(1)
    print("0    #     0")
    time.sleep(1)
    print("0    #     0")
    time.sleep(1)
    print("0          0")
    time.sleep(1)
    print("0          0")
    time.sleep(1)
    print("000000000000")
if dice is 3:
    print("0000000000000")
    time.sleep(1)
    print("0 #         0")
    time.sleep(1)
    print("0    #      0")
    time.sleep(1)
    print("0       #   0")
    time.sleep(1)
    print("0           0")
    time.sleep(1)
    print("0000000000000")
if dice is 4:
    print("0000000000000")
    time.sleep(1)
    print("0 #        # 0")
    time.sleep(1)#
    print("0            0")
    time.sleep(1)
    print("0            0")
    time.sleep(1)
    print("0 #        # 0")
    time.sleep(1)
    print("0000000000000")
if dice is 5:
    print("0000000000000")
    time.sleep(1)
    print("0 #        # 0")
    time.sleep(1)
    print("0     #      0")
    time.sleep(1)
    print("0 #        # 0")
    time.sleep(1)
    print("0000000000000")
if dice is 6:
    print("0000000000000")
    time.sleep(1)
    print("0 #        # 0")
    time.sleep(1)
    print("0            0")
    time.sleep(1)
    print("0 #        # 0")
    time.sleep(1)
    print("0            0")
    time.sleep(1)
    print("0 #        # 0")
    time.sleep(1)
    print("0            0")
    time.sleep(1)
    print("0000000000000")
time.sleep(2)
print("Largest Number Problem ")
number1 = input("Enter your first number:   ")
number2 = input("Enter your second number:  ")
if number1 > number2:
    print("Number 1 was the larger one !")
if number2 > number1:
    print('Number 2 was the larger one\nand this is what I learnt to do yesterday')
nitra = float(input("Enter the nitrate level which is between 1 and 50:   "))
if nitra > 10:
    print("Dose is 3ml!")
else:
    if nitra > 2.5:
        print("Dose is 2ml!")
    else:
        if nitra <= 1:
            print("Dose is 0.5ml!")
        else:
            print("Dose is 1ml")
print("Vocational Grade Problem")
ana = int(input("Enter the analysis marks:  "))
des = int(input("Enter the design marks:    "))
imp = int(input("Enter the implementation marks:    "))
evo = int(input("Enter the evaluation marks:    "))
marks = ana + des + imp + evo
print("You scored" , str(marks) + "!")
if marks < 2:
    print("Ungraded")
elif marks < 4:
    print("Grade 1 ")
    next4 = 4 - marks
    print("Next level is" , next4 , "marks away")
elif marks < 13:
    print("Grade 2")
    next13 = 13 - marks
    print("Next level is", next13, "marks away")
elif marks < 22:
    print("Grade 3")
    next22 = 22 - marks
    print("Next level is", next22, "marks away")
elif marks < 31:
    print("Grade 4")
    next31 = 31 - marks
    print("Next level is", next31, "marks away")
elif marks < 41:
    print("Grade 5")
    next41 = 41 - marks
    print("Next level is", next41, "marks away")
elif marks < 54:
    print("Grade 6")
    next54 = 54 - marks
    print("Next level is", next54, "marks away")
elif marks < 67:
    print("Grade 7")
    next67 = 67 - marks
    print("Next level is", next67, "marks away")
elif marks < 80:
    print("Grade 8")
    next80 = 80 - marks
    print("Next level is", next80, "marks away")
else:
    print("Grade 9")
time.sleep(2)
print("Periodic Table Sorter- 6 elements from 2 groups")
print("Periodic Table Sorter- 6 elements from 2 groups")
sorter = input("Enter a symbol (ie. Lithium would be Li) or a name or group:    ")
def printLithium():
    print("Element: Lithium ")
    print("Atomic Weight: 7")
    print("Group: Alkali Metals")
def printSodium():
    print("Element: Sodium ")
    print("Atomic Weight: 23")
    print("Group: Alkali Metals")
def printPotassium():
    print("Element: Potassium ")
    print("Atomic Weight: 39")
    print("Group: Alkali Metals")
def printBery():
    print("Element: Beryllium")
    print("Atomic Weight: 9")
    print("Group: 2 ")
def printMagnesium():
    print("Element: Magnesium ")
    print("Atomic Weight: 12 ")
    print("Group : 2")
def printCalcium():
    print("Element: Calcium")
    print("Atomic Weight: 40 ")
    print("Group : 2")
def group1():
    printLithium()
    printSodium()
    printPotassium()
def group2():
    printBery()
    printMagnesium()
    printCalcium()
if sorter == "Li" or sorter == "Lithium":
    printLithium()
elif sorter == "Na" or sorter == "Sodium":
    printSodium()
elif sorter == "K" or sorter == "Potassium":
    printPotassium()
elif sorter == "Be" or sorter == "Beryllium":
    printBery()
elif sorter == "Mg" or sorter == "Magnesium":
    printMagnesium()
elif sorter == "Ca" or sorter == "Calcium":
    printCalcium()
elif sorter == "1":
    group1()
elif sorter == "2":
    group2()
else:
    print("Exception not handled!")
time.sleep(5)
exit()
