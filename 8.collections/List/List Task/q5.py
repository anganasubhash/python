#5. Classroom Attendance
#Store attendance status:
#["P", "A", "P", "P", "A"]
#bullet Count present students.
#bullet Count absent students

attendence=["P", "A", "P", "P", "A"]
count_p=0
count_A=0
for i in attendence:
    if i=="P":
        count_p+=1
    else:
        count_A+=1
print("Present student=",count_p)
print("Absent student=",count_A)
