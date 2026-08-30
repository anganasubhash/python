#6. Sum of Digits
#A mobile app calculates the sum of all digits entered by the user.
#Write a Python program to:
#•  Read a number.
#•  Find the sum of all digits using a loop.
#•  Display the result

n=int(input("Enter the number:"))
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n//=10

print("Sum of digits of number is",sum)