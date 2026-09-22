
#Create a function attendance(days) that accepts attendance for several days and counts present
#days
def attendance(days):
    count=0
    for i in range(1,days+1):
        attendance=input("Enter P for present A for absent: ")
        if attendance=="P":
            count+=1
    print(count)
day=int(input("Enter the days:"))
attendance(day)