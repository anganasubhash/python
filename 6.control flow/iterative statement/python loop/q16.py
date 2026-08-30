#16. Automorphic Number
#An Automorphic number is a number whose square ends with the same digits as the number itself.
#Write a Python program to:
#•  Read a number.
#•  Find its square.
#•  Check whether it is an Automorphic number


n=int(input("Enter the number:"))
square=n*n
if square%(10**len(str(n)))==n:
    print(n,"is a Automorphic number")
else:
    print(n,"is not Automorphic number")