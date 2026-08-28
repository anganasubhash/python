#8. Bakery Sales
#Display the day numbers when cake sales exceeded 100 cakes
n=int(input("Enter the total number of days:"))
for i in range(1,n+1):
    sales=int(input("Enter the number of cakes saled:"))
    if sales>100:
        print("Day number cake sales exceeded 100 is Day ",i)