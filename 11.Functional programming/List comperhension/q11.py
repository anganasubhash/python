
#lst1=[1,2,2,3,3,3,7,8,7,4]
#count the number
#1:1 2:2 3:3 7:2 8:1 4:1

lst1=[1,2,2,3,3,3,7,8,7,4]
lst1=[(i,lst1.count()) for i in lst1 ]
print(lst1)