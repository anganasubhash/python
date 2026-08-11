#12. Bank Deposit
# Enter deposit amounts until the user enters 0. Display the final balance.

final_balance=0
deposit=int(input("Enter the deposit:"))
while deposit!=0:
      final_balance+=deposit
      deposit=int(input("Enter the deposit:"))
print("Final balance=",final_balance)

