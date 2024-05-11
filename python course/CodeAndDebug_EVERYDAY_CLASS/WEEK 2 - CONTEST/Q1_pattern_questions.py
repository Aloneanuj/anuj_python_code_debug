'''
Q1. Make a function named sumPattern that takes an integer n as an
argument from the user. And then calculate the sum of the following
pattern.

Example:
sumPattern(5)

Means
1/1! + 1/2! + 1/3! + 1/4! + 1/5!

1.7166666666666668 (output)

'''
def factorial(n):
    i=1
    fact=1
    while(i<=n):
        fact = fact * i
        i+=1
    return fact

def sumPattern(num):
    i=1
    sum=0
    while(i<=num):
        sum=sum+ 1/ factorial(i)
        i+=1
    return sum

num= int(input("Enter the number: "))
result= sumPattern(num)
print(result)

