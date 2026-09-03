#read the file
#Add to list

"""file2=open("numbers","r")
for i in file2:
    print(i)"""


file2=open("numbers","r")
lst1=[]
for i in file2:
    lst1.append(int(i))
print(lst1)

file2=open("numbers","r")
lst1=[]
for i in file2:
    lst1.append(int(i.rstrip()))
print(lst1)
print(sum(lst1))

#strip --->used to remove---> /n
#strip---->lstrip--remove from left ,rstrip ---remove from right

