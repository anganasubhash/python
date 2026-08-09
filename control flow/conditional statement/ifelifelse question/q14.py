
#Input parcel weight.
#Display: Up to 1 kg → 50 | 1-5 kg → 100
#5-10 kg → 200 | Above 10 kg → 400

parcel_weight=int(input("enter the weight in kg:"))
if  parcel_weight<=1:
    print("50")
elif parcel_weight<=5:
    print("100")
elif parcel_weight<=10:
    print("200")
else:
    print("400")
