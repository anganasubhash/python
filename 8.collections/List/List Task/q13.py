#13. Bank Transactions
#Store daily transaction amounts.
#bullet Count deposits.
#bullet Count withdrawals.
#bullet Find the total balance.
transaction=[5000,-1000,500,-200,3000]
deposit_count=0
withdraw_count=0
balance=0
for i in transaction:
    if i>0:
        deposit_count+=1
        balance+=i
    elif i<0:
        withdraw_count+=1
        balance+=i
    else:
        pass
print("Deposite count=",deposit_count)
print("Withdrawal count=",withdraw_count)
print("Total balance=",balance)