python = ("Anu", "Rahul", "Meera", "Arun")
data_science = ("Meera", "Arun", "Priya", "Vishnu")
exactly_one = []
for student in python:
    if student not in data_science:
        exactly_one.append(student)
for student in data_science:
    if student not in python:
        exactly_one.append(student)
print("Students enrolled in exactly one course:", exactly_one)