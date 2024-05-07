def addition(num1: int, num2: int) -> int:
    # sum = num1 + num2
    return num1 + num2

    # return sum


def checkEvenOdd(num: int) -> None:
    if num % 2 == 0:
        print("Even : ", num)
    else:
        print("Odd: ", num)


num1= int(input("Enter first integer: "))
num2= int(input("Enter second integer: "))

t = addition(num1, num2)
checkEvenOdd(t)


# def total(num1: int, num2: int) -> int:
#     return num1 + num2

# def checkEvenOdd(num: int) -> None:
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

# num1: int = int(input("Enter a number "))
# num2: int = int(input("Enter a number "))
# t = total(num1, num2)
# print(t)
# checkEvenOdd(t)
