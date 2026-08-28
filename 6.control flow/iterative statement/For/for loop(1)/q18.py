#18. Photography Contest
#Display participant numbers whose total score exceeded 400
n=int(input("Enter total number of participant:"))
for i in range(1,n+1):
    score=int(input("Enter the  total score:"))
    if score>400:
        print("Participate number total score exceeded 400 is",i)
