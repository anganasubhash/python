#19. Spy Number
#A Spy number has the sum of its digits equal to the product of its digits.
#Write a Python program to:
#•  Read a number.
#•  Calculate the sum and product of its digits.
#•  Compare both values

n=int(input("Enter the number;"))
temp=n
sum=0
product=1
while temp>0:
    digit=temp%10
    sum+=digit
    product*=digit
    temp//=10
if sum==product:
    print(n,"is spy number")
else:
    print(n,"is not spy number")
