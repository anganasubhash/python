#5. Grocery Bill
#  Enter item prices until the user enters 0. Display the final bill.
total_bill=0
price=int(input('Enter the price of product:'))
while price!=0:
    total_bill+=price
    price=int(input('Enter the price of product:'))
print("Final bill=",total_bill)
