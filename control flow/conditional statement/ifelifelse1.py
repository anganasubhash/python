#Red------------------>Stop
#Yellow---------------->Ready
#Green----------------->Go

signal=input("Enter the signal:")
if signal=="Red":
    print("Stop")
elif signal=="Yellow":
    print("Ready")
elif signal=="Green":
    print("GO")

else:
    print("invalid signal")