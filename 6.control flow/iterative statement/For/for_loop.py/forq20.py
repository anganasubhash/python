#20. Check Perfect Number
#Accept a number and determine whether it is a perfect number
#20. Check Perfect Number
#Accept a number and determine whether it is a perfect number
n=int(input("Enter the number"))
temp=n
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if n==sum:
    print(n,"is a prefect number")
else:
    print(n,"not a perfect number")