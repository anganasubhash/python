#2nd largest element
lst45=[19,34,23,56,78,54,67,89,890,432]
lst45.sort()
print(lst45)
print(lst45[-2])
#or reverse to decending 
#lst45(reverse=True)
#print(lst45[1])

#[56,78,54]
print(lst45[3:6])
print(lst45[8:])
print(lst45[-2:])
#34,23
print(lst45[1:3])
#[23,.....,432]
print(lst45[2:])
#[19,...89]
print(lst45[:-2])