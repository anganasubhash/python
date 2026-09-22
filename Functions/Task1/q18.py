#Q18. Prime Numbers Between Limits
#Task:
#Create a function prime_range(lower, upper)
def prime_range(lower, upper):
    for n in range(lower,upper+1):
        if n<2:
            continue
        flag=0
        for i in range(2,n):
            if n%i==0:
                flag=1
                break
        if flag==0:
           print(n,end=" ") 
lower1=int(input("Enter the lowerlimit:"))
upper1=int(input("Enter the upper limit:"))
prime=prime_range(lower1,upper1)
