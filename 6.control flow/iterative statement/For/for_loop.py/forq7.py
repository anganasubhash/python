#7. Reverse Number Using Loop
#Accept an integer and reverse it using a for loop (without converting it to a string)
n=int(input("Enter the number:"))
rev=0
for i in range(len(str(n))):
    digit=n%10
    rev=rev*10+digit
    n=n//10
print(rev)