#A company has 5  employee,enter their salaries and calculate total salary expense

salary=int(input("Enter the salary of employee:"))
Total_salary=0
for i in range (4):
    Total_salary+=salary
    salary=int(input("Enter the salary of employee:"))
Total_salary+=salary

print("Total salary expense=",Total_salary)
    
    