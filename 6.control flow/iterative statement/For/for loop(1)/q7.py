#7. Laptop Quality Inspection
#Whenever a laptop fails inspection, print its serial number
n=int(input("Enter the total number of laptop:"))
for i in range(1,n+1):
    inspection=input("Laptop inspection(Fail/Pass):")
    if inspection=="Fail":
        print("Laptop failed inspection serial number",i)
