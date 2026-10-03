user1 = ("Song A", "Song B", "Song C", "Song D")
user2 = ("Song C", "Song D", "Song E", "Song F")
common = []
for song in user1:
    if song in user2:
        common.append(song)
unique = []

for song in user1:
    if song not in unique:
        unique.append(song)

for song in user2:
    if song not in unique:
        unique.append(song)

print("Common songs:", common)
print("All unique songs:", unique)