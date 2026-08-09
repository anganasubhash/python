#26. Temperature Check
#Keep asking for temperature until it is below 38°C

temperature=float(input("Enter the temperature in c:"))
while temperature>=38:
    temperature=float(input("Enter the temperature in c:"))
print("Temperature entered successfully")
