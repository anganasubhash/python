#write python program that accepts  deposit amount repeatly
#Add each deposit to the balance
#stop when the user enters 0
#Display the final balance


balance=0
deposit=int(input("Enter the deposit:"))

while deposit!=0:
    balance=balance+deposit
    deposit=int(input("Enter the deposit:"))
print(balance)
