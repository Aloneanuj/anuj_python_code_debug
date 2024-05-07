# Calculate the factorial of a number.

# 1st way using while loop

# num= int(input("Enter the integer value : "))
# i=num
# fact=1
# while(i>=1):
#     fact=fact*i
#     i-=1

# print(fact)

# 2nd way using for loop
num=5
fact=1
for i in range(1,num+1):
    if(num>=1):
        fact=fact*i
    num-=1
print(fact)


