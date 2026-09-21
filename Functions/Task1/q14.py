#cenario:
# hospital calculates Body Mass Index.
#ask:
#reate a function calculate_bmi(weight, height).
def calculate_bmi(weight, height):
    bmi=weight/(height*height)
    print(bmi)
weight1=int(input("Enter your weight:"))
height1=int(input("Enter your height:"))
calculate_bmi(weight1,height1)

    
