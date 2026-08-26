#8. Count Digits in a Number
#Accept a number and count the number of digits using a for loop
n=int(input("Enter the number:"))
count=0
for i in range(len(str(n))):
    count+=1
print("Number of digits=",count)