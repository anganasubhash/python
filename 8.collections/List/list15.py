#[]
#1 to 50
#even-list
#odd-list
#sum of all
#len of all
list=[]
even_list=[]
odd_list=[]
even_sum=0
odd_sum=0
for i in range(1,51):
    list.append(i)
    if i%2==0:
        even_list.append(i)
        even_sum+=i
    else:
        odd_list.append(i)
        odd_sum+=i
        
print(list)
print(even_list)
print(odd_list)
print(even_sum)
print(odd_sum)
print(len(list))
print(len(even_list))
print(len(odd_list))