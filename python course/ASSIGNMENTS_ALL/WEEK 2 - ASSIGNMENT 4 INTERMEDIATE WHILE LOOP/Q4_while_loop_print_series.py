'''
Q4. Don’t create a function, just print the following pattern 1 11 111 1111 11111....n times (Ask n from user)
'''
num= int(input("Enter a number : "))
i=1
n=1
while(i <=num):
    print(n,end=" ")
    n=(n*10)+1
    i+=1
