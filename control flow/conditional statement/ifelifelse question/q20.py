
#Input marks for five subjects.
#Calculate the percentage and display: Distinction | First Class
#Second Class | Pass | Fail

mark1=int(input("Enter the mark of first subject:"))
mark2=int(input("Enter the mark of second subject:"))
mark3=int(input("Enter the mark of thrid subject:"))
mark4=int(input("Enter the mark of fouth subject:"))
mark5=int(input("Enter the mark of fifth subject:"))
total_mark=125#each subject in 25 ---->5*25
total_score=mark1+mark2+mark3+mark4+mark5

percentage=total_score/total_mark*100
print("percentage =",percentage)
if percentage>=90:
    print("Distinction")
elif percentage>=80:
    print("First class")
elif percentage>=70:
    print("second class")
elif percentage>=50:
    print("Pass")
else:
    print("Fail")

