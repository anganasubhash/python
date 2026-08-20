

lst34=['abc','hjh','cac','fds','sfgh','pop','yty','ret','ere','121','678','67856']
#hjh,cac,pop,yty,ere,121,454-----same starting and ending
#[]
#taking cac as i then 0==-1
#for---0 to n-1
#back---1 to -n
list=[]
for i in lst34:
    if i[0]==i[-1]:
        list.append(i)
print(list)
   