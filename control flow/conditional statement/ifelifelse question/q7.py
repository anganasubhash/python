
#Input units consumed.
#Display: 0-100 → 3/unit | 101-200 → 5/unit
#201-500 → 7/unit | Above 500 → 10/unit
unit=int(input("enter the units consumed:"))
if unit<=100:
    Bill=unit*3
elif unit<=200:
    Bill=unit*5
elif unit<=500:
    Bill=unit*7
else:
    Bill=unit*10
print("Total bill=" ,Bill)