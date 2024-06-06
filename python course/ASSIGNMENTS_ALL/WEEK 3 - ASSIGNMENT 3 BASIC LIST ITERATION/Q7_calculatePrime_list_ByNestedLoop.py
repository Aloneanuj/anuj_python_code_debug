# Q7. Create a function calculatePrime that accepts an List of 
# Integers and print all the prime numbers in that list.

# METHOD 1 (Nested Loops)
from typing import List
def calculatePrime(lst : List[int]) -> None:
    for i in range(0, len(lst)):
        count=0
        num=lst[i]
        for j in range(1, num+1):
            if num % j ==0:
                count+=1
        if count ==2:
            print(num, end=" ")

lst= [7,4,5,8,4,2,9,555,4,57,17]
calculatePrime(lst)
