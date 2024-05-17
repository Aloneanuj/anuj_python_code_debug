'''
Q2. Write a program to display the n terms of a harmonic series and their
sum.
1 + 1/2 + 1/3 + 1/4 + 1/5 ... 1/n terms
Lets suppose n=5.
1/1 + 1/2 + 1/3 + 1/4 + 1/5 = 2.283334
'''
def harmonic_series(num):
    sum=0
   
    # for i in range(1,num+1):
    #     sum=sum+1/i
    # return sum

    i=1
    while(i <= num):
        sum= sum + 1/i
        i+=1
    return sum


num = int(input("Enter the number : "))

result= harmonic_series(num)
print(result)
