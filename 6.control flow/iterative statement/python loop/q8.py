#8. Product of Digits
#A game calculates the product of digits to determine the player's score.
#Write a Python program to:
#•  Read a number.
#•  Multiply all its digits.
#•  Display the product


n=int(input("Enter the number:"))
product=1
while n>0:
    digit=n%10
    product*=digit
    n//=10
print("Product of digit is",product)