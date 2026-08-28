#28. Car Showroom Sales
#Print "Luxury Sale" whenever the selling price exceeds 20,00,000
n=int(input("Enter the total number of car:"))
for i in range(1,n+1):
    price=int(input("Enter the selling price:"))
    if price>2000000:
        print("Luxury scale")