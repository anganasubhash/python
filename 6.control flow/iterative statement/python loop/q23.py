#23. Binary to Decimal Conversion
#A network engineer receives binary data and wants to convert it into decimal.
#Write a Python program to:
#•  Read a binary number.
#•  Convert it into decimal using loops

n=int(input("Enter the binary number:"))
decimal=0
power=0
while n>0:
    digit=n%10
    decimal=decimal+(digit*(2**power))
    n//=10
    power+=1
print("Decimal number is" ,decimal)