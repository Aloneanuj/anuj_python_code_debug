'''
Q2. Make a function named checkPalindrome which accepts an integer n
from the user. Return True or False if the number is palindrome or not.
Palindrome means which is same as forward and backwards. Do not use
STRINGS.

Example :
checkPalindrome(91)
checkPalindrome(1221)
checkPalindrome(9854)
checkPalindrome(123454321)
'''
def checkPalindrome(n):
    temp=n
    rev=0
    while(temp!=0):
        r=temp%10
        rev= rev*10+r
        temp=temp//10
    if rev == n:
        return True
    else:
        return False
    
print(checkPalindrome(1221))


