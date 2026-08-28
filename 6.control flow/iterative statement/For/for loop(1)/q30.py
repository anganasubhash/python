#30. Ice Cream Shop
#Display the day numbers when sales crossed 10,000
n=int(input("Enter the total number of days:"))
for i in range(1,n+1):
    scale=int(input("Enter the scales:"))
    if scale>10000:
        print("Scales crossed 10000 is day",i)