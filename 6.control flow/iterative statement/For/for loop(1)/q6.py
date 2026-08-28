#6. Blood Donation Camp
#Display the volunteer numbers of people eligible to donate blood (18–60 years)
n=int(input("Enter  total number of  volunteer:"))
for i in range(1,n+1):
    age=int(input("Enter age  of volunteer:"))
    if age>=18 and age<=60:
        print("volunteer number eligible to donate blood is",i)