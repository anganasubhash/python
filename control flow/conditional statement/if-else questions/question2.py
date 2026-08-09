#.LaptopBatteryCheck
#If the laptop battery is 20% or below, display "Connect Charger". Otherwise, display "Battery
#Level is Sufficient".

Battery_charge=int(input("Enter the battery percentage;"))
if Battery_charge<=20:
    print("connect charger")
else:
    print("Battery level sufficient")