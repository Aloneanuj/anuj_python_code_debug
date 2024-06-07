"""
Create a function calculatePrime that accepts an List of Integers 
and print all the prime numbers in that list.

METHOD 2 (Using 2 functions)
"""

from typing import List
def is_prime(num):
    count = 0
    for i in range(1, num+1):
        if num%i==0:
            count+=1
    if count ==2:
        return True
    return False

def calculatePrime(my_lst):
    for i  in range(1, len(my_lst)):
        if is_prime(my_lst[i]):
            print(my_lst[i], end=" ")

my_lst = [4,7,5,8,55,33,22,1117,12,1,7,5,7,5,7,477]

calculatePrime(my_lst)