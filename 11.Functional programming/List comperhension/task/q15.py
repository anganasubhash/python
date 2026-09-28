#Given two lists of equal length a = [1, 2, 3] and b = [4, 5, 6], create a list of their
#element-wise sums using a list comprehension with zip().
a = [1, 2, 3]
b =[4 ,5 ,6]
lst1=[x+y for x,y in zip(a,b)]
print(lst1)
