#13. Factorial
#A mathematics student wants to calculate the factorial of a number.
#Write a Python program to:
#•  Read a positive integer.
#•  Find its factorial using a loop

n=int(input("Enter the positive integers:"))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)