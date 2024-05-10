# Q2. Create a function named as checkPrime that takes an integer as an argument. Print YES if the number passed is a prime number else print NO. 
def checkPrime(num):
    i=1
    count=0
    while i<num:
        if i % num == 0:
            count+=1
        i+=1

    if i>=1:
        print("NO")
    else:
        print("Yes")


num = int(input("Enter the number : "))
checkPrime(num)
