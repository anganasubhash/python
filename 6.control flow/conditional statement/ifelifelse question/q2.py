
#Input the traffic signal color.
#Display: Red → Stop | Yellow → Get Ready | Green → Go Otherwise → Invalid Signal
signal=input("Enter the signal:")
if signal=="Red":
    print("Stop")
elif signal=="Yellow":
    print("Ready")
elif signal=="Green":
    print("GO")

else:
    print("invalid signal")