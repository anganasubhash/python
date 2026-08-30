#5. Reverse a Number
#An ATM displays account numbers in reverse order for testing.
#Write a Python program to:
#•  Read an integer.
#•  Reverse the digits using a loop.
#•  Display the reversed number

n=int(input("Enter the number:"))
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
print("Reverse of number is",rev)