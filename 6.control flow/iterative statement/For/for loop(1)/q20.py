#20. Road Construction
#Print "Target Achieved" whenever weekly work exceeds 10 km
n=int(input("Enter the number of road constuction work:"))
for i in range(1,n+1):
    work=int(input("Enter the weekly work in km:"))
    if work>10:
        print("Target Achieved")
