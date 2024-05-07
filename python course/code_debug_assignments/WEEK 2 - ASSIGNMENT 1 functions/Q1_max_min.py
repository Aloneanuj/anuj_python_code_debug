'''
Write a Python function to find the Maximum and minimum of three
numbers. Use 3 parameters. Make 2 different functions named as maxi and
mini.

'''

def max_number(a,b,c):
    biggest_number = max(a,b,c)
    print("Largest Number : ",biggest_number)

def min_number(a,b,c):
    smallest_number = min(a,b,c)
    print("Smallest number : ",smallest_number)

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))
max_number(a,b,c)
min_number(a,b,c)

