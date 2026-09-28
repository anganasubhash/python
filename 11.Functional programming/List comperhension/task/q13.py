#Given a list of numbers with duplicates [1, 2, 2, 3, 4, 4, 5], create a list containing only
#the unique elements (preserve order).
lst1=[1, 2, 2, 3, 4, 4, 5]
lst3=[]
lst2=[lst3.append(i) for i in lst1 if i not in lst3]
print(lst3)
