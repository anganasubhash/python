
#Create a function electricity_bill(units) that calculates the bill.
def electricity_bill(units):
    return 150*units
cus1=int(input("Enter the units consumed:"))
bill=electricity_bill(cus1)
print(bill)