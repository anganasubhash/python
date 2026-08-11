#Allow admission only if the player's age is below 18 years

age=int(input("enter your age:"))
if age<18:
    print("Allow Admission")
else:
    print("Admission not allowed")