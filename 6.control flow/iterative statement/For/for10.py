#Print multiplication table of a number
n=int(input("Enter the number:"))
for i in range(1,11,):
    multi=i*n
    print(i,"X",n,"=",multi)