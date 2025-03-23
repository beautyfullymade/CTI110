
# Toni Bethune
# 03152025
# P2HW1
# create a program that does some basic math on numbers for a travel budget add dollar signs and have the amounts align.











budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
fuel = float(input("How much do you think you will spend on gas? "))
hotel = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))


total = fuel + hotel + food
balance = budget - total


print("\n------------ Travel Expenses ------------")
print(f"{'Location:':15s}{destination}")
print(f"{'Initial Budget:':15s}${budget:,.2f}")
print(f"{'Fuel:':15s}${fuel:,.2f}")
print(f"{'Accommodation:':15s}${hotel:,.2f}")
print(f"{'Food:':15s}${food:,.2f}")
print("-----------------------------------------")
print(f"\n{'Remaining Balance:':15s}${balance:,.2f}")
