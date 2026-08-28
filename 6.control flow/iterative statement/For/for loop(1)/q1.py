#1. School Uniform Inspection
#A teacher checks the uniforms of 25 students. If a student is not wearing the proper uniform, display
#that student's roll number



for i in range(1,26):
    uniform=input("Is student in proper uniform(Yes/No)")
    if uniform=="No":
       print("student not in proper uniform",i)