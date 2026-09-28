#Given a range of years 1990 to 2025, create a list of leap years using a list comprehension.
lst1=[year for year in range(1990,2026) if year%400==0 or (year%100!=0 and year%4==0)]
print(lst1)