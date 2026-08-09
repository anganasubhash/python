
#If electricity usage exceeds 500 units, print "High Consumption"; otherwise, print "Normal
#Consumption"


units=int(input("Enter electricity units:"))
if units>500:
    print("High consumption")
else:
    print("Normal consumption")