#22. Salary Collection
#Enter employee salaries until -1 is entered. Display the total salary expense

total_salary=0
salary=int(input("Enter employee salary:"))
while salary!=-1:
    total_salary+=salary
    salary=int(input("Enter employee salary:"))
print("Total salary expense:",total_salary)