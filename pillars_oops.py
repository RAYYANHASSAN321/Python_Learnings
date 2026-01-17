# ------------- Inheritance ---------------#

# Parent Class
class Animal:
    # Constructor
    def __init__(self , name):
        self.animalName = name
        
    #method
    def voice (self):
        print("Animal makes voice")
        
class Cat(Animal):
    def voice(self):
        print(f"{self.animalName} Meow.....")
        
class Lion(Animal):
    def voice(self):
        print(f"{self.animalName} Roar......")
    
c1 = Cat("Kitten")
c1.voice()

c2 = Cat("Kitten2")
c2.voice()

l1 = Lion("Tiger")
l1.voice()

a = Animal("Animal")
a.voice()