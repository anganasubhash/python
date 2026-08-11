 #Guess the Number Game

# Write a Python program that stores a secret number.

# Ask the user to guess the number.
# Continue until the correct number is guessed.
# Display the number of attempts taken.
secret_number=333
number=int(input("Guess the secret number:"))
count=0
count+=1
while number!=secret_number:
         count+=1
         number=int(input("Guess the secret number:"))
print("Number attempts taken=",count)
    
    
    
