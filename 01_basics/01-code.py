# Day 01 - Python Getting Started

# 1. Type Checking
# type() tells us the data type of a value.
print(type(1.0))       # float
print(type(20))        # int
print(type("hello"))   # str


# 2. Comparison / Relational Operators
# These operators compare two values and return True or False.
print(12 < 3)
print(12 > 3)
print(12 == 12)


# 3. String Concatenation
# The + operator joins two strings together.
first_name = "Sana"
second_name = "Ullah"

print(first_name + second_name)


# 4. String Duplication
# The * operator can repeat a string multiple times.
print("SANNY\n" * 10)


# 5. Logical Operators
# Logical operators are used to combine or modify conditions.
print(True and True)
print(False and True)
print(False or True)
print(not True)


# 6. Built-in Functions
# Python provides built-in functions for common operations.
# min() finds the smallest value.
# max() finds the largest value.
# pow() calculates a number raised to a power.

result = max(min(22, 3), pow(2, 3))

print(result)