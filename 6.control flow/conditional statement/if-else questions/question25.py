#If battery percentage is below 20%, display "Charge Your Device"; otherwise, display "Battery
#OK".

battery=int(input("enter the battery percentage:"))
if battery<20:
    print("charge your Device")
else:
    print("Battery ok")
