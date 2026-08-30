#21. Smallest Digit
#A banking application wants to find the smallest digit in an account number.
#Write a Python program to:
#•  Read a number.
#•  Find the smallest digit using a loop

n=int(input("Enter the number:"))
smallest=9
while n>0:
    digit=n%10
    if digit<smallest:
      smallest=digit
    n//=10
print("Smallest digit=",smallest)
