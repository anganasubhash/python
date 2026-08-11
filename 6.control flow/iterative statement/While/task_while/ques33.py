#33. Loan Repayment
#A customer pays 5,000 every month. Continue until the loan becomes zero
  
loan=int(input("Enter the loan amount:"))
while loan>0:
    loan-=5000
    print("Remaining loan is ",loan)
print("Loan fully paid")


