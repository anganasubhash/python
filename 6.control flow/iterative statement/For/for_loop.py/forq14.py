#14. Print All Prime Numbers
#Accept a range N and print all prime numbers from 2 to N
n=int(input("Enter the limit"))
for n in range(2,n+1):
        flag=0
        if n<2:
            continue
        else:
            for i in range(2,n):
              if n%i==0:
               flag=1
               break
        if flag==0:
          print(n,end=" ")