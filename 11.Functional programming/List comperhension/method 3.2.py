#(number,even number)
#(number,odd number)
lst=[(i,"Even") if i%2==0 else (i,"odd") for i in range(1,51)]
print(lst)
