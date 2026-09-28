#Given a list of words, create a list of words reversed (each word spelled backward), but only for
#words with an even number of letters
lst = ["apple", "banana", "cherry", "mango"]
lst1=[word[::-1] for word in lst if len(word)%2==0]
print(lst1)