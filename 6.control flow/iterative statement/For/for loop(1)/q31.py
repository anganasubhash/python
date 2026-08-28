#31. Construction Site
#Print worker IDs eligible for a productivity bonus (more than 500 bricks)
n=int(input("Enter the total number of workers:"))
for i in range(1,n+1):
    brick=int(input("Enter the number of bricks:"))
    if brick>500:
        print("workers IDs eligible for productivity bonus is W",str(i).zfill(3))