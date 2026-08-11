

# Write a Python program that allows a user to withdraw money repeatedly.

# Start with a balance of ₹10,000.
# Accept withdrawal amounts from the user.
# Deduct the amount from the balance.
# Stop when the balance becomes 0 or the user enters 0.
# Display the remaining balance after each withdrawal.

Balance=10000
withdrawal_amount=int(input("Enter the withdrawal amount;"))
Balance-=withdrawal_amount
print(Balance)
while withdrawal_amount!=0:
    withdrawal_amount=int(input("Enter the withdrawal amount;"))
    Balance-=withdrawal_amount
    print(Balance)
print("Remaining amount=",Balance)

