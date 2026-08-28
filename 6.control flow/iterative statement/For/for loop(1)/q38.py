##38. Water Quality Testing
#Display sample numbers that failed the quality test (pH outside 6.5–8.5)
n=int(input("Enter the total number of  taken water samples:"))
for i in range(1,n+1):
    ph=float(input("Enter the ph of water:"))
    if not(6.5<=ph<=8.5):
        print("Sample failed quality test id sample",i)