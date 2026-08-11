
#Input purchase amount.
#Display: Above 10,000 → 20% Discount | 5,000-10,000 → 10% Discount
#2,000-4,999 → 5% Discount | Below 2,000 → No Discount

purchase_amount=int(input("Enter the amount:"))
if purchase_amount<2000:
    print("No Discount")
elif purchase_amount<=4999:
    print("Discount=5%")
elif purchase_amount<=10000:
    print("DIscount=10%")
else:
    print("Discount=20%")
