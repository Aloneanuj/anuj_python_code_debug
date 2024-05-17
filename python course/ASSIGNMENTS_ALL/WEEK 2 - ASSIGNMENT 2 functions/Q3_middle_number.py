def find_middle_number(num1: int, num2: int, num3: int) -> int:
    if (num1 >= num2 and num3 <= num2) or (num1 <= num2 and num3 >= num2):
        return num2
    elif (num2 >= num1 and num3 <= num1) or (num2 <= num1 and num3 >= num1):
        return num1
    else:
        return num3

def check_middle_number_divisibility(middle_number: int) -> bool:
    if middle_number % 3 == 0 and middle_number % 4 == 0:
        return True
    else:
        return False  # This return handles the case when not divisible by both 3 and 4

# Get three numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Find the middle number
middle_number = find_middle_number(num1, num2, num3)

# Check if the middle number is divisible by both 3 and 4
if check_middle_number_divisibility(middle_number):
    print(f"Middle number is {middle_number}, which is divisible by both 3 and 4.")
else:
    print(f"Middle number is {middle_number}, which is NOT divisible by both 3 and 4.")
