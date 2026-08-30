#20. Largest Digit
#A mobile application wants to identify the largest digit in a user's PIN.
#Write a Python program to:
#•  Read a number.
#•  Find and display the largest digit using a loop

n=int(input("Enter the number:"))
largest=0
while n>0:
    digit=n%10
    if digit>largest:
       largest=digit
    n//=10
print("largest digit=",largest)

