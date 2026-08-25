#38. ATM Withdrawal
#Allow withdrawals until the account balance becomes zero or the user chooses to stop

balance=10000
withdraw=(input("Enter the withdrwal amount or Stop:"))
while balance!=0  and withdraw!="Stop":
    withdraw=int(withdraw)
    if withdraw<=balance:
        balance-=withdraw
        print("Remaining balance=",balance)
    else:
        print("insufficient balance" )
    if balance!=0:
         withdraw=(input("Enter the withdrwal amount:"))

print("Final balance=",balance)





67