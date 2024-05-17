# Function to find the average of three numbers
def find_average(num1: int, num2: int, num3: int) -> float:
    return (num1 + num2 + num3) / 3

# Function to compare the average with the fourth number
def average_compare(average: float, num4: int) -> bool:
    return average >= num4  # Return True if the average is greater than or equal to num4

# Get four numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))

# Find the average of the first three numbers
average = find_average(num1, num2, num3)

# Check if the average is greater than or equal to the fourth number
if average_compare(average, num4):
    print(f"The average of {num1}, {num2}, and {num3} is {average:.2f}, \n which is greater than or equal to the fourth number, {num4}.")
else:
    print(f"The average of {num1}, {num2}, and {num3} is {average:.2f}, \n which is smaller than the fourth number, {num4}.")
