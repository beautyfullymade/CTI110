# Toni Bethune
# 02282025
# P1HW1
# Using Python's input and print functions.

# ----Calculating Exponents----
print("-----Calculating Exponenets----\n")

# Get user input for base and exponent
base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))

# Calculate exponentiation
result = base ** exponent

# Display the result
print(f"\n{base} raised to the power of {exponent} is {result} !!\n")

# ----Addition and Subtraction----
print("-----Addition and Subtraction----\n")

# Get user input for the three integers
start_int = int(input("Enter a starting integer: "))
add_int = int(input("Enter an integer to add: "))
subtract_int = int(input("Enter an integer to subtract: "))

# Perform calculations
final_result = start_int + add_int - subtract_int

# Display the result
print(f"\n{start_int} + {add_int} - {subtract_int} is equal to {final_result}")
