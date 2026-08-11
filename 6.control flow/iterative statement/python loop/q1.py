#1. Fibonacci Series
##A teacher asks you to generate the first n numbers of the Fibonacci sequence. The Fibonacci series starts
#with 0 and 1, and each next number is the sum of the previous two numbers.
#Write a Python program to:
#  Read the value of n.
# Print the first n Fibonacci numbers using a loop

n=int(input("Enter value of n:"))
a=0
b=1
for i in range(n):
      print(a,end=" ")
      a,b=b,a+b
print()

       
       