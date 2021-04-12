import time
import random
for counter in range (1,20):
    square = counter * counter
    print(counter, "squared is", square)
print("GREEN BOTTLES INCOMING!!!!")
counter2 = int(input("Enter a number: "))
for a in range (counter2,0,-1):
    print(a, "green bottle on the wall.")
print("times Table Problem")
mult_fact = int(input("Enter a number between 1 & 12: "))
while mult_fact < 1 or mult_fact > 12:
    print("You cant do that. ")
    mult_fact = int(input("Enter a number between 1 & 12: "))
for b in range(1,13):
    prod = mult_fact * b
    print(mult_fact,"times",b, "is equal to", prod)
print("Fibonacci sequence")
prev = 1
prev2 = 1
print("The first term is", prev2)
print("The second term is", prev)
for c in range(2,20):
    fibb = prev + prev2
    prev2 = prev
    prev = fibb
    print("The", str(c + 1 ) + "th term is", fibb )
print("Averaging tool")
sum = 0
numbuild = int(input("How many numbers are being averaged: "))
for d in range (0,numbuild):
    num = int(input("Enter a value: "))
    sum = sum + num
avg = sum / numbuild
print("The average is", avg)
for num in range(0,100):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print ("Buzz")
    else:
        print("The value you entered", str(num) , "is not applicable to Fizz or Buzz.")

tester1 = random.randint(1,9)
tester2 = random.randint(1,9)
print("This is to test your addition.")
answer = input(str(tester1) + "+" + str(tester2) + "=")
while int(answer) != tester1 + tester2:
    print("Wrong.")
    answer = input("Try again, " + str(tester1) + "+" + str(tester2) + "=")
else:
    print("Your correct.")