# Toni Bethune
# 04132025
# P4HW2
# A program that calcautes an employee's hours,overtime and pay and loops until you put in Done.



# Initialize accumulators
total_employees = 0
total_overtime = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0

# Start sentinel loop
while True:
    employee_name = input('Enter employee\'s name or "Done" to terminate: ')
    
    if employee_name.lower() == "done":
        break

    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

    # Calculate pay
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
        regular_pay = 40 * pay_rate
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours_worked * pay_rate

    gross_pay = regular_pay + overtime_pay

    # Display employee summary
    print(f"\nEmployee name:     {employee_name}")
    print("------------------------------------------------------------")
    print("Hours Worked  Pay Rate  Overtime  Overtime Pay  RegHour Pay  Gross Pay")
    print("------------------------------------------------------------")
    print(f"{hours_worked:<13.2f}{pay_rate:<10.2f}{overtime_hours:<10.2f}"
          f"{overtime_pay:<14.2f}${regular_pay:<12.2f}${gross_pay:.2f}")
    print()

    # Update totals
    total_employees += 1
    total_overtime += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

# Display final totals
print(f"\nTotal number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
