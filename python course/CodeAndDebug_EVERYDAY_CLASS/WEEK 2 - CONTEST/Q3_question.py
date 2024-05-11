'''
Q3. Create a function named as printPrimeFactors that takes an integer n as a
 argument and print all the prime factors of that number
 printPrimeFactors(20)
 printPrimeFactors(7)
 printPrimeFactors(72)

 OUTPUTS:
 2 5
 7 
 2 3
'''
def prime(n):
    i=1
    count=0
    while(i<=n):
        if n%i==0:
            count+=1
        i+=1
    if count==2:
        return True
    else:
        return False
      
def printPrimeFactors(n):
    i=1
    while(i<=n):
        if n % i ==0:
            if prime(i):
                print(i,end=" ")
        i+=1

num = int(input("Enter the number: "))
printPrimeFactors(num)