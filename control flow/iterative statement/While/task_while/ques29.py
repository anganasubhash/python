#29. Exam Pass Count
#Enter marks for students until -1 is entered. Count how many students passed (marks >= 40)

passed=0
marks=int(input("Enter the mark scored:"))
while marks!=-1:
    if marks>=40:
        passed+=1
    else:
        pass
    marks=int(input("Enter your mark scord"))
print("Number of students passed =",passed)



