#1. Student Marks
#Create a list of marks for five students.
#bullet Print the first and last student's mark.
#bullet Find the highest 

lst1=[25,23,20,15,10]

print("First student mark is",lst1[0])
print("Last student mark is",lst1[4])
highest=0
for i in lst1:
    if i>highest:
        highest=i
print("Highest mark",highest)