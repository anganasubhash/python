#10. Print Odd Numbers
#A teacher wants to display all odd numbers up to a given limit.
#Write a Python program to:
#•  Read a limit n.
#•  Print all odd numbers from 1 to n

n=int(input("Enter the limit n:"))
for i in range(1,n+1):
    if i%2!=0:
        print(i,end=" ")
