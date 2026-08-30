#11. Prime Numbers Between Two Numbers
#A school science club wants to list all prime numbers within a given range.
#Write a Python program to:
#•  Read the starting and ending numbers.
#•  Print all prime numbers between them


lower_limit=int(input("Enter the lowerlimit;"))
upper_limit=int(input("Enter the upperlimit:"))
for n in range(lower_limit,upper_limit+1):
    
    if n<2:
        continue
    flag=0
    for i in range(2,n):
        if n%i==0:
            flag=1
            break
    if flag==0:
        print(n,end=" ")
    