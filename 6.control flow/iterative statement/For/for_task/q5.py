
#A store receives stock for 5 products 
#Enter quantity and calculate total stock

total_stock=0
for i in range(1,6):
    quantity=int(input("enter the quantity:"))
    total_stock+=quantity
print("Total stock=",total_stock)