import time
forename = input("Please enter your forename:   ")
surname = input("Please enter your surname:   ")
forename_upp= forename.upper()
ini = forename_upp[0:1]
uppersurname = surname.upper()
print("Initial is", ini , "and your surname is", uppersurname)
city1 = input("City from:")
City2 = input("City to: ")
ci1 = city1.upper()
ci2 = City2.upper()
Code1 = ci1[0:4]
Code2 = ci2[0:4]
print("Your code thing is", Code1 + "-" + Code2)
