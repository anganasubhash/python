#Task:
#Create a function factorial(num)
def factorial(num):
    fact=1
    for i in range(1,num+1):
         fact*=i 
    return fact
num1=int(input("Enter the number:"))
number=factorial(num1)
print("Factorial=",number)
