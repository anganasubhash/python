

lst=[1,2,3,4,5,6,7,8,9,10]
#map-->
def square(num):
    return num*num
lst1=list(map(square,lst))
print(lst1)

f=lambda num:num*num
lst1=list(map(f,lst))
print(lst1)