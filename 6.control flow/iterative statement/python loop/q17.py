#17. Harshad Number
#A Harshad number is divisible by the sum of its digits.
#Write a Python program to:
#•  Read a number.
#•  Find the sum of its digits.
#•  Check whether the number is divisible by that sum.


n=int(input("Enter the number:"))
temp=n
sum=0
while temp>0:
    digit=temp%10
    sum+=digit
    temp=temp//10
if n%sum==0:
    print(n,"is a harshad number")
else:
    print(n,"is not harshad number")