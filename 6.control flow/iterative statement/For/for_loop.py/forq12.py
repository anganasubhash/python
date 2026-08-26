#12. Check Palindrome Number
#Accept a number and determine whether it is a palindrome
n=int(input("Enter the number:"))
temp=n
rev=0
for i in range(len(str(temp))):
    digit=temp%10
    rev=rev*10+digit
    temp//=10
if n==rev:
    print(n,"is palindrome")
else:
    print(n,"not palindrome")