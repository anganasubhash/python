
#If the shopping amount is ₹1000 or more, shipping is free. Otherwise, shipping charges
#apply.


Amount=int(input("Enter the shopping amount:"))
if Amount>=1000:
    print("Shipping is free")
else:
    print("shipping charge apply")
