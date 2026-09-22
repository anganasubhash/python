#Task:
#Create a function emi_tracker(months) that displays all remaining EMI numbers
def emi_tracker(months) :
    for i in range(1,months+1):
        print("Emi number:",i)
months1=int(input("Enter the months:"))
emi_tracker(months1)