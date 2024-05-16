'''Q2. Create a function named pattern which takes an integer as an input and print the following pattern.
example 1:
patter(4)

output:
10 20 30 40

example 2:
pattern(11)

output:
10 20 30 40 50 60 70 80 90 10 110
'''

def pattern(num): 
    i=1
    while (i<=num):
        print(i*10, end=" ")
        i+=1
    
pattern(11)
