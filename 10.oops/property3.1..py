
#employee(name,salary)
#manager
#name,salary
#department-DS


class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(self.name,self.salary)
class Manger(Employee):
    def department(self):
        print("Department:DS")
m1=Manger("Anna",20000)
m1.display()
m1.department()
    
        