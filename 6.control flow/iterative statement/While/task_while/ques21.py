#21. Phone Unlock
#Allow only three password attempts. If all fail, display "Phone Locked.


user_password="abc@123"
attempt=0
while attempt<3:
    password=input("Enter password:")
    attempt+=1
    if password==user_password:
        print("Unlocked")
        break
    else:
        print("Incorrect password")  
if attempt==3 and password!=user_password:
    print("Phone locked")

     

