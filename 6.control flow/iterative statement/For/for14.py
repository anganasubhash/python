
#input lower limit ,upper limit
#Find even sum and odd sum

lower_limit=int(input("Enter the lower limit:"))
upper_limit=int(input("Enter the upper limit:"))
even_sum=0
odd_sum=0
for i in range(lower_limit,upper_limit+1,):
    if i%2==0:
        even_sum+=i
    else:
        odd_sum+=i
print("Sum of even number=",even_sum)
print("Sum of odd number=",odd_sum)