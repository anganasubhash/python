
#A bank account should have at least ₹1000 after withdrawal. Check whether the withdrawal
#is allowed

Total__amount=int(input("Enter the total amount:"))
withdrawal_amount=int(input("Enter amount to withdraw:"))
Total__amount-=withdrawal_amount
if Total__amount>=1000:
    print("Withdrawal is allowed")
else:
    print("Not allowed")