#19. Calculate Power Without Using **
#Accept a base and an exponent. Calculate the power using a for loop only
base=int(input("Enter the base:"))
exponent=int(input("Enter the exponent:"))
power=1
for i in range (exponent):
    power*=base
print("Power of number=",power)
