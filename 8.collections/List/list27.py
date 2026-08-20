#Employee
#Nested list
#Employ,id ,name,age,place,salary,decigonation
Employee=[[421,"Anju",34,"thrissur",20000,"Manager"],[422,"Amritha",23,"thirur",30000,"data analyts"],[423,"Ram",25,"ernakulam",35000,"ceo"]]
#30 age----[name]
#data scientist---[name,age]
for i in Employee:
    if i[2]>25:
        print(i[1])

for i in Employee:
    if i[5]=="data analyts":
        print(i[1:3])

