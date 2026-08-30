#22. Decimal to Binary Conversion
#A computer science student wants to understand binary conversion.
#Write a Python program to:
#•  Read a decimal number.
#•  Convert it to binary using loops.
#•  Display the binary value

n=int(input("Enter the number:"))
binary=""
while n>0:
    remainder=n%2
    binary=str(remainder)+binary
    n//=2
print("binary number of is",binary)