
smallest=10
n=int(input("Enter how many number do you want:"))
for i in range(n):
    num=int(input("Enter the number;"))
    if num<smallest:
        smallest=num
print("Smallest number is",smallest)
        
