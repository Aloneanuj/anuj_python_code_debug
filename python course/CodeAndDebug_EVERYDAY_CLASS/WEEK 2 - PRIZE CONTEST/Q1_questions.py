'''
Q1. Make a function named reverse which accepts an integer n from the
user. Reverse the number passed as a parameter and return the reverse
number. Do not use STRINGS.
Example 1:
reverse(91)
19 (OUTPUT)

reverse(1000)
1 (OUTPUT)

reverse(1474)
4741
'''
def reverse(num):
    rev=0
    while(num!=0):
        r=num%10
        rev= rev*10+r
        num=num//10
    return rev

print(reverse(1000))
