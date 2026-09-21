#Task:
#Create a function salary(basic_salary) that adds a 10% bonus and returns the final salary
def function_salary(basic_salary):
    final_salary=basic_salary+basic_salary*10/100
    return final_salary
salary1=int(input("Enter your salary:"))
salary=function_salary(salary1)
print(salary)
