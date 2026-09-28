
#From a list of words, create a list containing only the words with more than 4 letters
word=["washing machine","mouse","Tv","Ac","Heater"]
lst=[i for i in word if len(i)>4]
print(lst)