
#ENCAPSULATION
#------------------------
#wrapping data and function/methods together in a unit

class Bank:
    bank_name="SBI"
    def __init__(self,acc_holder,acc_no,balance):
        self.acc_holder=acc_holder
        self.acc_no=acc_no
        self.balance=balance
    def display(self):
        print(self.acc_holder,",",self.acc_no,",",self.balance,",",Bank.bank_name)
acc_holder1=Bank("Vishnu",9000878,30000)
acc_holder1.display()        

acc_holder2=Bank("Akash",9000880,10000)
acc_holder2.display()