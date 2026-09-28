#1 Given a list of numbers, create a list of squares only for the even numbers
lst=[i**2 for i in range(1,51) if i%2==0]
print(lst)