#13. Check Prime Number
#Accept a number and determine whether it is prime using a for loop
n=int(input("Enter the number:"))
flag=0 
if n<2:
    flag=1
else:
     for i in range(2,n):
       if n%i==0:
          flag=1
          break
if flag>0:
    print(n," notprime")
else:
    print(n,"prime")