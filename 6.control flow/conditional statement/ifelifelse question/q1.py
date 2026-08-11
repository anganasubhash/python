

#1. Grade Calculator
#Input a student's mark (0-100).
#Display: 90-100 → A+ | 80-89 → A | 70-79 → B
#60-69 → C | 50-59 → D | Below 50 → Fail



mark=int(input("Enter your mark :"))

if mark>=90:
    print("A +grade")
elif mark>=80:
    print("A grade")
elif mark>=70:
    print("B grade")
elif mark>=60:
    print("C grade")
elif mark>=50:
    print("D grade")

else:
    print("Failed")