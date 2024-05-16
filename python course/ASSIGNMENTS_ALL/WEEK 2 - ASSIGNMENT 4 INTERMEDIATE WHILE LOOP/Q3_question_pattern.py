'''Q3. Create a function named pattern which takes an integer as an input and print the following pattern.
example 1:
patter(4)

output:
1 2 4 8

example 2:
pattern(7)

output:
1 2 4 8 16 32 64 
'''
def pattern(num):
    i=1
    temp=1
    while i<=num:
       print(temp, end=" ") 
       temp = temp *2
       i+=1
pattern(7)