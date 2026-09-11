
#21. Duplicate Product Analysis
#Store the following products:
# ["Laptop", "Mouse", "Laptop", "Keyboard", "Mouse", "Monitor", "Printer"]
#bullet Find duplicate products.
#bullet Count the quantity of each product

product=["Laptop", "Mouse", "Laptop", "Keyboard", "Mouse", "Monitor", "Printer"]
duplicate=[]
for i in product:
    if i  in duplicate:
        duplicate.append(i)
        

print(duplicate)
print(len(product))