#Given a list of dictionaries [{"name": "Amit", "age": 25}, {"name": "Bala",
#"age": 17}, {"name": "Chitra", "age": 30}], create a list of names of people who
#are adults (age ‡ 18)
lst1=[{"name": "Amit", "age": 25}, {"name": "Bala","age": 17}, {"name": "Chitra", "age": 30}]
lst2=[sublist["name"] for sublist in lst1 if sublist["age"]>=18 ]
print(lst2)