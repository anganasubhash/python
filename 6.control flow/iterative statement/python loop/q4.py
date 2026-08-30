#4. Armstrong Number
#A mathematics teacher wants students to identify Armstrong numbers. An Armstrong number is equal to
#the sum of its digits raised to the power of the number of digits.
#Write a Python program to:
#•  Read a number.
#•  Find the number of digits.
#•  Calculate the Armstrong sum.
#•  Display whether it is an Armstrong number

n=int(input("Enter the number:"))
temp=n
num_digit=len(str(n))
total=0
while temp>0:
    digit=temp%10
    total=total+digit**num_digit
    temp//=10
if n==total:
    print(n,"Is armstrong number")
else:
    print(n,"is not armstrong number")
