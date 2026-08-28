#9. Cinema Snack Counter
#Print a receipt number (R001, R002...) for each customer
n=int(input("Enter number of customers:"))
for i in range(1,n+1):
    print("Recipt number:R",str(i).zfill(3))

