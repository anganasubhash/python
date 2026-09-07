
file3=open("word1","r")
fruits={}
for i in file3:
    word=i.rstrip('\n')
    if word not in fruits:
        fruits[word]=1
    else:
        fruits[word]+=1
print(fruits)
for key,value in fruits.items():
    print(key,":",value)