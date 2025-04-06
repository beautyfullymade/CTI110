# Toni Bethune
# 04042925
# P4LAB
#multiplication table







def show_multiplication_table(num):
    for i in range(1, 13):
        print(f"{num} * {i} = {num * i}")

def main():
    while True:
        try:
            number = int(input("Enter an integer: "))
            if number < 0:
                print("This program does not handle negative numbers.\n")
            else:
                show_multiplication_table(number)
        except ValueError:
            print("Invalid input. Please enter a valid integer.\n")
            continue

        run_again = input("\nWould you like to run the program again? ").strip().lower()
        if run_again != "yes":
            print("\nExiting program...")
            break
        print()  # Blank line before next run

# Run the program
main()
