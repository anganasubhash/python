#2. Find the Largest Number
#Accept N numbers from the user and print the largest number entered


n=int(input("How many number do you want:"))
largest=int(input("Enter the number:"))
for i in range(n-1):
    num=int(input("Enter the number :"))
    if num>largest:
        largest=num

print(largest)

 
    