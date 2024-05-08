# 1 3 6 8 11 13 16 18 21 23
def pattern(n):
    num=1
    i=0
    while i< n:
        print(num ,end=" ")
        if i%2 ==0:
            num=num+2
        else:
            num=num+3
        i+=1
        
pattern(100)