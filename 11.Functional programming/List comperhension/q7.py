#count length of words
sentence="This is a sample sentence"
lst=sentence.split()#convert to list
lst1=[len(i) for  i in lst]
print(lst1)

