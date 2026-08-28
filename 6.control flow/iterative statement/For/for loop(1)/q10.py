#10. School Bus Route
#Display the stop numbers where more than 10 students boarded
n=int(input("Enter total number of stops:"))
for i in range(1,n+1):
    students=int(input("Enter the number of students:"))
    if students>10:
        print("Stop number more than 10 students boarded =stop number",i)