#factorial of a number
#5
#5!=5*4*3*2*1
n=int(input("enter the number:"))
i=1
fact=1
while i<=n:
    fact=fact*i
    i+=1
print(fact)
