'''Q1. Create a function named factorial which takes a integer as an input 
and returns the factorial of that number. Factorial of 5 means 5 x 4 x 3 x 2 x 1 = 120 '''
def factorial(num):
    i=1
    fact=1
    while(i<=num):
        fact = fact * i
        i+=1
    print(fact)

factorial(5)


