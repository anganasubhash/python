#10. Product of Digits
#Accept an integer and calculate the product of its digits
n=int(input("Enter the number:"))
product=1
for i in range(len(str(n))):
    digit=n%10
    product*=digit
    n//=10
print("Product of digits=",product)