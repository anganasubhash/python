football = ("Anu", "Rahul", "Meera", "Arun")
cricket = ("Meera", "Arun", "Priya", "Vishnu")
only_football = []
for member in football:
    if member not in cricket:
        only_football.append(member)

print("Only football club:", only_football)