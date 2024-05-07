# # Find the sum of N natural number where N is input from user.
# N=int(input("Enter a Natural number : "))
# temp=N
# sum=0
# while(N!=0):
#     sum=sum+N
#     N-=1
# print(f"Sum of {temp} natural Numbers = {sum}")



num= int(input("Enter the number : "))
sum=0
i=0
while(i<=num):
    sum=sum+i
    i+=1
print(f"Sum of {num} natural number are : ", sum)