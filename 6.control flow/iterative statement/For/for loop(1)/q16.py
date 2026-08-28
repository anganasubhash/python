#16. Charity Donation
#Print a thank-you message only for donors contributing 1000 or more
n=int(input("Enter the total number of donars:"))
for i in range(1,n+1):
    contribution=int(input("Enter the donors contribution:"))
    if contribution>=1000:
        print("Thank-you")