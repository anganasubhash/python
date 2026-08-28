#Enter 10 numbers and count how much are even

count=0
for i in range(10):
    number=int(input("Enter the number:"))
    if number%2==0:
        count+=1
print("Count of even numbers =",count)

