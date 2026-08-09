
#Input a month number (1-12).
#Display: Summer | Rainy | Winter | Invalid Month
month=int(input("Enter the month(1-12) :"))

if month==4 or month==5 or month==6:
    print("Summer")
elif month==7 or month==8 or month==9:
    print("Rainy")
elif month==10 or month==11 or month==12 or month==1 or month==2 or month==3:
    print("Winter")
else:
    print("Invaild month")