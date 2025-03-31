# Toni Bethune
# 03302025
# P3HW2
# A program that calcautes an employee's hours,overtime and pay.











# -------------------------------------------------------------
# Pseudocode:
# -------------------------------------------------------------
# 1. Ask user to enter the employee's name.
# 2. Ask user to enter number of hours worked.
# 3. Ask user to enter pay rate.
# 4. Check if hours worked > 40:
#     a. If yes, calculate overtime hours (hours worked - 40)
#     b. Calculate overtime pay as overtime hours * pay rate * 1.5
#     c. Regular hours = 40
# 5. If no overtime, regular hours = total hours worked, overtime = 0
# 6. Calculate regular pay = regular hours * pay rate
# 7. Calculate gross pay = regular pay + overtime pay
# 8. Display employee name, hours worked, pay rate, overtime hours,
#    overtime pay, regular pay, and gross pay with proper formatting.
# -------------------------------------------------------------

# Input
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Processing
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
else:
    overtime_hours = 0
    regular_hours = hours_worked

overtime_pay = overtime_hours * pay_rate * 1.5
regular_pay = regular_hours * pay_rate
gross_pay = regular_pay + overtime_pay

# Output
print("-" * 65)
print(f"Employee name:    {employee_name}")
print()
print("Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay")
print("-" * 65)
print(f"{hours_worked:<14.1f}{pay_rate:<10.2f}{overtime_hours:<11.1f}"
      f"{overtime_pay:<15.2f}${regular_pay:<13.2f}${gross_pay:.2f}")
