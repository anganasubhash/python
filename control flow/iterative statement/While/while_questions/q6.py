# 9. Shopping Cart System

# Write a Python program that accepts product prices.

# Add each price to the total bill.
# Ask the user whether they want to add another item.
# Continue until the user enters "no".
# Display the final bill.

total_bill=0
price=int(input("Enter the product price:"))
another_item=input("Do you want to add another item:(yes/no)")
total_bill+=price
print(total_bill)


while another_item!="no":
    price=int(input("Enter the price of product:"))
    another_item=input("Do you want to add another item:(yes/no)")
    total_bill+=price
    print(total_bill)
        
       
    
print("FInal bill=",total_bill)





