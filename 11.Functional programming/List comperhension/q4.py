#count number of vowels in string
string="luminartechnolab"
vowels="aeiouAEIOU"
lst=[i for i in string if i in vowels]
print(lst)
print("Number of vowels=",len(lst))