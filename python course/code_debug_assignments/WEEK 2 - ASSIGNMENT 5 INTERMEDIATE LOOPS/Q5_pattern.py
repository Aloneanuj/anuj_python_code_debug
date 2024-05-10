'''
Q5. Create a function addDigits() that takes an integer as an argument.
Calculate the sum of digits of that number.
example 1:
addDigits(123)
6 (OUTPUT)

addDigits(56321)
17 (OUTPUT)
'''
def addDigits(num):
    sum=0
    while(num!=0):
        r=num%10
        sum=sum+r
        num=num//10
    return sum
result= addDigits(56321)
print(result)


