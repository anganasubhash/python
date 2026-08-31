#18. Website Visitors
#Store daily visitor counts.
#bullet Count days with more than 1000 visitors.
#bullet Find the busiest day

visitors=[2000,3000,1000,500,300]
count=0
for i in visitors:
    if i>1000:
        count+=1
print("Days with more than 1000 visitors =",count)
busiest_day=visitors.index(max(visitors))+1
print("Busiest day=",busiest_day)
