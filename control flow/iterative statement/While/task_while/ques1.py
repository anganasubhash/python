#Allow the user to enter the correct PIN.
#  Keep asking until the correct PIN is entered
user_password="abc@123"
password=input("Enter your password:")
while password!=user_password:
    password=input("wrong!,Enter password again :")
print("Access granted")

    
    