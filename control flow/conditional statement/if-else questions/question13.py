#If a person's age is 13 or above, they can watch a PG-13 movie. Otherwise, access is denied

Age=int(input("Enter your age:"))
if Age>=13:
    print("you can watch a pg-13 movie")
else:
    print("Access denied")