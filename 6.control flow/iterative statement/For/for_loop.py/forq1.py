#1. Count Even and Odd Numbers
#Write a program to accept N numbers from the user one by one using a for loop. Count how many are
#even and how many are odd
n=int(input("How many numbers you want to count:"))
count_even=0
count_odd=0
for i in range(n):
    num=int(input("Enter the number:"))
    if num%2==0:
        count_even+=1
    else:
        count_odd+=1
print("Number of even number:",count_even)
print("Number of odd number:",count_odd)
    
        

