#Allow a user only 3 attempt to enter the correct password

for i in range(3):
    password=input("Enter the password:")
    if password=="abc@23":
        print("Login sucessfull")
        break
    else:
        print("incorrect password")