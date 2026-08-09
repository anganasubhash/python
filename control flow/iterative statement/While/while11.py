lower_limit=int(input("enter the lower limit:"))
upper_limit=int(input("enter the upper limit:"))
sum=0
while lower_limit<=upper_limit:
    sum+=lower_limit
    lower_limit+=1
print(sum)