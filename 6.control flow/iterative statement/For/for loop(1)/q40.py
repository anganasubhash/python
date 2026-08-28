#40. Smart Parking System
#For 50 vehicles entering a parking lot, assign parking slots P001, P002, P003... P050 and display the
#assigned slot for each vehicle
n=50
for i in range(1,51):
    print("parking slots for vechicle",i,"is p",str(i).zfill(3))