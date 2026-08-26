#4. Count Positive, Negative, and Zero
#Accept N numbers from the user. Display the count of:
# Positive numbers
#Negative numbers
#Zeroes
n=int(input("Enter How many number do you want:"))
count_positive=0
count_negative=0
count_zeros=0
for i in range(n):
    num=int(input("Enter the number"))
    if num>0:
        count_positive+=1
    elif num<0:
        count_negative+=1
    else:
        count_zeros+=1

print(" count of positive numbers=",count_positive)
print("Count of negative numbers=",count_negative)
print("Count of zeros=",count_zeros)