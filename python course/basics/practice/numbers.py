def even_odd(num):
    if(num%2==0):
        print(f"The Number '{num}' is a Even Number ")
    else: 
        print(f"The Number '{num}' is a Odd Number ")

def prime(num):
    for i in range(2, (int(num**0.5)-1)):
      if num%i==0:
        print(f"The Number '{num}' is Not a prime number")
        break
    else:
        print(f"The Number '{num}' is a prime number")

def reverse(num):
    rev=0
    temp = num
    while num!=0:
        r=num%10
        rev=rev*10+r
        num=num//10
    print(f"The reverse of {temp} is '{rev}'")

def palindrom_number(num):
    rev= 0
    temp=num
    while(num!=0):
        r= num%10
        rev=rev*10+r
        num=num//10
    if(rev==temp):
        print(temp," Is a palindrome")
    else:
        print(temp," Is not a palindrome")

def armstrong_number(num):
    arm=0
    temp=num
    while(num!=0):
        r=num%10
        arm=arm+r*r*r
        num=num//10
    if(arm==temp):    
        print(temp, " Is a Armstrong number")
    else:
        print(temp, " Is Not a Armstrong number")

def perfect_number(num):
    sum=0
    for i in range(1,num+1):
        if num%i==0:
            sum=sum+i
    if sum==num:
        print(num," Is a perfect Number")
    else:
        print(num," Is not a perfect Number")
            





num=int(input("Enter the number: "))
even_odd(num)
prime(num)
reverse(num)
palindrom_number(num)
armstrong_number(num)
perfect_number(num)






