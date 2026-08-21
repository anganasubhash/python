

lst13=[10,10,89,67,54,34,78,89,89]

lst13.append(34)
print(lst13)

lst13.extend([23,56,66])
print(lst13)

lst13.insert(1,34)
print(lst13)

lst13.remove(54)
print(lst13)

lst13.pop()
print(lst13)

lst13.pop(4)
print(lst13)

print(lst13.index(78))

lst13.reverse()
print(lst13)

print(lst13.count(56))
print(sum(lst13))
print(max(lst13))
print(min(lst13))
print(len(lst13))

lst13.sort()
print(lst13)

lst13.sort(reverse=True)
print(lst13)

lst=lst13.copy()
print(lst)

lst13.clear()
print(lst13)