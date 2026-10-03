
server1 = {"P101", "P102", "P103", "P104"}
server2 = {"P103", "P104", "P105", "P106"}
players = server1.union(server2)
print("Unique players:", players)
print("Total unique players:", len(players))