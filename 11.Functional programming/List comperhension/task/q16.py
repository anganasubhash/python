#Given a string, create a list of characters that are digits, letters, or special characters separately
#(three lists) using list comprehensions
string = "Hello123@#World45!"
digits = [i for i in string if i.isdigit()]
letters = [i for i in string if i.isalpha()]
special = [i for i in string if not i.isalnum()]
print(digits)
print(letters)
print(special)