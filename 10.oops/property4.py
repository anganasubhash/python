#ABSTRACTION
#---------------
#hide unnecessary details,show necessary details

from abc import abstractmethod,ABC
class Vehicle(ABC):
    @abstractmethod
    def start(key):
        pass
class car(Vehicle):
    def start(self):
        print("car start with key")
class Bike(Vehicle):
    def start(self):
        print("Bike start with self")
c=car()
b=Bike()
c.start()
b.start()