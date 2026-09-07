#fruits.txt read---->copy
#fruits_copy
#read---->write
file=open("fruits","r")
file1=open("fruits_copy","w")
for i in file:
    file1.write(i)
#while taking i in loop no need for '\n'