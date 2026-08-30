#30. Complete Number Analyzer
#A number analysis application performs multiple checks on a single number.
#Write a Python program to:
#•  Read an integer.
#•  Determine whether it is: Even or Odd, Prime or Not Prime, Palindrome or Not, Armstrong or Not, Strong
#or Not, Harshad or Not.
#•  Display the result of each check using loops and conditional statements wherever applicable

n=int(input("Enter the number:"))


if n%2==0:
    print("Even number")
else:
    print("Odd number")


flag=0

if n<2:
    flag=1

for i in range(2,n):
    if n%i==0:
        flag=1
        break

if flag==0:
    print("Prime number")
else:
    print("Not a prime number")


temp=n
rev=0

while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp//=10

if n==rev:
    print("Palindrome")
else:
    print("Not a palindrome")



temp=n
total=0
num_digit=len(str(n))

while temp>0:
    digit=temp%10
    total=total+digit**num_digit
    temp//=10

if n==total:
    print("Armstrong number")
else:
    print("Not an Armstrong number")



temp=n
total=0

while temp>0:
    digit=temp%10

    fact=1

    for i in range(1,digit+1):
        fact=fact*i

    total=total+fact
    temp//=10

if n==total:
    print("Strong number")
else:
    print("Not a Strong number")



temp=n
digit_sum=0

while temp>0:
    digit=temp%10
    digit_sum=digit_sum+digit
    temp//=10

if n%digit_sum==0:
    print("Harshad number")
else:
    print("Not a Harshad number")

