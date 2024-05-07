# First way
# year = int(input("Enter the year : "))
# if(year%4==0 and year%100!=0) or (year%400==0 ):
#     print(f"Year {year} is a leap year")
# else:
#     print(f"Year {year} is NOT a leap year")

# USING Function
def is_leapYear(year):
    if year % 400 == 0:
        return True




year = int(input("Enter the year : "))
