#37. Warehouse Packaging
#Print employee IDs eligible for an incentive (packed more than 200 packages).
n=int(input("Enter total number of employee:"))
for i in range(1,n+1):
    package=int(input("Enter the packed package:"))
    if package>200:
        print("Employee id eligible for incentive is E",str(i).zfill(4))