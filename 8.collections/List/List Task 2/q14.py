#14. Student Result
#Store marks of 12 students.
#bullet Count students who passed (>=40).
#bullet Count students who scored above 75

mark=[80,90,65,50,99,94,60,55,85,70,72,42]
pass_count=0
above_75=0
for i in mark:
    if i>=40:
        pass_count+=1
    if i>75:
        above_75+=1
print("Student passed =",pass_count)
print("Student scored above 75=",above_75)
