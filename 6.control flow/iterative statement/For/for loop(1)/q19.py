#19. College Seminar
# #Display department numbers with attendance below 50
n=int(input("Enter total number of departments:"))
for i in range(1,n+1):
    attendance=int(input("Enter the attendence:"))
    if attendance<50:
        print("Department number with attendance below 50 is department",i)