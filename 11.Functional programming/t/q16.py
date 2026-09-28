employee_ids = (101, 102, 103, 104, 105)
id = int(input("Enter employee ID: "))
if id in employee_ids:
    print("Employee ID exists")
else:
    print("Employee ID does not exist")