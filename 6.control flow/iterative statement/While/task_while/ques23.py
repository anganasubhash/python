#23. Daily Expenses
#Enter expenses until 0 is entered. Display the total expense
total_expense=0
expense=int(input("Enter the expense;"))
while expense!=0:
    total_expense+=expense
    expense=int(input("Enter the expense;"))
print("Total expense=",total_expense)

