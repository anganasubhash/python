#
str="Luminartechnolab"
vowels="aeiouAEIOU"
count=0
list=[]
for i in str:
    if i in vowels: 
        list.append(i)
        count+=1
print(list)
print(count)