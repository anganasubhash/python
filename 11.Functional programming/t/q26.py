website = ("Anu", "Rahul", "Meera", "Arun")
mobile = ("Meera", "Arun", "Priya", "Vishnu")

both = []

for student in website:
    if student in mobile:
        both.append(student)

print("Students registered through both:", both)