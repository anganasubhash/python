#read file
#dictonary
#{aple:4,....}
#key:value
file1=open("word","r")
fruits={}
for j in file1:
    if j.rstrip() not in fruits:
        fruits[j.rstrip()]=1
    else:
        fruits[j.rstrip()]+=1
print(fruits)
for key,value in fruits.items():
    print(key,value)

    #or

#convert to list 
#Take a long paragraph
"""file2=open("Word","r")
dic={}
for i in file2:
    data=i.split(" ")
    print(data)
for j in data:
    if j not in dic:
        dic[j]=1
    else:
        dic[j]+=1
print(dic)"""

