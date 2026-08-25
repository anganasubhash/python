#40. Mini Calculator
#Display a menu:
#1 Addition
#2 Subtraction
#3 Multiplication
#4 Division
#5 Exit
#Repeat until the user select exit

choice=0
while choice!=5:
    print("1.Addition")
    print("2.substraction")
    print("3.multiplication")
    print("4.Division")
    print("5.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        print("Addition")
    elif choice==2:
        print("Substraction")
    elif choice==3:
        print("Multiplication")
    elif choice==4:
        print("Division")
    elif choice==5:
        print("Exit")
    else:
      print("inalid choice")