  #Check whether enough rooms are available before confirming a booking

rooms=int(input("enter number of available rooms:"))
if rooms>0:
    print("confrim booking")
else:
    print("not available")