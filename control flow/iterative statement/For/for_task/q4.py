
#Person deposit money for 7 days ,calculte the total deposited amount
total_deposit=0
for i in range(1,8):
    deposit=int(input("Enter the deposited amount:"))
    total_deposit+=deposit
print("Total deposited amount=",total_deposit)
