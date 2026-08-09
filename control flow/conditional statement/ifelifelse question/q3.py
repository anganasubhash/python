
#Input a number (1-7).
#Display the corresponding weekday.
#Otherwise display "Invalid Day".

Day=int(input("Enter number:"))
if Day==1:
    print("Monday")
elif Day==2:
    print("Tuesday")
elif Day==3:
    print("wednesday")
elif Day==4:
    print("Thursday")
elif Day==5:
    print("Friday")
elif Day==6:
    print("Saturday")
elif Day==7:
    print("Sunday")
else:
    print("Invalid day")
