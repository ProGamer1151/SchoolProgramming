import time
forename = input("Enter your forename:")
forename_uppercase = forename.upper()
print("Your name in capital letters is:",forename_uppercase)
surname = input("Enter your surname")
length_sur = len(surname)
print("There are", length_sur ,"letters in your name.")
sentence = "I saw a wolf in the forest. A lonely wolf."
characters = sentence[:5]
print(characters)
characters2 = sentence[:-12]
print(characters2)
characters3 = sentence[20:26]
print(characters3)
