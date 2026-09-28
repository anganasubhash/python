#Given a list of numbers, create a list of numbers rounded to 2 decimal places, but only keep
#those greater than a given threshold (e.g., 5.0)
lst = [2.345, 5.678, 7.891, 4.567, 9.123]
threshold = 5.0
lst1 = [round(i, 2) for i in lst if i > threshold]
print(lst1)