#class-student
#name,rollno,mark1,mark2,mark3
#total
#Average
#name,rollno,total,Average
class Student:
    def __init__(self,name,rollno,mark1,mark2,mark3):
        self.name=name
        self.rollno=rollno
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
    def total(self):
        return self.mark1+self.mark2+self.mark3
    def average(self):
        return (self.mark1+self.mark2+self.mark3)/3 #self.total()/3
    def printvalue(self):
        print(self.name,self.rollno,self.total(),self.average())
student1=Student("Ajay",13,20,25,24)
student1.printvalue()
student2=Student("Sanjay",24,21,25,24)
student2.printvalue()