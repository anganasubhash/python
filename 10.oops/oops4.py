

class Employee:
    company="Infosys"#Static variable---same /common one can set as common variable
    def setvalue(self,name,salary,designation):
        self.name=name
        self.salary=salary
        self.designation=designation
    def printvalue(self):
        print(self.name,self.salary,self.designation,Employee.company)
employee1=Employee()
employee1.setvalue("Rahul",20000,"Sofware engineer")
employee1.printvalue()




