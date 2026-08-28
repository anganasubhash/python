#23. School Notebook Distribution
#Display student IDs who received fewer than 3 notebooks
n=int(input("Enter total number of students:"))
for i in range(1,n+1):
    books=int(input("Enter the number of books received:"))
    if books<3:
        print("Student id of student received fewer than 3 notebook is S",str(i).zfill(4))