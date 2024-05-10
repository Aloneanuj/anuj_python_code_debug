'''
Q4. Make a function named checkArmstrong which accepts an integer n
from the user. Return True or False if that number is an armstrong number.
EXAMPLE:
checkArmstrong(153)
means: 1^3 + 5^3 + 3^3
OUTPUT: TRUE

checkArmstrong(407)
means: 4^3 + 0^3 + 7^3
OUTPUT: 
'''

def digitCount(n):
    count=0
    while n!=0:
        count+=1
        n=n//10
    return count

def checkArmstrong(num):
    calculated_digits = digitCount(num)
    temp= num
    num_sum=0
    while num!=0:
        r= num%10
        num_sum =num_sum+ r ** calculated_digits
        num= num//10
    if num_sum == temp:
        return True
    else:
        return False

num = int(input("Enter the number : " ))    
print(checkArmstrong(num))
    
