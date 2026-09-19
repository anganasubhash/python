
#x<40 mark--->
#41 to 60---->average
#above 61 to 100---->excellent
lst=[(i,"Poor") if i<=40 else (i,"Average") if 41<=i<=60 else(i,"Excellent")  for i in range(1,101)]
print(lst)