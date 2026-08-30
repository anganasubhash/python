#27. Armstrong Numbers in a Range
#A programming contest requires listing all Armstrong numbers within a specified range.
#Write a Python program to:
#•  Read the starting and ending numbers.
#•  Print all Armstrong numbers in that range

lower_limit=int(input("Enter the lower limit:"))
upper_limit=int(input("Enter the upper limit:"))
for n in range(lower_limit,upper_limit+1):
    temp=n
    total=0
    num_digit=len(str(n))
    while temp>0:
        digit=temp%10
        total=total+digit**num_digit
        temp//=10
    if n==total:
       print(n,end=" ")