#count number of vowels
#vowels
string="Luminartechnolab"
vowels="aeiou"
lst=[i  for i in string if i in vowels]
print(lst)
print("Count of vowels:",len(lst))
#consonants
lst1=[i for i in string if i not in vowels]
print(lst1)
print("count of consonants:",len(lst1))