#28. Palindrome Numbers in a Range
#A puzzle game rewards players for finding palindrome numbers.
#Write a Python program to:
#•  Read the starting and ending values.
#•  Print all palindrome numbers within the range

lower_limit=int(input("Enter the lower limit:"))
upper_limit=int(input("Emter the upper limit:"))
for n in range(lower_limit,upper_limit+1):
    temp=n
    rev=0
    while temp>0:
        digit=temp%10
        rev=rev*10+digit
        temp//=10
    if n==rev:
        print(n,end=" ")