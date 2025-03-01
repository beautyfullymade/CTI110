 # Toni Bethune
 # 02282025
 # P1HW2
 # create a program that does some basic math on numbers for a travel budget










print("This program calculates and displays travel expenses\n")

# Get user inputs
budget = float(input("Enter Budget: "))
destination = input("\nEnter your travel destination: ")

gas_expense = float(input("\nHow much do you think you will spend on gas? "))
hotel_expense = float(input("\nApproximately, how much will you need for accommodation/hotel? "))
food_expense = float(input("\nLast, how much do you need for food? "))

# Calculate total expenses and remaining balance
total_expenses = gas_expense + hotel_expense + food_expense
remaining_balance = budget - total_expenses

# Display results
print("\n------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}")
print(f"\nFuel: {gas_expense}")
print(f"Accommodation: {hotel_expense}")
print(f"Food: {food_expense}")
print(f"\nRemaining Balance: {remaining_balance}")
