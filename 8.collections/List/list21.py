#consoanants
str="Luminartechnolab"
vowels="aeiouAEIOU"
count=0
list=[]
for i in str:
    if i not in vowels:
        list.append(i)
        count+=1
print(count)
print(list)