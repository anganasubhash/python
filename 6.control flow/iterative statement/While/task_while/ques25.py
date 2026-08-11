#25. Online Registration
#Keep asking for age until the user enters an age greater than or equal to 18

age=int(input("Enter the age;"))
while age<18:
    age=int(input("Enter the age;"))
print("Registered successfully")
