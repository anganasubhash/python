
class Person:       #Person is the class
    def read(self):#self argument---can use in all function 
        print("Read a book")#     function inside the class is method here 2 method
    def write(self):
        print("Write....")

person1=Person()#object
person1.read()
person1.write()#reference

person2=Person()
person2.read()
person2.write()

