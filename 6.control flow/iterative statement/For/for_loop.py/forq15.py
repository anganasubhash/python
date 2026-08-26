#15. Print Factors of a Number
#Accept a number and print all of its factors
n=int(input("Enter the number:"))
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")