

#A class has 5 students .Take attendance(P forpresent,A for Absent)
#for each student and count the number of present students,
present=0
for i in range(5):
    attendence=input("Enter p for presnt,A for absent:")
    if attendence=="p":
        present+=1

print("Number of present student=",present)