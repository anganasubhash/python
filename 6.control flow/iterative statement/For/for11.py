#print even number 
lower_limiT=int(input("Enter the lower limit:"))
upper_limit=int(input("Enter the upper limit:"))

for i in range(lower_limiT,upper_limit+1):
    if i%2==0:
        print(i)
