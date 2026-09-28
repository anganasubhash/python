# Flatten a nested list [[1, 2, 3], [4, 5], [6, 7, 8, 9]] into a single list
list= [[1, 2, 3], [4, 5], [6, 7, 8, 9]] 
lst1=[i for sublist in list for i in sublist]
print(lst1)