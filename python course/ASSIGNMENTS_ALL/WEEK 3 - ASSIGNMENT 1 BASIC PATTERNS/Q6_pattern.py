'''
5 4 3 2 1 
5 4 3 2  
5 4 3  
5 4  
5  
'''

def patter(n):
    for i in range (1, n+1):
        for j in range (n,i-1, -1):
            print(j, end=" ")
        print()

patter(10)