#Enter marks until the user enters -1. Display the total marks

total_mark=0
mark=int(input("Enter the mark:"))

while mark!=-1:
    total_mark+=mark
    mark=int(input("Enter the mark:"))
    
print("Total mark=",total_mark)


