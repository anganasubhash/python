
#constructor

class student:
    def __init__(self,name,rollno,age):
        self.name=name
        self.rollno=rollno
        self.age=age
    def printvalue(self):
        print(self.name,self.rollno,self.age)
student1=student("Ajay",12,24)
student1.printvalue()
student2=student("Ammu",13,22)
student2.printvalue()