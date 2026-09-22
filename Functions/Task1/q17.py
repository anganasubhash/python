#Create a function table(num) that prints the table of a given number
def table(num):
    for i in range(1,11):
        print(i,"X",num,"=",num*i)
n1=int(input("Enter the number:"))
table(n1)