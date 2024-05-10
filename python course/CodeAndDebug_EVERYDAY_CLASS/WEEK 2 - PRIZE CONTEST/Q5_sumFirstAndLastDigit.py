'''
Q5. Make a function named sumOfFirstAndLastDigit which accepts an
integer n from the user. Calculate the sum of first and last digit of a
number and return it
'''

def sumOfFirstAndLastDigit(num):

    first_digit=num//10
    last_digit= num%10
    sum = first_digit + last_digit
    return sum

print(sumOfFirstAndLastDigit(13))