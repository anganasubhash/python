#1. Student Marks Analyzer
#Write a function analyze_marks().
#•  Accepts a list of student marks.
#•  Use a loop to find the highest mark.
#•  Count students scoring above 75.
#•  Display marks in ascending order
def analyze_mark():

     highest_mark=0
     count_above75=0
     for i in mark:
       if i>highest_mark:
          highest_mark=i
       if i>75:
           count_above75+=1
     print("Highest mark=",highest_mark)
     print("Count of students above 75=",count_above75)
     mark.sort()
     print(mark)
mark=[55,78,80,90,63,35,85]
analyze_mark(mark)