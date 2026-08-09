
#Compare the entered PIN with the stored PIN. Unlock the phone if they match

pin=int(input("Enter your pin:"))
if pin==3445:
    print("Matches")
else:
    print("incorrect pin")
