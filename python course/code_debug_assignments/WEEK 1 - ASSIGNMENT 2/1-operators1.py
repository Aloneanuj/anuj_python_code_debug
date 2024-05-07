a = 5
b = 10

# Line 1
print(a > 5 and b >= 10)
# Explanation: Is a greater than 5 AND is b greater than or equal to 10?
# Result: False, because a is not greater than 5.

# Line 2
print(a >= 5 or not b > 10)
# Explanation: Is a greater than or equal to 5 OR is not b greater than 10?
# Result: True, because a is equal to 5.

# Line 3
print(not (a > 5 and b > 5))
# Explanation: Is it NOT the case that both a is greater than 5 AND b is greater than 5?
# Result: True, because a is not greater than 5.

# Line 4
print(not (a < 10 or not b < 10))
# Explanation: Is it NOT the case that either a is less than 10 OR not b is less than 10?
# Result: False, because both conditions are true (a is less than 10, and b is less than 10).

# Line 5
print(not (not a <= 5 or not b >= 10))
# Explanation: Is it NOT the case that NOT (a is less than or equal to 5 OR not b is greater than or equal to 10)?
# Result: True, because both conditions in the inner parentheses are false.

