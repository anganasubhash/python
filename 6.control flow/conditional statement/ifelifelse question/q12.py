
#Input salary.
#Display: Less than 20,000 → Not Eligible | 20,000-39,999 → Eligible for 2 Lakhs 40,000-79,999 → Eligible for 5 Lakhs 
# | 80,000 and above → Eligible for 10 Lakhs
salary=int(input("enter your salary:"))
if salary<20000:
    print("Not eligible")
elif salary<=39999:
    print("eligible for 2 lakhs")
elif salary<=79999:
    print("eligible for 5 lakhs")
else:
    print("eligible for 10 lakhs")