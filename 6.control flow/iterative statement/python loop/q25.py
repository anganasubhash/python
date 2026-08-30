#25. Least Common Multiple (LCM)
#A scheduling application needs to find when two repeating events occur together.
#Write a Python program to:
#•  Read two numbers.
#•  Find their LCM using loops

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
lcm=(a*b)//gcd
print("least common multiple",lcm)
