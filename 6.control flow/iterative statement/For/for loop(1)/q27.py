#27. Hospital Health Camp
#Display patient IDs classified as Obese (BMI >=30)
n=int(input("Enter the total number of patients:"))
for i in range(1,n+1):
    bmi=int(input("Enter the bmi of patient:"))
    if bmi>=30:
        print("Patients ID of patients obese is P",str(i).zfill(4))