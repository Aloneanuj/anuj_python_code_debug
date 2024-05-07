# find the factorial of number enter by user.
num = int(input("Enter the number : "))
fact = 1
i = 1
while(i <= num):
    fact= fact* i
    i+=1
print(f"factorial of {num} : ",fact)