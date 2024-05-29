# Q2. Create a function sumCountOddEven that accepts an List of Integers and calculate sum of even and odd numbers.
from typing import List
def sumCountOddEven(myList: List[int]):
    sumEven=0
    sumOdd=0
    for i in range (0, len(myList)):
        if myList[i] % 2 ==0:
            sumEven= sumEven+myList[i]
        else:
            sumOdd= sumOdd+ myList[i]
    print("Sum of Even Numbers are : ", sumEven)
    print("Sum of Odd Numbers are : ", sumOdd)




myList= [4,9,32,14,25,17,28,36,95,363,56,899,44,65,65]
sumCountOddEven(myList)