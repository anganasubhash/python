#4. Milk Collection
#Record the milk collected from 8 cows. Display only the cows that produced more than 10 liters
for i in range(1,9):
    liters=int(input("Enter the liters  of milk cow produced:"))
    if liters>10:
        print("Cow that produced more than 10 liters is  cow no:",i)