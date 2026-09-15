#constructor+static variable
#employee
#static variable=company,designation 
#name,age,salary,designation,company

class Employee:
    company="Infosys"
    designation="Software engineer"
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def printvalue(self):
        print(self.name,self.age,self.salary,Employee.company,Employee.designation)

employee1=Employee("Rahul",24,20000)
employee1.printvalue()        
employee2=Employee("Reena",30,25000)
employee2.printvalue()