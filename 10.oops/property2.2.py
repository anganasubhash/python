#class UPI,card,atm
#pay
#different behaviour
class UPI:
    def pay(self):
        print("Pay with UPI")
class Card:
    def pay(self):
        print("Pay with card")
class Cash:
    def pay(self):
        print("Pay with cash")

u=UPI()
u.pay()
c=Card()
c.pay()
c1=Cash()
c1.pay()