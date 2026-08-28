#15. Juice Shop
#Display the hour numbers when sales were zero
#15. Juice Shop
#Display the hour numbers when sales were zero
n=int(input("Enter the total number of hours:"))
for i in range(1,n+1):
    sales=int(input("Enter the sales hours :"))
    if sales==0:
        print("Hour number when sales were zero is",i," th hour")