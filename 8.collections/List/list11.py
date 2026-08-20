lst=[]
#30
lst.append(30)
print(lst)
lst.append("Hello")
print(lst)
lst.append(20)
print(lst)

#To add multiple elements
lst.extend([100,200])
print(lst)
lst1=[]
lst1.extend([900,True,False,87,67])
print(lst1)
 #insert----------> to add new element to index position without replacing the other
lst1.insert(2,"hello")
print(lst1)