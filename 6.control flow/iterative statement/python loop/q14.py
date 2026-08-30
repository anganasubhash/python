#14. Perfect Number
#A number is called a perfect number if the sum of its proper divisors equals the number itself.
#Write a Python program to:
#•  Read a number.
#•  Find all proper divisors.
#•  Check whether it is a perfect number


n=int(input("Enter the number:"))
sum=0
for i in range(1,n):
    if n%i==0:
        print(i,end=" ")
        sum+=i
print()
if n==sum:
    print(n,"is a perfect number")

