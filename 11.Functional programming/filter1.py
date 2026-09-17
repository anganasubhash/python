#filter the even numbers from the list

lst=[1,2,3,4,5,6,7,8,9,10]
f=lambda x : x%2==0
lst1=list(filter(f,lst))
print(lst1)