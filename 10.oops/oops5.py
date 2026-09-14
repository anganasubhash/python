class Student:
    college="Christ college"
    def setvalue(self,rollno,name,age,mark):
        self.rollno=rollno
        self.name=name
        self.age=age
        self.mark=mark
    def printvalue(self):
        print(self.rollno,self.name,self.age,self.mark,Student.college)
student1=Student()
student1.setvalue(21,"Rahul",18,78)
student1.printvalue()

student2=Student()
student2.setvalue(34,"Meenu",18,80)
student2.printvalue()

student3=Student()
student3.setvalue(37,"Renju",18,95)
student3.printvalue()