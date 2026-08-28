#34. Online Course Completion
#Print certificates only for students who completed 100% of the course
n=int(input("Enter total number of students:"))
for i in range(1,n+1):
    course=input("Did you complete the  course(Yes/No):")
    if course=="Yes":
        print("Certificate granted")