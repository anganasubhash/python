

#Input monthly data usage.
#Display the appropriate plan based on usage.
data=int(input("enter monthly data usage:"))
if data<=3:
    print("basic plan")
elif data<=7:
    print("permium plan")
else:
    print("unlimted plan")
