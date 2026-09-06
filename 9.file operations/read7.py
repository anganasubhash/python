file2=open("C:\\Users\\abhishek\\Downloads\\data.txt","r")
for i in file2:
    data=i.rstrip('\n').split(',')
    #print(data)
    age=data[2]

    if age=="21":
        print(data)
    if age>"22":
        print(data[:4])
    if age<"23":
        print(data[:2],data[4])

    place=data[4]
    if place=="Ernakulam":
        print(data[:4])
    if place=="Thrissur" and age>"23":
        print(data[0],data[2],data[4])




    
    


