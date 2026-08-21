 
lst12=["apple","orange","banana"]
#papaya
#APPEND---------->Add
lst12.append("papaya")
print(lst12)
#EXTEND-------->Add mulitiple element
lst12.extend(["kiwi","Avocado"])
print(lst12)
#INSERT------>index location based
lst12.insert(1,"mango")
print(lst12)


#REMOVE-------to remove elements
#ist12.remove("name of element to remove")
lst12.remove("banana")
print(lst12)

#  POP
#------------------
#pop()----------->it remove the last element
#pop(mention the index)
#pop(1)------------->it remove from that index
lst12.pop(1)
print(lst12)


#INDEX
#---------
#To get the index of the given element
print(lst12.index("Avocado"))


#REVERSE
#------------
lst12.reverse()
print(lst12)


lst12.append("apple")
print(lst12)

#COUNT
#-------------
print(lst12.count("apple"))

#COPY
#----------
#copy lst12 to fruits
fruits=lst12.copy()
print(fruits)


#CLEAR
#--------
#empty the list
lst12.clear()
print(lst12)


#sort-----ascending
#sort(reverse=True)------desening


#function--------#sum()
#                 #len()
#                 #max()
#                 #min()


#Forward slicing
#Backward slicing
