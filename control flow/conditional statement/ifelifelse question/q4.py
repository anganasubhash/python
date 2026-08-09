
#Input two numbers and an operator (+, -, *, /).
#Perform the operation.
#Display "Invalid Operator" if the operator is incorrect.
num1=int(input("enter the number 1:"))
num2=int(input("enter the number 2:"))
operator=input("enter the operator (+,-,*,/):")
if operator=="+":
    print("sum of num1 and num2 is ",num1+num2)
elif operator=="-":
    print("difference of num1 and num2 is;",num1-num2)
elif operator=="*":
    print("multiplication of num1 and num2 is ;",num1-num2)
elif operator=="/":
    print("division of num1 and num2 is ;",num1/num2)
else: 
    print("Inalid operator")