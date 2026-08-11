#If seats are available, confirm the booking; otherwise, show "House Full"

seats=int(input("enter the number of seats available"))
if seats>0:
    print("confrim booking")
else:
    print("House full")