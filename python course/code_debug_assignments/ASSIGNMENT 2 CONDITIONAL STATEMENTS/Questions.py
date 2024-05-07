"""
NOTE:
Q1. Write a program that takes two numbers as input and checks if the first
number is divisible by the second.
Q2. A student will not be allowed to sit in exam if his/her attendance is less
than 75%.
Take following input from user
Q3. Write a program to check if number is divisible by 2 and 3 but not 8.
Q4. Write a Python program that takes a student's score as input and
prints the corresponding grade. Use the following grading scale:
A: 90-100
B: 80-89
C: 70-79
ASSIGNMENT 2
CONDITIONAL STATEMENTSinfo@codeanddebug.in Code and Debug codeanddebug.in
No need to submit anywhere, just keep track of all the PDF you made in a specific folder.
Compare your solution with the solution I’ll provide, in case of doubts, kindly reach out
to me.
You may get assignment solution in format of PDF or VIDEO solution, depending on the
difficulty level.
Number of classes held
Number of classes attended.
1. Print percentage of class attended
2. Print Is student is allowed to sit in exam or not.
D: 60-69
F: Below 60
Q5. Write a program to calculate bill. Ask the final amount from the user.
You have to give discount and print the final bill after discount.
50000 above - 30% discount
40000 - 49999 - 25% discount
30000 - 39999 - 20% discount
10000 - 29999 - 10% discount
1 - 9999 - No discount
Print the discount and the final amount to be paid.
Example 1
Enter bill amount = 80000
You got 30% discount
Your final bill is Rs. 56000
Q6. Ask 4 numbers from user. Make sure all the numbers entered by user
are different. Print which number is the smallest.
Q7. Take Salary as input from User and Update the salary of an employee.
Q8. An extra day is added to the calendar almost every four years as
February 29, and the day is called a leap day. A leap year contains a leap
day.
These are the conditions used to identify leap years:
salary less than 10,000, 5 % increment
salary between 10,000 and 20, 000, 10 % increment
salary between 20,000 and 50,000, 15 % increment
salary more than 50,000, 20 % increment
if the year can be evenly divided by 4, it is then a leap year
This means the years 2000 and 2400 are leap years, while 1800, 1900,
2100, 2200, 2300 and 2500 are NOT leap years.
Ask a year input from user. And tell if the year entered by user is leap or
not.
but if the year is evenly divided by 4 and also by 100, then it is NOT a
leap year
but if the year is evenly divided by 4 and also by 400, then it is a leap
year
"""

# ------------------solutions below-----------------------
# NOTE:
# Q1. Write a program that takes two numbers as input and checks if the first
# number is divisible by the second.
# Q2. A student will not be allowed to sit in exam if his/her attendance is less
# than 75%.
# Take following input from user
# SOLUTION - ASSIGNMENT 2
# CONDITIONAL STATEMENTSinfo@codeanddebug.in Code and Debug codeanddebug.in
# No need to submit anywhere, just keep track of all the PDF you made in a specific folder.
# Compare your solution with the solution I’ll provide, in case of doubts, kindly reach out
# to me.
# You may get assignment solution in format of PDF or VIDEO solution, depending on the
# difficulty level.
# Number of classes held
# Number of classes attended.
# 1. Print percentage of class attended
# Q3. Write a program to check if number is divisible by 2 and 3 but not 8.
# Q4. Write a Python program that takes a student's score as input and
# prints the corresponding grade. Use the following grading scale:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60
# 2. Print Is student is allowed to sit in exam or not.
# Have a look how we are comparing scores, you can do it using 2 ways.
# Q5. Write a program to calculate bill. Ask the final amount from the user.
# You have to give discount and print the final bill after discount.
# 50000 above - 30% discount
# 40000 - 49999 - 25% discount
# 30000 - 39999 - 20% discount
# 10000 - 29999 - 10% discount
# 1 - 9999 - No discount
# Print the discount and the final amount to be paid.
# Example 1
# Enter bill amount = 80000
# 90 <= score <= 100
# score >= 90 and score <= 100 (preferred method)
# You got 30% discount
# Your final bill is Rs. 56000
# Q6. Ask 4 numbers from user. Make sure all the numbers entered by user
# are different. Print which number is the smallest.
# Q7. Take Salary as input from User and Update the salary of an employee.
# salary less than 10,000, 5 % increment
# salary between 10,000 and 20, 000, 10 % increment
# salary between 20,000 and 50,000, 15 % increment
# salary more than 50,000, 20 % increment
# Q8. An extra day is added to the calendar almost every four years as
# February 29, and the day is called a leap day. A leap year contains a leap
# day.
# These are the conditions used to identify leap years:
# This means the years 2000 and 2400 are leap years, while 1800, 1900,
# 2100, 2200, 2300 and 2500 are NOT leap years.
# Ask a year input from user. And tell if the year entered by user is leap or
# not.
# Answer 1
# if the year can be evenly divided by 4, it is then a leap year
# but if the year is evenly divided by 4 and also by 100, then it is NOT a
# leap year
# but if the year is evenly divided by 4 and also by 400, then it is a leap
# year
# Answer 2