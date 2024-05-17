'''
Q3. Ask x and n from user and then calculate the following answer.
Example 1:
pattern(x=6, n=4)

Output:

6/1 + 6/3 + 6/5 + 6/7
10.05714285(OUTPUT)

pattern(x=9, n=11)

9/1 + 9/3 + 9/5 + 9/7 + 9/9 + 9/11 + 9/13 . . . . upto n times
19.627871200(OUTPUT)
'''
def patter(x, n):
    i = 1
    j=1
    sum=0
    while i<=n:
        sum=sum+x/j
        j+=2
        i+=1
    return sum

result=patter(9,11)
print(result)