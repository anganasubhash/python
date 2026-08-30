#18. Neon Number
#A Neon number is a number where the sum of the digits of its square equals the original number.
#Write a Python program to:
#•  Read a number.
#•  Calculate its square.
#•  Find the sum of digits of the square.
#•  Check whether it is a Neon number

n=int(input("Enter the number:"))
square=n*n
temp=square
sum=0
while temp>0:
    digit=temp%10
    sum+=digit
    temp//=10
if n==sum:
    print(n,"is neon number")
else:
    print(n,"is not neon number")
