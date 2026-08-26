#9. Sum of Digits
#Accept an integer and calculate the sum of its digits.
n=int(input("Enter the number:"))
sum=0
for i in range(len(str(n))):
    digit=n%10
    sum+=digit
    n//=10
print("Sum of digits=",sum)