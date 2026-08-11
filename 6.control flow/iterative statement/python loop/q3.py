#3. Palindrome Number
#A company stores product IDs. Some IDs read the same from both directions.
#Write a Python program to:
#•  Read a number.
#•  Reverse the number using a loop.
#•  Check whether the original number and reversed number are equal
number=int(input("Enter the number:")) 
temp=number
rev=0
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10

if number==rev:
    print("palindrome")  
else:
      print("Not palindrome")
        
