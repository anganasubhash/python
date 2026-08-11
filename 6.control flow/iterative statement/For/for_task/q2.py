
#A customer buys 4 items 
#Enter the price of each item and find total bill
total_bill=0
for i in range(1,5):
    price=int(input("Enter the price of the item:"))
    total_bill+=price
print("Total bill=",total_bill)