#abstraction
#Bank-parent class
#childclass-SBI,ICIC,HDFC
#method--->interest
#


from abc import abstractmethod,ABC
class Bank(ABC):
    @abstractmethod
    def interest(self):
        pass
class SBI(Bank):
    def interest(self):
        print("SBI:Interest is 5%")
class ICIC(Bank):
    def interest(self):
        print("ICIC:interest is 7%")
class HDFC(Bank):
    def interest(self):
        print("HDFC:interest is 4%")
cus1=SBI()
cus1.interest()
cus2=ICIC()
cus2.interest()
cus3=HDFC()
cus3.interest()
        
