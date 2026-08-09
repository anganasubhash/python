
#Input age.
#Display: Below 5 → Free | 5-18 → Student Fare 19-59 → Full Fare | 60+ → Senior Citizen Fare
age=int(input("enter your age:"))
if age<5:
    print("Free")
elif age<=18:
    print("student fare")
elif age<=59:
    print("Full fare")
else:
    print("senior citizen fare")