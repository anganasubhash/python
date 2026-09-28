#iven a string "Hello World", create a list of only the vowels present in it
string="Hello world"
vowels="aeiouAEIOU"
lst1=[i for i in string if i in vowels]
print(lst1)