
#Employee class
#object
#name,salary
#count the employee

class Employee:
    count=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.count+=1
    def display(self):
        print(self.name,self.salary)

employee1=Employee("Rahul",20000)
employee1.display()
employee2=Employee("Sanjay",5000)
employee2.display()
employee3=Employee("Arjun",30000)
employee3.display()
print("Employee count=",Employee.count) 