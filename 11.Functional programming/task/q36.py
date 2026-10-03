

eligible = ("Anu", "Rahul", "Meera", "Arun", "Priya")
training = ("Anu", "Meera", "Priya")
missed_training = []
for student in eligible:
    if student not in training:
        missed_training.append(student)
print("Eligible students who missed training:", missed_training)