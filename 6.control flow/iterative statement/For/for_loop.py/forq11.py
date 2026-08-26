#11. Check Armstrong Number
#Accept a three-digit number and check whether it is an Armstrong number
n=int(input("Enter the number:"))
temp=n
number_digit=(len(str(n)))
number=0
for i in range(len(str(temp))):
    digit=temp%10
    number=number+digit**number_digit
    temp//=10
if n==number:
    print(n,"armstrong number")
else:
    print(n,"not armstrong number")


