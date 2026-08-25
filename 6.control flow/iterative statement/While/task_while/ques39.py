#39. Delivery Tracking
#A delivery vehicle has 50 km remaining. Reduce the remaining distance by 5 km in each iteration
#until it reaches the destination

remaining_km=50
while remaining_km!=0:
    remaining_km-=5
    print("Remaining distance=",remaining_km)   