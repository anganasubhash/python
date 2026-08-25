#34. Online Quiz
#Ask 5 questions one by one. Count the correct answer
  

count=0
i=0
while i<5:
    if i==0:
        q=int(input("Number of state in india"))
        if q==28:
            count+=1
    if i==1:
        q=int(input("Total number of bones in human body:"))
        if q==206:
            count+=1
    if i==2:
        q=input("Capital of india:")
        if q=="Delhi":
            count+=1

    if i==3:
        q=int(input("23+45="))
        if q==68:
            count+=1

    if i==4:
        q=int(input("5x3="))
        if q==15:
            count+=1
    i+=1
print("Number of correct answers",count)













