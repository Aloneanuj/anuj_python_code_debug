'''
Q6. Write a function named pattern which accepts an integer n as an
argument. Then print the following pattern.

Example: 1
pattern(4)
output:
1 4 9 16

Example: 2
pattern(10)
output:
1 4 9 16 25 36 49 64 91 100

'''
def pattern(n):
    i=1
    while i<=n:
        print(i* i, end=" ")
        i+=1
pattern(14)


