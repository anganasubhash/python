#6. Fruits List
#Create a list of fruits.
#bullet Add two new fruits.
#bullet Remove one fruit.
#bullet Print the total number of fruits

fruits=["Grape","Apple","avacado"]
print(fruits)
fruits.extend(["Orange","Mango"])
fruits.remove("Apple")
print(fruits)
print("Total number of fruits =",len(fruits))