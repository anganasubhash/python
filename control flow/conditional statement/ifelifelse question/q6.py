
#Input age.
#Display ticket price: Below 5 → Free | 5-12 → 100
#13-59 → 200 | 60 and above → 120
age=int(input("enter the age:"))
if age<5:
    print("Free")
elif age<=12:
    print("100 rs")
elif age<=59:
    print("200 rs")
else:
    print("120 rs")