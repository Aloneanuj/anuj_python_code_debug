# check the number is prime or not

def check_prime(num):
    i=1
    count=0
    while i<=num    :
        if num%i ==0:
            count=count+1
        i+=1
    if count==2:
        print("It's a prime number")
    else:
        print("It's NOT a prime number")

check_prime(20)
        