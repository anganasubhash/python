#2. Prime Number Check
#A bank uses prime numbers for encryption. Your task is to check whether a given number is prime. A
#prime number has exactly two factors: 1 and itself.
#Write a Python program to:
#•  Read a number.
#•  Check whether it is prime using a loop.
#•  Display an appropriate message

n=int(input("Enter the value of n: "))
flag=0
if n<2:
    print("Not prime")
else:
    for i in range(2,n):
      if n%i==0:
        flag=1
        break
    if flag>0:
     print("Not prime")
    else:
     print("Prime")