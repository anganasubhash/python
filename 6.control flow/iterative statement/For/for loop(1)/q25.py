#25. Toy Factory
#Display worker IDs who produced more than 100 toys

n=int(input("Enter the total number of workers:"))
for i in range(1,n+1):
    toys=int(input("Enter the number of toys produced:"))
    if toys>100:
        print("Workers IDs produced more than 100 toys is T",str(i).zfill(3))