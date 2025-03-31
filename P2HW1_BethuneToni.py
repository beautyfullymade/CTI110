
# Toni Bethune
# 03152025
# P2HW1
# This program calculates and displays travel expenses

# Inputs
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
fuel = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accomodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Calculations
total_expenses = fuel + accommodation + food
balance = budget - total_expenses

# Output
print("\n------------Travel Expenses------------")
print(f"{'Location':<15}{destination}")
print(f"{'Initial Budget':<15}${budget:.2f}")
print(f"{'Fuel':<15}${fuel:.2f}")
print(f"{'Accomodation':<15}${accommodation:.2f}")
print(f"{'Food':<15}${food:.2f}")
print("----------------------------------------")
print(f"{'Remaining Balance':<15}${balance:.2f}")
