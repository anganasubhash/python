#18. Find the Least Common Multiple (LCM)
#Accept two numbers and find their LCM using a for loop
num1=int(input("Enter the number1:"))
num2=int(input("Enter the number2:"))
if num1<num2:
    small=num1
else:
    small=num2
gcd=0
for i in range(1,small+1):
    if num1%i==0 and num2%i==0:
        gcd=i
lcm=(num1*num2)/gcd
print("LCM=",lcm)