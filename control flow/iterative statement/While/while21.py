#Password verification system
#write a python program that ask the user to enter a password
#continue asking untill the correct password is entered
#display access granted 
pwd=input("Enter your password:") 
password="abc@234"
while password!=pwd:
      
      pwd=input("Enter your password:")
      if pwd==password:
            print("Access granted")
        

     
    