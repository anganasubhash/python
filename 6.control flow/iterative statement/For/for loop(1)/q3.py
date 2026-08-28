#3. Classroom Fan Inspection
#Inspect 12 classroom fans. Display the fan numbers that need repair

for i in range(1,13):
    repair=input("Enter Yes if need repair: ")
    if repair=="Yes":
        print("Fan number need repair is",i)
