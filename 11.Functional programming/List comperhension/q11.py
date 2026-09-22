
#lst1=[1,2,2,3,3,3,7,8,7,4]
#count the number
#1:1 2:2 3:3 7:2 8:1 4:1

lst=[1,2,2,3,3,3,7,8,7,4]
dic1={i:lst.count(i) for i in lst}#dictonary comprehension 
print(dic1)

"""lst1=[(i,lst.count(i)) for i in set(lst)]
print(lst1)"""




