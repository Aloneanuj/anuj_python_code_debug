# make a function printMtoN using while loop
def printMtoN(m , n):
    i=m
    while i <= n:
        print(i,end=" ")
        i+=1

m = int(input("please enter the starting number : "))
n = int(input("please enter the ending number : "))
printMtoN(m,n)