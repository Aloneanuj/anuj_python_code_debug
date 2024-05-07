'''
Enter a number =5
Enter a number =10
Enter a number =7
Enter a number =0

output: total = 22
'''

total=0
while True:
    num =  int(input("Enter a number = "))
    total= total+num

    if num==0:
        break
print(total)


