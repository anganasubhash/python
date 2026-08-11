#Keep asking the user to enter a password until its length is at least 8 characters.
password=input("Enter your password:") 
while len(password)<8:
    password=input("Inalid!,Enter another passwoed:")
print("successfull")
    
    

