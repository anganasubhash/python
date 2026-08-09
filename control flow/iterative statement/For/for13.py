#sum of even number
lower_limit=int(input("Enter the lower limit:"))
upper_limit=int(input("Enter the upper limit:"))
even_sum=0
for i in range(lower_limit,upper_limit+1):
    if i%2==0:
        even_sum+=i
print(even_sum)