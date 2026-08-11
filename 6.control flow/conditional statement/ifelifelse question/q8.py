
#Input account balance and withdrawal amount.
#Display: Insufficient Balance | Invalid Amount | Withdrawal Successful
account_balance=int(input("Enter the account balance:"))
withdrawal_amount=int(input("Enter the withdrawal amount:"))
if  account_balance<withdrawal_amount:
    print("insufficient balance")
elif withdrawal_amount<=0:
    print("Inalid Amount")
else:
    print("Withdrawal sucessfull")