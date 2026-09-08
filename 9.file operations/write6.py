
file1=open("data123.txt","r")
count_doctor=0
profession_count={}
country_count={}
oldest_age=0
oldest_person=[]
youngest_age=100
youngest_person=[]
ages=[]


for i in file1:
    data=i.rstrip("\n").split(",")
    #print(data)
    age=int(data[3])
    """if age>50:
      print(data)"""
    """if age<25:
        print(data)"""
    """if age>=25 and age<=40:
        print(data)"""
    country=data[6]
    """if country=="India":
        print(data)"""
    profession=data[7]
    """if profession=="Doctor":
        print(data)"""
    """if profession=="Engineer":
        print(data)"""
    """if country=="UK":
        print(data)"""
    """if profession=="Doctor" and country=="India":
        print(data)"""
    """ if profession=="Doctor" and country=="UK":
        print(data)"""
    """if profession=="Pilot" and age>40:
        print(data)"""
    gender=data[4]
    """if gender=="Female":
        print(data[1],data[3],data[7])"""
    city=data[5]
    """if city=="Kochi":
        print(data)"""
    """if profession=="Doctor":
        count_doctor+=1
print("Total number of doctors=",count_doctor)"""
    """ if profession not in profession_count:
        profession_count[profession]=1
    else:
        profession_count[profession]+=1
for k,v in profession_count.items():
    print(k,":",v)
            """
    """if country not in country_count:
        country_count[country]=1
    else:
        country_count[country]+=1
for k,v in country_count.items():
    print(k,":",v)"""
    """if age>oldest_age:
        oldest_age=age
        oldest_person=data
print("Oldest person =",oldest_person)"""
    """ if age<youngest_age:
        youngest_age=age
        youngest_person=data
print("youngest person=",youngest_person)"""
    """ages.append(age)
print(ages)
print("Average age of all people=",(sum(ages)/len(ages)))"""
    """if country=="India" and age>30 and (profession =="Doctor" or profession=="Engineer"):
        print(data[1:4],data[5],data[7])"""











    

    
    
    




    
