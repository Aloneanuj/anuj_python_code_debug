# check the given number is armstrong or not using while loop.

num =  int(input("Enter the number : "))
arm=0
temp = num
while (num!=0):
    r = num%10
    arm=arm + (r*r*r)
    num=num//10
if(arm == temp):
    print(f"The number {temp} is a Armstrong number")
else:
    print(f"The number {temp} is not a Armstrong number")
