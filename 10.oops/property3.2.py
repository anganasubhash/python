#parent class car
#child class-brand
#name,price
#car name is driving
class Car:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def printvalue(self):
        print(self.name,self.price)
class Brand(Car):
    def display(self):
        print(self.name,"is driving")

car1=Brand("BMW",20000000)
car1.printvalue()
car1.display()
    