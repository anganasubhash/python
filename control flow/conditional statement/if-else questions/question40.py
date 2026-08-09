#Deliver the order only if the payment has been completed

payment=input("Did you complete your payment?(yes/no):")
if payment=="yes":
    print(" order delivered")
else:
    print("payment not completed")