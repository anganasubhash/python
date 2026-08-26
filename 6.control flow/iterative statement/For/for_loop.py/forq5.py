#5. Sum of Multiples of 5
#Accept a limit N. Find the sum of all numbers between 1 and N that are divisible by 5
n=int(input("Enter limit:"))
sum=0
for i in range(1,n+1):
    if i%5==0:
       sum+=i
print(sum)
 