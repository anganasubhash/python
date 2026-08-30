#26. Perfect Numbers in a Range
#A mathematics teacher wants to display all perfect numbers within a given range.
#Write a Python program to:
#•  Read the starting and ending values.
#•  Print every perfect number in that range

lower_limit=int(input("Enter the lower limit:"))
upper_limit=int(input("Enter the upper limit:"))
for n in range(lower_limit,upper_limit+1):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    if n==sum:
        print(n,end=" ")
