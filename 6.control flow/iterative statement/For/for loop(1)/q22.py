#22. Fashion Store
#Print "Gift Coupon" for customers whose bill exceeds 3000
n=int(input("Enter the total number of customers:"))
for i in range(1,n+1):
    bill=int(input("Enter the bill amount:"))
    if bill>3000:
        print("Gift Coupon")