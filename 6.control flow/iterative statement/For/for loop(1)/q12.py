#12. Library Reading Competition
#Display the student numbers who qualified for the final round (more than 5 books)
n=int(input("Enter the total number of students:"))
for i in range(1,n+1):
    read=int(input("Enter the number of books readed:"))
    if read>5:
        print("Student qualified for the final round=student number",i)