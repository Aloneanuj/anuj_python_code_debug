def additions(num1, num2):
    sum=num1+num2
    print("add = ", sum)

def subtraction(num1, num2):
    sub=num1-num2
    print("Subtraction = ",sub)

def multiplication(num1, num2):
    mul=num1*num2
    print("multiplication = ",mul)

def division(num1, num2):
    div=num1/num2
    print("Division = ",div)

def biggest_number(num1, num2):
    if(num1>num2):
        print(f"The Number {num1} is greater than {num2}")
    elif(num2>num1):
        print(f"The Number '{num2}' is greater than {num1}")
    else:
        print(f"The number '{num1}' and '{num2}' both are equal")


num1=int(input("Enter the first Number: "))
num2=int(input("Enter the second Number: "))
additions(num1,num2)
subtraction(num1,num2)
multiplication(num1, num2)
division(num1, num2)
biggest_number(num1, num2)