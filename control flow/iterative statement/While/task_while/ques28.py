#28. Factory Production
#Increase the production count until 500 items are produced
count=0
items=int(input("Enter number items produced:"))
while count<500:
    count+=items
    if count<500:
     items=int(input("Enter number items produced:"))
print("Total production count=",count)
    