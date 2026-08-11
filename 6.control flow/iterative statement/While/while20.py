#write a python program that allow a user to withdraw money repeatly
# start with a balance=10000
#accept withdrawal amount from the user
# deduct the amount from the balance
#stop when the balance become 0 or the user enter 0
#Display the remaining balance after each withdrawal




balance=10000
withdrawal_amount=int(input("enter the withdrawal amount:"))
while withdrawal_amount!=0:
    balance-=withdrawal_amount
    print(balance)
    withdrawal_amount=int(input("enter the withdrawal amount:"))
print("Final balance=",balance)