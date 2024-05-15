'''
make a function that accept two integers as an arguments .(n1, n2)
print all prime number in betweens

printPrime(2,10)
OUTPUT: 2 3 5 7

'''
def printPrime(n1, n2):
   
   for num in range(n1, n2+1):
    count=0
    for j in range(1, num+1):
        if num % j ==0:
            count+=1
    if count ==2:
        print(num)

printPrime(5,15)