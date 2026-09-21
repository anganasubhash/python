#Scenario:
#A restaurant needs to calculate customer bills.
#Task:
#Create a function calculate_bill(price, quantity) that returns the total bill.
def calculate_bill(price, quantity):
    total_bill=price*quantity
    return total_bill
price1=int(input("Enter the price:"))
quantity1=int(input("Enter the quqntity:"))
bill=calculate_bill(price1,quantity1)
print("Total bill=",bill)