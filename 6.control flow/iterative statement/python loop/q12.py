#12. Fibonacci Series up to a Limit
#Instead of printing a fixed number of terms, generate Fibonacci numbers until they reach a given limit.
##Write a Python program to:
#•  Read a limit.
#•  Print Fibonacci numbers less than or equal to the limit

limit=int(input("Enter the limit n:"))
a=0
b=1
while a<=limit:
    print(a,end=" ")
    a,b=b,a+b
    

