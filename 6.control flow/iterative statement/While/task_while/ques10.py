#10. Attendance Counter
#  Enter student names until the user types "stop". Display the total number of students.

total=0
name=input("Enter student  name:")
while name!="Stop":
    total+=1
    name=input("Enter student  name:")

print("Total number of student",total)