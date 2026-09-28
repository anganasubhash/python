#Given a sentence, create a list of word lengths, but only for words that don't start with a vowel
sentence="I watch television in the evening"
vowels="aeoiuAEIOU"
lst=sentence.split( )
lst1=[len(word)for word in lst if word[0] not in vowels]
print(lst1)