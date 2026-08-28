#24. Electricity Meter Reading
#Display house numbers that qualify for an energy-saving reward (usage below 100 units)
n=int(input("Enter the total number of houses:"))
for i in range(1,n+1):
    energy=int(input("Enter the energy used in units:"))
    if energy<100:
        print("Energy saving reward qualified house number",i)
