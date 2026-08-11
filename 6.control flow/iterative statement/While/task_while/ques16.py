
#16. Shopping Discount
#Enter product prices until 0 is entered. Calculate the total amount
total=0
price=int(input("Enter the product price:"))
while price!=0:
    total+=price
    price=int(input("Enter the product price:"))
print("Total amount=",total)

