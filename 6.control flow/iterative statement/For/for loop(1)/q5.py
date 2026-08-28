#5. Book Reading Challenge
#Record pages read for 7 days. Display the day numbers on which the student read more than 20
#pages.
for i in range(1,8):
    read=int(input("Enter the number of pages read;"))
    if read>20:
        print("The day student read more than 20 pages is day",i)