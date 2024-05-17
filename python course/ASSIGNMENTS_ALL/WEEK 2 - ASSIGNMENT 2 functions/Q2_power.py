"""Q2. Implement a function that takes two parameters, base and exponent,
and returns the result of raising the base to the power of the exponent."""
def find_power(base_value, exponent_value):
    power= base_value**exponent_value
    print(power)

# find_power(3,3)

base_value = 2
exponent_value = 3
result_power = find_power(base_value, exponent_value)
print(f"{base_value} raised to the power of {exponent_value} is: {result_power}")