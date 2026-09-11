#11. Employee Salary Analysis
#Store salaries of 10 employees.
#bullet Count employees earning above 40,000.
#bullet Display salaries below 25,000


salaries=[20000,15000,50000,45000,10000,15000,60000,55000,75000,13000]
count=0
for i in salaries:
    if i>40000:
        count+=1
    elif i<25000:
        print(i,end=" ")
    else:
        pass
print("\nEmployees earning above 40000=",count)

