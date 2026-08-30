

tup12=("Car","bike",109,56,9000,87)
#add "jeep" on index 2
lst=(list(tup12))
lst[2]="jeep"
tup12=tuple(lst)
print(tup12)