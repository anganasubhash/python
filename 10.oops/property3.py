#INHERITANCE
#---------------
#one class uses property of other class
class Animal:
    def eat(self):
        print("eating......")
class Dog(Animal):
    def sound(self):
        print("barking....")

d=Dog()
d.sound()
d.eat()