#29. Prime Fibonacci Numbers
#A research project requires identifying Fibonacci numbers that are also prime.
#Write a Python program to:
#•  Read a limit.
#•  Generate Fibonacci numbers up to the limit.
#•  Print only those Fibonacci numbers that are prime

limit=int(input("Enter the limit:"))
a=0
b=1
while a<=limit:
    num=a
    flag=0
    if num<2:
        flag=1
    for i in range(2,num):
        if num%i==0:
          flag=1
          break
    if flag==0:
        print(num,end=" ")
    a,b=b,a+b
print()



    