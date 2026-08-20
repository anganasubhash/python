#no duplicate
list1=[10,10,45,65,45,89,32,23,32,"ML","DL","ML"]
list=[]
for i in list1:
     if i not in list:
      list.append(i)
print(list)