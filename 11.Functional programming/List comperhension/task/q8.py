#Create a list of all pairs (x, y) where x is from [1, 2, 3] and y is from [4, 5, 6], but only
#if x + y is even
lst1=[1, 2, 3]
lst2=[4, 5, 6]
number=[(x,y)for x in lst1 for y in lst2 if (x+y)%2==0]
print(number)