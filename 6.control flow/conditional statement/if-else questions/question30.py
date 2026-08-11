#If the total weight is within the lift's capacity, allow the lift to move; otherwise, display
#"Overload"

lift_capacity=int(input("enter the lift capacity:"))
total_weight=int(input("enter the total weight"))
if total_weight<=lift_capacity:
    print(" flit moves")
else:
    print("overload")
