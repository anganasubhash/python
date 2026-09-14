
class Bank:
    bank_name="state bank of india"
    def setvalue(self,acc_no,name,balance):
        self.acc_no=acc_no
        self.name=name
        self.balance=balance
    def printvalue(self):
        print(self.acc_no,self.name,self.balance,Bank.bank_name)

bank1=Bank()
bank1.setvalue("Acc000678","Rahul",60000)
bank1.printvalue()

bank2=Bank()
bank2.setvalue("Ac000567","Meenu",40000)
bank2.printvalue()

bank3=Bank()
bank3.setvalue("Ac000987","Rithu",1000000)
bank3.printvalue()