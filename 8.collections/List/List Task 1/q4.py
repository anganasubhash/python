#4. Cricket Score Analysis
#Write a function cricket_stats().
#•  Store runs scored in multiple matches.
#•  Use a loop to calculate total runs.
#•  Find the highest score.
#•  Count the number of half-centuries (50–99)


def cricket_stats():
    total_runs=0
    highest_score=0
    count=0
    for i in runs:
        total_runs+=i
        if i>highest_score:
            highest_score=i
        if i>=50 and i<=99:
            count+=1
    print(total_runs)
    print(highest_score)
    print(count)
runs=[56,80,99,40,35,25,50]
cricket_stats()