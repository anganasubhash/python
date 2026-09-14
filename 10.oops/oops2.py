

class Person:
    def setvalue(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    def printvalue(self):
        print(self.name,self.age,self.course)

person1=Person()
person1.setvalue("Anna",54,"DS")
person1.printvalue()

person2=Person()
person2.setvalue("Meena",20,"DA")
person2.printvalue()

person3=Person()
person3.setvalue("Rahul",24,"Ds")
person3.printvalue()

person4=Person()
person4.setvalue("Rithu",20,"DS")
person4.printvalue()