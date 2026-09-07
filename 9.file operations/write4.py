#doctors:5
#police officers:4
#teacher:7

#Read
#dic={}
#write
file1=open("customer.txt","r")
file2=open("customer_copy","w")
dic={}
for i in file1:
    data=i.rstrip("\n").split(",")
    prof=data[4]
    if prof not in dic:
        dic[prof]=1
    else:
        dic[prof]+=1
print(dic)

for k,v in dic.items():
    res=k+":"+str(v)+"\n"
    file2.write(res)
    



    


    

