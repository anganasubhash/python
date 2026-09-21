#Task:
#Create a function loan_eligibility(salary) that returns Eligible or Not Eligible
def  loan_eligibility(salary):
    if salary>25000:
        return "eligible for loan"
    else:
        return "Not eligible"
salary1=int(input("Enter your salary:"))
Salary=loan_eligibility(salary1)
print(Salary)