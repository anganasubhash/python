#4. Cricket Scores
#Store runs scored in six overs.
#bullet Find the total runs.
#bullet Find the highest score

runs=[10,5,6,8,11,7]
total=0
highest=0
for i in runs:
    total+=i
    if i>highest:
        highest=i
print("Total runs=",total)
print("Highest score=",highest)