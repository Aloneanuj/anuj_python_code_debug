# print all the factor of number 

def printFactor(num):
    i=1
    while i<=num:
        if num % i ==0:
            print(i , end=" ")
        i+=1

printFactor(30)

# print all the factor of number and there sum
print("\n---------------")

def printFactor_sum(num):
    i=1
    count=0
    while i<=num:
        if num % i ==0:
            count=count+i
            print( i , end=" ")
        i+=1
    print("\n count of all the factor : ", count)
    
printFactor_sum(30)