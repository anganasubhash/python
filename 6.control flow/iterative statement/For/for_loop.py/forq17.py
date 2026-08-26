#17. Find the Highest Common Factor (HCF)
#Accept two numbers and find their HCF using a for loop
num1=int(input("Enter the number 1:"))
num2=int(input("Enter the number2:"))
if num1<num2:
    small=num1
else:
    small=num2
hcf=0
for i in range(1,small+1):
    if num1%i==0 and num2%i==0:
       hcf=i
print("HCF=",hcf)