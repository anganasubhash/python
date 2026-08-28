#17. Plantation Drive
#Display volunteer IDs who planted at least 20 trees.
n=int(input("Enter the total number of volunters:"))
for i in range(1,n+1):
    planted=int(input("Enter the number trees planted:"))
    if planted>=20:
        print("Volunteers ID planted more than 20 trees is V",str(i).zfill(4))