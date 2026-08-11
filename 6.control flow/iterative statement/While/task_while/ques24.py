#24. Library Fine
#Enter overdue days until a valid positive number is entered

number=int(input("Enter the number:"))
while number<=0:
    print("invalid number")
    number=int(input("Enter the number"))
print("overdue days",number)
