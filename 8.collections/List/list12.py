#empty list
#1 to 50
#Method1
list=[]
for i in range(1,51):
    list.append(i)
print(list)

#Method2
#extend
list=[]
for i in range(1,51):
    list.extend([i])
print(list)