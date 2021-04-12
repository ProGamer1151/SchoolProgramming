import time
import random
print("Enter the name, attack and defense")
name = input("Enter the name:")
attack = input("Enter the attack between 0 and 100: ")
defense = input("Enter the defense between 0 and 100: ")
f = open("attrib.txt" , "w+")
f.write(name + "\n" + attack + "\n" + defense + "\n")
f.close()
g = open("attrib.txt" , "r")
name1 = g.readline().rstrip()
attack1 = g.readline().rstrip()
defense1 = g.readline().rstrip()
g.close()
print(attack1 , defense1 , name1)
h = open("Quote of the day.txt" , "r+")
lines = h.readlines()
inf = random.randrange(0, len(lines))
quote = lines[inf].rstrip()
print(quote)
h.close()
print("Input 0 to enter a new product into the catalogue, 1 to output all the items and 2 to find a product and its price")
menuent = input("")
while menuent != 4:
    if menuent == 0:
        i = open("Prods.txt", "w")
        prodname = input("Enter the product name: ")
        prodprice = input("Enter price: ")
        i.write(prodname + "\n" + prodprice + "\n")
        i.close()
    elif menuent == 1:
        j = open("Prods.txt" , "r")
        prodes = j.readlines()
        for a in range(0,len(prodes),2):
            print(prodes[a].rstrip())
        j.close()
    elif menuent == 2:
        k = open("Prods.txt", "r")
        query = input("Which product are you looking for: ")
        proges = k.readlines()
        found = False
        for b in range(0, len(proges), 2):
            if query == proges[b].rstrip():
                print(proges[b].rstrip(), proges[b+1].rstrip())
                found = True
        if found == False:
            print("Object could not be found.")






