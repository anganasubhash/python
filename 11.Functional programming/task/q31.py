donors = ["D101", "D102", "D103"]
new_donor = "D104"
if new_donor not in donors:
    donors.append(new_donor)
    print("Donor registered")
else:
    print("Donor already registered")
print(donors)