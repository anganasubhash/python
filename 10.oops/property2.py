#POLYMORPHISM
#-----------------
#Same name different behaviour

class Dog:
    def sound(self):
        print("Bark")
class Cat:
    def sound(self):
        print("meow")
d=Dog()
c=Cat()
d.sound()
c.sound()