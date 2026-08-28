#39. Drone Delivery Service
#Display order IDs where delivery took more than 60 minutes
n=int(input("Enter the total number of order taken:"))
for i in range(1,n+1):
    time=int(input("Enter the time taken for order in minutes:"))
    if time>60:
        print("Order IDs delivery took more than 60 mimutes is R",str(i).zfill(2))
