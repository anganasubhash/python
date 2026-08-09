#If the course fee is paid, grant access to the course; otherwise, deny access

fee=input("enter yes if you paid the fee :")
if fee=="yes":
    print("Access to the course")
else: 
    print("Deny access")