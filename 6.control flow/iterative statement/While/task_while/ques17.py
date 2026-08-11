#17. Cricket Runs
#Enter runs scored ball by ball until 30 balls are completed. Display total runs
total_runs = 0
balls=1
while balls<=30:
    runs=int(input("Enter the runs scored:"))
    total_runs+=runs
    balls+=1
print("Total runs=",total_runs)
