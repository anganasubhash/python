#9. Monthly Expenses
#Store five monthly expenses.
#bullet Calculate the total expense.
#bullet Find the highest expense

expense=[500,1000,2000,1500,500]
total_expense=0
highest_expense=0
for i in expense:
    total_expense+=i
    if i>highest_expense:
        highest_expense=i
print("Total expense=",total_expense)
print("Highest expense=",highest_expense)