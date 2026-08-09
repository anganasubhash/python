
#If available data is greater than 0 GB, internet can be used; otherwise, show "Recharge
#Required".

Data=int(input("Enter your available data:"))
if Data>0:
    print("internet can be used")
else:
    print("Recharge required")
