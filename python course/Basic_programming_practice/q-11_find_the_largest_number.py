# Find the largest of three numbers.
print("Enter the Three integer number")
num1 = int(input("Enter the First number : "))
num2 = int(input("Enter the second number : "))
num3 = int(input("Enter the third number : "))
if(num1>num2 and num1> num3):
    print("The greatest number is : ", num1)
elif( num2> num3 and num2> num1):
    print("The greatest number is : ", num2)
else:
    print("Ther greatest number is : ", num3)