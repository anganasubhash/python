#35. Hotel Customer Feedback
#Display customer IDs who gave a 5-star rating
n=int(input("Enter total number of customers:"))
for i in range(1,n+1):
    rating=int(input ("Enter the rating:"))
    if rating==5:
        print("customer ID gave 5 star rating is C",str(i).zfill(4))