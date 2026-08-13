#check the number both multiple of 3 and 5
number=int(input("Enter the number:"))
if number%3==0 and number%5==0:
    print(number,"is multiple of 3 and 5 ")
else:
    print(number,"is not multiple of 3 and 5")