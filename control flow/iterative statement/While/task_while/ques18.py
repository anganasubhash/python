#
#18. Restaurant Order
#Keep entering food prices until the customer types 0. Display the bill
bill=0
price=int(input("Enter the food price:"))
while price!=0:
    bill+=price
    price=int(input("Enter the food price:"))
print("Total bill=",bill)
