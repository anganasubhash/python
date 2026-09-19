#Method2
#---------
#list of elements added in to list based on one condition
#1-100---evennumber
lst=[i for i in range(1,101) if i%2==0]
print(lst)

#1-50--- odd numbers
lst=[i for i in range(1,51) if i%2!=0]
print(lst)