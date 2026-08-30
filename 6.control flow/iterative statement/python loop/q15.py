#15. Strong Number
#A Strong number is equal to the sum of the factorials of its digits.
#Write a Python program to:
#•  Read a number.
#•  Calculate the factorial of each digit.
#•  Check whether it is a Strong number

n=int(input("Enter the number:"))
temp=n
sum=0
while temp>0:
    digit=temp%10
    fact=1
    for i in range(1,digit+1):
        fact*=i
    sum+=fact
    temp//=10
if n==sum:
    print(n, "is a strong number")
else:
    print(n,"is not strong number")
