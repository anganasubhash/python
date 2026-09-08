#dic={}
#district with its highest temperature
file1=open("dis_temp.txt","r")
file2=open("dis_temp2.txt","w")
temperatue={}
for i in file1:
    data=i.rstrip("\n").split(",")
    print(data)
    dist=data[0]
    temp=int(data[1])
    if dist not in temperatue:
        temperatue[dist]=(temp)
    else:
        if (temp)>temperatue[dist]:
            temperatue[dist]=(temp)
print(temperatue)
for k,v in temperatue.items():
    file2.write(k+":"+str(v)+"\n")
    
