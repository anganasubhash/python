#get only numbers in a sentence 
sentence=" in 1984 there were 13 instance of a protest with over 1000 people attending"
lst=sentence.split( )#not converting to list it print as single digit
lst1=[i for i in lst if i.isdigit()]
print(lst1)
