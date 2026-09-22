#Q15. Discount Calculator
#Scenario:
#An online shopping website gives a 20% discount.
#Task:
#Create a function discount(price).
def discount(price):
    if price>=5000:
        discount_amount=price*20/100
        final_amount=price-discount_amount
        print("discount",discount_amount)
        print("Final amount",final_amount)
    else:
        print("No discount")
price1=int(input("Enter the price:"))
discount(price1)