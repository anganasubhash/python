#14. Mobile Repair Shop
#Display repair IDs whose repair charge exceeded 5000
n=int(input("Enter the total number of mobile repair: "))
for i in range(1,n+1):
    charge=int(input("Enter the repair charge:"))
    if charge>5000:
        print("Repair id of mobile  repair charge exceed 5000 is m",str(i).zfill(3))