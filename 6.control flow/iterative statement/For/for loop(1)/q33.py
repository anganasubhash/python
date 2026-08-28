#33. Mobile Network Survey
#Display location IDs where signal strength is below 30%.
n=int(input("Enter the total number of location taken:"))
for i in range(1,n+1):
    signal=int(input("enter the signal strength in percentage:"))
    if signal<30:
        print("Location IDs signal strength less than 30 if location no",i)