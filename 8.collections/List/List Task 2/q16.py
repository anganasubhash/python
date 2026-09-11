#16. Bus Reservation
#Store booked seat numbers.
#bullet Check whether seat number 15 is booked.
#bullet Book seat number 18.
#bullet Sort the seat numbers

seats=[5,15,16,20,22]
if 15 in seats:
    print("Seat 15 is booked")
else:
    print("seat 15 is not booked")

seats.append(18)
seats.sort()
print(seats)