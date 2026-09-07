#copy
#without apple
file1=open("fruits","r")
file2=open("fruits_copy2","w")
for i in file1:
    if i!="Apple\n":
        file2.write(i)

#while writing one by one '\n'
#to read last apple
#type enter to next line in that file then  there \n read it

# or
for i in file1:
    if "Apple" not in i:
        file2.write(i)

for i in file1:
    if i=="Apple" or i=="Apple\n":
        pass
    else:
        file2.write(i)
