seats = ("A1", "VIP1", "B2", "VIP2", "C3", "VIP3")
count = 0
for seat in seats:
    if seat.startswith("VIP"):
        count += 1
print(count)

