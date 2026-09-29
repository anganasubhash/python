electronics = (101, 102, 103, 104)
fashion = (103, 104, 105, 106)
both = []
for customer in electronics:
    if customer in fashion:
        both.append(customer)

print("Customers who purchased from both:", both)