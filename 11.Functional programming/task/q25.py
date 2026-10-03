store1 = (101, 102, 103, 104)
store2 = (103, 104, 105, 106)
merged = store1 + store2
print("Merged:", merged)
duplicates = []
for id in merged:
    if merged.count(id) > 1 and id not in duplicates:
        duplicates.append(id)

print("Duplicate IDs:", duplicates)