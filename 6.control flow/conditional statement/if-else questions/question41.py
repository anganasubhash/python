#Turn on the motor if the water level is below the minimum level; otherwise, keep it off 

minimum_level=int(input("enter minimum water level:"))
water_level=int(input("enter the water level"))
if water_level<minimum_level:
    print("Turn on the motor")
else:
    print("keep it off")