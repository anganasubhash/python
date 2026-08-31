#Dictonary
#---------------
#Collection  that is used to  store  multiple values under single  variable name
#value=key,value pairs
#support all data type

#syntax

"""dit_name={
    "key ": "value",
    "key" : "value"
}
print(dit_name)"""

"""student={
    "Name":"Angana",
    "Age" : 24,
    "college" :"S N college"

}
print(student)"""



#Duplicate Values
#------------------

#it allow duplicates in values
"""student={
    "Name":"Priya",
    "Name1":"Priya",

}
print(student)"""


#Not allow Duplicates in key

"""student={
    "Name":"Priya",
    "Name":"Anju"
}
print(student)"""


#Accessing Dictonary elements
#-------------------
#using keys

"""student={
    "Name":"Priya",
    "Age" :20,
    "Place":"Thrissur"
}
print(student["Name"])#Key based
print(student["Age"])
print(student["Place"])"""

#Not index based ----->will show error

"""print(student[0])"""

#2.Get
"""student={
    "Name":"Priya",
    "Age" :20,
    "Place":"Thrissur"
}
print(student .get("Name"))
print(student.get("Age"))
print(student.get("Place"))
print(student.get("Number"))#if key doesnot exit-none
print(student.get("Number","Not available"))"""





#---------
#Adding a new element
#1.dictonary_name[key name]=value

"""student={
    "Name":"Priya",
    "Age" :20,
    "Place":"Thrissur",
    
}
student["Mark"]=67.1
print(student)
#updating a value
student["Mark"]=30
print(student)"""

#if key already exist-Update the value
#if key does not exist-add a new key
"""student["Number"]=30
print(student)"""


#2.using update ()-is used to add or update one or more key value pairs
"""student={
    "Name":"Priya",
    "Age" :20,
    "Place":"Thrissur",
    
}

student.update({
    "Roll number":34,
    "Mark":80
})
print(student)"""


#Removing elements
#1.pop()------>Removing element using its key

"""student={
    "Name":"Priya",
    "Age" :20,
    "Place":"Thrissur",
    
}
print(student)
student.pop("Age")
print(student)"""

#2. popitem()----- Remove last inserted key:value pair
"""student={
    "Name":"Priya",
    "Age" :20,
    "Place":"Thrissur",
    
}
print(student)
student.popitem()
print(student)"""

#3.del-used to delete a specific key-value pair
"""student={
    "Name":"Priya",
    "Age" :20,
    "Place":"Thrissur",
    
}
print(student)
del student["Age"]
print(student)"""


#4.clear-remove all elements from the dictonary
"""student={
    "Name":"Priya",
    "Age" :20,
    "Place":"Thrissur",
    
}
print(student)
student.clear()
print(student)"""



#check whether a key exist,using membership operators-age
student={
    "Name":"Priya",
    "Age" :20,
    "Place":"Thrissur",
    
}
print("Age" in student)
print("Age" not in student)
print("num" in student)
print("num" not in student)