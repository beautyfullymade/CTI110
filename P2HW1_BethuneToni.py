 # Toni Bethune
 # 03152025
 # P2HW1
 # create a program that does some basic math on numbers for a travel budget add dollar signs and have the amounts align.










budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
fuel = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Calculate remaining balance
remaining_balance = budget - (fuel + accommodation + food)

# Display formatted travel expenses
print("\n------------Travel Expenses------------")
print(f"{'Location:':<15} {destination}")
print(f"{'Initial Budget:':<15} ${budget:,.2f}")
print(f"{'Fuel:':<15} ${fuel:,.2f}")
print(f"{'Accommodation:':<15} ${accommodation:,.2f}")
print(f"{'Food:':<15} ${food:,.2f}")
print("--------------------------------------")
print(f"Remaining Balance: ${remaining_balance:,.2f}")
