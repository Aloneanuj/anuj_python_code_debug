# Q1. Create a function countOddEven that accepts an List of Integers and print how many even and odd numbers are there.
from typing import List
def countOddEven(myList:List[int]):
    countEven=0
    countOdd=0
    for i in range(0, len(myList)):
        if myList[i] % 2==0:
            countEven+=1
        else:
            countOdd+=1
    print("Even Numbers are: ",countEven)
    print("Odd Numbers are: ",countOdd)

myList= [45,22,62,28,447,36,31,17,1]
countOddEven(myList)