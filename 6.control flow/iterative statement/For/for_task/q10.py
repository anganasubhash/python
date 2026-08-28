#Theater sells tickets to 5 customers
#Enter the ticket count for  each customer and calculate total ticket sold
count=0
for i in range(5):
   ticket=int(input("Enter the number of tickets:"))
   count+=ticket
print("Total tickets sold=",count)
