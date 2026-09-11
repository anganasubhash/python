#15. Rainfall Analysis
#Store rainfall for seven days.
#bullet Count days with rainfall above 50 mm.
#bullet Find the average rainfall.

rainfall=[75,65,34,23,55,45,33,]
days=0
for i in rainfall:
    if i>50:
        days+=1
print("Days rainfall above 50 mm=",days)
print("Average rainfall",sum(rainfall)/len(rainfall))