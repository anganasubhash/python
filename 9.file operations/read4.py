#number 200-211


file3=open("number1","r")
number=[]
even_number=[]
odd_number=[]
for i in file3:
    number.append(int(i.rstrip()))
print(number)
for j in number:
    if j%2==0:
        even_number.append(j)
    else:
        odd_number.append(j)
print(number)
print(even_number)
print(odd_number)
print(sum(number))
print(sum(even_number))
print(sum(odd_number))