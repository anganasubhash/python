
#Create a function is_prime(num) that returns True or False
def prime(num):
    if num<2:
        return False
    flag=0
    for i in range (2,num):
        if num%i==0:
            flag=1
            break
    if flag>0:
        return False
    else:
        return True
num1=int(input("Enterthe number:"))
number=prime(num1)
print(number)


      
       

