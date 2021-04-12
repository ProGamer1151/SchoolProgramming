#55 Objective 2 - Input strings and numbers into variables
import time
heyMan = "Nice, your test results are being processed!"
print("Hello! I is Satya Nadella, Bill Gates' son. Please give me your data!")
time.sleep(0.4)
name_entered = input("What is your name: ")
time.sleep(0.4)
print("Thank you", name_entered)
age = int(input("How old are you: "))
time.sleep(0.4)
print("Your name is" , name_entered , "and you are" , age,"years old")
time.sleep(0.4)
x = int(input("Addition time. Let us do something basic! Enter a number: "))
y = int(input("Enter a another number: "))
print (x + y)
time.sleep(2)
z = int(input("Enter your first test results now: "))
if z > 100:
    print("AS THE GREAT MICHEAL REEVES WOULD SAY - THAT IS LIES AND DECIET!!")
else:
    print(heyMan)
time.sleep(4)
a = int(input("Enter the second results now: "))
if a > 100:
    print("AS THE GREAT MICHEAL REEVES WOULD SAY - THAT IS LIES AND DECIET!!")
else:
    print(heyMan)
time.sleep(4)
b = int(input("Enter the third results now: "))
if b > 100:
    print("AS THE GREAT MICHEAL REEVES WOULD SAY - THAT IS LIES AND DECIET!!")
else:
    print("heyMan")
c = z + a + b
print("The total for your tests is" , c)
print("And ther mean is" , c/3)
time.sleep(0.4)
print("WE heard you wanted to move to America and so need to use the puny Farenhenit system and so we made a Centigrade converted just fro you!")
d = float(input("Enter a temperature: "))
e = d - 32
f = e * 5/9
print("The temperature in degrees Celcius is" , f)
time.sleep(0.4)
print("And lets do height and weight calculation because America loves imperialism- even units")
inches = int(input("Enter your height in inches: "))
centi = inches * 2.54
print("Your height in centimeters is " , centi)
stone = float(input("And now let's turn stone in to KG's- imperialism go brrrrrrrrrrrrrrr. Enter Weight: "))
Kg = stone * 6.364
print("The weight is: ", Kg)
time.sleep(2)
print("You are a worker who gets paid £12/hour plus a solid 60p for each toy you make.")
hours = int(input("How many hours do you work: "))
toyGen = int(input("How many toy cars have you finished today: "))
salary =(hours * 12)+(toyGen * 0.6)
time.sleep(4)
print("You got paid " , salary , "today")
print("We heard you wanted to buy a fish tank. Let's find the volume!")
d = float(input("Enter the length of the tank in cm: "))
time.sleep(0.4)
e = float(input("Enter the width of the tank in cm: "))
time.sleep(0.4)
f = float(input("Enter the height of the tank in cm: "))
time.sleep(0.4)
g = d * e * f
print("The Area is " , g , "cm^3")
time.sleep(0.4)
print("Lets do circle stuff.")
time.sleep(0.4)
time.sleep(0.4)
diameter = float(input("Enter the diameter for the radius: "))
radius = diameter / 2
arcAngle = float(input("Enter an arc angle: "))
rad = radius * radius
area = 3.141 * rad
circum = 3.141 * diameter
arcLength = (arcAngle * circum)
sectorLength = (arcAngle / 360) * circum
print("The radius is", radius , "cm.")
time.sleep(0.4)
print("The area is", area , "cm^2.")
time.sleep(0.4)
print("The circumfrence is", circum , "cm.")
time.sleep(0.4)
print("The arc length is", sectorLength , "cm.")
time.sleep(0.4)
print("And that's it!")
time.sleep(0.4)