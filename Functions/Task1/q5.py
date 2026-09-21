#Task:
#Create a function check_temperature(temp) that displays whether the weather is Hot, Normal, or
#Cold.

def check_temperature(temp):
    if temp>35:
        return "Hot"
    elif temp>20:
        return "Normal"
    else:
        return "Cold"
temp1=float(input("Enter the temperature:"))
temperature=check_temperature(temp1)
print(temperature)