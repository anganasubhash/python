
#Input BMI.
#Display: Underweight | Normal | Overweight | Obese

BMI=int(input("enter your BMI value:"))
if BMI<20:
    print("underweight")
elif BMI<30:
    print("normal")
elif BMI<40:
    print("overweight")
else:
    print("obese")