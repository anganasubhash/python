#3. Employee Salary Increment
#Write a function salary_update().
#•  Store employee salaries in a list.
#•  Increase salaries below n25,000 by 10%.
#•  Use a loop to display updated salaries.
#•  Find the average salary
def salary_update():
    for i in range(len(salary)):
        if salary[i]<25000:
            salary[i]+=salary[i]*10/100
    for i in salary:
        print(i)
    print(sum(salary)/len(salary))
salary=[20000,40000,30000,15000,10000,55000]
salary_update()