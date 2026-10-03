
event1 = ["Anu", "Rahul", "Meera", "Arun"]
event2 = ["Meera", "Arun", "Priya", "Vishnu"]
event3 = ["Arun", "Meera", "Vishnu", "Asha"]
all_three = []
for student in event1:
    if student in event2 and student in event3:
        all_three.append(student)
print("Students participating in all three:", all_three)