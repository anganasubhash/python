#oddnumbers, square
lst=[10,21,31,40,51,60,71,80,90]
lst1=list(filter(lambda x:x%2!=0,lst))
print(lst1)
lst2=list(map(lambda x:x*x,lst1))
print(lst2)