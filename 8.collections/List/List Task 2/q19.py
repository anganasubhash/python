#19. Hospital Patients
#Store patient ages.
#bullet Count children (below 18).
#bullet Count senior citizens (60 and above).

Age=[11,10,8,67,45,34,2,4,15,70]
count_childern=0
count_seniorcitizen=0
for i in Age:
    if i<18:
        count_childern+=1
    elif i>=60:
        count_seniorcitizen+=1
print("Childern=",count_childern)
print("Senior citizen=",count_seniorcitizen)
