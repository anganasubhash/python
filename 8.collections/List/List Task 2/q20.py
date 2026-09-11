#20. Library Books
#Store book names.
#bullet Find duplicate book names.
#bullet Print unique book names

books=["half girlfriend","Love story","Home alone","mom and me","Love story"]
duplicate=[]
unique=[]
for i in books:
    if i in unique:
        if i not in duplicate:
            duplicate.append(i)
    else:
        unique.append(i)
print("Duplicate book name=",duplicate)
print("Unique book name=",unique)