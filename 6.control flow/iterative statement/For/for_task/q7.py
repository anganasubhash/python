#Enter temperature for 7 days  and find the highest

highest=float(input("Enter the temperature:"))
for i in range(6):
    temperature=float(input("Enter the temperature:"))
    if temperature>highest:
        highest=temperature
print("highest temperature=",highest)


