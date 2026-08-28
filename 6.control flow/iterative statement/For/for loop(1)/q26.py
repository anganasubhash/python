#26. Airport Baggage Check
#Display passenger IDs whose baggage exceeds the weight limit
n=int(input("Enter the total number of passenger:"))
weight_limit=100
for i in range(1,n+1):
    weight=int(input("Enter the weight of passengers:"))
    if weight>weight_limit:
        print("Passenger IDs baggage exceeds the weight limit is P",str(i).zfill(3))