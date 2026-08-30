#7. Count Digits
#An online form validates the length of an ID number.
#Write a Python program to:
#•  Read an integer.
#•  Count the total number of digits using a loop.
#•  Display the count

n=int(input("Enter the number:"))
count=0
while n>0:
    digit=n%10
    count+=1
    n//=10
print("Total number of digit=",count)