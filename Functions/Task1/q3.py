#Create a function calculate_grade(mark) that returns:
#• A for 90+
#• B for 75+
#• C for 50+
#• F otherwis
def calculate_mark(Mark):
    if Mark>90:
        return "A"
    elif Mark>75:
        return"B"
    elif Mark>50:
        return "C"
    else:
        return "F"

mark1=int(input("Enter the mark :"))
grade=calculate_mark(mark1)
print("Grade=",grade)

