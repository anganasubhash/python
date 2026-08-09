#Mobile Recharge
#  Keep entering recharge amounts until the balance reaches 500.

balance=0

while balance<500:
    recharge=int(input("Enter the recharge amount"))
    balance+=recharge

print("Recharged successfully")


