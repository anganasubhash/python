#From a list of numbers, replace even numbers with "Even" and odd numbers with "Odd".
lst=[23,56,78,34,55,90]
lst1=["even"if i%2==0 else "odd" for i in lst]
print(lst1)