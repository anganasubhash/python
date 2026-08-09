
# Write a Python program that accepts deposit amounts repeatedly.

# Add each deposit to the account balance.
# Stop when the user enters 0.
# Display the final balance.



deposit=int(input("Enter the deposit amount:"))
Balance=deposit
while deposit!=0:
    deposit=int(input("Enter the deposit amount:"))
    Balance+=deposit
    
print("Final amount=",Balance)

