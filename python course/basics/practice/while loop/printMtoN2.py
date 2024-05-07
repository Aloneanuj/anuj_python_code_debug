''''
input: 10 , 15
output: 10 11 12 13 14 15

input 15, 10
output: 10 11 12 13 14 15

input 10 , 10
output: 10
'''
def printMtoN(m,n):
    if m< n:
        i= m
        while i<=n:
            print(i, end=" ")
            i+=1
    elif n < m :
        i=n
        while i<=m:
            print(i, end=" ")
            i+=1
    else:
        print(n)

m = int(input("please enter the starting number : "))
n = int(input("please enter the ending number : "))
printMtoN(m,n)