
#Given two lists names = ['Amit', 'Bala', 'Chitra'] and marks = [85, 40, 92],
#create a list of names where marks are greater than 50
names = ['Amit', 'Bala', 'Chitra']
marks = [85, 40, 92]
lst = [names[i] for i in range(len(names)) if marks[i] > 50]
print(lst)
