#11. Rainfall Measurement
#  Enter rainfall for each day until -1 is entered. Display the total rainfall.
total_rainfall=0
rain_fall=int(input("Rainfall for each day:"))
while rain_fall!=-1:
    total_rainfall+=rain_fall
    rain_fall=int(input("Rainfall for each day:"))
print("Total rainfall",total_rainfall)
