import time
class Charecter:
    def __init__ (self , n , cul , rst , age , rl , fer, mg , ht):
        self.name = n 
        self.culture = cul
        self.resistance = rst
        self.age = age
        self.resilience = rl
        self.ferocity = fer
        self.magic = mg
        self.height = ht
    def Print_Charecter(self):
        print("--------------------------------------")
        print("Name:", self.name)
        print("--------------------------------------")
        print("Culture:", self.culture)
        print("--------------------------------------")
        print("Resistance:" , self.resistance)
        print("--------------------------------------")
        print("Age:",self.age)
        print("--------------------------------------")
        print("Resilience:",self.resistance)
        print("--------------------------------------")
        print("Ferocity:", self.ferocity)
        print("--------------------------------------")
        print("Magic:", self.magic)
        print("--------------------------------------")
        print("Height:" , self.height)
        print("--------------------------------------")
#                                                                    #
card1 = Charecter("Legolas","Elf", 2 , 7000, 8, 42 , 14 , 71)
card2 = Charecter("Boromit","Human", 1 ,40 ,6 ,52 ,0 , 71)
card3 = Charecter("Frodo Baggins","Hobbit", 3 , 50 , 10 , 28 , 4 , 46 ) 
deck = [card1 , card2 , card3]
print(card3.name ,",", card3.culture)
print(card2.magic ,",", card2.height)
time.sleep(2)
card1.Print_Charecter()
