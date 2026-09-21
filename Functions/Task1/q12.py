#Create a function validate_password(password)
#A website requires passwords with at least 8 characters.
def validate_password(password):
    if len(password)<8:
        print("invalid password")
    else:
        print("Login sucessfull")
password1=input("Enter the password:")
validate_password(password1)