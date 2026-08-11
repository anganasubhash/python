# 3. Online Quiz System

# Write a Python program that asks a question repeatedly.#

# If the answer is incorrect, ask again.
# Stop when the correct answer is entered.
# Display "Correct Answer".

user_answer=int(input("Total number of bones in human body;"))
answer=206
while user_answer!=answer:
    print("INcorrect answer")
    user_answer=int(input("Total number of bones in human body;"))

print("Correct answer")
