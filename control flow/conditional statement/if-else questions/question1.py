

#OnlineShoppingDiscount
#A customer gets a 10% discount if their purchase amount is ₹5000 or more. Otherwise, no
#discount is applied. Write a program to check whether the customer receives the discount

purchase_amount=int(input("Enter the purchase amount:"))
discount_amount=(purchase_amount)*10/100
final_amount=purchase_amount-discount_amount
if  purchase_amount>=5000:
    print(" 10 % Discount appiled")
    print("Amount to pay:",final_amount)
else:
    print("Not discount appiled")


