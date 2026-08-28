#11. Hospital Medicine Distribution
#Display patient IDs who received more than 5 medicine packets
n=int(input("Enter total number of patient:"))
for i in range(1,n+1):
    packects=int(input("Enter the number medicine packet:"))
    if packects>5:
        print("patient IDS received more than 5 medicine packet is p",str(i).zfill(3))
