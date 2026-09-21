#Create a function check_voting(age) that returns whether the person can vote
def check_voting(Age):
    if Age>=18:
        return "You can vote"
    else:
        return "you cannot vote"
age1=int(input("Enter your age:"))
age=check_voting(age1)
print(age)