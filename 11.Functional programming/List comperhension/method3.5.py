#list---->value>3000
dic12={"car":3200,"bike":2000,"bus":6000,"lorry":7000,"jeep":5000,"bicycle":1200}
lst=[(k,v) for k,v in dic12.items() if v>3000]
print(lst)