#Check whether the passenger has a valid ticket before allowing boarding

ticket=input("enter yes if you have ticket otherwise no")
if ticket=="yes":
    print("allow boarding")
else:
    print(" not allowed")