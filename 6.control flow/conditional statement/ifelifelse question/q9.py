
#Input employee's years of experience.
#Display: Less than 2 years → No Bonus | 2-5 years → 5,000
#6-10 years → 10,000 | Above 10 years → 20,000

experience=int(input("enter years of experience:"))
if experience<2:
    print("NO bonus")
elif experience<=5:
    print("Bonus=5000")
elif experience<=10:
    print("Bonus=10000")
else:
    print("Bonus=20000")
