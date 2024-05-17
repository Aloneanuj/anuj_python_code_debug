'''Attempt the same leap year question (Week 1 - Assignment 2 - Q8) but
using function. Try calling function with different years as a parameter and
check the output.
'''
def find_leap_year(year):
    if ( year % 4 ==0 and year % 100 !=0 )  or year % 400==0:
        print("Leap year : ", year)
    else: 
        print("NOT a Leap year : ", year)

year = int(input("Enter the year : ")) 
find_leap_year(year)