#FUNCTIONAL PROGRAMMING
#------------------------------
#functions---->Reusability--->traditional apporach
#functional programming is modern apporach
"""def add(num1,num2):
    res=num1+num2
    print(res)
add(20,23)"""
#-----------------------------
#Lambda
#Map
#Filter
#List comprehension

#LAMBDA
#-----------------
#Anonymous function----No name function
#variable=lambda argument:operations
#print(variable(inputs))

#FILTER_MAP(convert)
#---------------
#map
#[1,2,3,4,5,6,7,8,9,10]====>[1,4,9,25,36,49,64,81,100]
#[1000,2000,3000]=====>[6000,7000,8000]====>(adding 5000)
#To convert each one/Apply on each one

#filter
#[1,2,3,4,5,6,7,8,9,10]=====>[2,4,6,8]---taken even one



#syntax
#mapping
#-----------------
#fully convert 
#var=list(map(function,itertable))
#function----operation
#itertable ----list want to convert
#filter
#-----------------
#condition based filteration
#var=list(filter(function,itertable))



#LIST COMPERHENSION
#-------------------
#single line optimization
#list--1-100
"""lst=[]
for i in range(1,101):
    lst.append(i)
print(lst)"""

#shortcut

#Method1
#--------
#list/Range of elements added in to list
#var=[print range]
"""lst=[i for i in range(1,101)]
    print(lst) """  

#Method2
#---------
#list of elements added in to list based on one condition

#var=[print range condition]
"""lst=[i for i in range(1,71) if i%5==0]
    print(lst)"""

#Method3
#--------
#list of elements added in to list based on more one condition/Muitiple condition
#var=[print condition1 condition2 range]
#no elif
#var=[print1 if cond1 else print2 range]
#var=[print1 if cond1 else print2 if cond2 else print3 if cond3 range]


