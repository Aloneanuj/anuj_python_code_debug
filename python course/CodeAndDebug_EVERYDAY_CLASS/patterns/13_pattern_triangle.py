'''
       *     
     * * *    
    * * * * *   
  * * * * * * *  
* * * * * * * * * 
'''
def pattern(n):    
    for i in range(1, n+1):
        for j in range(i, n+1):
            print(" ", end=" ") 
        for k in range (1, (2*i)-1+1):
            print("*",end=" ")
        print()
    for l in range(n-1, 0 , -1):
        for m in range(n, l-1, -1) :
            print(" ", end=" ") 
        for o in range(2*l-1):
            print("*",end=" ")
        print()

pattern(7)