#32. Wildlife Survey
#Display the forest zone numbers where no animals were spotted
n=int(input("Enter the number of forest zone:"))
for i in range(1,n+1):
    animal=input("Enter animal spotted(Yes/No):")
    if animal=="No":
        print("Forest zone number where no animals were spotted is zone",i)