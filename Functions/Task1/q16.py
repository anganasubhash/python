#Task:
#Create a functiontoke generate_ns(n) that prints token numbers from 1 to n
def  generate_ns(n) :
    for i in range(1,n+1):
        print("Token number",i)
n1=int(input("Enter total token number:"))
generate_ns(n1)