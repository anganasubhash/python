#36. Solar Power Plant
#Display the day numbers when electricity generation crossed 1000 units
n=int(input("Enter total number of days:"))
for i in range(1,n+1):
    elecctricty_generation=int(input("Enter the electricity  generation in units:"))
    if elecctricty_generation>1000:
        print("electricity generation crossed 1000 units day",i)