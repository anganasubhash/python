#2. Shopping Cart Manager
#Write a function manage_cart().
#•  Store shopping items in a list.
#•  Use a loop to display all items.
#•  Add a new item.
#•  Remove an unavailable item.
#•  Count the total number of items

def manage_cart(item): 
    for i in item:
        print(i)
    item.append("Washing machine")
    print(item)
    item.remove("Tv")
    print(item)
    print(len(item))
items=["Laptop","Mobile phone","Tv","AC"]
manage_cart(items)

    