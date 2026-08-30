#24. Greatest Common Divisor (GCD)
#Two students want to find the greatest common divisor of two numbers.
#Write a Python program to:
#•  Read two integers.
#•  Find their GCD using loops.

a=int(input("Enter number1:"))
b=int(input("Enter number2:"))
small=0
if a<b:
    small=a
else:
    small=b
gcd=0
for i in range(1,small+1):
    if a%i==0 and b%i==0:
        gcd=i
print("Greatest common divisor of 2 number=",gcd)

