'''
Q4. Ask x and n from user and then calculate the following answer.

Example 1:
patter(x=6, n=4)

output:
6^1 - 6^3 + 6^5 - 6^7
-272370(OUTPUT)

pattern(x=9, n=11)
6^1 - 6^3 + 6^5 - 6^7 + 6^9 - 6^11 + 6^13 - 6^15 . . . . upto n times
108084611215274403609(OUTPUT)
'''

def patter(x, n):

    i=1
    j=1
    total  = 0
    while i<= n:
        if i%2 != 0:
            total = total + x ** j
        else:
            total = total - x ** j
        i+=1
        j+=2

    return total

result= patter(9 , 11)
print(result)