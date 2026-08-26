#6. Product of Even Numbers
#Accept a limit N. Find the product of all even numbers from 1 to N
n=int(input("Enter the limit:"))
product_even=1
for i in range(1,n+1):
    if i%2==0:
        product_even*=i
print("Product of all even number=",product_even)
