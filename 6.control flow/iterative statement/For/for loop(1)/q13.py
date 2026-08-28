#13. Bike Service Center
#Print "Free Wash" for every 5th customer

n=int(input("Enter the total number of customers:"))
for i in range(1,n+1):
    if i%5==0:
        print("Free wash for customer",i)