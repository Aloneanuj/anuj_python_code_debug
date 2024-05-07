# check whether the number entered by the user is prime or not
# def is_prime(num):
#     if num<=1:
#         return False
#     elif num<=3:
#         return True
#     i=2
#     while(i*i<=num):
#         if num%i==0:
#             return False
#         i+=1
#     return True

# num = int(input("Enter the number : "))
# if is_prime(num):
#     print(num, " Is Prime number ")
# else:
#     print(num, " is not a prime number")

# def is_prime(num):
#     if num<=1:
#         return False
#     elif num<=3:
#         return True
#     i=2
#     while(i*i<=num):
#         if num%i==0:
#             return False
#         i+=1
#     return True

# num=int (input("Enter your number "))
# if is_prime(num):
#     print(f"The {num} is a Prime number")
# else:
#     print(f"The {num} is not a Prime number")

def is_prime(num):
    if num<=1:
        return False
    elif num<=3:
        return True
    i=2
    while(i*i<=num):
        if(num%i==0):
            return False
        i+=1
    return True
        
num = int(input("Enter the number : "))
result =  is_prime(num)
if result:
    print("Its a prime number: ", num)
else:
    print("It's not a prime number : ", num)

