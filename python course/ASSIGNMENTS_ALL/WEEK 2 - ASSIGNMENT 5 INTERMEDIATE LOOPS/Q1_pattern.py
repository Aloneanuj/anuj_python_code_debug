# Q1. 2 22 222 2222 22222 ... upto n. (Ask n from user)

num = int(input("Enter the number : "))
# i=2
# j=0
# while num!=0:
#     print(i)
#     i=i*10+2
#     num=num-1

temp=2
for i in range (num):
   print(temp)
   temp = temp*10+2
