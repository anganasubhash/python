#Task:
#Create a function ticket_price(no_of_tickets) that returns the total amount.
def ticket_price(no_of_tickets):
    total_amount=250*no_of_tickets
    return total_amount
tickets_number=int(input("Enter the number of tickets:"))
tickets=ticket_price(tickets_number)
print(tickets)