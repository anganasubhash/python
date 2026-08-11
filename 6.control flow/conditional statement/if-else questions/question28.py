#If the team's score is greater than the target, print "Team Wins"; otherwise, print "Team
#Loses"

target=int(input(" enter the target score:"))
score=int(input("enter the team score"))
if score>target:
    print("Team wins")
else:
    print("Team loses")