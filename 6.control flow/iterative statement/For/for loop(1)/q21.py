#21. Courier Service
#Display package IDs requiring heavy-load handling (weight > 10 kg)
n=int(input("Enter the total number of package:"))
for i in range(1,n+1):
    weight=int(input("Enter the package weightage in kg:"))
    if weight>10:
        print("Package id requiring heavy load handling is W",str(i).zfill(4))