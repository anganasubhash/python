
#Input water usage (litres).
#Calculate bill using slab rates.
water_usage=int(input("Enter water usage in litres:"))
if water_usage<=5:
    bill=water_usage*2
elif water_usage<=10:
    bill=water_usage*3
else :
    bill=water_usage*5
print("water bill=",bill)