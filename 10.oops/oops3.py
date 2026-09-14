 

class Employee:
    def setvalue(self,fname,lname,designation,salary,company):
        self.fname=fname
        self.lname=lname
        self.designation=designation
        self.salary=salary
        self.company=company
    def printvalue(self):
        print(self.fname,self.lname,self.designation,self.salary,self.company)
Employee1=Employee()
Employee1.setvalue("Rahul ,","Krishnan,","Data analyst,",30000,",Amazon")
Employee1.printvalue()

Employee2=Employee()
Employee2.setvalue("Meena,","Ramesh,","Doctor,",25000,",Elite hostipal")
Employee2.printvalue()

Employee3=Employee()
Employee3.setvalue("Anjana,","Kishor,","Data analyst, ",35000,"onepene")
Employee3.printvalue()

Employee4=Employee()
Employee4.setvalue("Sumesh,","Ks,","Engineer,",50000,"kms Group")
Employee4.printvalue()