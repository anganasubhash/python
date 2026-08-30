#tuple is unmutable
#so use list()--convert tuple to list
# then list to tuple

#convert tuple to list added the element
tup4=(100,200,300,400,500,600)
print(tup4)
list=list(tup4)
list[2]="Hello"
print(list)

# convert list to tuple
# use tuple() function
tup=tuple(list)
print(tup)