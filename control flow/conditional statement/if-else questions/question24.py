#If fuel in the vehicle is greater than 5 liters, allow the journey; otherwise, ask to refuel

fuel=int(input("Enter the fuel in the vehicle in liters:"))
if fuel>5:
    print("Allow journey")
else:
    print("Refuel")