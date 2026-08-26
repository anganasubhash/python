#3. Find the Smallest Number
#Accept N numbers from the user and print the smallest number

n=int(input("Enter how many number do you want:"))
smallest=int(input("Enter the number:"))
for i in range(n-1):
    num=int(input("Enter the number;"))
    if num<smallest:
        smallest=num
print("Smallest number is",smallest)
        
