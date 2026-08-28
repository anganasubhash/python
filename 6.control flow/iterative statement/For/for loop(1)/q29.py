#29. School Scholarship
#Display the roll numbers of scholarship-eligible students.
lower_limit=int(input("Enter the lower_limit:"))
upper_limit=int(input("Enter the upperlimit:"))
for i in range(lower_limit,upper_limit+1):
    total_score=int(input("Enter the total score:"))
    if total_score>100:
        print("Eligible for scholarship is roll number",i)
