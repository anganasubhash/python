# . Exam Registration System

# Write a Python program that accepts student names.

# Continue accepting names until the user enters "stop".
# Count the number of registered students.
# Display the total registrations.

name=input("Enter student name:")
count=0
while name!="stop":
    count+=1
    name=input("Enter student name:")
print("Total registration=",count)

