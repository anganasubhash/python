#Generate a list of tuple containing two numbers whose  sum  is even number
#number=[1,2,3,4,5]
#0/p==>[(1,1),(1,3),(1,5).....]
number=[1,2,3,4,5]
lst=[(i,j)for i in number for j in number if (i+j)%2==0]
print(lst)
